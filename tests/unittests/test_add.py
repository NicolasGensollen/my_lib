import pytest


@pytest.mark.parametrize(
    "first,second,expected",
    [
        (0, 0, 0),
        (0, 1, 1),
        (1, 1, 2),
        (2, 3, 5),
        (1, -1, 0),
    ]
)
def test_add(first, second, expected):
    from my_lib import add

    assert add(first, second) == expected

