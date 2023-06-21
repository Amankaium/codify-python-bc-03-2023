txt = '''
Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule.[34]

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[35][36]

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[37] Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2.[38]

Python consistently ranks as one of the most popular programming languages.[39][40][41][42]
'''
keyword = ["Python", "is", "in", "with"]
# result = ["Python", 9, "is", 4, "in", 3, 'with', 2]
result = ["Python", 0, "is", 0, "in", 0, 'with', 0]
words = txt.split()  # ['Python', 'is', 'a', 'high-level,'...]
for word in words:
    if word == keyword[0]:
        result[1] += 1
    elif word == keyword[1]:
        result[3] += 1  # result[3] = result[3] + 1
    elif word == keyword[2]:
        result[5] += 1
    elif word == keyword[3]:
        result[7] += 1
print(result)
