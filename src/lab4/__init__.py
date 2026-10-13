"""Лабораторная работа №4: Функциональное программирование."""

from .decorators import log_calls, timer
from .generators import random_range, infinite_random, prime_generator
from .functional import (
    sum_reduce,
    product_reduce,
    compose,
    curry,
    CountdownIterator,
)

__version__ = "1.0.0"
__all__ = [
    "log_calls",
    "timer",
    "random_range",
    "infinite_random",
    "prime_generator",
    "sum_reduce",
    "product_reduce",
    "compose",
    "curry",
    "CountdownIterator",
]
