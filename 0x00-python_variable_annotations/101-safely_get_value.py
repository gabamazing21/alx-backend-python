#!/usr/bin/env python3
""" workig with type annotation"""

from typing import TypeVar, Mapping, Any, Union
from types import NoneType

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, NoneType] = None
        ) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
