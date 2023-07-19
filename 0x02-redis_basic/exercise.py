#!/usr/bin/env python3

"""
creating the cache class for the redis model
"""

from uuid import uuid4
import redis
from typing import Union
from collections.abc import Callable
from functools import wraps


class Cache:
    """ cache"""

    def __init__(self):
        """ initializing the cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def count_calls(method: Callable) -> Callable:
        """ creating a wrapper function"""
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            key = method.__qualname__
            count_key = key + "_count"
            self._redis.incr(count_key)
            return method(self, *args, **kwargs)
        return wrapper

    def call_history(method: Callable) -> Callable:
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            inputs_key = f"{method.__qualname__}:inputs"
            outputs_key = f"{method.__qualname__}:outputs"
            self._redis.rpush(inputs_key, str(args))
            result = method(self, *args, **kwargs)
            self._redis.rpush(outputs_key, result)

            return result

        return wrapper

    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ a class store that takes in data"""
        id = str(uuid4())

        if isinstance(data, (int, float)):
            data = str(data)
        self._redis.set(id, data)
        return id

    def get(
            self,
            key: str,
            fn: Callable[[], None] = None
    ) -> Union[str, bytes, int, None]:
        data = self._redis.get(key)
        if data is None:
            return None

        if fn is not None:
            return fn(data)

    def get_str(self, key: str) -> Union[str, bytes, None]:
        """ get str function"""
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, bytes, None]:
        """ get int method"""
        return self.get(key, fn=int)

    def replay(self, method: Callable):
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        inputs = self._redis.lrange(inputs_key, 0, -1)
        outputs = self._redis.lrange(outputs_key, 0, -1)

        print(f"{method.__qualname__} was called {len(inputs)} times:")

        for input_args, output in zip(inputs, outputs):
            input_args = input_args.decode("utf-8")
            output = output.decode("utf-8")
            print(f"{method.__qualname__}(*{input_args}) -> {output}")
