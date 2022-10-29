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
    for count, empty_position in enumerate(empty_positions, start=1):
        if count == 1 and empty_position > 0:
            result.extend(range(empty_position+1)[:-0:-1])
        if count == len(empty_positions):
            result.extend(range(street_len-empty_position))
            break

        distance_between_empty = abs(empty_position - empty_positions[count])
        range_endfix = 1
        distance_range = range(int(distance_between_empty/2) + range_endfix)
        result.extend(distance_range[:])
        if distance_between_empty > 1 + range_endfix:
            if distance_between_empty % 2 == 0:
                result.extend(distance_range[-2:0:-1])
            else:
                result.extend(distance_range[:-0:-1])
    return result


if __name__ == '__main__':
    street_len, build_numbers = read_input()
    empty_positions = [
        count for count, val in enumerate(build_numbers) if val == 0
    ]
    print(" ".join(map(str, get_distance(street_len, empty_positions))))
