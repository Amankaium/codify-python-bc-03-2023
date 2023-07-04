# Создайте класс машины, со свойствами колёса, равным 4,
# uses_fuel равным True, а также конструктором,
# который принимает марку и модель

class Car:
    wheels = 4
    uses_fuel = True
    mileage = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def go(self, km):
        self.mileage += km


bmw = Car("BMW", "X5")
print(bmw.model, bmw.brand)
# print(dir(bmw))
print(bmw.mileage)
bmw.go(3)
print(bmw.mileage)
bmw.go(5)
bmw.go(4)
print(bmw.mileage)
bmw.go(250)
print(bmw.mileage)

moskvich = Car("Москвич", "412")
print(moskvich.mileage)

def get_full_info(car_object):
    print("|-", '-' * 20, "-|")
    print(car_object.brand, car_object.model)
    print(car_object.wheels)
    print(car_object.uses_fuel)
    print(car_object.mileage)
    print("|-", '-' * 20, "-|")


get_full_info(moskvich)
get_full_info(bmw)
