# NoSQL databázové systémy

## Cvičení 8 - Aplikace dokumentových databází

### Zadání

Cílem tohoto cvičení je provádět základní CRUD operace nad databází Mongo z webového rozhraní pracovního rámce Flask.

#### 8.1 Komunikace s MongoDB z Flasku

lorem

#### 8.2 Vytvoření endpointů pro CRUD operace

lorem

Na dokument se zeptáme pomocí příkazu find: ```db.studenti.find({ jméno: “Pavel Beránek” })```

#### 8.3 Vytvoření endpointu pro dotazy nad Mongo

lorem

#### 8.4 Objektově-dokumentové mapování pro Mongo

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
