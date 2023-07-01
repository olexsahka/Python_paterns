"""
    Прототип
необходимо использовать copy.deepcopy, для того чтобы скопировать все атрибуты
copy            vs          deepcopy
копирутеся                  копируется
как ссылка                  все атрибуты
"""
import copy


class Address:
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country

    def __str__(self):
        return f"{self.street},{self.city},{self.country}"


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} lives  in {self.address}"


john = Person("John", Address("London Road", "London", "UK"))
# print(john)
# jane = john  # неправильно
# jane.name = "Jane"  # неправильно, так как ссылаются на 1 объкт
# print("john", john)  # одинаково
# print("jane", jane)  # одинаков
jane = copy.deepcopy(john)  # рекурсивная копия объекта которая копирует все атрибуты и создаёт совершенно новый объект
jane.name = "Jane"
jane.address.street = "London Road 1b"
print("john", john)  # отличается
print("jane", jane)  # отличается
