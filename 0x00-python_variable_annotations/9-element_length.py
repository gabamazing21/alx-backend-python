#!/usr/bin/env python3
""" workig with type annotation"""

from typing import List, Union, Tuple, Callable, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing each e
    lement and it's length

    Args:
        1st (Iterable[Sequence]): An iterable of s
        equences (e.g list of strings)
    """
    return [(i, len(i)) for i in lst]
