num_sum = 1000

for b in range(1, num_sum):  # 400 # 10 ** 6
    for a in range(1, b+1):  # 8000
        c = (a ** 2 + b ** 2) ** 0.5
        c1 = a ** 2 + b ** 2 == c ** 2
        c2 = a < b < c
        c3 = a + b + c == num_sum
        if c1 and c2 and c3:  # 1
            print(a, b, c, a * b * c)  # 1


# for a in range(1, num_sum):  # 8000 # 10 ** 9
#     for b in range(1, num_sum):  # 400 # 1000000
#         for c in range(1, num_sum):  # 20 # 1000
#             c1 = a ** 2 + b ** 2 == c ** 2
#             c2 = a < b < c
#             c3 = a + b + c == num_sum
#             if c1 and c2 and c3:  # 1
#                 print(a, b, c, a * b * c)  # 1
