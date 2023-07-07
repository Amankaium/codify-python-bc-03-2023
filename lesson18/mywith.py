
with open('example.txt', 'r', encoding='utf-8') as f1:
    print(f1)
    print(type(f1))
    txt = f1.read()
    print(txt)

# файл закрыт