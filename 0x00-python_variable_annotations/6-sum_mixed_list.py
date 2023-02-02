#!/usr/bin/env python3
'''Type annotated module'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Sum of list elements of mixed type'''
    return float(sum(mxd_lst))
