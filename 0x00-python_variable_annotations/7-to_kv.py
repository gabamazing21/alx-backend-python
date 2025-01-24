#!/usr/bin/env python3
from typing import List, Union
""" workig with type annotation"""


def to_kv(k: str, v: int | float) -> tuple:
    """ workig with type annotation"""
    v = v**2
    return (v, v)
