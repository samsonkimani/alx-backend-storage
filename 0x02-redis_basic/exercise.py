#!/usr/bin/env python3

"""
creating the cache class for the redis model
"""

from uuid import uuid4
import redis
from typing import Union

T = TypeVar('T')


class Cache:
    """ cache"""

    def __init__(self):
        """ initializing the cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ a class store that takes in data"""
        id = str(uuid4())

        if isinstance(data, (int, float)):
            data = str(data)
        self._redis.set(id, data)
        return id
