"""Тесты генераторов."""

import pytest
from src.lab4.generators import random_range, infinite_random, prime_generator


class TestRandomRange:
    def test_count(self):
        result = list(random_range(1, 10, count=5, seed=42))
        assert len(result) == 5

    def test_in_range(self):
        result = list(random_range(1, 10, count=100, seed=42))
        assert all(1 <= n <= 10 for n in result)

    def test_reproducibility(self):
        r1 = list(random_range(1, 100, count=5, seed=42))
        r2 = list(random_range(1, 100, count=5, seed=42))
        assert r1 == r2

    def test_zero_count(self):
        assert list(random_range(1, 10, count=0)) == []

    def test_invalid_count(self):
        with pytest.raises(ValueError):
            list(random_range(1, 10, count=-1))

    def test_invalid_bounds(self):
        with pytest.raises(ValueError):
            list(random_range(10, 1, count=5))


class TestInfiniteRandom:
    def test_infinite(self):
        gen = infinite_random(1, 100, seed=42)
        first_10 = [next(gen) for _ in range(10)]
        assert len(first_10) == 10

    def test_reproducibility(self):
        g1 = infinite_random(1, 100, seed=42)
        g2 = infinite_random(1, 100, seed=42)
        assert [next(g1) for _ in range(5)] == [next(g2) for _ in range(5)]


class TestPrimeGenerator:
    def test_primes_up_to_20(self):
        assert list(prime_generator(limit=20)) == [2, 3, 5, 7, 11, 13, 17, 19]

    def test_primes_up_to_2(self):
        assert list(prime_generator(limit=2)) == [2]

    def test_primes_up_to_1(self):
        assert list(prime_generator(limit=1)) == []
