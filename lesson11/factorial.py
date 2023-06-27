def factorial(n):
    r = 1
    for i in range(2, n+1):
        r *= i
    return r

print(factorial(7))
print(factorial(25))

# Создайте функцию power, которая принимает 2 числа,
# возводит первое число во второе
# и возвращает результат
