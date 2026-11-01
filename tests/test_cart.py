from src.cart import add_item, item_count


def test_add_item():
    assert add_item(["pen"], "book") == ["pen", "book"]


def test_item_count():
    assert item_count(["pen", "book"]) == 2
