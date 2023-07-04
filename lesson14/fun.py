# Написать функцию для нахождения гипотенузы
# по катетам
def find_gip(katet_1, katet_2):
    gip = ((katet_1 ** 2) + (katet_2 ** 2)) ** 0.5
    return gip

gip_1 = find_gip(3, 4)
print(gip_1)

# Написать функцию для нахождения катета
# по гипотенузе и другому катету
def find_kat(gip, kat_1):
    kat_2 = ((gip**2)-(kat_1**2)) ** 0.5
    return kat_2

print(find_kat(5, 3))
