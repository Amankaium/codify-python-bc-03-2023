name = input()  # информация о пользователе
males = ["Каюм", "Иван", "Мухаммад", "Давлят", "Арстан", "Искандер", "Аслан"]
females = ['Айдана', 'Алтынай', 'Алия', "Айсана"]
# students = males + females

if name in males:
    gender = 'male'
elif name in females:
    gender = 'female'
else:
    gender = None
    message = 'Человек не опознан!'

if gender == 'male':
    message = f'Вошёл {name}'
elif gender == 'female':
    message = f'Вошла {name}'

print(message)
