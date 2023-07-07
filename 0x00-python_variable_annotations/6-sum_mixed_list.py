#!/usr/bin/env python3
"""this is a type-annotated module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """this function takes a mixture of ints and floats as list
    and returns their sum as a float
    """
    return sum(mxd_lst)
