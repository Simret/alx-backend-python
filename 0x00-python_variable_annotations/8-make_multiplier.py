#!/usr/bin/env python3
'''Type annotated module'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Multiplier returning float'''
    return lambda x: x * multiplier
