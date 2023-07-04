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
print(pif_1.count_square())

tr_1 = Triangle(6, 8, 3)
print(tr_1.count_square(5, tr_1.side_3))
