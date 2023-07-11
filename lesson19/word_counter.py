# Посчитайте и выведите количество слов
# в тексте с файла message.txt

with open("message.txt", mode='r') as message_file:
    message_str = message_file.read()  # строка
    words = message_str.split()  # список
    print(len(words))
