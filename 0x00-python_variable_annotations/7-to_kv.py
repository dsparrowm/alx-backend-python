#!/usr/bin/env python3
"""this is a type annotated module"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """this function takea a string and int or a float and returns
    a tuple"""
    return k, float(v ** 2)
