"""
брокер событий(нужны события)
event broker(observer)
cqs - обработчик команд
"""
from abc import ABC
from enum import Enum
from types import NoneType


class Event(list): # события которые мы будем вызывать
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args,**kwargs)


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENCE = 2


class Query:
    def __init__(self, creature_name, what_to_query, default_value):
        self.creature_name = creature_name
        self.what_to_query = what_to_query
        self.value = default_value


class Game: # брокер событий
    def __init__(self):
        self.queries = Event()

    def perform_query(self, sender, query):
        print(query)
        self.queries(sender, query)


class Creature:
    def __init__(self, game, name, attack, defence):
        self.init_attack = attack # начальные значения
        self.init_defence = defence  # начальные значения
        self.name = name
        self.game = game

    @property
    def attack(self):
        # запрос с использованием брокера событий
        q = Query(self.name,WhatToQuery.ATTACK,self.init_attack)
        self.game.perform_query(self, q)
        return  q.value

    @property
    def defence(self):
        # запрос с использованием брокера событий
        q = Query(self.name, WhatToQuery.DEFENCE, self.init_defence)
        self.game.perform_query(self, q)
        return q.value

    def __str__(self):
        return f"{self.name}: ({self.attack}/{self.defence})"


class Modifier(ABC):
    def __init__(self, game, creature):
        self.creature = creature
        self.game = game
        self.game.queries.append(self.handle)

    def handle(self,sender,query):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.queries.remove(self.handle)

class DoubleAttackModifier(Modifier):
    def handle(self,sender,query):
        if sender.name == self.creature.name and query.what_to_query == WhatToQuery.ATTACK:
            query.value *= 2


if __name__ == "__main__":
    game = Game()
    goblin = Creature(game, "Strong goblin", 2, 2)
    print(goblin)
    with DoubleAttackModifier(game,goblin):
        print(goblin)
    print(goblin)