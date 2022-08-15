from Challanges.ip2int import int2ip, ip2int

ZEROES = '0.0.0.0'  # noqa: S104


def test_ip2int():
    assert ip2int(ZEROES) == 0
    assert ip2int('128.32.10.1') == 2149583361


def test_int2ip():
    assert int2ip(0) == ZEROES
    assert int2ip(2149583361) == '128.32.10.1'


def test_round_robin():
    assert int2ip(ip2int('192.168.1.32')) == '192.168.1.32'
    assert ip2int(int2ip(2149583361)) == 2149583361