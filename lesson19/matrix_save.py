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
                fruits.remove(fruit)


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


class SaveFile:
    def __init__(self, name='default_save.txt'):
        self.name = name
        self.encoding = 'utf-8'

    def save(self, **kwargs):
        with open(self.name, mode='w', encoding=self.encoding) as save_file:
            for key, value in kwargs.items():
                save_file.write(f"{key} {value}\n")  # points 7

    def load(self):
        with open(self.name, mode='r', encoding=self.encoding) as load_file:
            data = {}
            for i, row in enumerate(load_file):
                key, value = row.split()
                data[key] = int(value)
        return data

variant = int(input("""Выберите:
1. Начать новую игру
2. Продолжить
"""))
if variant == 1:
    iceworld = Map(25, 10)  # y, x
    player = Player(iceworld, 7, 3)
    apple = Fruit(map_object=iceworld, x=5, y=15, points=4)
    banana = Fruit(map_object=iceworld, x=6, y=20, points=3, bonus_time=20)
    fruits = [apple, banana]
    save_file = SaveFile("save_1.txt")

elif variant == 2:
    save_file = SaveFile("save_1.txt")
    load_data = save_file.load()

    iceworld = Map(load_data['length'], load_data['width'])  # y, x # length, width
    iceworld.points = load_data["points"]
    iceworld.timer = load_data["timer"]
    player = Player(iceworld, load_data['player_x'], load_data['player_y'])
    apple = Fruit(
        map_object=iceworld,
        x=load_data['fruit_x'],
        y=load_data['fruit_y'],
        points=load_data['fruit_points'],
        bonus_time=load_data['fruit_bonus_time']
    )
    fruits = [apple]

while True:
    x = player.x
    y = player.y
    iceworld.box[x][y] = iceworld.points
    iceworld.render()
    res = player.step(iceworld)
    if res == "Error":
        break

    iceworld.check(player, fruits)

    iceworld.box[x][y] = " "
    iceworld.timer -= 1
    if iceworld.timer == 0:
        break

    if len(fruits) > 0:
        save_file.save(
            points=iceworld.points,
            player_x=player.x,
            player_y=player.y,
            timer=iceworld.timer,
            fruit_x=fruits[0].x,
            fruit_y=fruits[0].y,
            fruit_points=fruits[0].points,
            fruit_bonus_time=fruits[0].bonus_time,
            length=iceworld.length,
            width=iceworld.width
        )
    # points
    # player x y
    # timer
    # fruits
    # map size

print("GAME OVER")
