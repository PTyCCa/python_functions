"""Вам предстоит реализовать декоратор, добавляющий функции мемоизацию. Мемоизация — это запоминание уже вычисленных результатов, для уже однажды встреченных аргументов.

Для простоты будем считать, что мемоизироваться будут численные функции одного аргумента (аргумент — число, результат — тоже число)."""

# BEGIN
def memoized(function):
    memory = {}

    def inner(argument):
        memoized_result = memory.get(argument)
        if memoized_result is None:
            memoized_result = function(argument)
            memory[argument] = memoized_result
        return memoized_result

    return inner
# END