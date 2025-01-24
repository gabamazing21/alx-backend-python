#!/usr/bin/env python3
from typing import List, Union
""" workig with type annotation"""


def sum_mixed_list(mixd_lst: List[Union[float, int]]) -> float:
    """
    type annotation
    """
    return sum(mixd_lst)
