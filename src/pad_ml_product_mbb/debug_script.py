"""Скрипт для отладки линтера, форматтера и тайпчекера."""

import os
import sys


def calculate_discount(price: float, discount: float) -> float:
    if not (0 <= discount <= 1):
        raise ValueError("Скидка должна быть в диапазоне от 0 до 1")
    return price * (1 - discount)


def main() -> None:
    final_price = calculate_discount(100.0, 0.2)
    print(f"Итоговая цена: {final_price}")

    # Специально для ошибки
    # bad_price = calculate_discount("100", 0.1)


if __name__ == "__main__":
    main()
