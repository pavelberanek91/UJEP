#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright Nigel Small
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import absolute_import, division

from codecs import decode
from collections import OrderedDict
from datetime import date, time, datetime, timedelta
from io import BytesIO
from struct import pack as struct_pack, unpack as struct_unpack

from pytz import FixedOffset, timezone, utc
import six

from interchange.geo import Point
from interchange.time import Duration, Date, Time, DateTime, UnixEpoch


INT_DATA = {}
for n in range(-0x8000, 0x8000):
    if -0x10 <= n < 0x80:
        INT_DATA[n] = struct_pack(">b", n)
    elif -0x80 <= n < -0x10:
        INT_DATA[n] = b"\xC8" + struct_pack(">b", n)
    else:
        INT_DATA[n] = b"\xC9" + struct_pack(">h", n)

BYTES_S_HEAD = [b"\xCC" + struct_pack(">B", value) for value in range(0x100)]
BYTES_M_HEAD = [b"\xCD" + struct_pack(">H", value) for value in range(0x10000)]

STR_S_HEAD = [b"\xD0" + struct_pack(">B", value) for value in range(0x100)]
STR_M_HEAD = [b"\xD1" + struct_pack(">H", value) for value in range(0x10000)]

LIST_S_HEAD = [b"\xD4" + struct_pack(">B", value) for value in range(0x100)]
LIST_M_HEAD = [b"\xD5" + struct_pack(">H", value) for value in range(0x10000)]

DICT_S_HEAD = [b"\xD8" + struct_pack(">B", value) for value in range(0x100)]
DICT_M_HEAD = [b"\xD9" + struct_pack(">H", value) for value in range(0x10000)]

UNPACKED_UINT_8 = {bytes(bytearray([x])): x for x in range(0x100)}
UNPACKED_UINT_16 = {struct_pack(">H", x): x for x in range(0x10000)}

UNPACKED_MARKERS = {b"\xC0": None, b"\xC2": False, b"\xC3": True}
UNPACKED_MARKERS.update({bytes(bytearray([z])): z for z in range(0x00, 0x80)})
UNPACKED_MARKERS.update({bytes(bytearray([z + 256])): z for z in range(-0x10, 0x00)})


INT64_MIN = -(2 ** 63)
INT64_MAX = 2 ** 63


UNIX_EPOCH_DATE_ORDINAL = UnixEpoch.to_ordinal()


class Structure(object):

    def __init__(self, tag, *fields):
        self.tag = tag
        self.fields = list(fields)

    def __repr__(self):
        return "Structure[#%02X](%s)" % (self.tag, ", ".join(map(repr, self.fields)))

    def __eq__(self, other):
        try:
            return self.tag == other.tag and self.fields == other.fields
        except AttributeError:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __len__(self):
        return len(self.fields)

    def __getitem__(self, key):
        return self.fields[key]

    def __setitem__(self, key, value):
        self.fields[key] = value


