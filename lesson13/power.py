def mult(a, b):
    res = 1
    for i in range(b):
        res *= a
    return res

def power(a, b):
    r = mult(a, b)
    return r


print(power(5, 3))
