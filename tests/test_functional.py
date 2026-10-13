"""Тесты функций и класса-итератора."""

import pytest
from src.lab4.functional import (
    sum_reduce,
    product_reduce,
    compose,
    curry,
    CountdownIterator,
)


class TestSumReduce:
    def test_sum(self):
        assert sum_reduce([1, 2, 3, 4]) == 10

    def test_empty(self):
        assert sum_reduce([]) == 0

    def test_generator(self):
        assert sum_reduce(x for x in range(5)) == 10


class TestProductReduce:
    def test_product(self):
        assert product_reduce([1, 2, 3, 4]) == 24

    def test_empty(self):
        assert product_reduce([]) == 1


class TestCompose:
    def test_compose_two(self):
        add1 = lambda x: x + 1
        double = lambda x: x * 2
        assert compose(add1, double)(5) == 11

    def test_compose_three(self):
        add1 = lambda x: x + 1
        double = lambda x: x * 2
        square = lambda x: x ** 2
        assert compose(add1, double, square)(3) == 19


class TestCurry:
    def test_curry_two(self):
        @curry
        def add(a, b):
            return a + b

        assert add(2)(3) == 5

    def test_curry_direct(self):
        @curry
        def add(a, b):
            return a + b

        assert add(2, 3) == 5


class TestCountdownIterator:
    def test_countdown(self):
        assert list(CountdownIterator(5)) == [5, 4, 3, 2, 1]

    def test_countup(self):
        assert list(CountdownIterator(3, 6)) == [3, 4, 5, 6]

    def test_len(self):
        assert len(CountdownIterator(5)) == 5

    def test_next_manually(self):
        it = CountdownIterator(3)
        assert next(it) == 3
        assert next(it) == 2
        assert next(it) == 1
        with pytest.raises(StopIteration):
            next(it)

    def test_repr(self):
        assert repr(CountdownIterator(5)) == "CountdownIterator(5, 1)"
