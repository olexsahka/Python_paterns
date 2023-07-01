"""
Декоратор классический - класс, который принимает декорированный объект в качетсве аргумента, а также принимает
дополнительные значения и выполняет дополнительную функциональность
"""
from abc import ABC


class Shape(ABC):
    def __str__(self):
        return ""


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f"Circle of radius{self.radius}"


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f"Square of side{self.side}"


class ColoredShape(Shape):
    def __init__(self, shape, color):
        if isinstance(shape, ColoredShape):
            raise Exception("can not apply Color decorator")
        self.shape = shape
        self.color = color

    def __str__(self):
        return f"{self.shape}  has color{self.color}"


class TransparentShape(Shape):
    def __init__(self, shape, transparency):
        self.shape = shape
        self.transparency = transparency

    def __str__(self):
        return f"{self.shape}  has transparency {self.transparency*100}%"


if __name__ == "__main__":
    circle = Circle(2)
    print(circle)
    red_color_shape = ColoredShape(circle, 'red')
    print(red_color_shape)
    red_color_half_transparent_circle = TransparentShape(red_color_shape, 0.5)
    print(red_color_half_transparent_circle)

