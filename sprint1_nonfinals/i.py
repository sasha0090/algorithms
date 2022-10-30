"""
Напишите программу, которая определяет,
будет ли положительное целое число степенью четвёрки.

Подсказка: степенью четвёрки будут все числа вида 4n,
где n – целое неотрицательное число.
"""


def is_power_of_four(number: int) -> bool:
    while number >= 4:
        number /= 4

    return number == 1


print(is_power_of_four(int(input())))
