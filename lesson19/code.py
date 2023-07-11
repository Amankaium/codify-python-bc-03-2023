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
        # ...
        return

file_1 = MyFile("my_test_1.txt")
print(file_1.create("Hello world!"))
print(file_1.update(" One Two Three"))
print(file_1.read())
file_1.delete()
print(file_1.read())


file_2 = MyFile("test_2.txt")
file_2.update("THis is test 2 text\n")
file_2.update("THis is SPARTA!")
print(file_2.read())
