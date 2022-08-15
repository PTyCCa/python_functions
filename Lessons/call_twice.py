"""Вам предстоит реализовать функцию call_twice(), которая должна

принять функцию и произвольный набор аргументов для неё,
вызвать функцию с заданными аргументами дважды,
вернуть пару из результатов вызовов (первый, затем второй)."""

def call_twice(function, *args, **kwargs):
    result1 = function(*args, **kwargs)
    result2 = function(*args, **kwargs)
    return result1, result2
# END