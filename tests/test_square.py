from pis_poetry_showcase.main import square


def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16
    assert square(5) == 25
    assert square(6) == 36
    assert square(7) == 49
    assert square(8) == 64
    assert square(9) == 81
    assert square(10) == 100
    assert square(11) == 121
    assert square(12) == 144
