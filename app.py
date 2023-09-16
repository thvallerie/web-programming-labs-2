from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start ():
    return """
    <!doctype html>
    <html>
      <head>
        <title>Бут Валерия Сергеевна, Лабораторная 1 </title>
      </head>
      <body>
        <header>
          НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>

        <footer>
          &copy; Бут Валерия, ФБИ-13, 3 курс, 2023
        </footer>
      </body>
    </html>
"""