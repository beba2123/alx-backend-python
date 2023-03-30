#!/usr/bin/env python3
"""
File: 7-to_kv.py
Desc: This python module contains a type-annotated function that
      takes a string and an int or float as argument and returns
      a tuple. The first element of the tuple is a string. The second
      element is the square of the int/float and should be annotated
      as a float.
Author: Gizachew Bayness
Date Created: Feb 2, 2023
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int,  float]) -> Tuple[str, float]:
    """Returns a type annotated tuple of k and v"""
    return (k, v ** 2)
