import os
from redis import Redis
from dotenv import load_dotenv

load_dotenv()

redis = Redis(
    host=os.getenv("REDIS_HOST"),  # type: ignore
    port=os.getenv("REDIS_PORT"),  # type: ignore
    db=os.getenv("REDIS_DATABASE")  # type: ignore
)
