class Tiger:  # class
    paws = 4
    tails = 1
    color = "striped"
    likes_meat = True
    places = ["Asia", "Europe"]

    def say(self):
        print("Arrr")

sherhan = Tiger()  # object, instance, объект, экземпляр
print(sherhan)
print(type(sherhan))
print(type(7))
sherhan.say()  # вызов метода
print(sherhan.places)  # обращение к свойству

nums = '5728'
new_lst = list(nums)  # class list
print(new_lst)  # ['5', '7', '2', '8']
new_lst.append(9)  # метод append
print(new_lst)  # ['5', '7', '2', '8', 9]
