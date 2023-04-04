#!/usr/bin/env python3
"""
file: 0-async_generator.py
Desc: A python module that contains codes related to async
      comprhensions.
Author: Anteneh Alem
Date Created: April 04, 2023
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' for generating a sequence of 10 numbers.'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10