from cachetools import cached, TTLCache, LFUCache

conf_cache = TTLCache(maxsize=1000, ttl=360)