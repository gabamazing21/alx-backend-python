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

    @parameterized.expand([
                ({}, ("a")),
                ({"a": 1}, ("a", "b"))
            ])
    def test_access_nested_map_exception(self, nested_map: Dict[str, Any], path: Tuple[str, ...]) -> None:
        """
        test method for error"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"'{path[-1]}'")
