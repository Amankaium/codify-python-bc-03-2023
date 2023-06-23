message = {
    'id': 772,
    "date": '23.06.2023',
    'time': "12:33",
    "text": "Доброе утро!",
    "is_sent": True,  # + v
    "is_arrived": True,  # + v
    "is_readed": False  # + v
}

# 1. Выведите текст сообщения
# print(message["text"])

# 2. Выведите дату сообщения
# print(message["date"])

# 3. Выведите время сообщения
# print(message["time"])

# 4. Выведите статус:
# кол-во птичек зависит от значений
# is_sent, is_arrived, is_readed
status = ''  # 'vvv'
if message["is_sent"]:
    status += 'v'
if message['is_arrived']:
    status += 'v'
if message['is_readed']:
    status += 'v'
# print(status)
message["status"] = status

print(message["date"])
print("- " * 15)
print(message["text"])
print(message["time"], '\t', message["status"])
print("- " * 15)
