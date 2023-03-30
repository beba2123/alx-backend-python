#!/usr/bin/env python3
"""
File: 5-sum_list.py
Desc: This python module contains a type-annotated function which
      takes a list of floats as argument and returns their sum as
      a float.
Author: Gizachew Bayness
Date Created: Feb 2, 2023
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of the numbers in the list"""
    return sum(input_list)
