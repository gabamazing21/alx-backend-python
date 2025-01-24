#!/usr/bin/env python3
from typing import List, Union, Tuple
""" workig with type annotation"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ workig with type annotation"""
    return (k, v**2)
