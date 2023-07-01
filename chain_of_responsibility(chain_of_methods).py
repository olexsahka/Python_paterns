"""
Цепочка методов
"""
class Creature:
    def __init__(self,name,attack,defence):
        self.name = name
        self.attack = attack
        self.defence = defence

    def __str__(self):
        return f"{self.name} :({self.attack}/{self.defence})"

class CreatureModifire:
    def __init__(self,creature):
        self.creature = creature
        self.next_modifier = None

    def add_modifier(self,modifier):
        if self.next_modifier: # Если модификатор существует, то мы у существующего модификатора вызываем метод add_modifier
            print(f"adding {modifier.__class__.__name__}")
            self.next_modifier.add_modifier(modifier) # К существующему модификатору добавляем дополнительный
        else: # Если не сущетсвует модификатора, то создаем модификатор на основе введенного
            self.next_modifier = modifier
            print(f"next_modifier = {modifier.__class__.__name__}")
    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()

    def __str__(self):
        if self.next_modifier is None:
            return "None"
        else:
            return self.next_modifier.name
class DoubleAttackModifier(CreatureModifire):
    def handle(self):
        print(f"double attack {self.creature.name}'s attack")
        self.creature.attack *= 2
        super().handle()

class IncreaseDefenceModifier(CreatureModifire):
    def handle(self):
        if self.creature.attack<=2:
            print(f"Increase defence {self.creature.name}'s defence")
            self.creature.defence += 1
        super().handle()

class NoBonusModifier(CreatureModifire):
    def handle(self):
        print(f"no bonuses modifire")

if __name__ == "__main__":
    goblin = Creature("Goblin",1,1)
    print(goblin)
    root = CreatureModifire(goblin)
    #root.add_modifier(NoBonusModifier(goblin))
    root.add_modifier(IncreaseDefenceModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))
    root.handle()
    print(goblin)
