"""Реализуйте функцию find_index_of_nearest(), которая принимает на вход список чисел и искомое число. Задача функции — найти в списке ближайшее число к искомому и вернуть его индекс.

Если в списке содержится несколько чисел, одновременно являющихся ближайшими к искомому числу, то возвращается наименьший из индексов ближайших чисел."""

# BEGIN
def find_index_of_nearest(number, source):
    if source:
        diff = list(map(lambda x: abs(x - number), source))
        return diff.index(min(diff))
# END

# BEGIN (write your solution here)
def distance_counter(position, neighbors):
    distance_map = {}
    for neighbor in neighbors:
        distance_map[neighbors.index(neighbor)] = abs(position - neighbor)
    minimum_distance = min(distance_map.values())

    return (distance_map, minimum_distance)


def find_index_of_nearest_2(position, neighbors):
    if neighbors:
        neighbors_map, nearest_nieghbor = distance_counter(position, neighbors)

        return min(
            [
                key for key, value in neighbors_map.items() if
                value == nearest_nieghbor
            ],
        )

# END