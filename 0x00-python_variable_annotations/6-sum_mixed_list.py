#!/usr/bin/env python3
from typing import List
""" workig with type annotation"""


def sum_mixed_list(mixd_lst: List[float | int]) -> float:
    """
    type annotation
    """
    return sum(mixd_lst)
