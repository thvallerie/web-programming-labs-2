from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start ():
  return redirect("/menu", code=302)

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
        {'book' : 'Божественная комедия', 'author' : 'Данте Алегьери', 'zhanr' : 'Поэма', 'str' : 548},
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

@app.route("/menu")
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

@app.route("/lab1")
def lab1():
  return """
    <!doctype html>
    <html>
      <head>
        <title>Бут Валерия Сергеевна, Лабораторная 1 </title>
      </head>
      <body>
        <header>НГТУ, ФБ, Лабораторная работа 1</header>

        <h1>web-сервер на flask</h1>

        <p>
          Flask — фреймворк для создания веб-приложений на языке
          программирования Python, использующий набор инструментов
          Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
          называемых микрофреймворков — минималистичных каркасов
          веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </p>

        <a href="/menu">Меню</a>

        <h2>Реализованные роуты</h2>

        <ol>
          <li><a href="/lab1/baobab">Баобаб</a></li>
          <li><a href="/lab1/student">Студент</a></li>
          <li><a href="/lab1/python">Python</a></li>
        </ol>

        <footer>
          &copy; Бут Валерия, ФБИ-13, 3 курс, 2023
        </footer>
      </body>
    </html>
"""

@app.route("/lab1/baobab")
def baobab  ():
  return '''
    <!doctype html>
    <head>
      <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''" />
    </head>
    <html>
      <body>
        <h1>Баобаб</h1>
        <img src="''' + url_for('static', filename='baobab.jpg') + '''">
      </body>
    </html>
'''

@app.route("/lab1/student")
def student  ():
  return '''
    <!doctype html>
    <html>
      <body>
        <h1>Бут Валерия Сергеевна</h1>
        <img src="''' + url_for('static', filename='nstu.jpg') + '''">
      </body>
    </html>
'''

@app.route("/lab1/python")
def python():
  return '''
    <!doctype html>
    <html>
      <body>
        <p>
          Python (МФА]; в русском языке встречаются названия пито́н[23] или па́йтон[24]) — высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью[25][26], ориентированный на повышение производительности разработчика, 
          читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ[27]. 
          <br>
          Язык является полностью объектно-ориентированным в том плане, что всё является объектами[25]. Необычной особенностью языка является выделение блоков кода пробельными отступами[28]. 
          Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к документации[27]. Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов[25]. 
          Недостатками языка являются зачастую более низкая скорость работы и более высокое потребление памяти написанных на нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, таких как C или C++[25][27].
        </p>

         <img src="''' + url_for('static', filename='py.webp') + '''">
       
      </body>
    </html>
'''