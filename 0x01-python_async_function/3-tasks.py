#!/usr/bin/env python3
"""
file: 3-tasks.py
Desc: This python module contains a python code related to
      asynchronous coroutine programing in python.
Author: Anteneh Alem
Date Created: April 3, 2023
"""
from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ 3-Tasks """
    task = create_task(wait_random(max_delay))
    return task