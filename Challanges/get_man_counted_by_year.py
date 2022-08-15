"""Реализуйте функцию get_men_counted_by_year(), которая принимает на вход список пользователей и возвращает словарь, в котором ключ — это год рождения, а значение — количество мужчин, родившихся в этот год."""

# BEGIN
from collections import Counter
from datetime import datetime


def date_string_to_year(date_string):
    dt = datetime.strptime(date_string, '%Y-%m-%d')
    return dt.year


def get_men_counted_by_year(users):
    men = filter(lambda user: user['gender'] == 'male', users)
    birth_years = map(lambda man: date_string_to_year(man['birthday']), men)
    return dict(Counter(birth_years))
# END