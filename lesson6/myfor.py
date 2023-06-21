n = int(input("Сколько чисел? "))

nums = [] # 7 5 9 0
for i in range(n):
    new_num = int(input())
    nums.append(new_num)
print(nums)
# 9 7 5 0
result = []
for i in range(len(nums)):
    my_max = max(nums)  # 7
    result.append(my_max)  # [9, 7]
    nums.remove(my_max)  # [5, 0]
print(result)
