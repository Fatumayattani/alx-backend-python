#!/usr/bin/env python3
"""
Module: 3-tasks
"""


import asyncio


''' Import wait_random from 0-basic_async_syntax.

    Write a function (do not create an async function, use the regular
    function syntax to do this) task_wait_random that takes an integer
    max_delay and returns a asyncio.Task.
'''


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''A function that creates a task for the scheduler'''

    wait_random = __import__('0-basic_async_syntax').wait_random

    return asyncio.create_task(wait_random(max_delay))


if __name__ == '__main__':
    async def test(max_delay: int) -> float:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
