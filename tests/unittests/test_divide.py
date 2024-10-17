import pytest


@pytest.mark.parametrize(
    "first,second,expected",
    [
        (0, 1, 0),
        (1, 1, 1),
        (2, 3, 2/3),
        (1, -1, -1),
    ]
)
def test_div(first, second, expected):
    from my_lib_gens import div

    assert div(first, second) == expected


def test_div_zero_division_error():
    from my_lib_gens import div

    with pytest.raises(ZeroDivisionError):
        div(2, 0)

