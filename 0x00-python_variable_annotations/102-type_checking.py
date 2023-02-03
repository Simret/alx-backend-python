#!/usr/bin/env python3
"""A function that returns  a list of integers"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Returns a list of integers"""
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
