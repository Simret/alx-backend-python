#!/usr/bin/env python3
'''Testing the utils module'''
import unittest
from typing import Dict, Tuple, Union
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    '''Testing the `access_nested_map` function'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
    ) -> None:
        '''Testing `access_nested_map`'s output'''
        response = access_nested_map(nested_map, path)
        self.assertEqual(response, expected)
