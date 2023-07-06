#   9
#########
#       # 4
#       #
#########

def render(box, points, timer):
    for row in box:  # row = ["#", " ", " ", "#"]
        for cell in row:  # cell = "#" или " "
            print(cell, end='')
        print()
    print(" -" * 20)
    print(f"Очки: {points} | Таймер: {timer}")
    print(" -" * 20)


def step(unit, length, width):
    command = input("Ход: ")
    if command == "w":
        if unit[0] > 1:
            unit[0] -= 1
    elif command == "s":
        if unit[0] < width - 2:
            unit[0] += 1
    elif command == "d":
        if unit[1] < length - 2:
            unit[1] += 1
    elif command == "a":
        if unit[1] > 1:
            unit[1] -= 1
    else:
        return "Error"
    return unit


def check(unit, apple, banana, fruits, points, timer):
    if unit[0] == apple[0] and unit[1] == apple[1]:
        points += 2
        apple = [None, None]

    if unit[0] == banana[0] and unit[1] == banana[1]:
        points += 3
        banana = [None, None]

    for i, fruit in enumerate(fruits):
        if unit[0] == fruit["x"] and unit[1] == fruit["y"]:
            points += fruit["points"]
            timer += fruit["time"]
            fruits[i]["x"] = None
            fruits[i]["y"] = None
    return apple, banana, fruits, points, timer

# 1. Генерация карты
length = int(input("Длина: "))  # 9
width = int(input("Ширина: "))  # 4
box = [[]]
for i in range(length):
    box[0].append("#")

for k in range(width-2):
    box.append(["#"])  # [["#", "#", ...], ["#"]]
    for j in range(length-2):
        box[-1].append(" ")  # [["#", "#", ...], ["#", " ", " ", ...]]
    box[-1].append("#")

box.append([])
for i in range(length):
    box[-1].append("#")


# 2. Генерация объектов
unit = [round(width/2), round(length/2)]  # x, y
apple = [1, 2] # 2 point
banana = [3, 7] # 3 point
points = 0
box[apple[0]][apple[1]] = "A"
box[banana[0]][banana[1]] = "B"
timer = 10

fruits = [
    {"x": 3, "y": 3, "points": 2, "time": 5},
    {"x": 5, "y": 1, "points": 3, "time": 10},
    {"x": 1, "y": length-2, "points": 4, "time": 15},
]
for fruit in fruits:
    box[fruit["x"]][fruit["y"]] = "*"


# 3. Запуск игры
while True:
    # m[1][2] = 7
    x = unit[0]
    y = unit[1]
    box[x][y] = points

    # 3.0 Рендеринг
    render(box, points, timer)

    # 3.1 Ход игрока
    unit = step(unit, length, width)
    if unit == "Error":
        break

    # 3.2 Проверяем ход
    apple, banana, fruits, points, timer = check(unit, apple, banana, fruits, points, timer)

    box[x][y] = " "
    timer -= 1
    if timer == 0:
        break
print("GAME OVER")
