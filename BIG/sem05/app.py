from snakebite.client import Client
import os
import time

client = Client('localhost', 9000)

# Definice cílové cesty
destination_path = './tmp/vysledky.txt'

# Zajištění, že cílová složka existuje
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Kopírování souboru z HDFS s opakovaným pokusem o přístup, pokud je soubor uzamčen
retry_attempts = 5
for attempt in range(retry_attempts):
    try:
        for f in client.copyToLocal(['/data/vysledky.txt'], destination_path):
            print(f)
        break
    except PermissionError as e:
        print(f"Attempt {attempt + 1} failed with error: {e}")
        time.sleep(1)  # Počkejte chvíli před dalším pokusem
    else:
        print("Soubor byl úspěšně zkopírován.")
