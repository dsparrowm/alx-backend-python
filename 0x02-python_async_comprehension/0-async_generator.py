#!/usr/bin/env python3
"""This module is an async generator"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """this function generates a random number between 0 and 10
    and counts to 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
