from Challanges.find_index_nearest import find_index_of_nearest


def test_find_index_of_solution():
    assert find_index_of_nearest(2, []) is None
    assert find_index_of_nearest(0, [10]) == 0
    assert find_index_of_nearest(0, [10, 15]) == 0
    assert find_index_of_nearest(1, [15, 10]) == 1
    assert find_index_of_nearest(12, [15, 10]) == 1
    assert find_index_of_nearest(0, [15, 10, 3, 4]) == 2
    assert find_index_of_nearest(4, [7, 5, 3, 2]) == 1
    assert find_index_of_nearest(4, [7, 5, 4, 4, 3, 6]) == 2
