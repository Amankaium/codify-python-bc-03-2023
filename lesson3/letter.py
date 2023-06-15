# Пользователь вводит текст письма
# если письмо не начинается с "Добрый день/Доброе утро/Добрый вечер"
# надо вывести ему подсказку, чтобы добавил приветствие

letter = input()

# 1
# if "Добрый день" not in letter and "Доброе утро" not in letter and "Добрый вечер" not in letter:
#     print("Вы забыли добавить приветсвие")

# 2
# intro_text = letter[:11]
# if intro_text != "Добрый день" and intro_text != "Доброе утро" and intro_text != "Добрый вече":
#     print("Вы забыли добавить приветсвие")

# 3
if not letter.startswith("Добрый день") and not letter.startswith("Доброе утро") and not letter.startswith("Добрый вечер"):
    print("Вы забыли добавить приветсвие")
