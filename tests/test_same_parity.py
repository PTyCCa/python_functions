from Challanges.same_parity import same_parity_filter


def test_same_parity_filter():
    assert same_parity_filter([5, 0, 1, -3, 10]) == [5, 1, -3]
    assert same_parity_filter([2, 0, 1, -3, 10, -2]) == [2, 0, 10, -2]
    assert same_parity_filter([-1, 0, 1, -3, 10, -2]) == [-1, 1, -3]
    assert same_parity_filter([10, -1.5, 1.3, -3, 25, -2]) == [10, -2]
    assert same_parity_filter([]) == []