from src.inventory import available, remaining


def test_available():
    assert available(10, 4) is True


def test_remaining():
    assert remaining(10, 4) == 6
