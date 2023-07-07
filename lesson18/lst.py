# txt.isalpha()
# txt.isnum()
# Получить список имён
# и список оценок
# с файла example.txt

my_file = open(
    'example.txt',
    mode='r',
    encoding='utf-8'
)
names = []
marks = []
words = my_file.read().split()
for i, value in enumerate(words):
    if value.isnumeric():
        marks.append(value)
    elif value.isalpha():
        names.append(value)
my_file.close()
print(names)
print(marks)
