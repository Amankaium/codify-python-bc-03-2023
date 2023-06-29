# Функция принимает список чисел и возвращает максимальное число

def mad_max(lst):
    dragon = lst[0]
    for i in lst:
        if i > dragon:
            dragon = i
    return dragon

a = [1, 5, 9, 0, 2]
print(mad_max(a))  # 9
