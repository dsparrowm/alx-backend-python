#!/usr/bin/env python3
"""this is a type annotated module"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """function that handles any type"""
    if lst:
        return lst[0]
    else:
        return None
