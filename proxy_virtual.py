"""
Виртуальный заместитель
"""


class Bitmap:
    def __init__(self,filename):
        self.filename = filename
        print(f"Loading img from {self.filename}")

    def draw(self):
        print(f"Drawing img {self.filename}")


class LazyProxy:
    def __init__(self,filename):
        self.filename = filename
        self._bitmap = None

    def draw(self):
        if not self._bitmap:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()


def draw(img):
    print("about to draw img")
    img.draw()
    print("Done drawing image")



if __name__ == "__main__":
    bmp = LazyProxy("test.jpg")
    draw(bmp)
    draw(bmp)
