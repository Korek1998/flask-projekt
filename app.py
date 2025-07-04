from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>wspolna wersja A i B naglowka = Witaj w aplikacji Flask/header>

        <nav>

            <a href="/">Strona główna</a> |
            <a href="/message">Wiadomość</a> |
            <a href="/health">Status</a>
        </nav>
    '''


@app.route('/msg')
def message():
    return jsonify(message="to jest poprawiony(PATCH) komunikat z servera flask")

@app.route('/health')
def health():
    return jsonify(status="OK")

@app.route('/contact')
def contact():
    return "<p>To jest nowa podstrona kontaktowa – dodana jako MINOR</p>"

from flask import request

@app.route('/add')
def add():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return jsonify(operation="add", result=a + b)

@app.route('/square/<int:n>')
def square(n):
    return jsonify(operation="square", result=n * n)


if __name__ == '__main__':
    app.run(debug=True)



# Jakas Zmiana do serwera Flask
