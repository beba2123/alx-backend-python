#!/usr/bin/env python3
"""
File: 100-safe_first_element.py
Desc: This python module contains a single typed-function.
Author: Gizachew Bayness
Date Created: Feb 2, 2023
"""
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Duck-typed function"""
    if lst:
        return lst[0]
    else:
        return None
