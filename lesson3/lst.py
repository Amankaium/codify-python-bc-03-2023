# Список - массивы
b = 44
a = [7, "hello", False, None, b]
print(a)

# 2
letter = input()
intro_text = letter[:11]
greetings = ["Добрый день", "Доброе утро", "Добрый вече"]
if intro_text not in greetings:
    print("Вы забыли добавить приветсвие")
