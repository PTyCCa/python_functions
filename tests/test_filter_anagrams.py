from itertools import permutations

from Challanges.filter_anagrams import filter_anagrams


def test_filter_anagrams_with_strings():
    empty = ''
    assert list(filter_anagrams(empty, [empty, 'foo', empty])) == [empty, empty]

    assert list(filter_anagrams('laser', ['lazing', 'lazy', 'lacer'])) == []

    assert list(filter_anagrams(
        'abba', ['aabb', 'abcd', 'bbaa', 'dada'],
    )) == ['aabb', 'bbaa']

    assert list(filter_anagrams(
        'racer', ['crazer', 'carer', 'racar', 'caers', 'racer'],
    )) == ['carer', 'racer']


def test_filter_anagrams_with_tuples():
    assert list(filter_anagrams((), [(), ()])) == [(), ()]

    tri = (1, 2, 3)
    irt = tuple(reversed(tri))
    assert list(filter_anagrams(
        tri, [tri, irt, tri + (4,)],
    )) == [tri, irt]


def test_filter_anagrams_with_false_anagrams():
    assert list(filter_anagrams('bob', ['boo', 'bo', 'obbo'])) == []


def test_filter_anagrams_with_permutations():
    sample = tuple('abcd')
    sample_permutations = list(permutations(sample))
    # ^ [('a', 'b', 'c', 'd'), ('a', 'b', 'd', 'c'), ...
    # ...('d', 'c', 'a', 'b'), ('d', 'c', 'b', 'a')]
    assert len(list(filter_anagrams(
        sample, sample_permutations,
    ))) == len(sample_permutations)