from src.quadratic_equation import solve


def test_no_roots():
    result = solve(1, 0, 1)
    assert len(result) == 0

def test_two_roots():
    result = solve(1, 0, -1)
    assert sorted(result) == sorted([1, -1])
