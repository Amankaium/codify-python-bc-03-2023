males = ["Каюм", "Иван", "Мухаммад", "Давлят", "Арстан", "Искандер", "Аслан"]
females = ['Айдана', 'Алтынай', 'Алия', "Айсана"]
students = males + females

i = 0
while i < len(students):
    output = f"{i+1}. {students[i]}"
    print(output)
    i = i + 1  # i += 1

print("Отсчёт окончен!")
