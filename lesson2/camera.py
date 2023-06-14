name = input()  # информация о пользователе

if name == "Каюм" or name == "Иван" or name == "Мухаммад" or name == "Давлят" or name == "Арстан" or name == "Искандер":
    gender = 'male'
elif name == 'Айдана' or name == 'Алтынай' or name == 'Алия':
    gender = 'female'
else:
    gender = None
    message = 'Человек не опознан!'

if gender == 'male':
    message = f'Вошёл {name}'
elif gender == 'female':
    message = f'Вошла {name}'

print(message)
