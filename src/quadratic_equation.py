import math

from settings import epsilon


def solve(a: float, b: float, c: float) -> list[float]:
    """
    Функция нахождения корней квадратного уравнения ax^2+b*x+c = 0
    :param a: коэффициент при x^2 (не должен быть равен 0)
    :param b: коэффициент при x
    :param c: свободный член уравнения
    :return: Список из найденных корней
    """
    result = []

    for coefficient in [a, b, c]:
        if math.isinf(coefficient):
            raise ValueError(f'Коэффициенты должны быть вещественными числами, а не бесконечностью')
        elif math.isnan(coefficient):
            raise ValueError(f'Значения коэффициентов должны быть числовыми, а не неопределенными (NaN)')

    if abs(a) < epsilon:
        raise ZeroDivisionError('Коэффициент \'a\' не может быть равен \'0\'')

    d = b**2 - (4*a*c)
    if d > epsilon:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return [x1, x2]
    elif abs(d) < epsilon:
        x = (-b)/(2 * a)
        return [x,]
    return result
