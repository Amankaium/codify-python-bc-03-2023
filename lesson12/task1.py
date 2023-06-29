# написать функцию для
# подсчёта периметра комнаты,
# но комната с неизвестным
# количеством углов

def find_perimeter(*args):
    p = 0
    for num in args:
        p += num
    return p


print(find_perimeter(5, 7, 3, 6, 2))