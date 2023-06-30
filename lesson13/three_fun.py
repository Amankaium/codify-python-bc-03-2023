def pow_2(a):
    return a ** 2

def pow_3(a):
    res = 1
    for i in range(3):
        res *= a
    return res

def power(a, b):
    # 2 -> pow_2
    if b == 2:
        r = pow_2(a)

    # 3 -> pow_3
    elif b == 3:
        r = pow_3(a)

    return r

# Вызывается функция power, которая принимает 2 числа,
# нужно возвести первое число во второе.
# Если второе число 2, то вызывается функция pow_2,
# если же 3, то pow_3, функции pow_2 и pow_3 высчитывают квадрат
# и куб числа соответственно