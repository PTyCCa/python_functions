"""Вам нужно реализовать функцию greet, которая должна принимать несколько имён (как минимум одно!) и возвращать строку приветствия."""

# BEGIN
def greet(who, *args):
    names = ' and '.join((who,) + args)
    return 'Hello, {}!'.format(names)
# END