class Packer(object):

    integer_types = six.integer_types
    text_type = six.text_type
    bytearray_type = bytearray
    list_type = list
    dict_type = dict

    def __init__(self, buffer, version=()):
        self._buffer = buffer
        self._write = self._buffer.write
        self.version = version

    def pack(self, value):
        t = type(value)

        # String (Unicode)
        if t is self.text_type:
            self._pack_unicode(value)

        # List
        elif t is self.list_type or t is tuple:
            self._pack_list(value)

        # Integer
        elif t in self.integer_types:
            self._pack_integer(value)

        # Float
        elif t is float:
            self._write(b"\xC1")
            self._write(struct_pack(">d", value))

        # Boolean
        elif value is True:
            self._write(b"\xC3")
        elif value is False:
            self._write(b"\xC2")

        # None
        elif value is None:
            self._write(b"\xC0")  # NULL

        # Byte array
        elif t is self.bytearray_type:
            self._pack_bytearray(value)

        # String (UTF-8)
        elif t is bytes:
            self._pack_utf8(value)

        # Dictionary
        elif t is dict or t is OrderedDict or isinstance(value, self.dict_type):
            self._pack_dict(value)

        # Bolt 2 introduced temporal and spatial types
        elif self.version < (2, 0):
            raise TypeError("Values of type %s are not supported "
                            "by Bolt %s" % (type(value), ".".join(self.version)))

        # DateTime
        #
        # Note: The built-in datetime.datetime class extends the
        # datetime.date class, so this needs to be listed first
        # to avoid objects being encoded incorrectly.
        #
        elif isinstance(value, datetime):
            self._pack_datetime(DateTime.from_native(value))
        elif isinstance(value, DateTime):
            self._pack_datetime(value)

        # Date
        elif isinstance(value, (date, Date)):
            self._write(b"\xB1D")
            self._pack_integer(value.toordinal() - UNIX_EPOCH_DATE_ORDINAL)

        # Time
        elif isinstance(value, (time, Time)):
            self._pack_time(value)

        # TimeDelta
        elif isinstance(value, timedelta):
            self._write(b"\xB4E")
            self._pack_integer(0)                                   # months
            self._pack_integer(value.days)                          # days
            self._pack_integer(value.seconds)                       # seconds
            self._pack_integer(1000 * value.microseconds)           # nanoseconds

        # Duration
        elif isinstance(value, Duration):
            self._write(b"\xB4E")
            self._pack_integer(value.months)                        # months
            self._pack_integer(value.days)                          # days
            self._pack_integer(value.seconds)                       # seconds
            self._pack_integer(int(1000000000 * value.subseconds))  # nanoseconds

        # Point
        elif isinstance(value, Point):
            self._pack_point(value)

        # Other
        else:
            raise TypeError("Values of type %s are not supported" % type(value))

    def _pack_unicode(self, value):
        # Count the number of chars and handle boundary cases
        size = len(value)
        if size == 0:
            self._write(b"\x80")
            return
        elif size >= 0x100000000:
            raise ValueError("String too large")
        # Count the number of bytes when encoded as UTF-8
        self._pack_utf8(value.encode("utf-8"))

    def _pack_utf8(self, value):
        size = len(value)
        # Write the string header
        if size < 0x10:
            self._write(bytearray([0x80 + size]))
        elif size < 0x100:
            self._write(STR_S_HEAD[size])
        elif size < 0x10000:
            self._write(STR_M_HEAD[size])
        elif size < 0x100000000:
            self._write(b"\xD2")
            self._write(struct_pack(">I", size))
        else:
            raise ValueError("String too large")
        # Write the string content
        self._write(value)

    def _pack_list(self, value):
        size = len(value)
        if size == 0:
            self._write(b"\x90")
            return
        elif size < 0x10:
            self._write(bytearray([0x90 + size]))
        elif size < 0x100:
            self._write(LIST_S_HEAD[size])
        elif size < 0x10000:
            self._write(LIST_M_HEAD[size])
        elif size < 0x100000000:
            self._write(b"\xD6")
            self._write(struct_pack(">I", size))
        else:
            raise ValueError("List too large")
        for item in value:
            self.pack(item)

    def _pack_integer(self, value):
        if -0x8000 <= value < 0x8000:
            self._write(INT_DATA[value])
        elif -0x80000000 <= value < 0x80000000:
            self._write(b"\xCA")
            self._write(struct_pack(">i", value))
        elif INT64_MIN <= value < INT64_MAX:
            self._write(b"\xCB")
            self._write(struct_pack(">q", value))
        else:
            raise ValueError("Integer %s out of range" % value)

    def _pack_dict(self, value):
        size = len(value)
        if size == 0:
            self._write(b"\xA0")
        elif size < 0x10:
            self._write(bytearray([0xA0 + size]))
        elif size < 0x100:
            self._write(DICT_S_HEAD[size])
        elif size < 0x10000:
            self._write(DICT_M_HEAD[size])
        elif size < 0x100000000:
            self._write(b"\xDA")
            self._write(struct_pack(">I", size))
        else:
            raise ValueError("Dictionary too large")
        for key, item in value.items():
            t = type(key)
            if t is self.text_type:
                self._pack_unicode(key)
            elif t is bytes:
                self._pack_utf8(key)
            else:
                raise TypeError("Dictionary keys must be "
                                "of type %r or bytes" % self.text_type)
            self.pack(item)

    def _pack_bytearray(self, value):
        size = len(value)
        if size < 0x100:
            self._write(BYTES_S_HEAD[size])
        elif size < 0x10000:
            self._write(BYTES_M_HEAD[size])
        elif size < 0x100000000:
            self._write(b"\xCE")
            self._write(struct_pack(">I", size))
        else:
            raise ValueError("Byte array too large")
        self._write(value)

    def _pack_time(self, t):
        try:
            nanoseconds = int(t.ticks * 1000000000)
        except AttributeError:
            nanoseconds = (3600000000000 * t.hour + 60000000000 * t.minute +
                           1000000000 * t.second + 1000 * t.microsecond)
        if t.tzinfo:
            self._write(b"\xB2T")
            self._pack_integer(nanoseconds)
            self._pack_integer(t.tzinfo.utcoffset(t).seconds)
        else:
            self._write(b"\xB1t")
            self._pack_integer(nanoseconds)

    def _pack_datetime(self, dt):
        tz = dt.tzinfo
        if tz is None:
            # without time zone
            seconds, nanoseconds = utc.localize(dt).to_clock_time() - UnixEpoch.to_clock_time()
            self._write(b"\xB2d")
            self._pack_integer(seconds)
            self._pack_integer(nanoseconds)
        elif hasattr(tz, "zone") and tz.zone:
            # with named time zone
            zone_epoch = DateTime(1970, 1, 1, tzinfo=dt.tzinfo)
            seconds, nanoseconds = dt.to_clock_time() - zone_epoch.to_clock_time()
            self._write(b"\xB3f")
            self._pack_integer(seconds)
            self._pack_integer(nanoseconds)
            self.pack(tz.zone)
        else:
            # with time offset
            zone_epoch = DateTime(1970, 1, 1, tzinfo=dt.tzinfo)
            seconds, nanoseconds = dt.to_clock_time() - zone_epoch.to_clock_time()
            self._write(b"\xB3F")
            self._pack_integer(seconds)
            self._pack_integer(nanoseconds)
            self._pack_integer(tz.utcoffset(dt).seconds)

    def _pack_point(self, p):
        dim = len(p)
        self._write(bytearray([0xB1 + dim]))
        if dim == 2:
            self._write(b"X")
        elif dim == 3:
            self._write(b"Y")
        else:
            raise ValueError("Cannot dehydrate Point with %d dimensions" % dim)
        self._pack_integer(p.srid)
        for value in p:
            self.pack(value)


