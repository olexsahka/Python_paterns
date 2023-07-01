"""
    Синглтон через аллокатор(переопредление)

"""
import random


class Database:
    _instance = None

    def __init__(self): # проблема в том что мы проходим инит 2 раза а не 1
        id = random.randint(1, 101)
        print(f"Loading db,id = {id}")

    def __new__(cls, *args, **kwargs): # в методе нью мы проверяем инстанс, и если такой уже существет мы создаем единственный экземпляр
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1 == d2 )