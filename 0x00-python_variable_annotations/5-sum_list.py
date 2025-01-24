#!/usr/bin/env python3
""" workig with type annotation"""


def sum(input_list: list[float]) -> float:
    """
    sum of float in pythong with type annotation
    """
    total: float = 0
    for i in input_list:
        total += i
    return total
