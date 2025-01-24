#!/usr/bin/env python3
from typing import List
""" workig with type annotation"""


def sum_list(input_list: List[float]) -> float:
    """
    Return the sum of a list of floats.

    Args:
        input_list (List(float)): A list of floats

    Returns:
        float: The sum of the float in the list
    """
    total: float = 0
    for i in input_list:
        total += i
    return total
