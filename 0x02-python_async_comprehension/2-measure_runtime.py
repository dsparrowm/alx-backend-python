#!/usr/bin/env python3
"""this module measures the runtime of a coroutine"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measures the runtime of a coroutine and returns it"""
    current_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    elapsed = time.perf_counter() - current_time
    return elapsed
