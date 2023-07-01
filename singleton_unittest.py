"""
    Моностостояние(тестирование)
"""
import unittest


class Singleton(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        self.population = {}

        with open("cap.txt", "r") as f:
            lines = f.readlines()
            for i in range(0, len(lines), 2):
                self.population[lines[i].strip()] = int(lines[i + 1].strip())


class SingletonRecordFinder:
    def total_population(self, cities):
        res = 0
        for c in cities:
            res += Database().population[c]
        return res


class DummyDatabase:
    population = {
        'a': 1,
        'b': 2,
        'c': 3
    }


class ConfigureSingletonRecordFinder:
    def __init__(self, db):
        self.db = db

    def total_population(self, cities):
        res = 0
        for c in cities:
            res += self.db.population[c]
        return res


class SingletonTests(unittest.TestCase):
    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)

    def test_singleton_total_popula(self):
        rf = SingletonRecordFinder()
        names = ['nur', 'spb']
        tp = rf.total_population(names)
        self.assertEqual(tp, 45)
        # проблема в том что тестирование провидится на реальной бд, а она может использоваться в данный момент и
        # меняться

    ddb = DummyDatabase()

    def test_dependent_singleton_total_popula(self):
        crf = ConfigureSingletonRecordFinder(self.ddb)
        self.assertEqual(3, crf.total_population(['a', 'b']))


if __name__ == "__main__":
    unittest.main()
