"""
    Solid
    5 - Принцип инверсии зависимостей(DIP - Dependency Inversion Principle)
высокоуровневые классы/модули не должны зависеть от низких уровней, а должны зависеть от абстракций(Интерфейсов)
В питоне - Утиная типизация
"""
from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SiBLING = 2


class Person:
    def __init__(self,name):
        self.name = name


class ReletionshipsBrowser:
    @abstractmethod
    def find_all_children(self, name):
        pass


class Reletionships(ReletionshipsBrowser):
    def __init__(self):
        self.relations = [] # мы не можем поменять на другой тип данных, так ка все что выше сломается

    def add_parent_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research: # Модуль высокого уровня
    # def __init__(self,relationships):
    #     self.relations = relationships.relations
    #     for r in self.relations:
    #         if r[0].name == "John" and r[1] == Relationship.PARENT:
    #             print(f"John has a child called {r[2].name}.")
    def __init__(self,browser):
        for p in browser.find_all_children("John"):
            print(f"John has a child called {p}.")


parent = Person("John")
child1 = Person("Chris")
child2 = Person("Mat")

relations = Reletionships()
relations.add_parent_child(parent, child1)
relations.add_parent_child(parent, child2)

Research(relations)
