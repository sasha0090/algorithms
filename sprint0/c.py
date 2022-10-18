"""
Вам дана статистика по числу запросов в секунду к вашему любимому
рекомендательному сервису.

Измерения велись n секунд.

В секунду i поступает qi запросов.

Примените метод скользящего среднего с длиной окна k к этим данным, и выведите
результат.
"""

from typing import List, Tuple


def moving_average(sec:int, arr: List[int], window_size: int) -> List[float]:
    result = []

    current_sum = sum(arr[0:window_size])
    result.append(current_sum / window_size)

    for i in range(0, sec - window_size):
        current_sum -= arr[i]
        current_sum += arr[i + window_size]
        current_avg = current_sum / window_size
        result.append(current_avg)
    return result


def read_input() -> Tuple[int, List[int], int]:
    sec = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return sec, arr, window_size


sec, arr, window_size = read_input()
print(" ".join(map(str, moving_average(sec, arr, window_size))))
