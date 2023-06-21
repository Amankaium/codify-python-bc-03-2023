#        1
##       2
###      3
####     ...
#####
######
# ...
n = int(input("Задайте высоту: "))

for i in range(n):
    print("#" * (i + 1))


for j in range(n):
    print(" " * (round(n/2)-j) + "#" * (j + 1))
