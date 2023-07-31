#!/usr/bin/env python3
"""
Unittest module for testing the utils module
"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """
        Test method to check if access_nested_map returns the correct output
        """
        real_output = access_nested_map(map, path)
        self.assertEqual(real_output, expected_output)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        """
        Test method to check if access_nested_map raises the correct exception
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
        self.assertEqual(wrong_output, str(e.exception))


class TestGetJson(unittest.TestCase):
    """
    Test case for the get_json function
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test method to check if get_json returns the correct output
        """
        # Create Mock object with json method that returns test_payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        # Function calls requests.get, need patch to get mock return value
        with patch('requests.get', return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            # Check that mocked method called once per input
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """
    Test case for the memoize function
    """

    def test_memoize(self):
        """
        Test method to check if memoize function works as expected
        """

        class TestClass:
            """
            Test class with a_method method and a_property property
            """

            def a_method(self):
                """
                Method to always return 42
                """
                return 42

            @memoize
            def a_property(self):
                """
                Returns memoized property
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mocked:
            spec = TestClass()
            spec.a_property
            spec.a_property
            mocked.assert_called_once()
