"""
    Синглтон через декоратор

"""
import random


def singleton(class_):
    instances = {}

    # Предотвращает двойной вызов instance
    def get_instance(*args, **kwargs):  # Если класса нет, то добавляем и возвращаем запрошенный класс
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
            return instances[class_]

    return get_instance


@singleton
class Database:

    def __init__(self):
        id = random.randint(1, 101)
        print(f"Loading db,id = {id}")


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1 == d2)