go_to_the_shop = True
buy_sugar = False

if go_to_the_shop and buy_sugar:
    print("Печь пироги")
else:
    print("Сделаю бутер")

has_chips = False
has_popcorn = True
if has_chips or has_popcorn:
    print("Есть чем смаковать")
else:
    print("Сделаю бутер")

print(not has_chips)
