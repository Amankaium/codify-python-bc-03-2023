names = ["Steve", "Alan", "Harry"]
points = [66, 35, 98]
# 1. Steve - 66
# 2...

for i, name in enumerate(names):
    p = points[i]
    order_num = i + 1
    print(f"{order_num}. {name} - {p}")
