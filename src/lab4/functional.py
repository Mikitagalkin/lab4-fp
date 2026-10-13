"""Функции высшего порядка и класс-итератор."""

from functools import reduce
from typing import Callable, Iterable, Iterator, Any


def sum_reduce(numbers: Iterable) -> float:
    """Сумма чисел через functools.reduce."""
    return reduce(lambda acc, x: acc + x, numbers, 0)


def product_reduce(numbers: Iterable) -> float:
    """Произведение чисел через functools.reduce."""
    return reduce(lambda acc, x: acc * x, numbers, 1)


def compose(*functions: Callable) -> Callable:
    """Композиция функций: compose(f, g)(x) == f(g(x))."""
    def composed(value: Any) -> Any:
        for func in reversed(functions):
            value = func(value)
        return value
    return composed


def curry(func: Callable) -> Callable:
    """Карринг функции."""
    def curried(*args: Any) -> Any:
        if len(args) >= func.__code__.co_argcount:
            return func(*args)
        return lambda *more: curried(*(args + more))
    return curried


class CountdownIterator:
    """Собственный класс-итератор: считает от start до end."""

    def __init__(self, start: int, end: int = 1):
        self.start = start
        self.end = end
        self._current = None

    def __iter__(self) -> Iterator[int]:
        self._current = self.start
        return self

    def __next__(self) -> int:
        if self._current is None:
            self._current = self.start

        if self.start >= self.end:
            if self._current < self.end:
                raise StopIteration
            value = self._current
            self._current -= 1
        else:
            if self._current > self.end:
                raise StopIteration
            value = self._current
            self._current += 1

        return value

    def __len__(self) -> int:
        return abs(self.end - self.start) + 1

    def __repr__(self) -> str:
        return f"CountdownIterator({self.start}, {self.end})"
