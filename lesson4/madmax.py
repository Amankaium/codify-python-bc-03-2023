a = int(input("Введите а: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
e = int(input("Введите e: "))

# var 1
if a > b and a > c and a > d and a > e:
    print(a)
elif b > a and b > c and b > d and b > e:
    print(b)
elif c > a and c > b and c > d and c > e:
    print(c)
elif d > a and d > b and d > c and d > e:
    print(d)
else:
    print(e)
