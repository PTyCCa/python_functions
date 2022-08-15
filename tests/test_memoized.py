from Lessons.memoized import memoized


def test_memoized():
    counter = [0]

    @memoized
    def xor(byte):
        counter[0] += 1
        return 255 ^ byte

    assert xor(xor(42)) == 42
    assert counter == [2], "At this moment xor should be called twice"

    assert xor(42) + xor(xor(42)) == 255
    assert counter == [2], "No extra xor calls should be happened"

    assert xor(127) == 128
    assert xor(128) == 127
    assert counter == [4], "Total number of calls should be four"


def test_memoized_independency():
    @memoized
    def double(x):
        return x * 2

    @memoized
    def triple(x):
        return x * 3

    argument = 42
    first_result = double(argument)
    second_result = triple(argument)
    assert argument * 3 != first_result, (
        "First function should not provide result for the second one"
    )
    assert double(argument) != second_result, (
        "Second function should not affect memory of first function"
    )