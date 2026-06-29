import redis
import os
import time

REDIS_URL = os.getenv("REDIS_URL")

redis_client = redis.Redis.from_url(REDIS_URL, 
                                    decode_responses=True)



def blacklist_token(jti: str,
                    exp: int):
    print("CALL BLACKLIST_TOKEN")
    ttl = exp - int(time.time())
    redis_client.setex(f"blacklist:{jti}", ttl, "true")


def is_token_blacklisted(jti: str) -> bool:
    print("CALL IS_TOKEN_BLACKLISTED")
    return redis_client.exists(f"blacklist:{jti}") == 1