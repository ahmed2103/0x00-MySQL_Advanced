#!/usr/bin/env python3
"""Module to count the number a certain page has been accessed"""
from typing import Callable

from requests import get
from redis import Redis
from functools import wraps

redis_client = Redis()


def cache_page(func: Callable) -> Callable:
    """Cache the page to increase performance"""
    @wraps(func)
    def wrapper(url: str) -> str:
        """Syntatic sugar wraps the callable function"""
        redis_client.incr("count:{}".format(url))
        cached_page = redis_client.get(url)
        if cached_page:
            return cached_page.decode("utf-8")
        result = func(url)
        redis_client.set("count:{}".format(url), 0)
        redis_client.setex('result:{}'.format(url), 10, result)
        return result
    return wrapper


@cache_page
def get_page(url: str) -> str:
    """Make http GET request to url and return the html content"""
    return get(url).text
