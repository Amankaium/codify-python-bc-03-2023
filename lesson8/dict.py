# словарь
names = ["Ivan", "Muhammad", "Aidana"]
human = {"name": "Kaium", 88: 623, "code": "python"}
# names_dictionary = {0: "Ivan", 1: "Muhammad", 2: "Aidana"}
# print(human["name"])
# print(human[88])
# print(human["code"])
human["framework"] = "django"
print(human)
human["name"] = "Aman"
print(human)
human[88] += 1
print(human)
print(len(human))
example = {}

for k in human:  # k - ключ
    print(k, human[k])

for key, value in human.items():
    print(key, value)

