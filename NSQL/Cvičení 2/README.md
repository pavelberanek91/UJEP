# NoSQL databázové systémy

## On-site cvičení 2

V této lekci se naučíte vyplnit šablony daty a pracovat s různými požadavky typu GET a POST na váš webserver.

### Úkol 2.1 Vyplnění šablony daty:

Flask slouží jako webový server, který zpracovává požadavky. Typickým požadavkem u běžných webových aplikací je návrat obsahu webové stránky. Na následující stránce naleznete návod, jak vrátit uživateli webovou stránku: [ZDE](https://www.tutorialspoint.com/flask/flask_templates.htm).

**app.py**
```
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

user_reviews = {
    "pepa": "Hele fakt bomba website, ale chybi mi tu vlastne vsechno",
    "franta": "Chtel jsem najit recept na smazeny vajicka, ale dostal jsem se tu. Nevi jak.",
    "alena": "Produkt teto firmy je nejlepsi. Pouzivame ho vsichni. Obcas ho pujcime i dedeckovi."
}

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("index.html", reviews=user_reviews)

@app.route("/datasets")
def datasets():
    return render_template("datasets.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```

**index.html**
```
{% extends "template.html" %}

{% block subtitle %}
About
{% endblock %}

{% block main %}
<p>This page have been seen <span id="view_count">{{ view_count }}</span> times</p>

<h3>Recenze:</h3>
<ul>
{% for user, review in reviews.items() %}
<li><span class="username">{{ user }}</span>:<span class="review">{{ review }}</span></li>
{% endfor %}
</ul>
{% endblock %}
```

### Úkol 2.2 Zpracování dat z formuláře:

Protokol HTTP umožňuje zasílat 4 typy metod. Nejčastěji užívanou metodou je metoda GET a POST. GET se používá pro stahování webových stránek a POST pro nahrávání dat na server. Data zaslané metodou post pak můžete na koncové bodě zpracovat. Návod na zpracování požadavků naleznete [ZDE](https://www.tutorialspoint.com/flask/flask_http_methods.htm)

**contact.html**
```
{% extends "template.html" %}

{% block subtitle %}
Contact
{% endblock %}

{% block main %}
<h2>Contact</h2>
<form action="/contact" method="post">
    <fieldset>
        <label for="username">Your name: </label>
        <input type="text" name="username" required>
        <label for="review">Your review: </label>
        <input type="text" name="review" required>
    </fieldset>
    <button type="submit">Send review</button>
</form>
{% endblock %}
```

**app.py**
```
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

user_reviews = {
    "pepa": "Hele fakt bomba website, ale chybi mi tu vlastne vsechno",
    "franta": "Chtel jsem najit recept na smazeny vajicka, ale dostal jsem se tu. Nevi jak.",
    "alena": "Produkt teto firmy je nejlepsi. Pouzivame ho vsichni. Obcas ho pujcime i dedeckovi."
}

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    counter = 1
    return render_template("index.html", reviews=user_reviews, view_count=counter)

@app.route("/datasets")
def datasets():
    return render_template("datasets.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        user_name = request.form.get("username")
        user_review = request.form.get("review")
        user_reviews[user_name] = user_review
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```

### Úkol 2.3 Zpracování dat z URL:

Jak zpracovávat data z URL koncových bodů naleznete: [ZDE](https://www.tutorialspoint.com/flask/flask_variable_rules.htm).

**app.py**
```
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

user_reviews = {
    "pepa": "Hele fakt bomba website, ale chybi mi tu vlastne vsechno",
    "franta": "Chtel jsem najit recept na smazeny vajicka, ale dostal jsem se tu. Nevi jak.",
    "alena": "Produkt teto firmy je nejlepsi. Pouzivame ho vsichni. Obcas ho pujcime i dedeckovi."
}

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    counter = 1
    return render_template("index.html", reviews=user_reviews, view_count=counter)

@app.route("/review/<username>")
def get_review(username):
    if username in user_reviews:
        return f"Returning requested review. {username}:{user_reviews[username]}"
    else:
        return "Username not found in database."

@app.route("/datasets")
def datasets():
    return render_template("datasets.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        user_name = request.form.get("username")
        user_review = request.form.get("review")
        user_reviews[user_name] = user_review
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```

### Úkol OS2.4 Bootstrap5:

Místo kaskádových stylů svépomocí se dnes využívají hotové frameworky. Nejoblíbenějším frameworkem je Bootstrap. Alternativou od W3schools je W3.css. Podívejte se na následující tutoriály a vyzkoušejte si implementaci těchto frameworků do vaší aplikace. Návod na Bootstrap5 [ZDE](https://www.w3schools.com/bootstrap5/index.php). Návod na W3.CSS [ZDE](https://www.w3schools.com/w3css/default.asp).

Ve finálním kódu, který je ve složce kody jsem udělal spousty zajímavých prvků odesignovaných bootstrapem, které si můžete prohlédnout.

## Domácí cvičení 2

### Úkol HW2.1 Bezpečné formuláře:

Pro řádné bezpečné formuláře doporučuji využít knihovu WTF flask. Návod na její používání naleznete [ZDE](https://www.tutorialspoint.com/flask/flask_wtf.htm).

### Video týdne 1: Docker

Pro snadné používání databází v našem vývojářském ekosystému budeme používat aplikaci Docker. Podívejte se na následující video, které vás do Dockeru zasvětí. [ZDE](https://www.youtube.com/watch?v=gAkwW2tuIqE)