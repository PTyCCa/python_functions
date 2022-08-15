"""В этом упражнении вам нужно будет реализовать две функции высшего порядка, возвращающие замыкания: partial_apply и flip.

partial_apply
partial_apply принимает функцию от двух аргументов и первый аргумент, а возвращает замыкание — функцию, которая примет второй аргумент и наконец применит замкнутую функцию к обоим аргументам (и вернёт результат).

Пример использования:

>>> def greet(name, surname):
...     return 'Hello, {name} {surname}!'.format(name=name, surname=surname)
...
>>> f = partial_apply(greet, 'Dorian')
>>> f('Grey')
'Hello, Dorian Grey!'
>>>
flip
Функция flip принимает в качестве единственного аргумента функцию от двух аргументов. Возвращаемое замыкание должно также принять два аргумента, а затем применить к ним замкнутую функцию, но аргументы подставить в обратном порядке. Таким образом flip как бы "переворачивает" ("flips") исходную функцию."""

# BEGIN
def partial_apply(function, arg1):
    def inner(arg2):
        return function(arg1, arg2)
    return inner


def flip(function):
    def inner(arg1, arg2):
        return function(arg2, arg1)
    return inner
# END