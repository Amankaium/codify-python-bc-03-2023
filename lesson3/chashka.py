num = int(input())

# если последняя цифра 1 и число НЕ находится в промежутке от 10 до 15
if num % 10 == 1 and not 10 < num < 15:
    word = 'чашка'
elif 2 <= num % 10 <= 4 and not 10 < num < 15:  # 2 <= num and num <= 4
    word = 'чашки'
else:
    word = 'чашек'

print(f'{num} {word}')
