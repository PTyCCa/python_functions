"""NRZI код (Non Return to Zero Invertive) — один из способов линейного кодирования. Обладает двумя уровнями сигнала и используется для передачи битовых последовательностей, содержащих только 0 и 1. NRZI применяется, например, в оптических кабелях, где устойчиво распознаются только два состояния сигнала — свет и темнота.

Принцип кодирования

При передаче логического нуля на вход кодирующего устройства передается потенциал, установленный на предыдущем такте (то есть состояние потенциала не меняется), а при передаче логической единицы потенциал инвертируется на противоположный.
Реализуйте функцию decode(), которая принимает cтроку в виде графического представления линейного сигнала и возвращает строку с бинарным кодом."""

# BEGIN
def decode(signal):
    levels = ''.join(filter(lambda x: x != '|', signal))
    # ^ удаляются "фронты" сигнала
    # кстати, можно было сделать signal.replace('|', '')
    start = signal[:1]
    # ^ угадывается уровень "в недавнем прошлом"
    return ''.join(map(
        lambda p, c: '0' if p == c else '1',
        start + levels,
        levels,
    ))
    # ^ здесь сигнал без "фронтов" сравнивается с самим собой после сдвига
    # '__¯____¯__¯¯¯'
    # '_¯____¯__¯¯¯'
    # и если сигнал изменился, то на выходе будет "1", иначе - "0"
# END

"""# BEGIN (write your solution here)
def decode(code):
    """Encode graph NRZI to binary."""
    res = []
    flag = True

    for i, j in enumerate(code):
        if j == '|':
            flag = False  # noqa F841
        elif i > 0 and code[i - 1] == '|':
            res.append('1')
        else:
            res.append('0')

    return ''.join(res)

# END"""