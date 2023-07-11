#!/usr/bin/env python3

'''Write a coroutine called async_generator that takes no arguments.

    The coroutine will loop 10 times, each time asynchronously wait 1
    second, then yield a random number between 0 and 10. Use the
    random module.
'''


import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''an async function that returns a float number'''
    for i in range(10):
        await asyncio.sleep(1)
        yield(uniform(0, 10))


if __name__ == '__main__':
    async def print_yielded_values():
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)

    asyncio.run(print_yielded_values())
