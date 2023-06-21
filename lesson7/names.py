# Пользователь вводит кол-во имён, а затем сами имена
# Вам нужно вывести список введённых имён

# 3
# Kaium
# Aman
# Izzat

# ["Kaium", "Aman", "Izzat"]

names = []
k = int(input("кол-во имён: "))

for i in range(k):
    name = input("Имя: ")
    names.append(name)

print(names)
