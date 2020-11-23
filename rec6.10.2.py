# Напишите код для описания геометрической фигуры.  Создайте  класс  «Прямоугольник» с помощью метода  __init__(). На
# выходе в консоли вам необходимо получить длину и ширину с итоговым значением.

class Rectangele:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


rec = Rectangele(50,100)

print(rec.get_width(),
      rec.get_height())

