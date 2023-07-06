class Human:
    def __init__(self, name, gender, floors=[1]):
        self.name = name
        self.gender = gender
        self.floor_accesses = floors

    floor_accesses = []

class Camera:
    def __init__(self, model, floor, orientir):
        self.model = model
        self.floor = floor
        self.orientir = orientir

    people = [
        'Иван', "Айдана",
        "Арстан", "Давлят",
        "Каюм", "Кама"
    ]

    def scan(self, human):
        print("---------------------")
        if human.name in self.people:  # распознование
            print("Человек распознан")
            if self.floor in human.floor_accesses:
                print("Доступ разрешён")
                print(self.message(human))
            else:
                print("Доступ запрещён!")
        else:
            print("Неопознанный человек!")
        print("----------------------")

    def message(self, human):
        if human.gender == "м":
            return f"Вошёл {human.name}"
        elif human.gender == 'ж':
            return f"Вошла {human.name}"

kaium = Human("Каюм", "м", [1, 2, 9])
aidana = Human("Айдана", "ж", [1, 4])
security = Human("Алмаз байке", "м", [1, 2, 3, 4, 5, 6, 7, 8, 9])
ivan = Human("Иван", "м", [1, 2, 3, 4, 5, 6, 7, 8, 9])

# Добавьте конструктор в класс Camera,
# который принимает model, floor, orientir
camera_door = Camera(model="HIK Vision 5", floor=1, orientir="door")  # model, floor, orientir
camera_lift = Camera(model="HIK Vision 7", floor=5, orientir="lift")

camera_door.scan(kaium)
camera_door.scan(aidana)
camera_door.scan(security)

camera_lift.scan(kaium)
camera_lift.scan(aidana)
camera_lift.scan(security)
camera_lift.scan(ivan)

# Улучшить метод scan, чтобы в начале видеть
# этаж, модель и ориентир камеры
# Если человек распознан, то вывести его имя
# рядом с сообщением "Человек распознан"