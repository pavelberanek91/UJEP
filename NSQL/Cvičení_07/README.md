# NoSQL databázové systémy

## Cvičení 7 - Dokumentová databáze MongoDB

V tomto cvičení budete realizovat jednoduchou aplikaci, která využívá nejzákladnější příkazy MongoDB pro CRUD operace. Začnete s tutoriálem z W3Schools na základě kterého vytvoříte aplikaci podle zadání.

### Zadání

Pojedeme podle nejjednoduššího možného tutoriálu (tj. tutoriál z newbie websitu w3schools.com).
1. Nainstalujte si PyMongo: [ZDE](https://www.w3schools.com/python/python_mongodb_getstarted.asp)
2. Vytvořte v MongoDB první databázi: [ZDE](https://www.w3schools.com/python/python_mongodb_create_db.asp)
3. Vytvořte v MongoDB první kolekci: [ZDE](https://www.w3schools.com/python/python_mongodb_create_collection.asp)
4. Vložte do vytvořené kolekce první záznam: [ZDE](https://www.w3schools.com/python/python_mongodb_insert.asp)
5. Vložte do kolekce více záznamů a zkuste je vyhledat pomocí find_one() a find() metod: [ZDE](https://www.w3schools.com/python/python_mongodb_find.asp)
6. Vložte si do kolekce více záznamů a zkuste je filtrovat pomocí regulárních výrazů: [ZDE](https://www.w3schools.com/python/python_mongodb_query.asp)
7. Seřaďte záznamy: [ZDE](https://www.w3schools.com/python/python_mongodb_sort.asp)
8. Smažte některé záznamy: [ZDE](https://www.w3schools.com/python/python_mongodb_delete.asp)
9. Upravte některý záznam: [ZDE](https://www.w3schools.com/python/python_mongodb_update.asp)
10. Smažte celou kolekci: [ZDE](https://www.w3schools.com/python/python_mongodb_drop_collection.asp)

Teď jste připravení na pravé zadání k dnešnímu cvičení :).

Vytvořte aplikaci, která slouží jako receptář studentských receptů. Funkcionální požadavky:
1. Aplikace bude mít 3 stránky: Domů (popis, co je to za projekt), Recepty (vypsaný seznam všech receptů z MongoDB), PřidejRecept (formulář, kterým může zaslat kdokoliv recept do systému). Recept bude mít tři informace: jméno receptu, jméno zadavatele, popis receptu.
2. Naplňte MongoDB několika prvotníma receptama a vypište si je na stránce Recepty na obrazovku.
3. Zpracujte formulář a přidejte zadaný recept z formuláře do MongoDB. 
4. Navrhněte si webové API rozhraní pro komunikaci se serverem na všechny CRUD operace (Create, Read, Update, Delete). 
5. Create přidává recept přes API. Pokud recept s daným názvem od daného uživatele již existuje v MongoDB, tak nebude přidan.
6. Read vrátí recept podle zadaného jména a zadaného uživatele.
7. Update upraví existující recept podle zadaného jména a zadaného receptu, pokud uživatel dodal správné tajné heslo k příslušnému záznamu.
8. Delete smaže existující recept podle zadného jména a zadaného receptu, pokud uživatel dodal správné tajné heslo k příslušnému záznamu.

## Materiály k samostudiu

Modelování API je důležitou součástí dnešních vývojových procesů. Podívejte se na jazyk RAML a proveďte modelování vašeho API a zdokumentujte si ho: [ZDE](https://raml.org/). Tento jazyk vám umožní modelovat API vaší webový služby na druhé úrovni Richardsonova modelu vyspělosti API [WIKI](https://en.wikipedia.org/wiki/Richardson_Maturity_Model)


## Řešení

### Úkol 1 - Tvorba šablon

Vytvořím si základní soubor pro flask s názvem app.py, který bude sloužit jako controller webové aplikace. Vytvořím příslušné koncové body, na kterých webový server naslouchá, a vracím podle zavolaných koncových bodů příslušné webové stránky.
```
#app.py
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "super secret key"


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/recipes')
def recipes():
    recipes_list = []
    return render_template('recipes.html', recipes=recipes_list)


@app.route('/form', methods=['GET'])
def form():
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
```

V šablonách mám šablonu pro všechny ostatní šablony. Ta obsahuje základní strukturu mých html5 stránek. Třídy u jednotlivých elementů jsou Bootstrap5. Mezi značkami main se nachází hlavní blok se zamýšleným obsahem pro ostatní šablony, které budou tuto šablonu rozšiřovat.
```
<!-- templates/template.html-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recistudentpes</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body>
    <nav class="navbar navbar-expand-md navbar-dark bg-dark">
        <div class="container-fluid">
            <div class="navbar-collapse collapse w-100 order-1 order-md-0 dual-collapse2">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="index">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="recipes">Recipes</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="form">Send Recipe</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <main class="p-5 text-center bg-light">
        {% block content %}{% endblock %}
    </main>
    <footer class="text-center text-lg-start bg-light text-muted">
        <p class="d-flex justify-content-center justify-content-lg-between p-4 border-bottom">&copy; Beranek Pavel</p>
    </footer>
</body>
</html>
```

Úvodní stránka, která obsahuje jen informace o tom, na jakém websitu se uživatel nachází.
![Alt text](index.png)
```
<!-- templates/index.html-->
{% extends "template.html" %}

{% block content %}
<h2>Home</h2>
<p>Welcome to my website with delicious recipes.</p>
{% endblock %}
```

Stránka, kam vypisuji všechny recepty. U každého receptu budu vypisovat název receptu, autora receptu a popis receptu.
![Alt text](recepty.png)
```
<!-- templates/recipes.html-->
{% extends "template.html" %}

{% block content %}
<h2>Recipes</h2>
<ul class="list-group">
{% for recipe in recipes %}
<li class="list-group-item">
    {{ recipe["name"] }} ({{ recipe["author"] }}) - {{ recipe["description"] }}
</li>
<ul >
{% endfor %}
</ul>
{% endblock %}
```

Stránka s formulářem pro zasílání receptu. Informace zasílám na stejný koncový bod jako je GET požadavek pro návrat této stránky. Kromě toho ja na konci stránky výpis informací o stavu uložení receptu do databáze MongoDB uživateli pomocí flash mechanismu flasku.
![Alt text](form.png)
```
<!-- templates/form.html-->
{% extends "template.html" %}

{% block content %} 
<form action="form" method="post">
    <fieldset>
        <div class="mb-3 mt-3">
            <label for="name" class="form-label">Name:</label>
            <input type="text" name="name" class="form-control" id="name" required>
        </div>
        <div class="mb-3 mt-3"></div>
            <label for="author" class="form-label">Author:</label>
            <input type="text" name="author" class="form-control" id="author" required>
        </div>
        <div class="mb-3 mt-3">
            <label for="description" class="form-label">Description:</label>
            <textarea name="description" class="form-control" id="description" cols="30" rows="10" required></textarea>
        </div>
    </fieldset>
    <button type="submit" class="btn btn-primary">Send</button>
</form>

{% with messages = get_flashed_messages() %}
    {% if messages %}
        {% for message in messages %}
            <p class="alert alert-success mt-5" role="alert">{{ message }}</p>
        {% endfor %}
    {% endif %}
{% endwith %}

{% endblock %}
```

### Úkol 2 - Naplnění mongoDB recepty

Připojím se k databázi mongo pomocí pymongo klienta. V řetězci pro připojení je nutné uvést z docker-compose.yml souboru login a heslo a také správný název serveru. Tento název odpovídá názvu služby (nezadávejte tedy localhost). Následně se připojím k databázi receptů a vytvořím si v ní kolekci receptů. Poté do ní vložím několik záznamů ve slovníkovém formátu (klíč: hodnota).

```
#app.py
import pymongo

mongo_client = pymongo.MongoClient("mongodb://admin:admin@mongodb:27017", connect=False)
db = mongo_client['recipes']
recipes_collections = db['recipes']

basic_recepts = [
  { "name": "Rohlik v parku", "author": "Ctirad", "description": "Dam rohlik do parku a ohreju v mikrovlnne troube.", "secret": "1234"},
  { "name": "Parek na sucho", "author": "Josefina", "description": "Dam si parek jen tak.", "secret": "parek"},
  { "name": "Omlaceny rohlik", "author": "Vlastislav", "description": "Omlatim rohlik nekomu o hlavu a snim to", "secret": "omlatit"},
  { "name": "Rohlik s colou", "author": "Melichar", "description": "Rohlik namocim v kole a snim to", "secret": "cocacola"},
  { "name": "Rohlik namazany chlebem", "author": "Jaromir", "description": "Nadrobim chleba na rohlik a rozprostru drobky podel rohliku", "secret": "chleb"},
  { "name": "Parek namazeny rohlikem", "author": "Borivoj", "description": "Udelam z rohliku neco jako pastiku a natru tim parek.", "secret": "rohlik"},
  { "name": "Chleba v parku v rohliku", "author": "Svatomil", "description": "Narvu rohlik do parku a takovou hmotu narvu do chleba. Snim to.", "secret": "nevim"},
]
recipes_collections.insert_many(basic_recepts)
```

### Úkol 3 - Přidání receptu z formuláře

V souboru s pythonem si vytvořím koncový bod s povolenými metodami GET a POST. Pokud požádá klient o GET, tak mu vrátím stránku s formulářem. Pokud požádá o POST, tak z jeho HTTP požadavku získám data z formuláře pomocí názvu formulářových prvků. Poté vygeneruji pro uživatele tajný klíč k receptu pro budoucí úpravy a uložím záznam do databáze. Tajný klíč mu ukážu na stránce pomocí flash funkce flasku. Následně ho přesměřuji zpátky na koncový bod pro formulář.

```
#app.py
from flask import request, redirect, flash, url_for
import string
import random

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        description = request.form['description']
        secret = "".join(random.sample(string.ascii_letters + string.digits + string.punctuation, 8))
        record = {'name': name, 'author': author, 'description': description, "secret": secret}
        recipes_collections.insert_one(record)

        # flash success and redirect to form
        flash(f'Your recipe has been added! Your secret is {secret}')
        return redirect(url_for('form'))
    else:
        return render_template('form.html')

```

### Úkol 4 - Návrh REST API pro CRUD operace

Pro komunikaci s uživatelem přes bezestavové rozhraní (REST API) využiju koncový bod /api a vytvořím pro něj dva koncové body /recipe a /recipes. Recipes bude použit pro hromadné operace (jen read) a recipe pro operace s jedním receptem. Operace pro jeden recept budou všechny z CRUD schématu, tedy:
1. Vytvoření nového záznamu (Create) - realizováno HTTP metodou POST
2. Vrácení existujícího záznamu (Read) - realizováno HTTP metodou GET
3. Úprava existujícího záznamu (Update) - realizováno HTTP metodou PUT
4. Smazání existujícího záznamu (Delete) - realizováno HTTP metodou DELETE

Tvorba nového záznamu vyžaduje název receptu, jméno autor a návod (popis) receptu. Pro čtení nám stačí jméno receptu a jméno autor. V případě čtení všech záznamů nepotřebujeme žádné parametry. Pro úpravu záznamu potřebuji znát tajné heslo, které zná jen autor. To se musí spárovat s jménem autora a názvem receptu. To stejné platí pro smazání receptu.

Přes webový prohlížeč lze otestovat snadno jen GET požadavek. Pro ostatní požadavky (POST, PUT, DELETE) budu využívat specializovanou aplikaci pro testování REST API rozhraní a to Postman: [ZDE](https://www.postman.com/). Doporučuji si ji nainstalovat. V dalších bodech je snímek obrazovky zachycující mé testování koncového bodu přes tuto aplikaci s potřebným nastavením parametrů.

```
#app.py

#CRUD - Create
@app.route('/api/recipe', methods=['POST'])
def api_post_recipe():
    name = request.args.get('name')
    author = request.args.get('author')
    description = request.args.get('description')
    ...
    
#CRUD - Read
@app.route('/api/recipes')
def api_get_recipes():
   ...

#CRUD - Read
@app.route('/api/recipe')
def api_get_recipe():
    name = request.args.get('name')
    author = request.args.get('author')
    ...
    
#CRUD - Update
@app.route('/api/recipe', methods=['PUT'])
def api_put_recipe():
    name = request.args.get('name')
    author = request.args.get('author')
    description = request.args.get('description')
    secret = request.args.get('secret')
    ...

#CRUD - Delete
@app.route('/api/recipe', methods=['DELETE'])
def api_delete_recipe():
    name = request.args.get('name')
    author = request.args.get('author')
    secret = request.args.get('secret')
    ...
```

### Úkol 5 - Create operace

Získám z REST API potřebné paramety (jméno, autor, popis receptu) a vygeneruji nové unikátní heslo pro úpravu nebo smazání receptu. Následně záznam uložím do databáze pokud takový v databázi již neexistuje. Informuji v JSON formátu uživatele zpět o úspěchu. Aby dopadla konverze BSON dokumentů z mongo na JSON správně, tak využiji modul bson.

```
#app.py
from flask import make_response
from bson import json_util

@app.route('/api/recipe', methods=['POST'])
def api_post_recipe():
    name = request.args.get('name')
    author = request.args.get('author')
    description = request.args.get('description')
    secret = "".join(random.sample(string.ascii_letters + string.digits + string.punctuation, 8))
    record = {'name': name, 'author': author, 'description': description, "secret": secret}
    if recipes_collections.find_one({'name': name, "author": author}) == None:
        recipes_collections.insert_one(record)
        return make_response(json_util.dumps({'success': 'Recipe added', "secret": secret}), 200)
    else:
        return make_response(json_util.dumps({'error': 'Recipe already exists'}), 400)
```

Test v Postmanovi:
![Alt text](post.png)

### Úkol 6 - Read operace

Získám z REST API potřebné paramety (jméno, autor) a vyhledám takový recept v databázi. Ze záznamu vynechám id a heslo, které nechci aby se vrátilo v JSON odevzě. Informuji v JSON formátu uživatele zpět o úspěchu a při úspěchu zašlu data.

```
@app.route('/api/recipe')
def api_get_recipe():
    name = request.args.get('name')
    author = request.args.get('author')
    recipe = recipes_collections.find_one({'name': name, "author": author},  {"_id": 0, "secret": 0})
    if recipe:
        return make_response(json_util.dumps(recipe), 200)
    else:
        return make_response(json_util.dumps({'error': 'Recipe not found'}), 404)
```

Test v Postmanovi:
![Alt text](get.png)


Vytvořím ještě jeden endpoint, který vrací všechny recepty.

```
@app.route('/api/recipes')
def api_get_recipes():
    recipes_list = recipes_collections.find({}, {"_id": 0, "secret": 0})
    return make_response(json_util.dumps(recipes_list), 200)
```

Test v Postmanovi:
![Alt text](getall.png)

### Úkol 7 - Update operace

Získám z REST API potřebné paramety (jméno, autor, popis receptu, heslo) a pokud takový záznam se nachází v databázi (popis receptu vynechám), tak upravím popis k příslušnému receptu. Informuji v JSON formátu uživatele zpět o úspěchu.

```
#app.py
@app.route('/api/recipe', methods=['PUT'])
def api_put_recipe():
    name = request.args.get('name')
    author = request.args.get('author')
    description = request.args.get('description')
    secret = request.args.get('secret')
    if recipes_collections.find_one({'name': name, "author": author, "secret": secret}):
        recipes_collections.update_one({'name': name, "author": author, "secret": secret}, {"$set": {"description": description}})
        return make_response(json_util.dumps({'success': 'Recipe updated'}), 200)
    else:
        return make_response(json_util.dumps({'error': 'Recipe not found'}), 404)
```

Test v Postmanovi:
![Alt text](put.png)


### Úkol 8 - Delete operace

Získám z REST API potřebné paramety (jméno, autor, heslo) a pokud takový záznam se nachází v databázi, tak příslušný záznam odstraním. Informuji v JSON formátu uživatele zpět o úspěchu.

```
#app.py
@app.route('/api/recipe', methods=['DELETE'])
def api_delete_recipe():
    name = request.args.get('name')
    author = request.args.get('author')
    secret = request.args.get('secret')
    if recipes_collections.find_one({'name': name, "author": author, "secret": secret}):
        recipes_collections.delete_one({'name': name, "author": author, "secret": secret})
        return make_response(json_util.dumps({'success': 'Recipe deleted'}), 200)
    else:
        return make_response(json_util.dumps({'error': 'Recipe not found'}), 404)
```

Test v Postmanovi:
![Alt text](delete.png)

### Domácí úkol - Modelování API

Zde je ukázka vymodelovaného REST API pomocí jazyka RAML 1.0. Pro ukázku můžete vložit do tohoto vizuálního editor [ZDE](https://raml.org/).

![Alt text](raml_api.png)
![Alt text](raml_recipe.png)
![Alt text](raml_delete.png)

```
#%RAML 1.0
title: Recistudentpes
baseUri: http://localhost:5000/api
version: 1.0

/recipe:
  get:
    description: Retrieves a specific recipe from DB
    responses:
      200:
        body:
          application/json:
            example: {
              "name": "Rohlik v parku",
              "author": "Ctirad",
              "description": "Dam rohlik do parku a ohreju v mikrovlnne troube."
            }
      404:
        body:
          application/json:
            example: {
              "error": "Recipe not found"
            }
    queryParameters:
      name:
        displayName: name
        type: string
        description: Recipe name
        example: Gulas
        required: true
      author:
        displayName: author
        type: string
        description: Recipe author
        example: Ctirad
        required: true

  post:
    description: Insert new recipe to database
    responses:
      200:
        body:
          application/json:
            example: {
              "success": "Recipe added",
              "secret": "5hg@!xd5",
            }
      404:
        body:
          application/json:
            example: {
              "error": "Recipe already exists"
            } 
    queryParameters:
      name:
        displayName: name
        type: string
        description: Recipe name
        example: Gulas
        required: true
      author:
        displayName: author
        type: string
        description: Recipe author
        example: Ctirad
        required: true
      description:
        displayName: description
        type: string
        description: Recipe description
        example: Namazeme rohlik maslem
        required: true

  put:
    description: Updates existing recipe if secret matches
    responses:
      200:
        body:
          application/json:
            example: {
              "success": "Recipe updated",
            }
      404:
        body:
          application/json:
            example: {
              "error": "Recipe not found."
            }
    queryParameters:
      name:
        displayName: name
        type: string
        description: Recipe name
        example: Gulas
        required: true
      author:
        displayName: author
        type: string
        description: Recipe author
        example: Ctirad
        required: true
      description:
        displayName: description
        type: string
        description: Recipe description
        example: Namazeme rohlik maslem
        required: true
      secret:
        displayName: secret
        type: string
        description: Recipe secret password for updates or deletes
        example: v5d!x
        required: true

  delete:
    description: Deletes existing recipe if secret matches
    responses:
      200:
        body:
          application/json:
            example: {
              "success": "Recipe deleted",
            }
      404:
        body:
          application/json:
            example: {
              "error": "Recipe not found."
            }
    queryParameters:
      name:
        displayName: name
        type: string
        description: Recipe name
        example: Gulas
        required: true
      author:
        displayName: author
        type: string
        description: Recipe author
        example: Ctirad
        required: true
      secret:
        displayName: secret
        type: string
        description: Recipe secret password for updates or deletes
        example: v5d!x
        required: true

/recipes:
  get:
    description: Retrieves all recipes from db
    responses:
      200:
        body:
          application/json:
            example: [
              {
                "name": "Rohlik v parku",
                "author": "Ctirad",
                "description": "Dam rohlik do parku a ohreju v mikrovlnne troube."
              },
              {
                "name": "Parek na sucho",
                "author": "Josefina",
                "description": "Dam si parek jen tak."
              },
              {
                "name": "Omlaceny rohlik",
                "author": "Vlastislav",
                "description": "Omlatim rohlik nekomu o hlavu a snim to"
              }
            ]

```

Zde je ukázka stejného REST API vymodelovaného pomocí standardu OpenAPI (například pro Swagger dokumentaci a vizualizaci). Pro ukázku můžete vložit do tohoto vizuálního editor [ZDE](https://editor.swagger.io/).

![Alt text](swagger.png)
![Alt text](swagger_put.png)

```
swagger: "2.0"
info:
  title: Recistudentpes
  version: "1.0"
host: localhost:5000
basePath: /api
schemes:
  - http
paths:
  /recipe:
    get:
      description: Retrieves a specific recipe from DB
      parameters:
        -
          name: name
          description: Recipe name
          required: true
          in: query
          type: string
        -
          name: author
          description: Recipe author
          required: true
          in: query
          type: string
      responses:
        "200":
          description: ""
          x-amf-mediaType: application/json
          schema:
            example:
              name: Rohlik v parku
              author: Ctirad
              description: Dam rohlik do parku a ohreju v mikrovlnne troube.
        "404":
          description: ""
          x-amf-mediaType: application/json
          schema:
            example:
              error: Recipe not found
    post:
      description: Insert new recipe to database
      parameters:
        -
          name: name
          description: Recipe name
          required: true
          in: query
          type: string
        -
          name: author
          description: Recipe author
          required: true
          in: query
          type: string
        -
          name: description
          description: Recipe description
          required: true
          in: query
          type: string
      responses:
        "200":
          description: ""
          x-amf-mediaType: application/json
          schema:
            example:
              success: Recipe added
              secret: 5hg@!xd5
        "404":
          description: ""
          x-amf-mediaType: application/json
          schema:
            example:
              error: Recipe already exists
    put:
      description: Updates existing recipe if secret matches
      parameters:
        -
          name: name
          description: Recipe name
          required: true
          in: query
          type: string
        -
          name: author
          description: Recipe author
          required: true
          in: query
          type: string
        -
          name: description
          description: Recipe description
          required: true
          in: query
          type: string
        -
          name: secret
          description: Recipe secret password for updates or deletes
          required: true
          in: query
          type: string
      responses:
        "200":
          description: ""
          x-amf-mediaType: application/json
          schema:
            example:
              success: Recipe updated
        "404":
          description: ""
          x-amf-mediaType: application/json
          schema:
            example:
              error: Recipe not found.
    delete:
      description: Deletes existing recipe if secret matches
      parameters:
        -
          name: name
          description: Recipe name
          required: true
          in: query
          type: string
        -
          name: author
          description: Recipe author
          required: true
          in: query
          type: string
        -
          name: secret
          description: Recipe secret password for updates or deletes
          required: true
          in: query
          type: string
      responses:
        "200":
          description: ""
          x-amf-mediaType: application/json
          schema:
            example:
              success: Recipe deleted
        "404":
          description: ""
          x-amf-mediaType: application/json
          schema:
            example:
              error: Recipe not found.
  /recipes:
    get:
      description: Retrieves all recipes from db
      responses:
        "200":
          description: ""
          x-amf-mediaType: application/json
          schema:
            example:
              -
                name: Rohlik v parku
                author: Ctirad
                description: Dam rohlik do parku a ohreju v mikrovlnne troube.
              -
                name: Parek na sucho
                author: Josefina
                description: Dam si parek jen tak.
              -
                name: Omlaceny rohlik
                author: Vlastislav
                description: Omlatim rohlik nekomu o hlavu a snim to
```