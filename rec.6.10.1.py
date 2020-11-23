class Figure:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_rectangele(self):
        return f"Rectangele({self.x}, {self.y}, {self.width}, {self.height})"


r1 = Figure(5,10,50,100)

print(r1.get_rectangele())