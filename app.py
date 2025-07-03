from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>to jest aplikacja flask</h1>"

@app.route('/message')
def message():
    return jsonify(message="to jest komunikat z servera flask")

@app.route('/health')
def health():
    return jsonify(status="OK")

if __name__ == '__main__':
    app.run(debug=True)

