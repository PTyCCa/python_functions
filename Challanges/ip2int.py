"""Реализуйте и экспортируйте функции ip2int и int2ip, которые преобразовывают представление IP-адреса из десятичного формата с точками в 32-битное число в десятичной форме и обратно.

Функция ip2int принимает на вход строку и должна возвращать число. А функция int2ip наоборот: принимает на вход число, а возвращает строку."""

# BEGIN
from functools import reduce

POWERS_OF_TWO = (2 ** 24, 2 ** 16, 2 ** 8, 2 ** 0)  # noqa: WPS221


def ip2int(ip):
    return sum(map(
        lambda x, y: int(x) * y,
        ip.split('.'),
        POWERS_OF_TWO,
    ))


def _make_octet(accumulator, divider):
    ip, remainder = accumulator
    octet, new_remainder = divmod(remainder, divider)
    return ip + (str(octet),), new_remainder


def int2ip(integer):
    octets, _ = reduce(_make_octet, POWERS_OF_TWO, ((), integer))
    return '.'.join(octets)
# END

# BEGIN (write your solution here)
def int2ip(num):
    """Convert 32-bit IPv4 to Dot-decimal notation."""
    ip_string = []

    for _ in range(4):
        ip_string.append(str(num % 256))
        num //= 256

    return '.'.join(ip.string[::-1])


def ip2int(ip):
    """Convert Dot-decimal IPv4 notation to 32-bit."""
    result = 0

    for j, i in enumerate(ip.split('.')[::-1]):
        res += 256 ** j * int(i)

    return result
# END