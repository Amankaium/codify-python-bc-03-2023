# Пользователь вводит размеры стены,
# вам надо написать программу, которая
# может посчитать сколько м2 обоев надо купить пользователю
a = int(input("Введите высоту: "))
b = int(input("Введите ширину: "))
c = 0.8  # ширина
k = b / c
res = round(k * a)
print(f"Вам нужно {res} метров")
