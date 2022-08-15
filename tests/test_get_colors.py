from Lessons.get_colors import get_colors, rgb


def test_colors():
    colors = get_colors()
    assert set(colors.keys()) == {'red', 'green', 'blue'}
    assert colors['red'] == rgb(red=255)
    assert colors['green'] == rgb(green=255)
    assert colors['blue'] == rgb(blue=255)