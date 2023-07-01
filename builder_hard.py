"""
        Паттерн Строитель
1) Некоторые объекты просты и могут быть созданы за один вызов конструктора
2) Для создания других объектов требуется больше действий
3) Наличие объекта с 10 аргументами в конструкторе непродуктивно
4) Вместо этого применяется пошаговое построение
5) Строитель представляет API для пошагового построения объекта

СТРОИТЕЛЬ продостовляет лаконичный API для поэтапного конструирования сложного объекта
"""


class Person:  # Есть Базовый класс
    def __init__(self):
        #  adddres
        self.street_addres = None
        self.postcode = None
        self.city = None
        #  employment
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self):  # Дандр метод для отображения
        return f"Addres: ({self.street_addres}, {self.postcode}, {self.city})" \
               f"Emplyment: ({self.company_name}, {self.position}, {self.annual_income})"


class PersonBuilder: # класс строителя в котором мы при ините создаем экземпляр базового класса
    def __init__(self, person=Person()):
        self.person = person

    @property # свойство для работы со строителем PersonJobBuilder
    def works(self):
        return PersonJobBuilder(self.person)

    @property # свойство для работы со строителем PersonAddressBuilder
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self): # Вовращаем заполненный объект
        return self.person


class PersonJobBuilder(PersonBuilder): # класс строителя связанный с работой
    def __init__(self, person ): # уже используем существующий объект
        super().__init__(person)

    def at(self, company_name): # накапливаем параметры
        self.person.company_name = company_name
        return self

    def as_a(self, position): # накапливаем параметры
        self.person.position = position
        return self

    def earning(self, annual_income): # накапливаем параметры
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):  # класс строителя связанный с адресом
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_addres): # накапливаем параметры
        self.person.street_addres = street_addres
        return self

    def with_postcode(self, postcode): # накапливаем параметры
        self.person.postcode = postcode
        return self

    def in_city(self, city): # накапливаем параметры
        self.person.city = city
        return self


pb = PersonBuilder()
person = pb \
    .lives \
    .at("address Person") \
    .in_city("SPB") \
    .with_postcode("254789") \
    .works \
    .at("Company") \
    .as_a("HR") \
    .earning(80000) \
    .build()

print(person)
