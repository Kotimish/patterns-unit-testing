from src.quadratic_equation import solve


def test_no_roots():
    result = solve(1, 0, 1)
    assert len(result) == 0
