def mult_range(start, end):
    if start > end:
        start, end = end, start
    result = 1
    for i in range(start, end+1):  # -2 8   # -2 -1 0 1 2 3 ...
        if i == 0:
            # continue
            i += 1
        result *= i

    return result

print(mult_range(-2, 8))
