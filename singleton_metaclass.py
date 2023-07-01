"""
    Синглтон через метакласс
принцип такой же как и в декораторе

"""
import random


class Singleton(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        return cls.instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        id = random.randint(1, 101)
        print(f"Loading db,id = {id}")


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1 == d2)