#!/usr/bin/env python3
'''Type annotated module'''

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Tuple of mixed type'''
    return (k, float(v**2))
