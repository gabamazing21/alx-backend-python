#!/usr/bin/env python3
""" workig with type annotation"""

from typing import Protocol, TypeVar, Optional, Sequence, Any, Union, NoneType


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return list of elements
    """
    if lst:
        return lst[0]
    else:
        return None
