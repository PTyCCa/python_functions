from Challanges.compose import compose


def add5(x):
    return x + 5


def mul3(x):
    return x * 3


def test_compose():
    assert compose(mul3, add5)(1) == 18
    assert compose(add5, mul3)(1) == 8
    assert compose(mul3, str)(1) == '111'
    assert compose(str, mul3)(1) == '3'