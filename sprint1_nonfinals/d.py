"""
Метеорологическая служба вашего города решила исследовать погоду новым способом.

Под температурой воздуха в конкретный день будем понимать максимальную
температуру в этот день.
Под хаотичностью погоды за n дней служба понимает количество дней,
в которые температура строго больше, чем в день до (если такой существует)
и в день после текущего (если такой существует).
Например, если за 5 дней максимальная температура воздуха составляла
[1, 2, 5, 4, 8] градусов, то хаотичность за этот период
равна 2: в 3-й и 5-й дни выполнялись описанные условия.
Определите по ежедневным показаниям температуры хаотичность погоды
за этот период.

Заметим, что если число показаний n=1, то единственный день будет хаотичным.
"""


from typing import List, Tuple


def get_weather_randomness(n, temp: List[int]) -> int:
    if n == 1:
        return 1

    chaotic_days = 0

    if temp[0] > temp[1]:
        chaotic_days += 1
    if temp[n-1] > temp[n-2]:
        chaotic_days += 1

    for i in range(1, n-1):
        if temp[i-1] < temp[i] and temp[i] > temp[i+1]:
            chaotic_days += 1
    return chaotic_days


def read_input() -> Tuple[int, List[int]]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return n, temperatures

n, temperatures = read_input()
print(get_weather_randomness(n, temperatures))
