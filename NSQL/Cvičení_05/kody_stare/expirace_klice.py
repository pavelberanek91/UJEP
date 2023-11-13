import redis 
from datetime import datetime, timedelta

r = redis.Redis()
r.setex(name='user324', value='True', time=timedelta(minutes=1))

if r.exists('user324'):
    print('Povoleno')
    print(r.ttl('user324'))
else:
    print('Zakazano')

#r.expireat(name='user324', when=datetime.date(year=2022, month=10, day=31))
#r.expireat(name='user324', when=datetime.time(hour=16, minute=10, secod=31))
#r.expireat(name='user324', when=datetime.datetime(year=2022, month=10, day=31, hour=16, minute=10, secod=31))
#r.persist(name='user324')
