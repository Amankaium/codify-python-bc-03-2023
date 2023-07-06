# n! означает n × (n − 1) × ... × 3 × 2 × 1
#
# Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Найдите сумму цифр в числе 100!.

n = 10
factorial = 1
for i in range(1, n+1):
    factorial *= i

result = sum([int(sym) for sym in list(str(factorial))])
