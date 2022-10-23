"""
Представьте себе онлайн-игру для поездки в метро: игрок нажимает на кнопку,
и на экране появляются три случайных числа.
Если все три числа оказываются одной чётности, игрок выигрывает.

Напишите программу, которая по трём числам определяет, выиграл игрок или нет.
"""


def check_parity(*args) -> bool:
    last_parity = args[0] % 2
    for i in args[1:]:
        if i%2 != last_parity:
            return False
    return True


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")


a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
