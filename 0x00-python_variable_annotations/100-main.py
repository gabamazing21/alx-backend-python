#!/usr/bin/env python3
""" workig with type annotation"""

from typing import Protocol, TypeVar, Optional
# Define a protocal for objects that support indexing and truthiness
class SupportsIndexingAndTruthiness(Protocol):
    def __getItem__(self, index: int):
        ... # Support Indexing (e.g lst[0])
    
    def __bool__(self) -> bool:
        ... # Supports truthiness (e.g .. if lst)
T = TypeVar('T')

def safe_first_element(lst: SupportsIndexingAndTruthiness) -> Optional[T]:
    if lst:
        return lst[0]
    else:
        return None