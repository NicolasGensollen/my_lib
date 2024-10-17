import pytest


@pytest.mark.parametrize(
    "first,second,expected",
    [
        (0, 1, 0),
        (1, 1, 0),
        (2, 3, 2),
        (1, -1, 0),
    ]
)
def test_mod(first, second, expected):
    from my_lib_gens import mod

    assert mod(first, second) == expected

