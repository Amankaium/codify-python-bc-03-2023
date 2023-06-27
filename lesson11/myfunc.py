print("hello")

def my_sum(a, b):
    print("Вы вызвали фукнцию")
    res = a + b
    print(f"Сумма равна {res}")
    print("Функция завершила своё исполнение")
    return res

my_sum(3, 4)
my_sum(23123, 9)
my_sum(23242, 234365345)

c = my_sum(232, 35) # 267
print(c)
