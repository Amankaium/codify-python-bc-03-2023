marks = open(
    'example.txt',
    mode='r',
    encoding="utf-8"
)
for i, value in enumerate(marks):
    print(value)
marks.close()

# txt_1 = marks.readline()
# txt_2 = marks.readline()
# print(txt_1) # "Ivan 85"
# print(txt_2) # "Arstan 95"
