from Lessons.memoizing import memoizing


def test_memoizing():
    arguments = []

    @memoizing(3)
    def inc(argument):
        arguments.append(argument)
        return argument + 1

    assert inc(inc(inc(0))) == 3
    assert arguments == [0, 1, 2]

    _ = inc(inc(inc(0)))  # noqa: WPS122
    assert arguments == [0, 1, 2], "All resluts sholud be got from memory!"

    assert inc(10) == 11
    assert arguments == [0, 1, 2, 10], "New argument should be added!"

    assert inc(0) == 1
    assert arguments == [0, 1, 2, 10, 0], (
        "Result for zero should be recalculated!",
    )


def test_memoizing_wrapping():
    @memoizing(3)
    def foo():
        """Return bar."""

    assert foo.__name__ == "foo", (
        "Wrapper should preserve function's name!",
    )
    assert foo.__doc__ == "Return bar.", (
        "Wrapper should preserve function's docstring!",
    )