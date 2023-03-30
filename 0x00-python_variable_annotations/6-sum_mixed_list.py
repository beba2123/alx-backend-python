#!/usr/bin/env python3
"""
File: 6-sum_mixed_list.py
Desc: This python module contains a type-annotated function which
      takes a list of integers and floats and returns their sum
      as a float.
Author: Gizachew Bayness
Date Created: Feb 2, 2023
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of the numbers in the list as afloat"""
    return float(sum(mxd_lst))
