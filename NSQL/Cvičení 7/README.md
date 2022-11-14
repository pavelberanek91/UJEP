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

lorem

#### 7.4 Komunikace s MongoDB přes Python

lorem

https://realpython.com/search?q=mongodb

https://realpython.com/introduction-to-mongodb-and-python/

https://realpython.com/web-scraping-with-scrapy-and-mongodb/
