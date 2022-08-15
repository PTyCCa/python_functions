"""Для задания цветов в HTML и CSS используются числа в шестнадцатеричной системе счисления. Чтобы не возникало путаницы в определении системы счисления, перед шестнадцатеричным числом ставят символ решетки #, например, #135278. Обозначение цвета (rrggbb) разбивается на три составляющие, где первые два символа обозначают красную компоненту цвета, два средних — зеленую, а два последних — синюю. Таким образом каждый из трех цветов — красный, зеленый и синий — может принимать значения от 00 до FF в шестнадцатеричной системе исчисления.

src/Solution.py
При работе с цветами часто нужно получить отдельные значения красного, зеленого и синего (RGB) компонентов цвета в десятичной системе исчисления и наоборот. Реализуйте функции rgb2hex() и hex2rgb(), которые конвертируют цвета в соответствующие представления цвета.

Функция rgb2hex() принимает 3 параметра (цветные компоненты) и возвращает строку. Функция должна работать как с позиционными, так и с именованными аргументами.

Функция hex2rgb() возвращает словарь со значениями компонентов."""


# BEGIN
from textwrap import wrap


def hex2rgb(color):
    r, g, b = map(lambda channel: int(channel, 16), wrap(color[1:], 2))
    return {'r': r, 'g': g, 'b': b}


def convert(channel):
    return hex(channel)[2:].rjust(2, '0')


def rgb2hex(r=None, g=None, b=None):
    return '#{}{}{}'.format(*map(convert, [r, g, b]))


# Альтернативное решение с использованием возможностей .format
# https://docs.python.org/3.4/library/string.html#format-specification-mini-language
# def rgb2hex(r=None, g=None, b=None):
#     return '#{:02x}{:02x}{:02x}'.format(r, g, b)
# END

# BEGIN (write your solution here)
def rgb2hex(r=0, g=0, b=0):
    """Enter colors and get color bytestring."""
    return f'#{r:02x}{g:02x}{b:02x}'  # noqa WPS305


def hex2rgb(str_color):
    """Convert color bytestring to color dict."""
    color = {'r': 0, 'g': 0, "b": 0}
    color['r'] = int(str_color[1:3], 16)
    color['g'] = int(str_color[3:5], 16)
    color['b'] = int(str_color[5:7], 16)

    return color

# END