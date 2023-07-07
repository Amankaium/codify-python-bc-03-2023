marks = open('example.txt', mode='r', encoding="utf-8")
txt = marks.read()  # "Ivan 85\nArstan 95\n"
words_list = txt.split()
print(words_list)
marks.close()
