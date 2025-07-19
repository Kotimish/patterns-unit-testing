import math


def solve(a: float, b: float, c: float) -> list[float]:
    """
    Функция нахождения корней квадратного уравнения ax^2+b*x+c = 0
    :param a: коэффициент при x^2 (не должен быть равен 0)
    :param b: коэффициент при x
    :param c: свободный член уравнения
    :return: Список из найденных корней
    """
    result = []
    d = b**2 - (4*a*c)
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return [x1, x2]
    elif d == 0:
        x = (-b)/(2 * a)
        return [x,]
    return result
