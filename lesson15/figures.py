class ForSize:
    sides_qty = 4
    corner_qty = 4
    corners = [90, 130, 100, 70]  # ToDo

    def check(self):
        print(self.corners)
        for c in self.corners:
            if c > 180:
                return False
        return True

class Paral(ForSize):
    sides_parallel = True

class Rectangle(Paral):
    corner = 90
    corners = [90, 90, 90, 90]

    def __init__(self, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2

    def count_square(self):
        return self.side_1 * self.side_2


class Romb(Paral):
    sides_equal = True

class Square(Rectangle, Romb):
    def __init__(self, side):
        self.side = side

    def count_square(self):
        return self.side ** 2

sq_1 = Square(7)
print(sq_1.sides_qty)
print(sq_1.corner_qty)
print(sq_1.corner)
print(sq_1.sides_parallel)
print(sq_1.sides_equal)
print(sq_1.check())
