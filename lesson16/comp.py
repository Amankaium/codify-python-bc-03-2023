class Electro:
    volt = 220

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


class Computer(Electro):
    contains = ["Monitor", "Cabels", "Keyboard", "Mouse", "SysBlock"]
    OS = "Windows"

    def __init__(self, **kwargs):
        brand = kwargs["brand"]
        model = kwargs["model"]
        super().__init__(brand, model, kwargs["price"])

        if "ram" in kwargs:
            self.ram = kwargs["ram"]

        if "gpu" in kwargs:
            self.gpu = kwargs["gpu"]


comp_1 = Computer(brand="HP", model="Pavillion", price=3000, ram=16, gpu="Ge Force 4090")
comp_2 = Computer(brand="Mac", model="Pro 16", price=1500, ram=8)
print(comp_2.ram)
# print(comp_2.gpu)  # error
print(comp_1.gpu)

# Laptop
# attributes: contains, weight (1.5), diagonal (15), has_wifi (True)

class Laptop(Computer):
    contains = ["Mouse", "Laptop", "Cabels"]
    has_wifi = True
    has_bluetooth = True
    weight = 1.5
    diagonal = 15

    def __init__(self, **kwargs):
        if "weight" in kwargs:
            self.weight = kwargs["weight"]
        if "diagonal" in kwargs:
            self.diagonal = kwargs["diagonal"]
        super().__init__(**kwargs)


samsung = Laptop(brand="Samsung", model="Alpha 5", price="600", weight=1, ram=8)
dirs = dir(samsung)
for element in dirs:
    print(element)
print(samsung.contains)

data = {
    "brand": "Lenovo",
    "model": "Legion 7",
    "price": "1500",
    "ram": 16,
    "gpu": "GeForce 2060",
}
lenovo = Laptop(**data)

for key in data:
    value = getattr(lenovo, key)
    print(key, value)
