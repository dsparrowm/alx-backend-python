#!/usr/bin/env python3
"""module to convert a function to task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Takes an int and returns asycio.Task"""
    task = asyncio.ensure_future(wait_random(max_delay))
    return task
