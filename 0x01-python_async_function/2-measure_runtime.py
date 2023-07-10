#!/usr/bin/env python3
"""a module to measure the runtine of a function"""
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """takes two args and returns a float"""
    current_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - current_time
    return elapsed / n
