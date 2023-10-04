from flask import Blueprint, redirect, url_for, render_template, request
lab3 = Blueprint('lab3', __name__)


@lab3.route("/")
@lab3.route("/index")
def start ():
  return redirect("/menu", code=302)


@lab3.route("/menu")
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
          <a href="/lab2">Вторая лабораторная работа</a>
          </li>
        </ol>

        <footer style="margin-top:20px;">
          &copy; Бут Валерия, ФБИ-13, 3 курс, 2023
        </footer>
      </body>
    </html>
'''


@lab3.route('/lab3/')
def lab():
    return render_template ('lab3.html')

@lab3.route('/lab3/form1')
def form1():
    errors = {}
    errorss = {}
    user = request.args.get ('user')
    if user == '':
       errors['user'] = 'Заполните поле!'

    age = request.args.get ('age')
    if age == '':
       errorss['age'] = 'Заполните поле!'

    sex = request.args.get ('sex')
    
    return render_template ('form1.html', user = user, age = age, sex = sex, errors = errors, errorss = errorss)


