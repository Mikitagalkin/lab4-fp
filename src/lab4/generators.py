"""Генераторы случайных чисел."""

import random
from typing import Generator


def random_range(
    start: int = 0,
    stop: int = 100,
    count: int = 10,
    seed: int = None,
) -> Generator[int, None, None]:
    """Генератор случайных целых чисел в диапазоне."""
    if count < 0:
        raise ValueError("count должен быть >= 0")
    if start > stop:
        raise ValueError("start должен быть <= stop")

    rng = random.Random(seed)
    for _ in range(count):
        yield rng.randint(start, stop)


def infinite_random(
    start: int = 0,
    stop: int = 100,
    seed: int = None,
) -> Generator[int, None, None]:
    """Бесконечный генератор случайных чисел."""
    if start > stop:
        raise ValueError("start должен быть <= stop")

    rng = random.Random(seed)
    while True:
        yield rng.randint(start, stop)


def prime_generator(limit: int = None) -> Generator[int, None, None]:
    """Генератор простых чисел."""
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    n = 2
    while limit is None or n <= limit:
        if is_prime(n):
            yield n
        n += 1
