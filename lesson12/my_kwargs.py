def count_square(**kwargs):
    s = kwargs["a"] * kwargs["b"]
    return s


print(count_square(a=7, b=9))  # 63
print(count_square(a=5, b=8))  # 40
