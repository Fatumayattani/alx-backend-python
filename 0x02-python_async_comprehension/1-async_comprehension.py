#!/usr/bin/env python3


'''Import async_generator from the previous task and then write a coroutine
    called async_comprehension that takes no arguments.

    The coroutine will collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.
'''

from typing import List


async def async_comprehension() -> List[float]:
    '''returns a list of rand numbers using async comprehension'''

    async_gen = __import__('0-async_generator').async_generator

    rand_num = [i async for i in async_gen()]

    return rand_num


if __name__ == '__main__':
    import asyncio

    print(asyncio.run(async_comprehension()))
