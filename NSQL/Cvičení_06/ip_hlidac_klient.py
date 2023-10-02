import redis

r = redis.Redis()

for _ in range(20):
    r.lpush("klient", "104.174.118.18")

print(r.blpop("klient"))