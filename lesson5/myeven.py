nums = [6, 2, 88, 23, 0, -5]

# Выведите чётные числа,
# используя цикл for
for i in range(len(nums)):
    num = nums[i]
    if num % 2 == 0:
        print(num)
