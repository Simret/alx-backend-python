#!/usr/bin/env python3
'''Type annotated module'''

from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')
Res = Union[T, None]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default=None) -> Res:
    ''''''
    if key in dct:
        return dct[key]
    else:
        return default
