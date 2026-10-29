from shopkit.customers import display_name


def test_nickname_wins():
    assert display_name({"nickname": "Ada", "first_name": "Ada", "last_name": "L"}) == "Ada"


def test_full_name_when_nickname_empty():
    assert display_name({"nickname": "", "first_name": "Grace", "last_name": "Hopper"}) == "Grace Hopper"


def test_email_fallback():
    assert display_name({"nickname": None, "email": "a@example.com"}) == "a@example.com"
