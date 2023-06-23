# Перевести список в словарь, где ключ это слово
# key и индекс элемента списка, а значение - сам элемент
# res = {"key0": 4, "key1": "test1", ...}
lst = [4, "test1", False, "hello"]
res = {}
for i, elem in enumerate(lst):  # индекс, значение элемента
    mykey = "key" + str(i)  # key1
    res[mykey] = elem  # res["key1"] = "test1"
print(res)
