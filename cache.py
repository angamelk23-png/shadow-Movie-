import redis
from config import REDIS_URL
r=redis.from_url(REDIS_URL)

def cache_set(k,v):
 r.setex(k,300,v)

def cache_get(k):
 return r.get(k)
