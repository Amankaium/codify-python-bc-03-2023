nums = []
k = int(input("Число предентов: "))
while k > 0:
    n = int(input("Введите число: "))
    nums.append(n)
    k = k - 1

# nums готов
m = nums[0]
i = 0
while i < len(nums): # i < 5
    p = nums[i]
    if p > m:
        m = p
    i = i + 1
print(nums)
print(m)
