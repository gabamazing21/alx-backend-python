#!/usr/bin/env python3
""" workig with type annotation"""

from typing import Sequence, Any, Union
from types import NoneType


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """
    Return list of elements
    """
    if lst:
        return lst[0]
    else:
        return None
