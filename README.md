# Aplikacja Flask – Projekt do laboratoriów

**pogrubienie**


## CI/CD

Projekt wykorzystuje GitHub Actions do automatycznego uruchamiania testów (`pytest`, `flake8`) przy każdym `push` i `pull request`.

Po przejściu testów, aplikacja jest automatycznie wdrażana na Render.com poprzez zintegrowane repozytorium GitHub.

- Wykorzystane narzędzia: GitHub Actions, Docker, pytest, flake8
- Środowisko uruchomieniowe: Python 3.11, Flask

https://flask-projekt-13ql.onrender.com/




Prosta aplikacja webowa w Flasku z 3 dostępnymi trasami:
- `/` – strona główna
- `/message` – przykladowa trasna, w przyszlosci rozwinieta
- `/health` – status działania


## Technologie
- Python 3
- Flask
- Git + GitHub


## Endpointy

- `/square/<n>` – zwraca n² jako wynik działania kalkulatora
- `/add/<n>`- sciezka do kalkulatora 
- `/health/<n>` - sprawdzenie stanu (pokazuje OK)
 

## Przykładowe użycie API:

- `GET /add?a=4&b=5` → `{"result": 9}`
- `GET /square/6` → `{"result": 36}`
- `GET /divide?a=10&b=0` → `{"error": "Nie można dzielić przez 0"}`




## Funkcjonalności

- `/add-ui` – graficzny kalkulator dodawania, odejmowania, mnożenia i dzielenia
- `/add?a=2&b=3` – REST API do dodawania
- `/subtract`,  `/*` – inne operacje
- `/square/<n>` – zwraca n²




## Interfejs graficzny (HTML):

Dostępny pod `/add-ui` – umożliwia łatwe wpisanie liczb i wybór działania bez przeładowywania strony.


# 1. Zbuduj obraz Dockera
docker build -t flask-kalkulator .

# 2. Uruchom kontener
docker run -p 5000:5000 flask-kalkulator

# 3. Wejdź w przeglądarce:
http://localhost:5000







```bash
pip install -r requirements.txt
python app.py

