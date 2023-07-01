"""
    Solid
    2 - Прицип открытости-закрытости(OCP - Open Closed Principle)
У нас 2 критерия и мы здесь делаем 3 метода фильтрации, а если будет 3 критерия то будет 7 методов, нужно делать масштабируемо
! Реализован шаблон Спецификация
! Нужно избегать ситуаций когда нужно менять код, который уже был написан
"""
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self,name,color,size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filer_by_color(self,products,color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self,products,size): # Нарушили принцип открытости закрытости мы должны добавлять через расширение а не модификацию
        for p in products:
            if p.color == size:
                yield p

    def filter_by_size_color(self,products,size,color): # Нарушили принцип открытости закрытости мы должны добавлять через расширение а не модификацию
        for p in products:
            if p.color == size and p.size == size:
                yield p


class Specification:
    def is_satisfied(self,item):
        pass

    def __and__(self, other):
        return AndSpecification(self,other)


class Filter:
    def filter(self,items,spec):
        pass


class ColorSpecification(Specification):
    def __init__(self,color):
        self.color = color

    def is_satisfied(self,item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self,*args):
        self.args = args

    def is_satisfied(self,item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ =="__main__":
    apple = Product("Apple",Color.GREEN,Size.SMALL)
    tree = Product("Tree",Color.GREEN,Size.MEDIUM)
    house = Product("House",Color.BLUE,Size.LARGE)
    products = [apple, tree, house]

    print("green products(old bad version(not SOLID)):")
    pf = ProductFilter()
    for p in pf.filer_by_color(products,Color.GREEN):
        print(f'- {p.name} is green')

    print("green products(new good version(SOLID)):")
    bf = BetterFilter()
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products,green):
        print(f'- {p.name} is green')

    print("Large products (SOLID):")
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products,large):
        print(f'- {p.name} is large')

    print("Large And  Blue products (SOLID):")
    blue = ColorSpecification(Color.BLUE)
    # large_blue = AndSpecification(large,blue)
    large_blue = large & blue
    for p in bf.filter(products,large_blue):
        print(f'- {p.name} is large and blue')