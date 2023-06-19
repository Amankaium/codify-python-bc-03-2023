nums = [6, 2, 88, 23, 0, -5, 30, 9, 20, 10, 6, 56, -7]
three = []
five = []
# Кратные 3:
# [6, 30, ...]

# Кратные 5:
# [-5, 30, ...]

# Выведите числа кратные 3 или 5
for num in nums:
    if num % 3 == 0 and num != 0:
        three.append(num)
    if num % 5 == 0 and num != 0:
        five.append(num)

    # if num != 0:
    #     if num % 3 == 0:
    #         three.append(num)
    #     if num % 5 == 0:
    #         five.append(num)
print(three)
print(five)
