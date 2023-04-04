#!/usr/bin/env python3
"""
file: 1-async_comprehension.py
Desc: A python module that contains codes related to async
      comprhensions.
Author: Anteneh Alem
Date Created: April 04, 2023
"""

import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Return values yielded by async_generator.'''
    return [value async for value in async_generator()]
