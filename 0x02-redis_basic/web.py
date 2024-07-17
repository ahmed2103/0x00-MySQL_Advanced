#!/usr/bin/env python3
"""Module to count the number a certain page has been accessed"""
from typing import Callable

from requests import get
from redis import Redis
from functools import wraps

redis_client = Redis()


def count_page(func: Callable) -> Callable:
    """Decorator to count the number a certain page has been loaded"""
    @wraps(func)
    def wrapper(url: str) -> str:
        """Syntatic sugar wraps the callable function"""
        redis_client.incr("count:{}".format(url))
        return func(url)
    return wrapper


def cache_page(func: Callable) -> Callable:
    """Cache the page to increase performance"""
    def wrapper(url: str) -> str:
        """Syntatic sugar wraps the callable function"""
        cached_page = redis_client.get(url)
        if cached_page:
            return cached_page.decode("utf-8")
        result = func(url)
        redis_client.setex(url, 10, result)
        return result
    return wrapper


@count_page
@cache_page
def get_page(url: str) -> str:
    """Make http GET request to url and return the html content"""
    content = get(url).text
    return content
