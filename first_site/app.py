# first_site/app.py <- файл обязательно
from flask import Flask

app = Flask(__name__)  # app.py

@app.route('/')
def homepage():
    with open('counter.txt', 'r') as my_file:
        number = int(my_file.readline())
        number += 1

    with open('counter.txt', 'w') as my_file:
        my_file.write(str(number))
    return "hello world!"

@app.route('/about')  # url, route, путь, path, маршрут, ссылка, адрес
def about_us():  # функция обработчик

    # Ответ пользователю
    return """  
<h3>
    Наш сайт предлалгает вам широкий выбор автомобилей на покупку и аренду.<br>
    Также вы можете реаизовать продажу через нас
</h3>    
<div>
    <img src='https://hsto.org/r/w780/getpro/habr/post_images/b2f/05f/cf0/b2f05fcf0629dfe8bf0ed7945477f9bc.jpg'/>
</div>
"""

