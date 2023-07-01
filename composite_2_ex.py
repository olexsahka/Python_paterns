"""
Компоновщик (пример нейронные сети)
Маскировка под скалярный объект под коллекцию
"""
from abc import ABC
from collections.abc import Iterable


class Connectable(Iterable, ABC):  # создаем абстраный класс для подключения
    def connect_to(self, other):  # устанавливаем связи между 1 и 2 объектом
        if self == other:
            return
        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)


class Neuron(Connectable):
    def __init__(self, name):
        self.name = name
        self.inputs = []
        self.outputs = []

    def __str__(self):
        return f"{self.name}," \
               f"{len(self.inputs)} inputs," \
               f"{len(self.outputs)} outputs"

    def __iter__(self):  # мы не может проходить циклом по скалярному объекту по этому делаем объект итерируемым  и
        # возвращаем самого себя
        yield self


class NeuronLayer(list, Connectable):
    def __init__(self, name, count):
        super().__init__()
        self.name = name
        self.count = count

        for i in range(0, count):
            self.append(Neuron(f"{name}-{i}"))

    def __str__(self):
        return f"{self.name} with {len(self)} neurons"


if __name__ == "__main__":
    n1 = Neuron("n1")
    n2 = Neuron("n2")
    l1 = NeuronLayer("L1", 5)
    l2 = NeuronLayer("L2", 7)

    n1.connect_to(n2)
    n1.connect_to(l1)
    l1.connect_to(n2)
    l1.connect_to(l2)

    print(n1)
    print(n2)
    print(l1)
    print(l2)
