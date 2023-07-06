class Factorial:
    def __init__(self, num):
        self.num = num
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        self.value = factorial  # 3628800

    def find_sum_of_digits(self):
        # result = sum([int(sym) for sym in list(str(self.value))])
        str_value = str(self.value)  # '3628800'
        lst_value = list(str_value)  # ['3', '6', ...]
        lst_int_value = []
        for e in lst_value:
            int_e = int(e)
            lst_int_value.append(int_e)
        result = sum(lst_int_value)
        self.sum_of_digits = result
        return self.sum_of_digits


ten = Factorial(10)
print(ten.num)  # само число
print(ten.value)  # его факториал
ten.find_sum_of_digits()  # посчитать сумму цифл факториала
print(ten.sum_of_digits)  # сумма цифр факториала
