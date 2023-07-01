"""
    Адаптер без кэширования
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def draw_point(p):
    print(".", end="")


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Rectangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x + width, y + height), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x, y)))


class LineToPointAdapter(list):
    count = 0

    def __init__(self,line):
        super().__init__()
        self.count += 1
        print(f"{self.count}: Generate points for line"
              f"[{line.start.x},{line.start.y}]->"
              f"[{line.end.x},{line.end.y}]")
        left = min(line.start.x,line.end.x)
        right = max(line.start.x,line.end.x)
        top = max(line.start.y,line.end.y)
        bottom = min(line.start.y,line.end.y)
        if left - right == 0:
            for y in range(top,bottom):
                self.append(Point(left,y))
        elif bottom - top == 0:
            for x in range(left,right):
                self.append(Point(x,top))
        else:
            pass


def draw(rcs):
    print("\n\n--- Drawing some stuff ---\n")
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)


if __name__ == "__main__":
    rs = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6)
    ]
    draw(rs)
    # при повторном вызове мы будем опять генерировать все точки, из-за того что мы использовали адаптер без кэширования
    draw(rs)