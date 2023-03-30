#!/usr/bin/env python3
"""
File: 9-element_length.py
Desc: This python module contains a function with some params and
      returns values with the appropriate types.
Author: Gizachew Bayness
Date Created: Feb 2, 2023
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns values with appropriate types"""
    return [(i, len(i)) for i in lst]
