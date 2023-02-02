#!/usr/bin/env python3
'''Type annotated module'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Sum of list elements'''
    return float(sum(input_list))
