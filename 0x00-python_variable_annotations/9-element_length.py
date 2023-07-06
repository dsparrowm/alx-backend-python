#!/usr/bin/env python3
"""this is a type annotated module"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns an iterable"""
    return [(i, len(i)) for i in lst]
