from other import redis
from typing import Any, Tuple
from utils.parser import parse_country_data
import json


#
def get_country_info(country_code: str) -> Tuple[int, Any]:
    cached_information = redis.get(str.lower(country_code))

    print(cached_information)

    if cached_information is not None:
        cache_to_json = json.loads(cached_information)
        return 200, cache_to_json

    parsed_information = parse_country_data(country_code)
    if parsed_information is None:
        return 404, None

    redis.set(
        str.lower(country_code),
        json.dumps(parsed_information),
        ex=4*3600
    )

    return 200, parsed_information
