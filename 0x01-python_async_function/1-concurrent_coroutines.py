#!/usr/bin/env python3
"""this module handles concurrent codes"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """this coroutine takes in two int values and returns a list
    of all the delays
    """
    delays = []
    result = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed((result)):
        delay = await task
        delays.append(delay)
    return delays
