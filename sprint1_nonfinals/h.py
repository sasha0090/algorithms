"""
Тимофей записал два числа в двоичной системе счисления и попросил Гошу вывести
их сумму, также в двоичной системе.
Встроенную в язык программирования возможность сложения двоичных чисел применять
нельзя. Помогите Гоше решить задачу.

Решение должно работать за O(N), где N –— количество разрядов максимального
числа на входе.
"""

from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    diff_num = len(first_number) - len(second_number)
    if diff_num != 0:
        if diff_num > 0:
            second_number = diff_num * '0' + second_number
        else:
            first_number = abs(diff_num) * '0' + first_number

    result = ''
    trace_num = 0
    for i in range(len(first_number))[::-1]:
        sum_num = int(first_number[i]) + int(second_number[i]) + trace_num
        trace_num = 0

        if sum_num > 1:
            trace_num = 1
            sum_num -= 2
        result += str(sum_num)

    if trace_num == 1:
        result += '1'

    return result[::-1]


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
