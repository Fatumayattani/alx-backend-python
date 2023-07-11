#!/usr/bin/env python3

"""
Async Generator Module
"""

import asyncio
import random
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
