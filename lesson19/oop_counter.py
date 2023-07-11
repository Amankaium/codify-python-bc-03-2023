class MyFile:
    def __init__(self, name, encoding='utf-8'):
        self.name = name
        self.encoding = encoding
        self.create()

    def create(self, initial_text=''):
        with open(self.name, mode='w', encoding=self.encoding) as my_file:
            my_file.write(initial_text)
        current_txt = self.read()
        return current_txt

    def read(self):
        with open(self.name, mode='r', encoding=self.encoding) as my_file:
            txt = my_file.read()
        res = f"""
______________________________________________
# Содержимое файла {self.name}:
""" + txt
        if txt == "":
            res += "# Пустой текст"
        res += "\n# Конец файла"
        return res

    def update(self, new_txt):
        my_file = open(self.name, mode='a', encoding=self.encoding)
        my_file.write(new_txt)
        my_file.close()
        current_txt = self.read()
        return current_txt

    def delete(self):
        with open(self.name, mode='w', encoding=self.encoding) as my_file:
            my_file.write("")
            print("Deleting...")

    def count_words(self):
        with open(self.name, mode='r') as message_file:
            message_str = message_file.read()  # строка
            words = message_str.split()  # список
            return len(words)

## Добавить логику подсчёта слов в тексте,
# офорить в виде ООП
file_1 = MyFile("my_test_1.txt")
file_1.create("Hello world!")
file_1.update(" One Two Three")
print(file_1.count_words())
