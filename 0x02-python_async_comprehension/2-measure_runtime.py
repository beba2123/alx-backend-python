#!/usr/bin/env python3
"""
file: 2-measure_runtime.py
Desc: A python module that contains codes related to async
      comprhensions.
Author: Anteneh Alem
Date Created: April 04, 2023
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Excutes async comprehension  4 times.'''
    begin_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - begin_time
