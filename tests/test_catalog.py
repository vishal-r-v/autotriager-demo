from shopkit.catalog import Catalog


def test_register_and_get():
    cat = Catalog()
    cat.register("mug-01", "Mug", 1200)
    assert cat.get("mug-01")["name"] == "Mug"
    assert len(cat) == 1
