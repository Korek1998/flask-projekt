from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Wersja A naglowka = Witaj w aplikacji Flask/header-a</h1>
        <nav>
            <a href="/">Strona główna</a> |
            <a href="/message">Wiadomość</a> |
            <a href="/health">Status</a>
        </nav>
    '''

@app.route('/message')
def message():
    return jsonify(message="to jest komunikat z servera flask")

@app.route('/health')
def health():
    return jsonify(status="OK")

if __name__ == '__main__':
    app.run(debug=True)

# Jakas Zmiana do serwera Flask
