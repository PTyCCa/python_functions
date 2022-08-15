"""Реализуйте функцию-предикат is_valid_ipv6(), которая проверяет IPv6-адреса (адреса шестой версии интернет протокола) на корректность. Функция принимает на вход строку с адресом IPv6 и возвращает True, если адрес корректный, и False, если нет.

Дополнительные условия:

Работа функции не зависит от регистра символов.
Ведущие нули в группах цифр необязательны.
Самая длинная последовательность групп нулей, например, :0:0:0: может быть заменена на два двоеточия ::. Такую замену можно произвести только один раз.
Одна группа нулей :0: не может быть заменена на ::.
>>> from solution import is_valid_ipv6
>>> is_valid_ipv6('10:d3:2d06:24:400c:5ee0:be:3d')
True
>>> is_valid_ipv6('::1')
True
>>> is_valid_ipv6('2607:G8B0:4010:801::1004')
False
>>> is_valid_ipv6('2.001::')
False
>>> 
Подсказки
IPv6
Для реализации проверки пограничных случаев изучите список IP-адресов в модуле с тестами.
Используйте константу string.hexdigits для проверки, что строка содержит валидное представление шестнадцатеричного числа."""

# BEGIN
def is_valid_group(group):
    if len(group) > 4:
        return False
    # Handle the error
    # https://docs.python.org/3/tutorial/errors.html
    try:
        decimal = int(group, 16)
    except ValueError:
        return False
    return decimal < 2 ** 16


def is_valid_ipv6(ipv6):
    if ipv6.count('::') > 1:
        return False

    groups = []

    for group in filter(None, ipv6.split('::')):
        groups.extend(group.split(':'))

    is_full = '::' not in ipv6
    length = len(groups) if is_full else len(groups) + 2
    if length > 8 or (is_full and length < 8):
        return False

    return False not in map(is_valid_group, groups)
# END

# BEGIN (write your solution here)
from collections import Counter
from ipaddress import IPv6Address, ip_address  # noqa I001 


def is_valid_ipv6_2(ip):
    """Check if IP is IPv6."""
    d = Counter(ip)[':']

    if d == 7 and '::' in ip:
        return False

    try:
        if isinstance((ip_address(ip)), IPv6Address):
            return True
    except ValueError:
        return False

# END