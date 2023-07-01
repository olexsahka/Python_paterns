"""
    Мост
Пример:
есть фигуры: круг и квадрат
есть реализация: векторная и скалярная,
чтобы перебрать все варинты нужно создать 4 объекта: кр-век, кр-растр, кв-век, кв-растр
чтобы уменьшить нужно разделить на фигуры и реализции с помощью мост
!! Нарушает принцип открытости закрытости, но позволяет избежать взрывного роста

"""
from abc import ABC


class Render(ABC):
    def render_circle(self, radius):
        pass
    # render_square


class VectorRender(Render):
    def render_circle(self, radius):
        print(f"Drawing vector circle of rad {radius}")


class RasterRender(Render):
    def render_circle(self, radius):
        print(f"Drawing Raster circle of rad {radius}")


class Shape:
    def __init__(self, render):
        self.render = render

    def draw(self): pass

    def resize(self): pass


class Circle(Shape):
    def __init__(self, render, radius):
        super().__init__(render)
        self.radius = radius

    def draw(self):
        self.render.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == "__main__":
    raster = RasterRender()
    vector = VectorRender()
    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
