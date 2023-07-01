"""
    Кусочное построение с помощью Builder
"""
#
# text = "hello"
# parts = ["<p>", text, "<p>"]
# print("".join(parts))
#
# words = ["hello", "world"]
# parts = ["<ul>"]
#
# for w in words:
#     parts.append(f"<li>{w}<li>")
# parts.append("</ul>")
# print("\n".join(parts))


class HTMLElement:
    indentsize = 2

    def __init__(self, name="", text=""):
        self.text = text
        self.name = name
        self.elements = []

    def __str(self, indent): # нужно для отрисовки
        lines = []
        i = ' ' * (indent * self.indentsize) # считаем количество пробелов
        lines.append(f"{i}<{self.name}>") # добавляем нужный элемент в строку

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indentsize) # считаем количество пробелов
            lines.append(f"{i1}{self.text}") # добавляем нужный текст элемента в строку

        for e in self.elements: # проходим по всем элементам
            lines.append(e.__str(indent + 1)) # добавляем нужный элемент с вызовом рекурсии в строку
        lines.append(f"{i}</{self.name}>") # добавляем нужный элемент в строку закрытие
        return "\n".join(lines)

    def __str__(self):
        return self.__str(0) # начинаем с нулевого отсутпа

    @staticmethod
    def create(name):
        return HTMLBuilder(name)


class HTMLBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HTMLElement(name=root_name) # создаем приватный атрибут рутнэйи

    def add_child_fluent(self, child_name, child_text): # добавляем элемент
        self.__root.elements.append(
            HTMLElement(child_name, child_text)
        )
        return self

    def __str__(self): # чтобы передать в другой класс
        return str(self.__root)


builder = HTMLElement.create("ul")
builder.add_child_fluent("li", "hello").add_child_fluent("li", "hello")
print("Ordinary builder")
print(builder)
