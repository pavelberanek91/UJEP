# Datová úložiště a nástroje pro Big Data (KI/BIG)

## Seminář 3 -  NoSQL databáze a BigData (MongoDB, Caché/Redis)

### Samostudium

#### S3.1 - NoSQL databáze

NoSQL databáze jsou typ databázových systémů, které se od tradičních relačních databází liší především tím, že nevyžadují pevně definované schéma a umožňují flexibilní a různorodé ukládání dat. „NoSQL“ doslova znamená „Not Only SQL“, což naznačuje, že tyto databáze mohou ukládat a spravovat data bez použití klasického strukturovaného dotazovacího jazyka SQL.¨

**Hlavní vlastnosti NoSQL databází**
- Flexibilní schéma: NoSQL databáze nevyžadují pevně definované schéma, což znamená, že struktura dat může být flexibilní a snadno upravitelná. To je užitečné pro aplikace, kde se struktura dat často mění.
- Horizontální škálování: NoSQL databáze jsou navrženy tak, aby podporovaly horizontální škálování, což znamená, že data mohou být rozložena na více serverů (tzv. sharding), čímž lze zvyšovat výkon i kapacitu databáze.
- Velké objemy dat: NoSQL databáze jsou ideální pro aplikace, které pracují s velkými objemy nestrukturovaných nebo polostrukturovaných dat, jako jsou například záznamy z internetu věcí, analýzy big data nebo logy.
- Rychlost a výkon: NoSQL databáze jsou optimalizované pro vysoký výkon a nízkou latenci, což je užitečné pro aplikace, které vyžadují rychlý přístup k datům (například real-time aplikace).

**Typy NoSQL databází**
NoSQL databáze se dělí do několika hlavních kategorií na základě způsobu, jakým ukládají data:
- Dokumentově orientované databáze: Ukládají data jako dokumenty (nejčastěji ve formátu JSON nebo BSON). Každý dokument může mít jinou strukturu, což umožňuje flexibilní ukládání složitých dat. Příkladem je MongoDB.
- Klíč-hodnota databáze: Ukládají data ve formě párů klíč-hodnota, kde každému klíči je přiřazena určitá hodnota. Tento typ databáze je velmi rychlý a efektivní pro jednoduché operace. Příkladem je Redis nebo Riak.
- Sloupcové databáze: Data jsou organizována do sloupců a ukládána po sloupcích, což je efektivní pro analytické dotazy na velkých datasetů. Příkladem je Apache Cassandra nebo HBase.
- Grafové databáze: Jsou optimalizované pro práci s daty, která jsou propojena složitými vztahy. Každý uzel v grafové databázi představuje entitu, a hrany reprezentují vztahy mezi těmito entitami. Příkladem je Neo4j.

**Výhody NoSQL databází**
- Škálovatelnost: Díky horizontálnímu škálování jsou NoSQL databáze vhodné pro velké objemy dat.
- Rychlost a výkon: Jsou optimalizovány pro rychlý přístup k datům a nízkou latenci.
- Flexibilní schéma: Umožňují snadné přizpůsobení struktury dat bez nutnosti měnit celkové schéma databáze.

**Paradigmata správy transakcní**

Důležité je ještě zmínit, jak databáze spravují transakce a konzistenci dat. ACID a BASE jsou dvě různá paradigmata pro správu transakcí a konzistence dat v databázích. Obě tato paradigmata mají odlišné přístupy k zajištění konzistence, dostupnosti a spolehlivosti dat, a zatímco ACID je tradičně spojován s relačními databázemi, BASE je častěji spojován s NoSQL databázemi.

ACID je sada vlastností, které zajišťují spolehlivost a konzistenci transakcí v tradičních relačních databázích. Díky těmto vlastnostem jsou relační databáze ideální pro aplikace, kde je kritická přesná konzistence a spolehlivost, například pro finanční systémy nebo systémy správy zásob.
- Atomicita (Atomicity): Transakce je „atomická“, což znamená, že buď proběhne úplně, nebo vůbec. Pokud nastane jakýkoli problém během provádění transakce, všechny změny se vrátí do původního stavu.
- Konzistence (Consistency): Transakce musí uvést databázi z jednoho konzistentního stavu do druhého, což znamená, že po transakci musí data splňovat všechny definované pravidla integrity.
- Izolace (Isolation): Transakce by měla být izolovaná od ostatních, což znamená, že jejich současné provádění by nemělo negativně ovlivnit výsledek každé z nich.
- Trvalost (Durability): Jakmile je transakce potvrzena, všechny změny jsou trvale uloženy, i kdyby došlo k výpadku systému.

