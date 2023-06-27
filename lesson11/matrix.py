nums = [
    [7, 22, 52],
    [33, 9, 3]
]

res = [num for row in nums for num in row]
# for row in nums:
#     for num in row:
#         res.append(num)
print(res)
