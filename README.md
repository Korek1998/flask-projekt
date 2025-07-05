# Aplikacja Flask – Projekt do laboratoriów

**pogrubienie**



Prosta aplikacja webowa w Flasku z 3 dostępnymi trasami:
- `/` – strona główna
- `/message` – komunikat JSON
- `/health` – status działania


## Technologie
- Python 3
- Flask
- Git + GitHub


## Endpointy

- `/square/<n>` – zwraca n² jako wynik działania kalkulatora


## Przykładowe użycie API:

- `GET /add?a=4&b=5` → `{"result": 9}`
- `GET /square/6` → `{"result": 36}`
- `GET /divide?a=10&b=0` → `{"error": "Nie można dzielić przez 0"}`




## Funkcjonalności

- `/add-ui` – graficzny kalkulator dodawania, odejmowania, mnożenia i dzielenia
- `/add?a=2&b=3` – REST API do dodawania
- `/subtract`, `/multiply`, `/divide` – inne operacje
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

