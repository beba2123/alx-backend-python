#!/usr/bin/env python3
'''
i am writing asynchronous coroutine function in which 
it takes an integer argument and name the function wait_random 
means that that waits random delay between 0 and max_delay and 
eventually returns it.
'''

import asyncio
import random

async def wait_random(max_delay:int = 10) -> float:
   gap = random.uniform(0, max_delay)
   await asyncio.sleep(gap)
   return gap


