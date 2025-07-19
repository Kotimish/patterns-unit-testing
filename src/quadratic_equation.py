import math


def solve(a: float, b: float, c: float) -> list[float]:
    """
    Функция нахождения корней квадратного уравнения ax^2+b*x+c = 0
    :param a: коэффициент при x^2 (не должен быть равен 0)
    :param b: коэффициент при x
    :param c: свободный член уравнения
    :return: Список из найденных корней
    """
    D = b**2 - (4*a*c)
    if D <= 0:
        return []
    return []
