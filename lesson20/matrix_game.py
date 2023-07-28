from matrix_driver import *
# from matrix_driver import Map, GameObject, Player, Fruit
from code import cool_print
import matrix_driver
iceworld = matrix_driver.Map(25, 10)  # y, x



# iceworld = Map(25, 10)  # y, x
player = Player(iceworld, 7, 3)
apple = Fruit(map_object=iceworld, x=5, y=15, points=4)
banana = Fruit(map_object=iceworld, x=6, y=20, points=3, bonus_time=20)
fruits = [apple, banana]

while True:
    x = player.x
    y = player.y
    iceworld.box[x][y] = iceworld.points
    iceworld.render()
    res = player.step(iceworld)
    if res == "Error":
        break

    # 3.2 Проверяем ход
    iceworld.check(player, fruits)

    iceworld.box[x][y] = " "
    iceworld.timer -= 1
    if iceworld.timer == 0:
        break
cool_print("GAME OVER")
    