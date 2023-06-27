names = [
    "Каюм", "Иван", "Арстан",
    "Айсана", "Арис"
]

res = []
for i, name in enumerate(names):
    num = i + 1
    res.append(f"{num}. {name}")

print(res)

res_gen = [f"{i+1}. {name}" for i, name in enumerate(names)]
print(res_gen)
