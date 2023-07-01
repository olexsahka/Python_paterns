"""
    Фасад
"""
class Console:
    def __init__(self):
        b = Buffer()
        self.current_viewport =ViewPort(b)
        self.buffers = [b]
        self.viewports =[self.current_viewport]

    def write(self,text):
        self.current_viewport.buffer.write(text)

    def get_char_at(self,index):
        return self.current_viewport.get_char_at(index)

class Buffer:
    def __init__(self, width=30 ,height=20):
        self.width = width
        self.height = height
        self.buffer = [""] * (width * height)

    def write(self,text):
        self.buffer += text

    def __getitem__(self, item):
        return self.buffer.__getitem__(item)


class ViewPort:
    def __init__(self,buffer=Buffer):
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self,index):
        return self.buffer[index+self.offset]

    def append(self,text):
        self.buffer.write(text)


if __name__ == "__main__":
    c =Console()
    c.write("hello")
    c.get_char_at(0)