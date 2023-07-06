#!/usr/bin/env python3
"""this is a type-annotated module"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """this function takes a list of floats and returns their sum
    as a float"""
    return sum(input_list)
