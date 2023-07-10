#!/usr/bin/env python3
"""
Module: 0-basic_async_syntax
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay
    (included) seconds and eventually returns it.

    Args:
        max_delay (int): The maximum delay in seconds (default is 10).

    Returns:
        float: The random delay.

    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
