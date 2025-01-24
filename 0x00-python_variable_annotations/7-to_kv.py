#!/usr/bin/env python3
""" workig with type annotation"""

from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ workig with type annotation"""
    return (k, v**2)
