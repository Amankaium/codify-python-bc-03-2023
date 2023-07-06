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



# Triangle	sides_qty	3
# 	corner_qty	3
# PifTriangle	has_90_corner	True
# RBTriangle	two_equal_sides	True
# CorrentTriangle	all_sides_equal	True
# 	all_corners_equal	True
# 	corners 	[60, 60, 60]

class Triangle:
    sides_qty = 3
    corner_qty = 3

    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def count_square(self, height, side):
        return height * side * 0.5

class PifTriangle(Triangle):
    has_90_corner = True

    def count_square(self):
        sides = [self.side_1, self.side_2, self.side_3]
        gip = max(sides)
        sides.remove(gip)
        katet_1 = sides[0]
        katet_2 = sides[1]
        # square = katet_1 * katet_2 * 0.5
        square = super().count_square(katet_1, katet_2)
        return square

class RBTriangle(Triangle):
    two_equal_sides = True

class CorrentTriangle(Triangle):
    all_sides_equal = True
    all_corners_equal = True
    corners = [60, 60, 60]

pif_1 = PifTriangle(3, 4, 5)
sq_1 = Square(7)

figures = [pif_1, sq_1] # 100, n
for figure in figures:
    print(figure.count_square())
squares = [f.count_square() for f in figures]  # [6, 49]
print(sum(squares))