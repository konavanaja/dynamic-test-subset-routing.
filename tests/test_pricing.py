from src.pricing import total_price, apply_discount


def test_total_price():
    assert total_price(20, 3) == 60


def test_apply_discount():
    assert apply_discount(100, 10) == 90
