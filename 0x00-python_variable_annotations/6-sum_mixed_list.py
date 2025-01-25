#!/usr/bin/env python3
""" workig with type annotation"""

from typing import List, Union


def sum_mixed_list(mixd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
        float: The sum of the elements in the list.
    """
    return sum(mixd_lst)
