"""
Игра «Тренажёр для скоростной печати» представляет собой поле из клавиш 4x4.
В нём на каждом раунде появляется конфигурация цифр и точек.
На клавише написана либо точка, либо цифра от 1 до 9.

В момент времени t игрок должен одновременно нажать на все клавиши, на которых
написана цифра t.
Гоша и Тимофей могут нажать в один момент времени на k клавиш каждый.
Если в момент времени t нажаты все нужные клавиши, то игроки получают 1 балл.

Найдите число баллов, которое смогут заработать Гоша и Тимофей,
если будут нажимать на клавиши вдвоём.
"""

from typing import List, Tuple


def read_input() -> Tuple[int, List[str]]:
    field_len = 4

    keys_push = int(input()) * 2
    field_keys = []
    for _ in range(field_len):
        field_keys.extend(list(input().strip()))
    return keys_push, field_keys


def find_num_points(keys_push: int, field_keys: List[str]) -> int:
    keys_set = set(field_keys)
    keys_set.discard('.')
    my_dict = {i: field_keys.count(i) for i in keys_set}
    points = 0
    for val in my_dict.values():
        if val <= keys_push:
            points += 1
    return points


if __name__ == '__main__':
    keys_push, field_keys = read_input()
    print(find_num_points(keys_push, field_keys))
