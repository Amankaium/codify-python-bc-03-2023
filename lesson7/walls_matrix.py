#   9
#########
#       # 4
#       #
#########
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


unit = [round(width/2), round(length/2)]  # x, y

while True:
    # m[1][2] = 7
    x = unit[0]
    y = unit[1]
    box[x][y] = "O"

    for row in box:  # row = ["#", " ", " ", "#"]
        for cell in row:  # cell = "#" или " "
            print(cell, end='')
        print()

    command = input("Ход: ")
    if command == "w":
        unit[0] -= 1
    elif command == "s":
        unit[0] += 1
    elif command == "d":
        unit[1] += 1
    elif command == "a":
        unit[1] -= 1
    else:
        print("ОШИБКА!")
        break

    box[x][y] = " "
