res_list = []
res_dict = {}
n = int(input("Введите количество студентов: "))

for i in range(n):
    print(f"Студент {i+1}")
    name = input("Имя: ")
    age = int(input("Возраст: "))
    print(" -" * 7)
    res_list.append(name)
    res_dict[name] = age

print(res_list)
print(res_dict)
