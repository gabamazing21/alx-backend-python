#!/usr/bin/env python3
from parameterized import parameterized
import unittest
from utils import access_nested_map
from typing import Any, Tuple, Any, Dict
"""
implement Testclass for utils module
"""


class TestAccessNestedMap(unittest.TestCase):
    """
    test class
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2) 
    ])
    def test_access_nested_map(self, nested_map: Dict[str, Any],  path: Tuple[str, ...], expected: Any) -> None:
        """
        test method
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
