class Car:
    wheels = 4
    uses_fuel = True
    mileage = 0
    remain_fuel = 50

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def go(self, km):
        self.mileage += km
        liter = (km * 10) / 100
        self.remain_fuel -= liter
        return self.mileage, self.remain_fuel


# добавить свойство топливо равное 50
# добавить логику изменения остатка
# топлива в баке в зависимости от
# расстояния, расход 10 л на 100 км

matiz = Car("Dew", "Matiz")
print(matiz.mileage)
print(matiz.remain_fuel)
matiz.go(30)
print(matiz.mileage)
print(matiz.remain_fuel)
matiz.go(250)
print(matiz.mileage)
print(matiz.remain_fuel)
print(matiz.go(25))
ml, fuel = matiz.go(15)
