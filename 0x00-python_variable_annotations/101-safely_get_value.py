#!/usr/bin/env python3
'''Type annotated module'''

from typing import Any, Mapping, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default=Optional[T]=None) -> Union[Any, T]:
    '''Type annotation values'''
    if key in dct:
        return dct[key]
    else:
        return default
