"""
Вася реализовал функцию, которая переводит целое число из десятичной системы
в двоичную. Но, кажется, она получилась не очень оптимальной.

Попробуйте написать более эффективную программу.

Не используйте встроенные средства языка по переводу чисел в бинарное
представление.
"""


def to_binary(number: int) -> str:
    if number == 0:
        return '0'
    result = ''
    while number:
        result += str(number % 2)
        number //= 2
    return result[::-1]


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
