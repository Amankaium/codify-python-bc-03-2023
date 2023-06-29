# Напишите функцию sum_range(start, end), которая суммирует все целые числа
# от значения «start» до величины «end» включительно.
# Если пользователь задаст первое число большее чем второе,
# просто поменяйте их местами.

def sum_range(start, end):
    if end < start:
        start, end = end, start

    s = 0
    for i in range(start, end + 1):
        s += i
    return s

print(sum_range(3, 7))
print(sum_range(10, 5))
print(sum_range(-3, 5))
