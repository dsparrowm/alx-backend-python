#!/usr/bin/env python3
"""this module handles concurrent codes"""
import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """this coroutine takes in two int values and returns a list
    of all the delays
    """
    delays = []
    result = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed((result)):
        delay = await task
        delays.append(delay)
    return delays
