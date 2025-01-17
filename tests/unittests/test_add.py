import pytest


@pytest.mark.parametrize(
    "first,second,expected",
    [
        (0, 0, 0),
        (0, 1, 1),
        (1, 1, 2),
        (2, 3, 5),
        (1, -1, 0),
        (0, 10, 10),
    ]
)
def test_add(first, second, expected):
    from my_lib_gens import add

    assert add(first, second) == expected

