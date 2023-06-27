r = 0
lst = []
n = 1000000  # 537    5! + 3! + 7! = 537
for i in range(3, n):
    nums = []
    for sym in str(i):  # '537'
        nums.append(int(sym))  # [5, 3, 7]

    factorials = []
    for num in nums:
        f = 1
        for k in range(1, num+1):
            f *= k
        factorials.append(f)  # [120, 6, 5040]
    if sum(factorials) == i:
        print(i)