BASE je soubor vlastností, který je často aplikován na NoSQL databáze. BASE vlastnosti vycházejí z principu, že pro některé aplikace může být výhodnější dosáhnout vyšší dostupnosti a škálovatelnosti i za cenu nižší konzistence. BASE je flexibilní přístup, který je vhodný pro aplikace, kde je prioritou vysoká dostupnost a horizontální škálovatelnost, například pro sociální sítě, streamovací služby nebo jiné systémy, kde může být mírná nekonzistence dočasně tolerována.
- Základní dostupnost (Basically Available): Systém garantuje dostupnost, což znamená, že vždy bude možné získat odpověď, i když nemusí být aktuální nebo úplně konzistentní.
- Měkký stav (Soft State): Stav systému se může časem měnit i bez vnějšího zásahu (například změny se šíří postupně, takže mohou být dočasně nekonzistentní).
- Eventuální konzistence (Eventual Consistency): Data se nakonec dostanou do konzistentního stavu, ale nemusí to být okamžitě. Tento model umožňuje, aby různé části systému měly dočasně různá data, dokud nedojde k jejich synchronizaci.

#### S3.2 - Redis

Redis (Remote Dictionary Server) je open-source in-memory databáze typu key-value (klíč-hodnota), která se často používá jako vyrovnávací paměť (cache), message broker nebo jako databáze pro rychlý přístup k datům. Redis ukládá data primárně v paměti RAM, což mu umožňuje velmi rychlý přístup, a díky tomu je vhodný pro aplikace, kde je klíčový výkon a nízká latence.

**Klíčové vlastnosti Redis**
- In-memory databáze: Redis ukládá data v paměti (RAM), což mu poskytuje extrémně rychlý přístup, což je ideální pro aplikace, kde je důležitá rychlost načítání dat, jako jsou vyrovnávací paměti.
- Struktury dat: Redis podporuje různé datové struktury jako řetězce, seznamy, množiny, řazení, hash mapy, bitmapy a další, což umožňuje efektivní a flexibilní práci s různými typy dat.
- Persistence: Redis umí také uchovávat data na disku, což zajišťuje jejich zachování i při restartu serveru. Má několik režimů persistencí, jako je ukládání snapshotů (dumping) nebo zapisování změn na disk (append-only file), které kombinují rychlost s trvalým ukládáním.
- Podpora pro pub/sub: Redis podporuje systém publikování a odběru (publish/subscribe), což ho činí vhodným pro aplikace, které vyžadují messaging a real-time notifikace.
- Replikace a clustering: Redis podporuje replikaci dat (master-slave architekturu) a clustering (shardování dat mezi více uzly), což umožňuje horizontální škálování pro vyšší výkon a dostupnost.
- Transakce: Redis umožňuje provádět transakce, což znamená, že lze provést více příkazů jako jednu jednotku práce (jediný atomický celek).

Redis se často používá jako cache pro uložení často přistupovaných dat, například pro urychlení odpovědí na API požadavky nebo pro uložení session dat uživatelů. Používá se také pro řízení fronty požadavků v reálném čase, například v aplikacích pro chat nebo streamování, kde může sloužit jako message broker.

#### S3.3 - MongoDB

MongoDB je dokumentově orientovaná NoSQL databáze, která ukládá data ve formátu JSON (přesněji BSON, což je binární formát JSON), čímž umožňuje flexibilní a škálovatelné ukládání dat. MongoDB je navržena tak, aby snadno pracovala s velkými objemy dat a poskytovala vysoký výkon i při horizontálním škálování.

**Klíčové vlastnosti MongoDB**
- Dokumentově orientovaná: Data jsou uložena jako dokumenty (záznamy) ve formátu BSON, což umožňuje flexibilní schéma a snadné ukládání složitých strukturovaných dat.
- Bez schématu (schema-less): Na rozdíl od tradičních relačních databází nemusí mít MongoDB pevně definované schéma, což znamená, že jednotlivé dokumenty mohou mít různou strukturu, což usnadňuje změny v datovém modelu.
- Flexibilita: MongoDB je ideální pro rychlý vývoj, protože umožňuje dynamicky přidávat nové atributy a upravovat strukturu dat podle potřeby.
- Škálovatelnost: MongoDB podporuje horizontální škálování, což znamená, že data mohou být rozdělena na více serverů (shardování), což usnadňuje správu velkých objemů dat.
- Indexování a vyhledávání: MongoDB podporuje indexování polí v dokumentech, což zvyšuje výkon při vyhledávání a zpracování dat.
- Agregační framework: MongoDB má robustní agregační pipelinu, která umožňuje provádět složité dotazy, analýzy a transformace dat přímo v databázi.

