"""
Рита и Гоша играют в игру.
У Риты есть n фишек, на каждой из которых написано количество очков.
Сначала Гоша называет число k, затем Рита должна выбрать две фишки,
сумма очков на которых равна заданному числу.

Рите надоело искать фишки самой, и она решила применить свои навыки
программирования для решения этой задачи.
Помогите ей написать программу для поиска нужных фишек.
"""

from typing import List, Tuple, Optional


def two_sum(len_arr: int, arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    for i in range(len_arr):
        for j in range(i+1, len_arr):
            if arr[i]+arr[j] == target_sum:
                return arr[i], arr[j]
    return None, None


def read_input() -> Tuple[int, List[int], int]:
    len_arr = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return len_arr, arr, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))


len_arr, arr, target_sum = read_input()
print_result(two_sum(len_arr, arr, target_sum))
