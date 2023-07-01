"""
Компоновщик (пример геометрические фигуры)
можно использовать рекурсию для обхода всех дочерних элементов

"""


class GraphicObject:  # сделала класс компоновщик который можно использовать как отдельный элемент или как набор элементов
    def __init__(self, color=None):
        self.color = color
        self.children = [] # помещает в себя все остальные класс
        self._name = "Main Group"

    @property # сделаем свойство для использования в наследуемых классах
    def name(self):
        return self._name

    def _print(self, items, depth): # рекурсивный метод который будет печатать все элементы группы
        items.append("*" * depth)
        if self.color:
            items.append(self.color)
        items.append(f"{self.name}\n")
        for child in self.children:
            child._print(items, depth + 1)

    def __str__(self):
        items = []
        self._print(items, 0)
        return "".join(items)


class Circle(GraphicObject):
    @property
    def name(self):
        return "Circle"


class Square(GraphicObject):
    @property
    def name(self):
        return "Square"


if __name__ == "__main__":
    drawing = GraphicObject()
    drawing.children.append(Square("Red"))
    drawing.children.append(Square("Yellow"))

    group = GraphicObject()
    group.children.append(Square("Blue"))
    group.children.append(Square("Blue"))
    drawing.children.append(group)

    print(drawing)
