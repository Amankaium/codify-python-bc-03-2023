lst_i = []


i = 10
p = 2
while len(lst_i) <= 30:  # 123 # 36
    i += 1

    if (i ** (1/p)) % 1 > 0 and (i ** (1/p+1)) % 1 > 0:
        continue

    # i_string = str(i)  # '123'
    # sum_i = 0
    # for sym in i_string:  # '1'
    #     num = int(sym)  # 1
    #     sum_i += num  # 1  >  3  >  6
    sum_i = sum([int(sym) for sym in str(i)])

    if sum_i ** p > i:
        continue

    res = 0
    k = p
    if sum_i in [0, 1]:
        continue

    while res < i:
        res = sum_i ** k
        if res == i:
            lst_i.append(i)
            p = k
            print(i, p, len(lst_i))
            break
        k += 1

print(lst_i)
