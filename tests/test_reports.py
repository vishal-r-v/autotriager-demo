from shopkit.reports import customer_totals, top_customers

ORDERS = [
    {"customer_id": "acme", "total_cents": 9000},
    {"customer_id": "bob", "total_cents": 500},
    {"customer_id": "acme", "total_cents": 1000},
]


def test_customer_totals():
    assert customer_totals(ORDERS) == {"acme": 10000, "bob": 500}


def test_top_customers_includes_everyone_when_n_is_large():
    assert dict(top_customers(ORDERS, n=10)) == {"acme": 10000, "bob": 500}
