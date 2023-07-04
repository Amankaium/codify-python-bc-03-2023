class Tiger:  # Родительский класс  # Предок
    skin = 'striped'
    color = ['yellow', 'black']

    def __init__(self, name):
        self.name = name

class WhiteTiger(Tiger):  # Дочерний класс
    color = ['white', 'black']
    rare = True

class TibetWhiteTiger(WhiteTiger):  # Потомок
    place = "Tibet"

class RevatWhiteTiger(WhiteTiger):
    place = "Reva"

akuma = WhiteTiger("Akuma")
print(akuma.skin)
print(akuma.color)
print(akuma.name)
