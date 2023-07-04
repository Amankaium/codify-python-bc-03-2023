class Tiger:
    tail = 1
    places = ["Asia", "Europe"]
    paws = 4

    def __init__(self, name, age):  # "Sher Han"
        self.tiger_name = name  # новое свойство
        self.age = age

sherhan = Tiger("Sher Han", 5)  # __init__
print(sherhan.tail)
print(sherhan.tiger_name)  # значение св-ва tiger_name
print(sherhan.age)  # значение св-ва age # 5

tigra = Tiger("Тигра", 0.5)
print(tigra.age)
tigra.age = 1
print(tigra.age)
tigra.jumping = True
print(tigra.jumping)
