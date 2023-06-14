a = "hello world"
b = 'mouse'

print(b + ' keyboard')  # склеивание
print(b * 3) # mousemousemouse

# длина
len("hello world")  # 11
len(b)  # 5

# Индекс
print(a[0])  # h
print(a[1])  # e
print(a[8])  # r
print(a[4])  # o
print(a[-1]) # d
print(a[-3]) # r

# срез
print(a[1:5])  # ello,
print(a[:6])  # hello
print(a[4:])  # o world
print(a[2:-3])  # llo wo
print(a[1:9:2])  # el 0
print(a[:-1:3])  # hl wl
print(a[::3])  # hl wl
print(a[::4])  # hor
print(a[1:9:1])  # ello wor
print(a[9:1:-1])  # lrow oll
print(a[::-1])  # dlrow olleh
print(a[::-2])  # drwolh

# методы
k = a.find('wor')  # index 6
print(k)
print(a.find('o'))  # 4

# a = a.replace('o', '0')
# a = a.replace('l', '1')
print(a.replace('o', '0'))

print(a.split())  # ['hello', 'world']
print(a.split("o"))  # ['hell', ' w', 'rld']
print(a.isdigit())  # False
print(b.isalpha())  # True
print(a.isalnum())  # False
print(b.isalnum())  # True
print("4373".isdigit())  # True
print("4373".isalnum())  # True
print("kai4373".isalnum())  # True
print("kai4373!".isalnum())  # False
print(a.islower())  # True
print("TEST".isupper())  # True
print(b.isupper())  # False
print(a.isspace())  # False
print(b.upper())  # MOUSE
print(a.startswith('hello')) # True
print(a.startswith('he')) # True
print(ord('a'))  # 97
print(ord('5'))
