#!/usr/bin/env python3
from parameterized import parameterized
from unittest.mock import patch, Mock
from unittest import TestCase
from utils import access_nested_map, get_json, memoize
from typing import Any, Tuple, Any, Dict
import requests
"""
implement Testclass for utils module
"""


class TestAccessNestedMap(TestCase):
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


class TestGetJson(TestCase):
    """
    Test class for utils.get_json modul
    """
    @parameterized.expand([
       ("http://example.com", "True"),
       ("http://holberton.io", "False")
       ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """test the api call"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(TestCase):
    """
    test class for Memoize
    """
    def test_memoize(self):
        """
        Test the memoize
        """
        class TestClass:
            """
            demo class
            """

            def a_method(self):
                """
                demo method
                """
                return 42

            @memoize
            def a_property(self):
                """
                method decorator
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            instance = TestClass()
            first_call = instance.a_property
            second_call = instance.a_property
            self.assertEqual(first_call, 42)
            self.assertEqual(second_call, 42)
            mock_method.assert_called_once()
