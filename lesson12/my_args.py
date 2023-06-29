def max_num(*args):
    dragon = args[0]
    for i in args:
        if i > dragon:
            dragon = i
    return dragon


print(max_num(1, 22, 9, 2, 7, 23, 23, 25))  # 9
