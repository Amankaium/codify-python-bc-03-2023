b = 44
a = [52, 42, b]
print(a)  # [52, 42, 44]
print(a[1])  # 42
a.append(7)
print(a)  # [52, 42, 44, 7]
c = len(a)  # 4
a.append(c)
print(a)  # [52, 42, 44, 7, 4]
print(len(a))  # 5