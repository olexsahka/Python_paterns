"""
    Моностостояние - вариация синглтона
Лучше использовать либо декоратор или метакласс
"""


class MonoState:
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(MonoState,cls).__new__(cls,*args,**kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class CFO(MonoState):
    def __init__(self):
        self.name = ""
        self.money_manage = 0

    def __str__(self):
        return f"{self.name} (CFO) manage {self.money_manage}"


class CEO:
    __shared_state= { # при изменении любого экземпляра мы меняем все
        'name': 'Steve',
        'age' : 55
    }

    def __init__(self):
        self.__dict__ =self.__shared_state
        print(self.__shared_state)

    def __str__(self):
        return f"{self.name} ( CEO ) is {self.age}  old"


if __name__ == "__main__":
    # ceo1 =CEO()
    # print(ceo1)
    # ceo2 = CEO() # аттрибуты ссылаются на тоже стостояние что и  CEO1
    #              # делаем копию ссылки на данные
    # ceo2.age = 77
    # print(ceo2)
    # print(ceo1)

    cfo1 = CFO()
    cfo1.name = "Alex"
    cfo1.money_manage =1
    print(cfo1)
    cfo2 = CFO()
    cfo2.name = "Gab"
    cfo2.money_manage = 2
    print(cfo1,cfo2,sep="\n")