from flask import Flask, redirect, url_for, render_template
from lab1 import lab1 

app = Flask(__name__)
app.register_blueprint(lab1)

@app.route('/lab2/example')
def example():
    name, lab_num, group, course ='Бут Валерия', 2, 'ФБИ-13', 3
    fruits = [
      {'name': 'яблочки', 'price': 100},
      {'name': 'груши', 'price': 120},
      {'name': 'апельсинчики', 'price': 80},
      {'name': 'мандаринчики', 'price': 95},
      {'name': 'манго', 'price': 321},
    ]

    return render_template('example.html',
                         name=name, lab_num=lab_num, group=group,
                         course=course, fruits=fruits, books=books)

books = [
        {'book' : 'Мастер и Маргарита', 'author' : 'Михаил Булгаков', 'zhanr' : 'Любовный роман', 'str' : 480},
        {'book' : 'Убийство в восточном экспрессе', 'author' : 'Агата Кристи', 'zhanr' : 'Детектив', 'str' : 317},
        {'book' : 'Код Да Винчи', 'author' : 'Дэн Браун', 'zhanr' : 'Детектив, Триллер', 'str' : 544},
        {'book' : 'Ганнибал', 'author' : 'Томас Харрис', 'zhanr' : ' Психологический роман ужасов', 'str' : 580},
        {'book' : 'Финансист', 'author' : 'Теодор Драйзер', 'zhanr' : 'Роман', 'str' : 576},
        {'book' : 'Дракула', 'author' : 'Брэм Стокер', 'zhanr' : 'Роман', 'str' : 500},
        {'book' : 'Приключения Шерлока Холмса', 'author' : 'Артур Конан-Дойл', 'zhanr' : 'Детектив', 'str' : 2300},
        {'book' : 'Божественная комедия', 'author' : 'Данте Алигьери', 'zhanr' : 'Поэма', 'str' : 548},
        {'book' : 'Не тупи', 'author' : 'Джон Синсеро', 'zhanr' : 'Зарубежная психология', 'str' : 70},
        {'book' : 'Дюна', 'author' : 'Фрэнк Герберт', 'zhanr' : 'Фантастика', 'str' : 768},
        {'book' : 'Фауст', 'author' : 'Иоганн Гёте', 'zhanr' : 'Филосовская драма', 'str' : 350},
    ]

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/moodboard')
def moodboard():
    return render_template('moodboard.html')

