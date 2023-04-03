#!/usr/bin/env python3
''' Description: Import wait_random from the previous python file that
                 you’ve written and write an async routine called wait_n
                 that takes in 2 int arguments: max_delay and n. You will
                 spawn wait_random n times with the specified max_delay.
                 wait_n should return the list of all the delays(float values)
                 The list of the delays should be in ascending order without
                 using sort() because of concurrency.
    Arguments: n: int, max_delay: int = 10
'''
from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' Return execution time for wait_n given `n` and `max_delay`. '''
    start = time()
    run(wait_n(n, max_delay))
    end = time()
    elapsed_time = end - start
    return elapsed_time / n