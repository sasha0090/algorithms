"""
Даны два массива чисел длины n.
Составьте из них один массив длины 2n, в котором числа из входных массивов
чередуются (первый — второй — первый — второй — ...).
При этом относительный порядок следования чисел из одного массива должен быть
сохранён.
"""

from typing import List, Tuple


def zipper(a: List[int], b: List[int], n: int) -> List[int]:
    zip_result = []
    for i in range(n):
        zip_result.extend([a[i], b[i]])
    return zip_result


def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b, n


a, b, n = read_input()
print(" ".join(map(str, zipper(a, b, n))))