# NoSQL databázové systémy

## Cvičení 8 - Aplikace dokumentových databází

### Zadání

Cílem tohoto cvičení je provádět základní CRUD operace nad databází Mongo z webového rozhraní pracovního rámce Flask.

#### 8.1 Komunikace s MongoDB z Flasku

lorem

#### 8.2 Objektově-dokumentové mapování pro Mongo

Podobně jako v relačních databázích existuje objektově-relační mapování ORM, tak různé balíčky umožňují podobnou práci i s MongoDB (jedná se však o silně zjednodušenou verzi, jelikož ORM je značně komplikovaný a silný nástroj). Balíčky mongoengine umožňuje vytvářet třídy, které lze pak ukládat jako JSON dokumenty do dokumentové databáze, tedy tzv. ODM (objektově-dokumentové mapování). 

Model se v ODM technicky realizuje jako třída, která je potomkem třídy Dokument. Název třídy pak odpovídá kolekci, do které se instance uloží, jen se nahradí velké počáteční písmeno třídy za malé. Třídní atributy pak představují atributy dokumentu, které jsou instancí tříd Field. MongoDB neobsahuje schéma, avšak můžete pomocí mongoenginu vytvářet integritní omezení pro atributy. Každá instance Field má své vlastní integritní omezení pomocí parametrů v konstruktoru, které naleznete v dokumentaci [ZDE](https://docs.mongoengine.org/apireference.html#fields).

K uloženým instancím máte přístup přes název třídy (název kolekce s velkým písmenem) a přes metodu objects, do které píšete filtrační podmínku. Pokud nechcete filtrační podmínku a chcete vypsat všechny dokumenty, tak objects nevoláte se závorkami (má dunder metodu __callable__).

```
from mongoengine import Document, ListField, StringField, URLField

class Clanek(Document):
  nadpis = StringField(required=True, max_length=70)
  autor = StringField(required=True, max_length=20)
  klicova_slova = ListField(StringField(max_length=20))
  url = URLField(required=True)
  
clanek1 = Clanek(
  nadpis="Dezoláti a milovníci Ruska se sešli. A moc jich nebylo",
  autor="Johana Hovorková",
  klicova_slova=["dezoláti", "max dva zuby", "flákanec", "za Babiše bylo lépe", "USA žere děti za živa"],
  url="https://www.forum24.cz/dezolati-a-milovnici-ruska-se-sesli-a-moc-jich-nebylo/"
)

clanek1.save()

for dokument in Clanek.objects(autor="Johana Hovorková"):
  print(doc.url)


for dokument in Clanek.objects:
  print(doc.nadpis)
```

**Úkol**

Předělejte váš kód tak, aby využíval ODM.


#### 8.3 Vytvoření metod pro CRUD operace

Mezi 4 základní operace, které všechny systémy pro řízení báze dat musí obsahovat jsou CRUD operace (Create, Read/Retrieve, Update, Delete). Create je operace, která v databázi vytvoří nový záznam (v relačních DB známo jako INSERT). Read (někdy se uvádí jako Retrieve) je operace, která vrací vybraný záznam (v relačních DB známo jako SELECT WHERE). Update je operace, která upravuje atribut nalezeného záznamu na novou hodnotu nebo přidává nový atribut (v relačních DB známo jako UPDATE WHERE). Delete je operace, která maže existující záznam (v relačních DB známo jako DELETE WHERE).

Create operaci jsme již dělali v předchozím cvičení:

```
clanek = Clanek(
  nadpis="Dezoláti a milovníci Ruska se sešli. A moc jich nebylo",
  autor="Johana Hovorková",
  klicova_slova=["dezoláti", "max dva zuby", "flákanec", "za Babiše bylo lépe", "USA žere děti za živa"],
  url="https://www.forum24.cz/dezolati-a-milovnici-ruska-se-sesli-a-moc-jich-nebylo/"
)

clanek.save()
```

Read operaci jsme si v Mongo již taky ukázali. Pokud chceme jen jeden záznam, což je nejčastější výsledek výsledné množiny (result-set) REST aplikací, tak musíme z výsledné množiny vybrat první nalezený záznam:

```
clanek = Clanek.objects(autor="Johana Hovorková").first()
```

Update operace se v Mongo realizuje následovně (můžete i přidat nový atribut):

```
opraveny_clanek = Clanek.objects(autor="Johana Hovorková").first()
opraveny_clanek.update(autor="Lorema Ipsunová")
opraveny_clanek.update(upraveno="Jo!")
```

Delete operace se v Mongo realizuje následovně:

```
clanek_ke_smazani = Clanek.objects(autor="Johana Hovorková").first()
clanek_ke_smazani.delete()
```

**Úkol**

Vytvořte CRUD operace pro váš ODM kód.

#### 8.4 Vytvoření endpointu pro dotazy nad Mongo

S mongoDB se nejčastěji pracuje skrze API, které volá CRUD operace. API nevolá uživatel sám, ale volají ho aplikace, které jsou na serverovou instanci Flasku datově navázané (typicky mobilní aplikace). Tím se zmenší datová zátěž, kterou vyvíjíte na mobilní internet uživatele. 

```
import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'novinky',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

class Clanek(db.Document):
    nadpis = StringField(required=True, max_length=70)
    autor = StringField(required=True, max_length=20)
    klicova_slova = ListField(StringField(max_length=20))
    url = URLField(required=True)
    def to_json(self):
        return {
                "nadpis": self.nadpis,
                "autor": self.autor,
                "klicova slova": self.klicova_slova,
                "url": self.url
                }
                
clanek = Clanek(
  nadpis="Dezoláti a milovníci Ruska se sešli. A moc jich nebylo",
  autor="Johana Hovorková",
  klicova_slova=["dezoláti", "max dva zuby", "flákanec", "za Babiše bylo lépe", "USA žere děti za živa"],
  url="https://www.forum24.cz/dezolati-a-milovnici-ruska-se-sesli-a-moc-jich-nebylo/"
)

@app.route('/', methods=['GET'])
def read():
    autor = request.args.get('autor')
    clanek = Clanek.objects(autor=autor).first()
    if not clanek:
        return jsonify({'chyba': 'clanek od zadaneho autora nebyl nalezen'})
    else:
        return jsonify(clanek.to_json())

@app.route('/', methods=['PUT'])
def create():
    zaznam = json.loads(request.data)
    clanek = Clanek(
                nadpis=zaznam["nadpis"],
                autor=zaznam["autor"],
                klicova_slova=zaznam["klicova slova"]
                url=zaznam["url"]
             )
    clanek.save()
    return jsonify(clanek.to_json())

@app.route('/', methods=['POST'])
def update():
    zaznam = json.loads(request.data)
    nadpis = zaznam['nadpis']
    autor = zaznam["autor"]
    klicova_slova = zaznam["klicova slova"]
    url = zaznam["url"]
    clanek = Clanek.objects(nadpis=nadpis).first()
    if not clanek:
        return jsonify({'chyba': 'clanek se zadanym nadpisem nebyl nalezen'})
    else:
        clanek.update(autor=zaznam['autor'])
        clanek.update(klicova_slova=zaznam['klicova slova'])
        clanek.update(url=zaznam['url'])
    return jsonify(user.to_json())

@app.route('/', methods=['DELETE'])
def delete_record():
    zaznam = json.loads(request.data)
    clanek = Clanek.objects(name=record['name']).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.delete()
    return jsonify(user.to_json())

if __name__ == "__main__":
    app.run(debug=True)
    
```

**Úkol**

Vytvořte endpointy pro CRUD operace.