**Použití MongoDB**
MongoDB se běžně používá v aplikacích, kde je potřeba ukládat a rychle načítat velké objemy dat, jako jsou webové aplikace, e-commerce platformy, analýzy big data a IoT. Je také vhodná pro aplikace, kde je struktura dat různorodá nebo se často mění.

Zde je ukázka připojení k databázi a založení prvotního kolekce (tabulky) záznamů. Pro lepší představu uvádím i SQL ekvivalent v SQLite3:

**Připojení se k MongoDB pomocí Pymongo**
```sql
CREATE TABLE IF NOT EXISTS moje_kolekce (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    city TEXT
);
```

```python
from pymongo import MongoClient

# Připojení k MongoDB
client = MongoClient("mongodb://localhost:27017/")
# Výběr databáze a kolekce
db = client["moje_databaze"]
collection = db["moje_kolekce"]
```

#### S3.4 - Mongo Query Language (MQL)

Mongo Query Language (MQL) je jazyk dotazů používaný v MongoDB, který umožňuje práci s daty v dokumentově orientovaných databázích. Jeho syntaxe je založena na JSON a podporuje různé operace pro manipulaci s dokumenty v kolekcích, jako je například vkládání, aktualizace, mazání a vyhledávání dat. Následují ukázky základních operací v Pymongo a k tomu ekvivalentni dotazy v SQL (pro SŘBD SQLite3):

**Vložení jednoho dokumentu do kolekce**
```sql
INSERT INTO moje_kolekce (name, age, city) VALUES ("John", 30, "New York");
```

```python
document = {"name": "John", "age": 30, "city": "New York"}
collection.insert_one(document)
```

**Vložení více dokumentů najednou**
```sql
INSERT INTO moje_kolekce (name, age, city) VALUES
("Alice", 25, "Los Angeles"),
("Bob", 27, "Chicago"),
("Charlie", 35, "San Francisco");
```

```python
documents = [
    {"name": "Alice", "age": 25, "city": "Los Angeles"},
    {"name": "Bob", "age": 27, "city": "Chicago"},
    {"name": "Charlie", "age": 35, "city": "San Francisco"}
]
collection.insert_many(documents)
```

**Vyhledání všech dokumentů v kolekci**
```sql
SELECT * FROM moje_kolekce;
```

```python
for doc in collection.find():
    print(doc)
```

**Vyhledání dokumentů na základě podmínky (například věk > 25)**
```sql
SELECT * FROM moje_kolekce WHERE age > 25;
```

```python
query = {"age": {"$gt": 25}}
for doc in collection.find(query):
    print(doc)
```

**Vyhledání dokumentů s výběrem konkrétních polí (name a city)**
```sql
SELECT name, city FROM moje_kolekce WHERE age > 25;
```

```python
query = {"age": {"$gt": 25}}
projection = {"name": 1, "city": 1, "_id": 0}  # Skryjeme pole "_id"
for doc in collection.find(query, projection):
    print(doc)
```

**Aktualizace jednoho dokumentu (změníme věk na 31 pro dokument, kde name je "John")**
```sql
UPDATE moje_kolekce SET age = 31 WHERE name = "John";
```

```python
collection.update_one({"name": "John"}, {"$set": {"age": 31}})
```

**Aktualizace více dokumentů (zvýšení věku o 1 pro všechny, kdo mají věk > 25)**
```sql
UPDATE moje_kolekce SET age = age + 1 WHERE age > 25;
```

```python
collection.update_many({"age": {"$gt": 25}}, {"$inc": {"age": 1}})
```

**Smazání jednoho dokumentu (smaže dokument, kde name je "Alice")**
```sql
DELETE FROM moje_kolekce WHERE name = "Alice";
```

```python
collection.delete_one({"name": "Alice"})
```

