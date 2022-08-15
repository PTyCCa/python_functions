"""Гистограмма — это графическое представление данных в виде столбцов или колонок.

src/solution.py
Реализуйте функцию histo(), которая принимает на вход список или кортеж с числами и возвращает гистограмму в виде строки, столбцы гистограммы в ней разделены символами \n. Каждый столбец отображает количество вхождений числа в список: графически с помощью заданных символов и в виде числового значения, за исключением случаев, когда количество равно нулю.

Необязательные параметры:

min_value — определяет минимальное значение, для которого рисуется гистограмма. По умолчанию не задан, то есть верхний стобец в гистограмме соответствует минимальному из переданных чисел.

max_value — определяет максимальное значение, для которого рисуется гистограмма. По умолчанию не задан, то есть нижний столбец в гистограмме соответствует максимальному из переданных чисел.

bar_char — символ, с помощью которого создаются столбцы в гистограмме. По умолчанию — #.

Для решения используйте встроенный инструмент — Counter.

>>> print(histo([1, 1, 3, 4, 5]))                                                                                                                               
1|## 2
2|
3|# 1
4|# 1
5|# 1
>>> print(histo([1, 1, 3, 4, 5], bar_char = '*'))                                                                                                               
1|** 2
2|
3|* 1
4|* 1
5|* 1
>>> print(histo([1, 1, 3, 4, 5], min_value = 3, max_value = 4))                                                                                                 
3|# 1
4|# 1
>>> print(histo([], min_value = 1, max_value = 5))                                                                                                              
1|
2|
3|
4|
5|"""

from collections import Counter


def histo(samples, min_value=None, max_value=None, bar_char='#'):
    """Draws a horizontal histogram."""
    # BEGIN
    if min_value is None:
        min_value = min(samples)
    if max_value is None:
        max_value = max(samples)

    axis = range(min_value, max_value + 1)
    counts = Counter(samples)

    lines = map(
        lambda value, count: '{}|{}{}'.format(
            value,
            bar_char * count,
            ' ' + str(count) if count else '',
        ),
        axis,
        map(lambda key: counts[key], axis),
    )

    return '\n'.join(lines)
    # END

from collections import Counter


def histo_2(samples, min_value=None, max_value=None, bar_char='#'):
    """Draws a horizontal histogram."""
    # BEGIN (write your solution here)
    if min_value is None:
        min_value = min(samples)

    if max_value is None:
        max_value = max(samples)

    elem_count = Counter(samples)
    horiz_bar_graph = ''

    for i in range(min_value, max_value + 1):
        if i not in elem_count.keys():
            horiz_bar_graph += '{0}|\n'.format(i)
        else:
            horiz_bar_graph += '{0}|{1} {2}\n'.format(
                i, elem_count[i] * bar_char, elem_count[i],
            )
    return horiz_bar_graph[:-1]
    # END