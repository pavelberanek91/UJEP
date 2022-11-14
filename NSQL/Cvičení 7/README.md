# NoSQL databázové systémy

## Cvičení 7 - Dokumentová databáze Mongo

### Zadání

Cílem tohoto cvičení je zprovoznit databázi MongoDB.

#### 7.1 Spuštění MongoDB před Docker

Obraz pro MongoDB stáhneme příkazem v terminále: ```docker pull bitnami/mongodb:latest```. Tím se stáhne nejnovější verze obrazu MongoDB. 

Spuštění obrazu se provádí příkazem: ```docker run --name mongo mongodb```, kde mongo je název kontejneru a mongodb je název obrazu.

#### 7.2 Komunikace s MongoDB přes příkazovou řádku

Do obrazu se připojíme příkazem ```docker exec -it mongo bash```. Tím se spustí interaktivní shell, do kterého můžeme zadávat příkazy.

Příkazem ```use fakulta``` vytvoříme databázi falulta. Do této databáze přidáme 3 dokumenty do kolekce studenti:

```
db.studenti.save({ jméno: “Pavel Beránek” })
db.studenti.save({ jméno: “Jiří Škvor” })
db.studenti.save({ jméno: “Petr Kubera” })
```

Na dokument se zeptáme pomocí příkazu find: ```db.studenti.find({ jméno: “Pavel Beránek” })```

#### 7.3 Připojení MongoDB obrazu do docker-compose souboru

Pokud chcete přidat mongodb obraz do vaší aplikace s architekturou mikroslužeb, pak spuštění mongo v compose souboru vypadá takto:
```
version: '3.7'
services:
  mongodb_container:
    image: mongo:latest
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: rootpassword
    ports:
      - 27017:27017
    volumes:
      - mongodb_data_container:/data/db

volumes:
  mongodb_data_container:
```

#### 7.4 Komunikace s MongoDB přes Python

Pro komunikace s mongodb budeme potřebovat ovladač pro python: ```pip install pymongo```. Poté můžeme provést základní test komunikace python aplikace s mongodb:
```
from pymongo import MongoClient
  
# připojení do mongo databáze pomocí mongo klienta
client=MongoClient()
client = MongoClient(“mongodb://localhost:27017/”)
  
# připojení do konkrétní databáze
db = client["fakulta"]
  
# připojení ke kolekci
kolekce=db[‘studenti’]
  
# dokument ve formátu json (slovník slovníků), který přidáme do databáze
zaznam = {
  "jméno": "Pavel Beránek", 
  "obor": "Aplikovaná informatika", 
  "tags": ["KI", "PŘF", "APLINF"], 
  "počet kreditů": 120
}
  
# vložení záznamu (dokumentu) do databáze
zaznam = db.kolekce.insert(zaznam)

# čtení záznamů z databáze
for záznam in db.kolekce.find({jméno: "Pavel Beránek"})
    print(i)

```