class Unpacker(object):

    def __init__(self, data, offset=0):
        if six.PY2:
            self._data = bytearray(data)  # FIXME
        else:
            self._data = data
        self._offset = offset

    def unpack(self):
        marker = self._data[self._offset]
        self._offset += 1

        # Tiny collections
        if marker == 0x80:
            return ""
        elif 0x81 <= marker <= 0x8F:  # TINY_STRING
            start = self._offset
            self._offset = start + (marker & 0x0F)
            return decode(self._data[start:self._offset], "utf-8")
        elif marker == 0x90:
            return []
        elif marker == 0x91:
            return [self.unpack()]
        elif marker == 0x92:
            return [self.unpack(), self.unpack()]
        elif marker == 0x93:
            return [self.unpack(), self.unpack(), self.unpack()]
        elif 0x94 <= marker <= 0x9F:    # TINY_LIST
            return [self.unpack() for _ in range(marker & 0x0F)]
        elif 0xA0 <= marker <= 0xAF:    # TINY_DICT
            size = marker & 0x0F
            value = {}
            for _ in range(size):
                key = self.unpack()
                value[key] = self.unpack()
            return value

        # Integer
        elif 0x00 <= marker <= 0x7F:
            return marker
        elif 0xF0 <= marker <= 0xFF:
            return marker - 0x100
        elif marker == 0xC8:
            return self._read_i8()
        elif marker == 0xC9:
            return self._read_i16be()
        elif marker == 0xCA:
            return self._read_i32be()
        elif marker == 0xCB:
            return self._read_i64be()

        # String
        elif marker == 0xD0:  # STRING_8:
            size = self._read_u8()
            return decode(self._read(size), "utf-8")
        elif marker == 0xD1:  # STRING_16:
            size = self._read_u16be()
            return decode(self._read(size), "utf-8")
        elif marker == 0xD2:  # STRING_32:
            size = self._read_u32be()
            return decode(self._read(size), "utf-8")

        # Structure
        elif 0xB0 <= marker <= 0xBF:    # TINY_STRUCT
            tag = self._read_u8()
            fields = [self.unpack() for _ in range(marker & 0x0F)]
            if tag == 68:  # 'D'
                return self._hydrate_date(*fields)
            elif tag in (84, 116):  # 'T' and 't'
                return self._hydrate_time(*fields)
            elif tag in (70, 100, 102):  # b"F", b"f", b"d"
                return self._hydrate_datetime(*fields)
            elif tag == 69:  # b"E"
                return self._hydrate_duration(*fields)
            elif tag in (88, 89):  # b"X", b"Y"
                return self._hydrate_point(*fields)
            else:
                return Structure(tag, *fields)

        # Float
        elif marker == 0xC1:
            return self._read_f64be()

        # Boolean
        elif marker == 0xC2:
            return False
        elif marker == 0xC3:
            return True

        # Null
        elif marker == 0xC0:
            return None

        # Bytes
        elif marker == 0xCC:
            size = self._read_u8()
            return bytes(self._read(size))
        elif marker == 0xCD:
            size = self._read_u16be()
            return bytes(self._read(size))
        elif marker == 0xCE:
            size = self._read_u32be()
            return bytes(self._read(size))

        # List
        elif marker == 0xD4:  # LIST_8:
            size = self._read_u8()
            return [self.unpack() for _ in range(size)]
        elif marker == 0xD5:  # LIST_16:
            size = self._read_u16be()
            return [self.unpack() for _ in range(size)]
        elif marker == 0xD6:  # LIST_32:
            size = self._read_u32be()
            return [self.unpack() for _ in range(size)]

        # Dictionary
        elif marker == 0xD8:  # MAP_8:
            size = self._read_u8()
            value = {}
            for _ in range(size):
                key = self.unpack()
                value[key] = self.unpack()
            return value
        elif marker == 0xD9:  # MAP_16:
            size = self._read_u16be()
            value = {}
            for _ in range(size):
                key = self.unpack()
                value[key] = self.unpack()
            return value
        elif marker == 0xDA:  # MAP_32:
            size = self._read_u32be()
            value = {}
            for _ in range(size):
                key = self.unpack()
                value[key] = self.unpack()
            return value

        else:
            raise ValueError("Unknown PackStream marker %02X" % marker)

    def _hydrate_date(self, days):
        """ Hydrator for `Date` values.

        :param days:
        :return: Date
        """
        return Date.from_ordinal(UNIX_EPOCH_DATE_ORDINAL + days)

    def _hydrate_time(self, nanoseconds, tz=None):
        """ Hydrator for `Time` and `LocalTime` values.

        :param nanoseconds:
        :param tz:
        :return: Time
        """
        seconds, nanoseconds = map(int, divmod(nanoseconds, 1000000000))
        minutes, seconds = map(int, divmod(seconds, 60))
        hours, minutes = map(int, divmod(minutes, 60))
        seconds = (1000000000 * seconds + nanoseconds) / 1000000000
        t = Time(hours, minutes, seconds)
        if tz is None:
            return t
        tz_offset_minutes, tz_offset_seconds = divmod(tz, 60)
        zone = FixedOffset(tz_offset_minutes)
        return zone.localize(t)

    def _hydrate_datetime(self, seconds, nanoseconds, tz=None):
        """ Hydrator for `DateTime` and `LocalDateTime` values.

        :param seconds:
        :param nanoseconds:
        :param tz:
        :return: datetime
        """
        minutes, seconds = map(int, divmod(seconds, 60))
        hours, minutes = map(int, divmod(minutes, 60))
        days, hours = map(int, divmod(hours, 24))
        seconds = (1000000000 * seconds + nanoseconds) / 1000000000
        t = DateTime.combine(Date.from_ordinal(UNIX_EPOCH_DATE_ORDINAL + days),
                             Time(hours, minutes, seconds))
        if tz is None:
            return t
        if isinstance(tz, int):
            tz_offset_minutes, tz_offset_seconds = divmod(tz, 60)
            zone = FixedOffset(tz_offset_minutes)
        else:
            zone = timezone(tz)
        return zone.localize(t)

    def _hydrate_duration(self, months, days, seconds, nanoseconds):
        """ Hydrator for `Duration` values.

        :param months:
        :param days:
        :param seconds:
        :param nanoseconds:
        :return: `duration` namedtuple
        """
        return Duration(months=months, days=days, seconds=seconds, nanoseconds=nanoseconds)

    def _hydrate_point(self, srid, *coordinates):
        """ Create a new instance of a Point subclass from a raw
        set of fields. The subclass chosen is determined by the
        given SRID; a ValueError will be raised if no such
        subclass can be found.
        """
        try:
            point_class, dim = Point.class_for_srid(srid)
        except KeyError:
            point = Point(coordinates)
            point.srid = srid
            return point
        else:
            if len(coordinates) != dim:
                raise ValueError("SRID %d requires %d coordinates (%d provided)" % (srid, dim, len(coordinates)))
            return point_class(coordinates)

    def _read(self, n=1):
        q = self._offset + n
        m = self._data[self._offset:q]
        self._offset = q
        return m

    def _read_u8(self):
        q = self._offset + 1
        n, = struct_unpack(">B", self._data[self._offset:q])
        self._offset = q
        return n

    def _read_u16be(self):
        q = self._offset + 2
        n, = struct_unpack(">H", self._data[self._offset:q])
        self._offset = q
        return n

    def _read_u32be(self):
        q = self._offset + 4
        n, = struct_unpack(">I", self._data[self._offset:q])
        self._offset = q
        return n

    def _read_i8(self):
        q = self._offset + 1
        z, = struct_unpack(">b", self._data[self._offset:q])
        self._offset = q
        return z

    def _read_i16be(self):
        q = self._offset + 2
        z, = struct_unpack(">h", self._data[self._offset:q])
        self._offset = q
        return z

    def _read_i32be(self):
        q = self._offset + 4
        z, = struct_unpack(">i", self._data[self._offset:q])
        self._offset = q
        return z

    def _read_i64be(self):
        q = self._offset + 8
        z, = struct_unpack(">q", self._data[self._offset:q])
        self._offset = q
        return z

    def _read_f64be(self):
        q = self._offset + 8
        r, = struct_unpack(">d", self._data[self._offset:q])
        self._offset = q
        return r


def pack(*values, **kwargs):
    buffer = BytesIO()
    packer = Packer(buffer, **kwargs)
    for value in values:
        packer.pack(value)
    return buffer.getvalue()


def unpack(data, offset=0):
    s = Unpacker(data, offset)
    while True:
        try:
            yield s.unpack()
        except IndexError:
            break
