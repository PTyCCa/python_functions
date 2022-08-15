from Challanges.rgb2hex import hex2rgb, rgb2hex

cases = [
    ('#000000', (0, 0, 0)),
    ('#ffffff', (255, 255, 255)),
    ('#00840c', (0, 132, 12)),
    ('#24ab00', (36, 171, 0)),
    ('#c60123', (198, 1, 35)),
    ('#543fab', (84, 63, 171)),
    ('#f700de', (247, 0, 222)),
]


def test_compose_hex():
    for hex_, rgb in cases:
        r, g, b = rgb
        assert rgb2hex(r, g, b) == hex_
    assert rgb2hex(r=84, g=63, b=171) == '#543fab'
    assert rgb2hex(r=247, b=222, g=0) == '#f700de'


def test_compose_rgb():
    for hex_, rgb in cases:
        r, g, b = rgb
        assert hex2rgb(hex_) == {'r': r, 'g': g, 'b': b}
