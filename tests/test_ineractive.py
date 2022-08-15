from Challanges.interactive import asks, interactive


def non_interactive(**kwargs):
    """
    Заменяет собой interactive, симулируя диалог с пользователь.

    Вместо запросов на ввод будут подставлены указанные значения,
    а функция в итоге вернёт результат вызова оригинальной функции.

    Arguments:
        kwargs - параметры для подстановки. Значения должны быть строками.

    Returns:
        декоратор, который обернёт нужную функцию.

    """
    def wrapper(function):
        def inner():
            output = []
            interactive(
                '',
                input_function=lambda key, _: kwargs[key],
                output_function=output.append,
            )(function)()
            return output[1]  # нужен только "выведенный" результат
        return inner
    return wrapper


def test_interactive():
    def should_not_input(*_):
        raise AssertionError("Shouldn't ask for input")

    output = []

    @interactive(
        'Foo',
        input_function=should_not_input,
        output_function=output.append,
    )
    def bar():
        return 'Bar'

    assert bar() is None, "Interactive function should not return something!"
    assert output == ['Foo', 'Bar']


def test_non_interactive():
    @non_interactive()
    def foo():
        return 42

    assert foo() == 42


def test_asks():
    @non_interactive(x='42', y='57')
    @asks('x', 'Enter first number: ')
    @asks('y', 'Enter second number: ')
    def add(x, y):
        return int(x) + int(y)

    assert add() == 99


def test_asks_order():
    order = []

    @interactive(
        '',
        input_function=lambda key, _: order.append(key) or '',
        output_function=lambda _: None,
    )
    @asks('a', '?')
    @asks('b', '??')
    def two_args(a, b):
        return a + b

    two_args()
    assert order == ['a', 'b'], "Questions should be asked in ceratin order!"
