# В тесте можно набрать максимально 250 баллов,
# пользователь вводит количество набранных баллов
# Если пользователь набирает более 70% баллов, то он проходит
# Напишите программу, которое высчитывает и выводит
# прошёл ли студент или нет

# Пример ввода: 90  # баллов
# Вывод: не пройдено

passed = 80 # процент
max_points = 500 # баллов

# Пользователь вводит количетсво баллов
points = int(input())

# Переводим в проценты
pip = (100 * points) / max_points

# Проидено ли?
if pip > passed:
    print("Успешно сдано")
else:
    print("не пройдено")

