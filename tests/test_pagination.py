import pytest

from shopkit.pagination import paginate


def test_page_count_and_has_next():
    p = paginate(list(range(45)), page=1, per_page=20)
    assert p.pages == 3 and p.has_next and p.total == 45


def test_rejects_bad_arguments():
    with pytest.raises(ValueError):
        paginate([1, 2], page=0)
    with pytest.raises(ValueError):
        paginate([1, 2], per_page=0)
