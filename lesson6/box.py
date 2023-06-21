length = int(input("Длина: "))
width = int(input("Ширина: "))
#   9
#########
#       # 4
#       #
#########
print("#" * width)

for i in range(length-2):
    print(f"#{' ' * (width - 2)}#")

print("#" * width)
