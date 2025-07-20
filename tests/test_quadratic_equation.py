import pytest

from src.quadratic_equation import solve
from settings import epsilon


def test_no_roots():
    result = solve(1.0, 0.0, 1.0)
    assert len(result) == 0.0

def test_two_roots():
    result = solve(1.0, 0.0, -1.0)
    assert sorted(result) == sorted([1.0, -1.0])

@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1.0, 2.0, 1.0, [-1.0,]),
        # c = 1.0-(0.125*epsilon) - это среднее между верхней (1.0) и
        # нижней границей (1.0-0.25*epsilon) коэффициента с
        (1.0, 2.0, 1.0-(0.125*epsilon), [-1.0,]),
    ]
)
def test_one_root(a: float, b: float, c: float, expected: list[float]):
    result = solve(a, b, c)
    assert sorted(result) == sorted(expected)

def test_invalid_first_coefficient():
    with pytest.raises(ZeroDivisionError) as e:
        solve(0.0, 2.0, 1.0)