**Smazání více dokumentů (smaže všechny dokumenty, kde věk je větší než 30)**
```sql
DELETE FROM moje_kolekce WHERE age > 30;
```

```python
collection.delete_many({"age": {"$gt": 30}})
```

**Použití agregační pipeliny ke zjištění průměrného věku pro každé město**
```sql
SELECT city, AVG(age) AS average_age FROM moje_kolekce GROUP BY city;
```

```python
pipeline = [
    {"$group": {"_id": "$city", "average_age": {"$avg": "$age"}}}
]

for result in collection.aggregate(pipeline):
    print(result)
```

**Použití logických operátorů**
```sql
SELECT * FROM moje_kolekce WHERE age > 25 OR city = "San Francisco";
```

```python
query = {
    "$or": [
        {"age": {"$gt": 25}},
        {"city": "San Francisco"}
    ]
}

for doc in collection.find(query):
    print(doc)
```

#### S3.5 - Agregační roury

V MongoDB jsou agregační roury (pipelines) pokročilým nástrojem pro zpracování a analýzu dat. Umožňují kombinovat různé kroky (tzv. stages), které postupně zpracovávají dokumenty z kolekce. Každý krok v pipelině vykonává určitý úkol, jako například filtrování, třídění, seskupování nebo transformaci dat. Výstup jednoho kroku se stává vstupem pro další krok, což umožňuje postupné vytváření komplexních dotazů.

**Klíčové kroky v agregační rouře**
1. $match – Filtrování dokumentů podle specifických kritérií (např. {"age": {"$gte": 18}}).
2. $group – Seskupování dat podle určitého pole, například počítání průměru, součtu nebo dalších agregovaných hodnot.
3. $project – Transformace nebo výběr polí, která mají být součástí výstupu. Umožňuje také vytvářet nová pole z existujících (např. formátování dat).
4. $sort – Třídění výsledků podle zadaných kritérií (např. {"date": -1} pro sestupné pořadí).
5. $limit a $skip – Omezení počtu dokumentů nebo přeskočení určitého počtu dokumentů, což může být užitečné pro stránkování výsledků.
6. $lookup – Provedení "joinu" mezi kolekcemi, což je obdoba SQL spojení mezi tabulkami.
7. $unwind – "Rozbalení" polí typu pole (array) do jednotlivých dokumentů, což umožňuje práci s daty uvnitř pole každého dokumentu.

Příklad agregační roury:
```
db.orders.aggregate([
  { "$match": { "date": { "$gte": ISODate("2024-10-01") }}},
  { "$group": { "_id": "$product_id", "totalRevenue": { "$sum": "$price" }}},
  { "$sort": { "totalRevenue": -1 }}
])
```
* $match filtruje objednávky pouze z posledního měsíce
* $group seskupuje objednávky podle product_id a počítá celkový příjem (totalRevenue) pro každý produkt
* $sort třídí produkty podle příjmu v sestupném pořadí

### Cvičení

Účelem tohoto cvičení je procvičit si práci s agregační pipelinou v MongoDB na rozsáhlých datech. Budete analyzovat dataset obsahující informace o prodejích v e-commerce.

#### C3.1 - Připrava docker prostředí
Připravte si vývojové prostředí, ve kterém budete pracovat s mongem. Pro cvičení budete potřebovat 3 komponenty:
1. Dash - datové dashboardy v Pythonu (můžete pro prvotní úkoly vynechat)
2. Mongodb
3. Mongo-express - client k prohlížení mongodat 

#### C3.2 - Generování umělých dat
Spusťte následující skript, který vám vygeneruje potřebná data na zkoumání principů agregačních rour v MongoDB. Budete si muset nastavit URI podle Vašeho docker-compose souboru.

