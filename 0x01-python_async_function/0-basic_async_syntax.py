#!/usr/bin/env python3
"""this module contains a coroutine that returns  a string"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """a coroutine that generates a random number and wait for that
       time
    """
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
