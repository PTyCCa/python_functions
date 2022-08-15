"""Анаграммы — это слова, которые состоят из одинаковых букв. Например:

спаниель — апельсин
карат — карта — катар
топор — ропот — отпор
src/solution.py
Реализуйте функцию filter_anagrams(), которая находит все слова-анаграммы. Функция принимает исходное слово и последовательность (iterable) слов для проверки, а возвращает последовательность анаграмм.

Я использовал в абзаце "слова" только для краткости. Строго говоря, ваша функция должна уметь находить анаграммы любых последовательностей, в том числе списков и кортежей. То есть решение должно быть максимально общим.

>>> list(filter_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
['aabb', 'bbaa']
>>> list(filter_anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
['carer', 'racer']
>>> list(filter_anagrams('laser', ['lazing', 'lazy',  'lacer']))
[]
>>> list(filter_anagrams([1, 2], [[2, 1], [2, 2], [1, 2]]))
[[2, 1], [1, 2]]"""


# BEGIN
def normalized(string):
    return list(sorted(string))


def filter_anagrams(word, words):
    norm = normalized(word)
    return filter(lambda item: normalized(item) == norm, words)
# END

# BEGIN (write your solution here)
def filter_anagrams_2(word, search_list):
    """Search for possible anagrams."""
    return [x for x in search_list if sorted(list(word)) == sorted(list(x))]  # noqa C414
# END