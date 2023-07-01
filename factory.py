"""
    Фабрика -Фабричный класс содержащая кучу фабричных методов
"""
import math
from enum import Enum


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x=0 ,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x : {self.x}, y : {self.y}"

    class PointFactory:
        @staticmethod
        def new_cartesian_point(x, y):
            return Point(x, y)

        @staticmethod
        def new_polar_point(rho, theta):
            point = Point()
            point.x = rho * math.cos(theta)
            point.y = rho * math.sin(theta)
            return point


if __name__ == "__main__":
    p1 = Point(2, 3)
    p2 = Point.PointFactory.new_polar_point(2,3)
    print(p2)