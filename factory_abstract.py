"""
    Фабрика (Абстракция) - Абстрактный класс
"""
from abc import ABC
from enum import auto, Enum


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print("this tea is delicious")


class Coffee(HotDrink):
    def consume(self):
        print("this coffee is delicious")


class HotDrinkFactory(ABC): # можно не использовать эту абстракцию, но она дает понимание, что мы будем делать в базовом классе
    def prepare(self,amount): # В других яп Абсрактный класс нужен
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self,amount):
        print("Put in tea is bag,boil water",f"poor {amount}ml, enjoy")
        return Tea


class CoffeeFactory(HotDrinkFactory):
    def prepare(self,amount):
        print("Grind some beans is delicious",f"poor {amount}ml, enjoy")
        return Coffee

def make_drink(type):
    if type == "tea":
        return TeaFactory().prepare(200)
    elif type == "coffee":
        return CoffeeFactory().prepare(50)
    else:
        None

class HotDrinkMachine:
    class AvailableDrinks(Enum):
        COFFEE = auto()# автономерация
        TEA =  auto()# автономерация

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for drink in self.AvailableDrinks:
                name = drink.name[0] + drink.name[1:].lower()
                factory_name = name + "Factory" # Получаем название фабрики
                factory_instance = eval(factory_name)() # создаем объект по названию factory_name
                self.factories.append((name,factory_instance))
            print(self.factories)

    def make_drink(self):
        print("Available drinks")
        for f in self.factories:
            print(f[0])
        s = input("pick drink")
        idx =int(s)
        s = input("pick amount")
        amount =int(s)
        return self.factories[idx][1].prepare(amount) # берем заранее подготовленный объект
        # из списка кортежей и вызываем метод prepare

if __name__ == "__main__":
    hdm = HotDrinkMachine()
    hdm.make_drink()
