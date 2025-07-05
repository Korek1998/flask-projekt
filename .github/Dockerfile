# Używamy oficjalnego obrazu Pythona
FROM python:3.11-slim

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj pliki do kontenera
COPY . /app

# Zainstaluj zależności
RUN pip install --no-cache-dir -r requirements.txt

# Otwórz port, na którym będzie działać Flask
EXPOSE 5000

# Uruchom aplikację
CMD ["python", "app.py"]
