"""
Тимофей ищет место, чтобы построить себе дом.
Улица, на которой он хочет жить, имеет длину n, то есть состоит из n одинаковых
идущих подряд участков. Каждый участок либо пустой, либо на нём уже построен дом.

Общительный Тимофей не хочет жить далеко от других людей на этой улице.
Поэтому ему важно для каждого участка знать расстояние до ближайшего
пустого участка.
Если участок пустой, эта величина будет равна нулю — расстояние до самого себя.

Помогите Тимофею посчитать искомые расстояния.
Для этого у вас есть карта улицы. Дома в городе Тимофея нумеровались
в том порядке, в котором строились, поэтому их номера на карте никак
не упорядочены. Пустые участки обозначены нулями.
"""

from typing import List, Tuple


def read_input() -> Tuple[int, List[int]]:
    street_len = int(input())
    building_numbers = list(map(int, input().strip().split()))
    return street_len, building_numbers


def get_distance(street_len: int, empty_positions: List[int]) -> List[int]:
    result = []
    RANGE_ENDFIX = 1
    if empty_positions[0] > 0:
        # Прописываем дальность, если 0 не вначале
        result.extend(range(empty_positions[0] + RANGE_ENDFIX)[:0:-1])

    for count, empty_position in enumerate(empty_positions[:-1], start=1):
        # Находим длину до след точки
        # (включительно, чтобы не нагромождать дальше конструкциями)
        distance_between_empty = empty_positions[count] - empty_position
        # Ищем значение середины, т.к. пик дальности
        distance_range = range(int(distance_between_empty / 2) + RANGE_ENDFIX)
        # Прописываем значения до пика
        result.extend(distance_range[:])

        # Делаем реверс
        if distance_between_empty % 2 == 0:
            # не включая сам пик, т.к. между точками количество не четное
            result.extend(distance_range[-2:0:-1])
        else:
            # и на оборот
            result.extend(distance_range[:0:-1])

    # В самом конце добавляем окончание
    result.extend(range(street_len - empty_positions[-1]))

    return result


if __name__ == '__main__':
    street_len, build_numbers = read_input()
    # Создаем список с местами пустых значений
    empty_positions = [
        count for count, val in enumerate(build_numbers) if val == 0
    ]
    print(" ".join(map(str, get_distance(street_len, empty_positions))))
