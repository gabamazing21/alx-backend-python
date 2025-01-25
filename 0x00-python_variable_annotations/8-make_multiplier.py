#!/usr/bin/env python3
""" workig with type annotation"""

from typing import List, Union, Tuple, Callable


def make_multiplier(multiplier: float) -> callable[[float], float]:
    """
    return a function that multiples a float by the given the multopler."""
    def multipler_function(x: float) -> float:
        return x * multiplier
    return multipler_function
