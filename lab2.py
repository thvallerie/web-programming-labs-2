from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route("/")
@lab2.route("/index")
def start ():
  return redirect("/menu", code=302)


@lab2.route("/menu")
def menu ():
  return '''
    <!doctype html>
    <html>
      <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''" />
      </head>
      <body>
        <header>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</header>

        <h1>web-сервер на flask</h1>

        <h3>Меню: </h3>
        <ol>
          <li>
          <a href="/lab1">Первая лабораторная работа</a>
          </li>
          <li>
          <a href="/lab2">Вторая  лабораторная работа</a>
          </li>
        </ol>

        <footer style="margin-top:20px;">
          &copy; Бут Валерия, ФБИ-13, 3 курс, 2023
        </footer>
      </body>
    </html>
'''

@lab2.route('/lab2/example')
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

@lab2.route('/lab2/')
def lab():
    return render_template ('lab2.html')

@lab2.route('/lab2/moodboard')
def moodboard():
    return render_template ('moodboard.html')
