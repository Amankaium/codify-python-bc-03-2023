a = int(input("Введите а: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))

# var 1
# if a > b and a > c and a > d:
#     print("a максимальное")
# elif b > a and b > c and b > d:
#     print("b максимальное")
# elif d > a and d > b and d > c:
#     print("d максимальное")
# else:
#     print("с максимальное")


# var 2
if a > b:
    if a > c:
        if a > d:
            print(a)
        else:
            print(d)
    else:
        if c > d:
            print(c)
        else:
            print(d)
else:
    if b > c:
        if b > d:
            print(b)
        else:
            print(d)
    else:
        if c > d:
            print(c)
        else:
            print(d)
