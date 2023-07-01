"""
        Solid
        1 - Принцип единственной ответсвенности (SRP - Single Responsability principle)
    Не надо перезагружать классы!!!!!!!!
"""


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self,text):
        self.count += 1
        self.entries.append(f'{self.count}:{text}')

    def remove_entry(self,pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # def save(self,filename): # Плохо
    #     file = open(filename,"w")
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename): # Плохо
    #     pass
    #
    # def loaw_from_web(self, filename): # Плохо
    #     pass


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename): # хорошо
        file = open(filename, "w")
        file.write(str(journal))
        file.close()




j = Journal()
j.add_entry("hello")
j.add_entry("its me")
print(f'journal entries:\n{j}')
file = "test.txt"
PersistenceManager.save_to_file(j,file)
with open(file) as f:
    print(f.read())