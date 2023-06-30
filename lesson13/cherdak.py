def cherdak(x, result):
    if isinstance(x, list):
        for element in x:
            result = cherdak(element, result)
    else:
        result.append(x)
    return result

sunduk = [5, 62, 3, 23, [6, 23], 52, [[[[[[[[5, 7]]]], 8, 2]]]]]
box = [5, 4, 9]
runduk = [6, 3, [0, 2], 9]

print(cherdak(runduk, []))
