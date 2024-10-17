import pytest


@pytest.mark.parametrize(
    "first,second,expected",
    [
        (0, 0, 0),
        (0, 1, -1),
        (1, 1, 0),
        (2, 3, -1),
        (1, -1, 2),
    ]
)
def test_sub(first, second, expected):
    from my_lib_gens import sub

    assert sub(first, second) == expected

