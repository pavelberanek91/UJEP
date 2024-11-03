# Dockerfile pro Dash aplikaci

# Použijte základní obraz s Pythonem
FROM python:3.9-slim

# Nastavte pracovní adresář
WORKDIR /app

# Zkopírujte soubory aplikace do kontejneru
COPY . /app

# Nainstalujte potřebné balíčky
RUN pip install -r requirements.txt

# Spusťte aplikaci
CMD ["python", "app.py"]
