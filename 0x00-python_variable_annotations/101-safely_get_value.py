#!/usr/bin/env python3
"""
File: 101-safely_get_value.py
Desc: This python module contains a pre-written function that needs to be
      typed with python typea annotations.
Author: Gizachew Bayness
Date Created: Feb 2, 2023
"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Type Anotated function"""
    if key in dct:
        return dct[key]
    else:
        return default