```
import random
from datetime import datetime, timedelta
import pymongo

# Připojení k MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ecommerce"]
orders_collection = db["orders"]
returns_collection = db["returns"]

# Pomocná funkce pro generování náhodného data
def random_date(start, end):
    delta = end - start
    random_days = random.randrange(delta.days)
    return start + timedelta(days=random_days)

# Rozsah dat pro generování objednávek
start_date = datetime.now() - timedelta(days=730)  # Poslední 2 roky
end_date = datetime.now()

# Data pro generování
product_names = ["Laptop", "Smartphone", "Headphones", "TV", "Tablet", "Camera", "Printer", "Monitor"]
categories = ["Electronics", "Home Appliances", "Clothing", "Sports", "Books"]
regions = ["North America", "Europe", "Asia", "Australia", "South America"]
return_reasons = ["Defective", "Not as described", "Arrived late", "Changed mind"]

# Parametry
num_orders = 10000
return_probability = 0.1  # 10 % objednávek bude vráceno

# Generování dat
orders_data = []
returns_data = []

for i in range(num_orders):
    order_id = i + 1
    product_name = random.choice(product_names)
    category = random.choice(categories)
    price = round(random.uniform(5, 2000), 2)  # Cena mezi 5 a 2000
    quantity = random.randint(1, 5)
    order_date = random_date(start_date, end_date)
    customer_region = random.choice(regions)

    # Vytvoření záznamu objednávky
    order = {
        "order_id": order_id,
        "product_name": product_name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "order_date": order_date,
        "customer_region": customer_region,
    }
    orders_data.append(order)

    # Náhodné rozhodnutí, zda bude objednávka vrácena
    if random.random() < return_probability:
        return_date = order_date + timedelta(days=random.randint(1, 30))  # Datum vrácení do 30 dnů
        reason = random.choice(return_reasons)
        return_record = {
            "return_id": len(returns_data) + 1,
            "order_id": order_id,
            "return_date": return_date,
            "reason": reason,
        }
        returns_data.append(return_record)

# Vložení dat do MongoDB
orders_collection.insert_many(orders_data)
returns_collection.insert_many(returns_data)

# Uzavření připojení
client.close()

print(f"Inserted {len(orders_data)} orders and {len(returns_data)} returns into the database.")
```

#### C3.3 - Zpracování velkých dat s MongoDB

**Seskupování a filtrování: Nejprodávanější produkty**
- Pomocí agregační pipeliny vyberte top 5 nejprodávanějších produktů na základě počtu prodaných kusů. 
- Použijte kroky $group, $sort, a $limit.

**Analýza podle kategorie: Průměrná cena produktů**
- Seskupte data podle kategorie (category) a vypočítejte průměrnou cenu produktů v každé kategorii. 
- Použijte kroky $group a $avg.

**Trend podle regionů: Prodeje v průběhu času**
- Pomocí $match vyberte pouze objednávky za poslední rok. 
- Poté použijte $group a $sum, abyste zjistili celkový prodej (hodnotu) v jednotlivých regionech (customer_region) po měsících. 
- Pro zjednodušení použijte $dateToString pro extrahování roku a měsíce z order_date.

**Detekce sezónních výkyvů: Nejvyšší prodeje během roku**
- Zjistěte, ve kterém měsíci byl celkový objem prodejů (součet price krát quantity) nejvyšší. 
- Použijte $group a $max.

**Analýza ziskovosti: Výpočet celkového příjmu za kategorii a region**
- Seskupte data podle kategorie a regionu zákazníka a vypočítejte celkový příjem. 
- Použijte $group s využitím výpočtu celkového příjmu jako price * quantity.

**Zákaznická věrnost: Počet objednávek na zákazníka**
- Předpokládejte, že zákazník má jednoznačný customer_id. 
- Spočítejte, kolik objednávek vytvořil každý zákazník, a určete, kolik zákazníků vytvořilo více než 10 objednávek. 
- Použijte $group a $count.

#### C3.4 - Pokročilé příkazy

**Spojení s další kolekcí ($lookup): Analýza vratek**
- Přidejte druhou kolekci, například returns, která obsahuje údaje o vrácených objednávkách:
    - return_id: ID vrácení
    - order_id: ID původní objednávky
    - return_date: datum vrácení
    - reason: důvod vrácení
- Pomocí $lookup propojte kolekci orders s kolekcí returns, abyste zjistili, kolik procent objednávek bylo vráceno v jednotlivých kategoriích produktů. 
- Použijte $group pro seskupení podle category, spočítejte celkový počet objednávek a počet vratek pro každou kategorii.

**Rozbalení polí ($unwind): Práce s více položkami na objednávku**
- Rozšiřte dataset orders, aby každá objednávka mohla obsahovat pole items, což je pole objektů s více položkami (každá položka má product_name, price, a quantity). 
- Použijte $unwind k „rozbalení“ položek objednávky na jednotlivé dokumenty, a pak:
    - Seskupte je podle product_name a spočítejte celkový počet prodaných kusů každého produktu.
    - Identifikujte, které produkty jsou nejčastěji součástí větších objednávek (například těch, které obsahují 3 a více položek).

