"""Тесты декораторов."""

import pytest
from src.lab4.decorators import log_calls, timer


class TestLogCalls:
    def test_logs_call(self, caplog):
        @log_calls
        def add(a, b):
            return a + b

        with caplog.at_level("INFO"):
            result = add(2, 3)

        assert result == 5
        assert "add(2, 3)" in caplog.text

    def test_logs_kwargs(self, caplog):
        @log_calls
        def greet(name, greeting="Привет"):
            return f"{greeting}, {name}!"

        with caplog.at_level("INFO"):
            result = greet("Иван", greeting="Здравствуй")

        assert result == "Здравствуй, Иван!"

    def test_logs_error(self, caplog):
        @log_calls
        def divide(a, b):
            return a / b

        with caplog.at_level("ERROR"):
            with pytest.raises(ZeroDivisionError):
                divide(1, 0)

        assert "ZeroDivisionError" in caplog.text

    def test_preserves_metadata(self):
        @log_calls
        def my_func():
            """Docstring."""
            pass

        assert my_func.__name__ == "my_func"


class TestTimer:
    def test_measures_time(self, capsys):
        @timer
        def slow():
            import time
            time.sleep(0.05)

        slow()
        captured = capsys.readouterr()
        assert "slow" in captured.out

    def test_preserves_metadata(self):
        @timer
        def my_func():
            pass

        assert my_func.__name__ == "my_func"
