#!/usr/bin/env python3
"""this module is an async comprehension"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """this function returns a list of floats"""
    result = [x async for x in async_generator()]
    return result
