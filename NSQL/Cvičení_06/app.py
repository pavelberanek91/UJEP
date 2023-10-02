import redis
import datetime
import pprint

r = redis.Redis()
#r = redis.Redis(host='localhost', port=6379, db=0, password=None)

r.mset({
    'ceska republika':'praha',
    'slovensko':'bratislava',
})
print(r.get('slovensko').decode('utf-8'))

dnesek = datetime.date.today()
navstevnici = ["10.3.1.41", '12.4.31.54', '95.34.123.56', '43.234.23.1']
r.sadd(dnesek.isoformat(), *navstevnici)
print(r.smembers(dnesek))

r1 = redis.Redis()
zpravy = {
    "zprava 1": {
        "email": "baf@haf.cz",
        "zprava": "mate hnusny produkty",
    },
    "zprava 2": {
        "email": "pepa@centrum.cz",
        "zprava": "spam spam spam",
    },
    "zprava 3": {
        "email": "jana@seznam.cz",
        "zprava": "chci si objednat tricko a nevim jak",
    },
    "zprava 4": {
        "email": "lojza@volny.cz",
        "zprava": "je tam nekdo?",
    },
    "zprava 5": {
        "email": "tomas@gmail.cz",
        "zprava": "komu se mam ozvat, kdyz chci reklamovat boty?",
    },
}

with r.pipeline() as sekvence_transakci:
    for zprava_id, obsah_zpravy in zpravy.items():
        sekvence_transakci.hmset(zprava_id, obsah_zpravy)
    sekvence_transakci.execute()

print(r.keys())
pprint(r.hgetall('zprava 1'))