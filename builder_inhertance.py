"""
    Строители через наследование
всякий раз когда нужно добавить инфу нужно наследовать от строителя который уже есть
! Можно использовать строителей как наследников других строителей !
! Решает проблему исходного корневого строителя!
"""


class Person:
    def __init__(self):
        self.name = None
        self.job = None
        self.born = None

    def __str__(self):
        return f"{self.name} work as {self.job}  and born in {self.born}"

    @staticmethod
    def new():
        return BornBuilder()


class Builder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class NameBuilder(Builder):
    def called(self, name):
        self.person.name = name
        return self


class JobBuilder(NameBuilder):
    def work(self,job):
        self.person.job = job
        return self


class BornBuilder(JobBuilder):
    def born(self,born):
        self.person.born = born
        return self


pb = Person.new()

person = pb\
    .called("Alex").work("programmer").born("01.04.2000").build()

print(person)
