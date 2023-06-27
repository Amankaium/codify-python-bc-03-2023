nums = [
    7, 22, 52,
    33, 9, 3
]

# res = [num + 3 for num in nums]
# print(res)

pow_res = [num ** num for num in nums]

d_res = {num: num**2 for num in nums}
# {7: 49, 22: 484, ...}
print(d_res)