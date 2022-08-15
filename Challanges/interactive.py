"""Это испытание имеет повышенную сложность. Вам предстоит реализовать два декоратора, образующих маленький DSL, позволяющий превращать обычные функции в интерактивные программы.

Декоратор asks() добавляет описание одного из аргументов преобразуемой функции. Для каждого аргумента нужен будет отдельный вызов asks(). Важный момент: порядок появления запросов во время диалога с пользователем должен соответствовать порядку расположения декораторов в файле (а не порядку их фактического применения) — смотрите пример ниже.

После того, как все аргументы преобразуемой функции будут описаны с помощью asks(), применяется декоратор interactive(). После его применения результирующая функция перестаёт принимать аргументы и возвращать результат (None в итоге возвращается, конечно), зато начинает общаться с пользователем.

Обе функции в модуле уже объявлены, но не реализованы. Вам нужно будет написать "тела" этих функций. Обе функции снабжены docstrings (в порядке исключения — на русском языке), которые поясняют назначение аргументов каждой функции."""

def simple_input(_, prompt):
    """Just input string."""
    return input(prompt)  # noqa: S322, WPS421


def asks(name, prompt):
    """
    Описывает один запрос аргумента.

    Arguments:
        name - имя аргумента оборачиваемой функции,

        prompt - текст приглашения.

    Returns:
        декоратор, который и обернёт нужную функцию. Помните, после
        описания всех аргументов нужно результат обернуть в
        декоратор interactive!

    """
    # BEGIN
    def wrapper(function):
        function.questions = (
            (name, prompt),
        ) + getattr(function, 'questions', ())
        return function
    return wrapper
    # END


def interactive(
    description,
    input_function=simple_input,
    output_function=print,  # noqa: T002
):
    """
    Делает функцию с описанными параметрами интерактивной.

    Интерактивной может быть функция без параметров. В этом случае декоратор
    asks не потребуется.

    Arguments:
        description - описание, которое будет выведено в начале
        диалога (интерактивной сессии).

        input_function - функция, принимающая имя аргумента и приглашение,
        и возвращающая введённый пользователем текст (str).

        output_function - функция, которая будет использована для вывода
        описания и результата вызова оборачиваемой функции.

    Returns:
        декоратор, который обернёт целевую функцию.

    """
    # BEGIN
    def wrapper(function):
        def inner():
            questions = getattr(function, 'questions', ())
            output_function(description)
            kwargs = {}
            for argument, prompt in questions:
                kwargs[argument] = input_function(argument, prompt)
            return output_function(
                function(**kwargs),
            )
        return inner
    return wrapper
    # END


@interactive('Calculator')
@asks('x', 'Enter first number: ')
@asks('y', 'Enter second number: ')
def calc(x, y):
    return int(x) + int(y)


if __name__ == '__main__':
    calc()