def a():
    print("Вызов функции 1")
    num = 7 # 3
    print(num)

def b(): # 2
    print("Вызов функции 2")
    a()


def c():
    print("Вызов функции 3")
    b()
    a()

a()
c()
b()
