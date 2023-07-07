#!/usr/bin/env python3
"""this is a type annotated module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float amd returns a function that multiplies a flaat
    by multiplier
    """
    def multiply(x: float) -> float:
        "''takes a float and returns a float"""
        return x * multiplier
    return multiply
