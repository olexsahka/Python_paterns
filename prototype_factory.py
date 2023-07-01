"""
    Прототип
часто бывает неудобно копировать в ручную
! Легче обернуть в отдельный компонент, например в фабрику
Если есть конечное число прототипов то можно создать фабрику с фабричными методами для создания новых объектов
"""
import copy


class Address:
    def __init__(self, street, city, suite):
        self.street = street
        self.city = city
        self.suite = suite

    def __str__(self):
        return f"{self.street},{self.city},{self.suite}"


class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} work  in {self.address}"


class EmployeeFactory:
    main_office_employee = Employee("", Address("123 East Drive", 0, "London"))
    aux_office_employee = Employee("", Address("123B East Drive", 0, "London"))

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee, name, suite
        )

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee, name, suite
        )

    @staticmethod
    def __new_employee(proto, name, suite):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result


john = EmployeeFactory.new_main_office_employee("John", 101)
jane = EmployeeFactory.new_main_office_employee("Jane", 500)
print(john)
print(jane)