**Hierarchické seskupování ($bucket nebo $bucketAuto): Cenové segmenty produktů**
- Vytvořte cenové segmenty pro produkty pomocí $bucket nebo $bucketAuto. Například:
    - Segment „Nízká cena“ pro produkty do 50 Kč
    - Segment „Střední cena“ pro produkty mezi 50 a 200 Kč
    - Segment „Vysoká cena“ pro produkty nad 200 Kč
- Určete počet produktů v každém segmentu a zjistěte, která cenová skupina se prodává nejvíce v jednotlivých regionech.

**Textové vyhledávání ($text): Analýza důvodů vratek**
- U kolekce returns přidejte textový index na pole reason, který umožní textové vyhledávání důvodů vratek. 
- Vyhledejte všechny záznamy, kde důvod vrácení obsahuje klíčové slovo „poškozené“ nebo „neodpovídá“. 
- Spočítejte, jak často se tyto důvody vracení objevují a identifikujte regiony s nejvyšším počtem takto označených vratek.

**Analýza trendů v průběhu času ($dateToString): Prodeje v sezónních obdobích**
- Vytvořte agregaci, která sleduje počet prodejů pro každé roční období (jaro, léto, podzim, zima) na základě data objednávky. 
- Pomocí $dateToString extrahujte měsíc z order_date a přiřaďte jej k příslušnému období. 
- Vyhodnoťte, které produkty nebo kategorie mají sezónní výkyvy a v kterém období se prodávají nejvíce.

**Dynamické výpočty ($addFields a $expr): Výpočet marže**
- Přidejte do kolekce orders nebo items pole cost_price, které představuje nákladovou cenu produktu. 
- Pomocí $addFields vypočítejte marži jako price - cost_price a označte produkty, které mají marži nižší než průměrná marže pro danou kategorii. 
- Pomocí $expr vyfiltrujte produkty s nízkou marží a určete, které kategorie obsahují nejvíce těchto produktů.

#### C3.5 - Vizualizace informací
Vytvořte pomocí Dash/Plotly interaktivní datový dashboard, který vizualizuje klíčové metriky a trendy z e-commerce dat získaných z MongoDB agregační pipeliny.

**Přehled nejprodávanějších produktů (Top 5)**
- Vytvořte sloupcový graf, který zobrazuje top 5 nejprodávanějších produktů podle počtu prodaných kusů.
- Načtěte data z MongoDB pomocí agregační pipeliny, která seskupí objednávky podle produktů a seřadí je podle počtu prodaných kusů.

**Prodeje v průběhu času podle regionů**
- Vytvořte čárový graf nebo sloupcový graf, který zobrazuje měsíční prodeje v různých regionech.
- Použijte agregační pipelinu k seskupení prodejů po měsících a následně je rozdělte podle regionů (customer_region).

**Analýza vratek podle produktové kategorie**
- Zobrazte vrácené objednávky jako procento z celkových prodejů pro každou produktovou kategorii pomocí koláčového grafu.
- Pomocí $lookup propojte orders s returns, spočítejte počet vratek a vypočítejte podíl vratek na objednávkách v jednotlivých kategoriích.

**Cenové segmenty produktů**
- Pomocí $bucket seskupte produkty do cenových segmentů (např. Nízká cena, Střední cena, Vysoká cena) a zobrazte počet produktů v jednotlivých segmentech pomocí histogramu nebo sloupcového grafu.
- Vizualizace by měla zahrnovat i možnost filtrování podle kategorie nebo regionu.

**Sezónní prodeje v jednotlivých regionech**
- Vytvořte čárový graf, který zobrazuje sezónní prodeje produktů v jednotlivých regionech.
- Pomocí agregační pipeliny seskupte objednávky podle období (jaro, léto, podzim, zima) a porovnejte prodeje v regionech. Tento graf by měl umožňovat analyzovat sezónní trendy.

#### C3.6 - Cachování výsledků z roury do Redis
Přidejte si do docker-compose databázi Redis. Použijte ji pro zlepšení výkonu tím způsobem, že ji budete využívat jako cache pro ukládání výsledků agregačních operací z MongoDB. To umožní aplikaci Dash rychle přistupovat k těmto výsledkům bez nutnosti opakovaně dotazovat MongoDB.