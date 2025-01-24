#!/usr/bin/env python3
from typing import List
""" workig with type annotation"""


def sum_list(input_list: List[float]) -> float:
    """
    sum of float in pythong with type annotation
    """
    total: float = 0
    for i in input_list:
        total += i
    return total
