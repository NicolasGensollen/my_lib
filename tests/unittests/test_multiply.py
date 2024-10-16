import pytest


@pytest.mark.parametrize(
    "first,second,expected",
    [
        (0, 0, 0),
        (0, 1, 0),
        (1, 1, 1),
        (2, 3, 6),
        (1, -1, -1),
    ]
)
def test_mult(first, second, expected):
    from my_lib_gens import mult

    assert mult(first, second) == expected

