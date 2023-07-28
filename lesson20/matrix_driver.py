class Map:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        box = [[]]
        for i in range(length):
            box[0].append("#")

        for k in range(width - 2):
            box.append(["#"])  # [["#", "#", ...], ["#"]]
            for j in range(length - 2):
                box[-1].append(" ")  # [["#", "#", ...], ["#", " ", " ", ...]]
            box[-1].append("#")

        box.append([])
        for i in range(length):
            box[-1].append("#")

        self.box = box

    points = 0
    timer = 150

    def render(self):
        for row in self.box:  # row = ["#", " ", " ", "#"]
            for cell in row:  # cell = "#" или " "
                print(cell, end='')
            print()
        print(" -" * 20)
        print(f"Очки: {self.points} | Таймер: {self.timer}")
        print(" -" * 20)

    def check(self, player, fruits):
        for i, fruit in enumerate(fruits):
            if player.x == fruit.x and player.y == fruit.y:
                self.points += fruit.points
                self.timer += fruit.bonus_time
                fruit.x = None
                fruit.y = None

class GameObject:
    def __init__(self, map_object, x, y, skin):
        map_object.box[x][y] = skin
        self.x = x
        self.y = y
        self.skin = skin

class Player(GameObject):
    def __init__(self, map_object, x, y):
        super().__init__(map_object, x, y, 0)

    def step(self, map_object):
        command = input("Ход: ")
        if command == "w":
            if self.x > 1:
                self.x -= 1
        elif command == "s":
            if self.x < map_object.width - 2:
                self.x += 1
        elif command == "d":
            if self.y < map_object.length - 2:
                self.y += 1
        elif command == "a":
            if self.y > 1:
                self.y -= 1
        else:
            return "Error"

class Fruit(GameObject):
    def __init__(self, map_object, x, y, points=1, bonus_time=10):
        super().__init__(map_object, x, y, '*')
        self.points = points
        self.bonus_time = bonus_time

