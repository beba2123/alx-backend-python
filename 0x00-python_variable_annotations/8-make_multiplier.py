#!/usr/bin/env python3
"""
File: 8-make_multiplier.py
Desc: This python module contains a type-annotated function that
      takes a float as argument and returns a fuction that multiplies
      a float by multiplier.
Author: Gizachew Bayness
Date Created: Feb 2, 2023
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a type-annotated function"""
    def fun(a: float) -> float:
        """Multiplies two numbers"""
        return a * multiplier
    return fun
