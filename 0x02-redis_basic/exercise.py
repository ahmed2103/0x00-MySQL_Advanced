#!/usr/bin/env python3
"""Exercise module on redis how to use?"""

import redis
from typing import Callable, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """decorator function that counts the number of times
     a method has been called"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """decorator function that tracks inputs abd outputs of function"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to call history"""
        input_list = '{}:inputs'.format(method.__qualname__)
        output_list = '{}:outputs'.format(method.__qualname__)
        self._redis.rpush(input_list, str(args))
        outputs = method(self, *args, **kwargs)
        self._redis.rpush(output_list, str(outputs))
        return outputs
    return wrapper


def replay(method: Callable):
    """function to restore the past with required format"""
    meth_name = method.__qualname__
    red = redis.Redis()
    num_calls = red.get("{}".format(meth_name)).decode("utf-8")
    print("{} was called {} times:"
          .format(meth_name, num_calls))
    inputs = red.lrange(meth_name + ':inputs', 0, -1)
    outputs = red.lrange(meth_name + ':outputs', 0, -1)
    for inp, out in zip(inputs, outputs):
        inp = inp.decode("utf-8")
        out = out.decode("utf-8")
        print('{}(*{}) -> {}'.format(meth_name, inp, out))


class Cache:
    """Class represents redis cache"""

    def __init__(self):
        """Instantiate redis instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data as value for generated key"""
        from uuid import uuid4
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get_int(self, key: str) -> int:
        """callable to cast value to int type"""
        return self.get(key, lambda x: int(x))

    def get_str(self, key: str) -> str:
        """callable to cast value to str type"""
        return self.get(key, lambda x: x.decode("utf-8"))

    def get(self, key: str, fn: Callable = None) -> (
            Union)[bytes, str, bytes, int, float, None]:
        """Converts bytes of redis to the original data type"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data
