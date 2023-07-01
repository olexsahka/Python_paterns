"""
    Фабричный метод
любой метод который создает объект(как правило, он статичен), альтернатива конструктору, с хорошим неймингом
"""
import math
from enum import Enum


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * math.cos(theta), rho * math.sin(theta))

    def __str__(self):
        return f"x : {self.x}, y : {self.y}"
    """ Нарушает принцип открытости закрытости, потому что если систем много надо бдует модифицировать код """  # def __init__(self, a, b, system= CoordinateSystem.CARTESIAN):
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = a * math.cos(b)
    #         self.y = b * math.cos(b)


p1 = Point(2, 3)
p2 = Point.new_polar_point(1, 2)
print(p2)