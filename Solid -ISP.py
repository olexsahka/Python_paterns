"""
    Solid
    4 - Принцип разделения интерфейсов(ISP - Interface Segregation Principle)
! Не стоит добавлять слишком много методов в интерфейс
! Создание интерфейсов содержащих слишком много методов не лучшая идея они попросту могут быть не нужны для наследумых классов
! Нужно разделить интерфесы на самые узкие части которые можно только создать
"""
from abc import abstractmethod


class Machine:
    def print(self, doc):
        raise NotImplementedError

    def scan(self, doc):
        raise NotImplementedError

    def fax(self, doc):
        raise NotImplementedError


class MultifunctionPrinter(Machine):
    def print(self, doc):
        pass

    def scan(self, doc):
        pass

    def fax(self, doc):
        pass


class OldFashionPrinter(Machine):  # не умеет сканировать и отправлять факс
    def print(self, doc):
        # ok
        pass

    def scan(self, doc):
        #  1 вариант - ничего здесь не делать, но это будут видеть что он ничего не делает
        pass

    def fax(self, doc):
        """NOT SUPPORTED!!!"""
        #  2 вариант - вызвать исключение, но если это не заметят, будет грустно
        raise NotImplementedError("Printer cannot scan!")


class Printer:
    @abstractmethod
    def print(self,doc):
        pass


class Scanner:
    @abstractmethod
    def scan(self,doc):
        pass


class Fax:
    @abstractmethod
    def fax(self, doc):
        pass


class Myprinter(Printer):
    def print(self, doc):
        print(doc)


class PhotoCopier(Printer, Scanner):
    def print(self, doc):
        pass

    def scan(self, doc):
        pass


class MultifunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self,doc):
        pass

    @abstractmethod
    def scan(self,doc):
        pass


class MultifunctionMachine(MultifunctionDevice):
    def __init__(self, printer, scanner):
        self.priter = printer
        self.scaner = scanner

    def print(self, doc):
        self.priter.print(doc)

    def scan(self, doc):
        self.scaner.scan(doc)

