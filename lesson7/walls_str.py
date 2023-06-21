length = int(input("Длина: "))  # 9
width = int(input("Ширина: "))  # 4
#   9
#########
#       # 4
#       #
#########

print("#" * length)  #  символ # 9 раз
row = "#" + (" " * (length - 2)) + "#\n"
print(row * (width - 2), end='')
print("#" * length)
