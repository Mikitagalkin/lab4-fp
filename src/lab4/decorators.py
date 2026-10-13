"""Декораторы для логирования и замера времени."""

import functools
import time
import logging
from typing import Callable, Any


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

logger = logging.getLogger(__name__)


def log_calls(func: Callable) -> Callable:
    """Декоратор, который логирует вызов функции и результат."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        args_str = ", ".join(
            [repr(a) for a in args] + [f"{k}={v!r}" for k, v in kwargs.items()]
        )
        logger.info(f"Вызов: {func.__name__}({args_str})")

        try:
            result = func(*args, **kwargs)
            logger.info(f"Результат: {func.__name__}({args_str}) -> {result!r}")
            return result
        except Exception as e:
            logger.error(f"Ошибка в {func.__name__}: {type(e).__name__}: {e}")
            raise

    return wrapper


def timer(func: Callable) -> Callable:
    """Декоратор, который замеряет время выполнения функции."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} выполнилась за {elapsed:.4f} сек")
        return result

    return wrapper
