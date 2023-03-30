#!/usr/bin/env python3
"""
File: 102-type_checking.py
Desc: This python module contains a pre-written function to be
      modified with necessary changes and to be validated using mypy.
Author: Gizachew Bayness
Date Created: Feb 2, 2023
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Type checked function"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
