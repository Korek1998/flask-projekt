from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Kalkulator Flask</h1>

        <nav>

            <a href="/">Strona główna</a> |
            <a href="/msg">Wiadomość</a> |
            <a href="/health">Status</a>
	    <a href="/add">Dodawania</a>
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


@app.route('/add')
def add_ui():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Kalkulator</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; padding: 30px; background: #f5f5f5; }
            nav a { margin: 0 10px; text-decoration: none; color: #0077cc; }
            input[type=number] { width: 60px; padding: 5px; margin: 5px; }
            button { padding: 10px 20px; margin: 10px; }
            #result { font-size: 24px; margin-top: 20px; color: #333; }
            .calc-box { background: #fff; display: inline-block; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px #ccc; }
        </style>
    </head>
    <body>
        <h1>Kalkulator Flask</h1>
        <nav>
            <a href="/">Strona główna</a> |
        </nav>

        <div class="calc-box">
            <h2>Dodaj liczby</h2>
            <input type="number" id="a" placeholder="a">
            <input type="number" id="b" placeholder="b">
            <br>
            <button onclick="calculate('+')">Dodaj</button>
            <button onclick="calculate('-')">Odejmij</button>
            <button onclick="calculate('*')">Pomnóż</button>
            <div id="result"></div>
        </div>

        <script>
            function calculate(op) {
                const a = document.getElementById('a').value;
                const b = document.getElementById('b').value;
                fetch(`/${op}?a=${a}&b=${b}`)
                    .then(res => res.json())
                    .then(data => {
                        document.getElementById('result').innerHTML = `<strong>Wynik:</strong> ${data.result ?? data.error}`;
                    })
                    .catch(() => {
                        document.getElementById('result').innerHTML = 'Błąd w obliczeniach';
                    });
            }
        </script>
    </body>
    </html>

    '''



@app.route('/api/add')
def add_api():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return jsonify(result=a + b)




@app.route('/+')
def add():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return jsonify(result=a + b)

@app.route('/-')
def subtract():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return jsonify(result=a - b)

@app.route('/*')
def multiply():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return jsonify(result=a * b)





@app.route('/square/<int:n>')
def square(n):
    return jsonify(operation="square", result=n * n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



# Jakas Zmiana do serwera Flask
