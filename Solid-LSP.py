"""
    Solid
    3 - Принцип подставновки Libskov(LSP - Libskov SubSituation Principle)
Если у вас есть интерфейс, принимающий какой-то базовый класс, вы должны иметь возможность использовать любых его наследников
"""


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, val):
        self._width = val

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, val):
        self._height = val

    @property
    def area(self):
        return self._height * self._width

    def __str__(self):
        return f"Width = {self._width},height = {self._height} "


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, val):
        self._width = self._height = val

    @Rectangle.height.setter
    def height(self, val):
        self._height = self.width = val


def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w * 10)  # Так не правильно
    # expected = int(rc.width * rc.height) Так правильно

    print(f"expected area of {expected} ,got {rc.area}")


rc = Rectangle(2, 3)
use_it(rc)
# Вот тут и ошибка мы используем в методе "use_it", в нем переобределяем зачение height и тем самым меняем квадрат на
# прямоугольник
sq = Square(5)
use_it(sq)
