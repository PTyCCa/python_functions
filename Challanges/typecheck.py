"""Внимание, испытание повышенной сложности!

Аннотации функций

В Python с версии 3.0 существует синтаксис, позволяющий дополнить описание аргумента функции аннотацией. Выглядит это так:

def multiply(times: int, value: str) -> str:
    return value * times
Здесь через : указаны аннотации для аргументов, а -> указывает тип возвращаемого значения. Аннотацией может быть любое Python-выражение. Сам Python вычисляет значения выражений в момент выполнения блока кода, в котором объявлена функция (в этот момент выполнится print в примере ниже) и сохраняет аннотации в атрибуте __annotations__ объекта функции.

В дальнейшем сам интерпретатор никак эти значения не использует, но их может использовать программист! Вот как выглядят аннотации с точки зрения интерпретатора:

>>> def f(
...     x: 1 + 2,
...     y: print("Hello!"),
...     z: "this is zet!",
...     foo: {'a': 42, 'b': 'bar'}
... ):
...     pass
...
Hello!
>>> f.__annotations__
{'x': 3, 'y': None, 'z': 'this is zet!', 'foo': {'a': 42, 'b': 'bar'}}
Как видите, это просто словарь, где ключи — имена аргументов, а значения — результаты вычисления выражений-аннотаций!

Подробнее об аннотациях функций можно почитать в соответствующем "PEP 3107 - Function Annotations".

src/solution.py
Вам предстоит написать пару декораторов, выполняющих проверку типов аргументов согласно их (аргументов) аннотациям. Если при вызове функции тип какого-либо значения не соответствует указанному в аннотации типу аргумента, обёрнутая функция не должна быть вызвана. Вместо этого декоратор должен вернуть соответствующую ошибку.

Требуемые для реализации функции уже объявлены в модуле, но не реализованы. docstrings функций описывают (в порядке исключения — на русском) принимаемые функциями аргументы. Можете считать эти "болванки" функций техническим заданием :)

Уточняю несколько моментов:

функция typecheck() останавливает выполнение (и проверку) на первой ошибке типизации;
функция typecheck_all() проверяет все аргументы, накапливая ошибки, и лишь потом останавливает выполнение, если ошибки были;
обе функции оборачивают только функции, принимающие именованные аргументы;
аннотации должны быть простыми типами, чтобы можно было проверить соответствие типа с помощью вызова isinstance(value, some_type).
Постарайтесь выразить typecheck_all() через typecheck(). Это непросто, но интересно!"""

from functools import wraps  # не забываем правильно оборачивать!


def format_error(error):
    """Format type violation message."""
    argument, value, expected_type = error
    return (
        'Bad argument type for argument "{name}":'
        ' {type} instead of {expected}'.format(  # noqa: WPS326
            name=argument,
            type=type(value),
            expected=expected_type,
        )
    )


def throw_error(*args):
    """Raise one typing violation."""
    raise TypeError(format_error(args))


def throw_errors(errors):
    """Raise one error for all typing violations."""
    raise TypeError('\n'.join(map(format_error, errors)))


def typecheck(error_callback=throw_error):
    """
    Добавляет к функции предусловие, проверяющие типы аргументов.

    Проверка типов делается на основе аннотаций, указанных в сигнатуре
    оборачиваемой функции.

    Arguments:
        error_callback - функция, получающая информацию об ошибке типизации.
        Функция принимает имя аргумента, значение и ожидаемый тип.
        Обычно error_callback ничего не возвращает, а вместо этого возбуждает
        исключение (см. реализацию по умолчанию - throw_error).

    Returns:
        Декоратор, добавляющий проверку типов к функции.

    """
    # BEGIN
    def wrapper(function):
        @wraps(function)
        def inner(**kwargs):
            contract = function.__annotations__  # noqa: WPS609
            for argument, value in kwargs.items():
                types = contract.get(argument)
                if types is not None and not isinstance(value, types):
                    error_callback(argument, value, types)
            return function(**kwargs)
        return inner
    return wrapper
    # END


def typecheck_all(error_callback=throw_errors):
    """
    Добавляет к функции предусловие, проверяющие типы аргументов.

    Проверка типов делается на основе аннотаций, указанных в сигнатуре
    оборачиваемой функции.

    Arguments:
        error_callback - функция, получающая информацию об ошибке типизации.
        Функция принимает список кортежей, описывающих все ошибки типизации.
        Каждый кортеж содержит имя аргумента, значение и ожидаемый тип.
        Обычно error_callback ничего не возвращает, а вместо этого возбуждает
        исключение (см. реализацию по умолчанию - throw_errors).

    Returns:
        Декоратор, добавляющий проверку типов к функции.

    """
    # BEGIN
    def wrapper(function):
        @wraps(function)
        def inner(**kwargs):
            errors = []

            @wraps(function)  # __annotations__ тоже копируются
            def wrapped(**kwargs):
                if errors:
                    error_callback(errors)
                return function(**kwargs)

            return typecheck(
                lambda *args: errors.append(args),
            )(wrapped)(**kwargs)
        return inner
    return wrapper
    # END


if __name__ == '__main__':
    @typecheck_all()
    def multiply(times: int, value: (str, tuple)):
        return value * times

    print(multiply(times=10, value=(42,)))
    print(multiply(times=10, value='1'))

    # оба аргумента — не того типа
    print(multiply(times='12', value=None))