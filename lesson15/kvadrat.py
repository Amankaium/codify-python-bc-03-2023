# Rectangle (прямоугольник)
# родитель, со свойствами:
# corner со значением 90
# corner_qty со значением 4
# добавьте конструктор,
# который принимает
# длины двух сторон

# Square (Квадрат) - дочерний класс
# добавьте конструктор,
# который принимает
# длину одной стороны
class Rectangle:
    corner = 90
    corner_qty = 4

    def __init__(self, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2

class Square(Rectangle):
    def __init__(self, side):
        self.side = side

sq_1 = Square(7)
print(sq_1.sides_parallel)
