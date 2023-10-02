# NoSQL databázové systémy

## On-site cvičení 1

V této lekci si připravíte jednoduchý webový portál, který bude vracet html stránky. Webový portál bude realizovaný webovým pracovním rámcem Flask v jazyce Python. Instalace závislostí bude provedena do dedikovaného virtuálního prostředí z modulu venv jazyka Python.

### Úkol 1.1 Vytvoření prostředí pro vývoj:

Pro vývoj v jazyce Flask si budeme muset Flask modul nainstalovat. Doporučuji si jako první vytvořit a aktivovat virtuální prostředí. Jako první se ujistěte, že máte mezi balíčky nainstalován balíček pro tvorbu virtuálních prostředí (např.: venv nebo virtualenv).

```
python3 -m venv
```

Dále si vytvořte virtuální prostředí s nějakým názvem do pracovního adresáře.

```
python3 -m venv venv
```

Prostředí si aktivujte postupem podle vašeho operačního systému. V operačním systému Windows se vám vygeneruje aktivační skript pro powershell a dávkový soubor .bat. Stačí tento skript jednoduše vyhledat a spustit. V operačních systémech jako je Linux nebo MacOS musíte použít příkat source.

```
source venv/bin/activate
```

Pokud máte v terminále vedle vašeho uživatelského jména v závorkách název virtuálního prostředí, tak aktivace proběhla správně.

Ve vámi vybraném editoru zvolte interpretr jazyka Python právě ten interpret z virtuálního prostředí. V prostředí VS Code stačí stisknout klávesovou zkratku cmd(ctrl)+shift+P a zvolit možnost "Python: vybrat interpret".

### Úkol 1.2 Flask:

Flask je microframework pro vývoj webových aplikací v jazyce Python. Oproti například frameworku Django se jedná o jen to nejmenší nutné, aby python šlo využít pro tvorbu webových aplikací. Vytvořte si projekt ve vašem oblíbeném editoru, vytvořte virtuální prostředí v jazyce Python a balíčkovacím systémem pip si nainstalujte Flask. 

Návod naleznete zde: [ZDE](https://flask.palletsprojects.com/en/2.2.x/installation/)

Instalace modulu Flask se provede pomocí příkazu:

```
pip install flask
```

### Úkol 1.3 Vytvoření Flask projektu:

Vytvořte si adresář code, do kterého umistěte soubor s názvem app.py. Tento soubor bude prozatím obsahovat vše, co se týká jazyka Python a frameworku Flask. Později si uděláte korektní strukturu vašeho projektu. Na této stránce naleznete návod, jak spustit Flask aplikaci: [ZDE](https://www.tutorialspoint.com/flask/flask_application.htm).

Pro pohodlnost si nastavte debug režim (změny v kódu se projeví bez nutnosti restartu aplikace) a rovnou si nastavte i port (napište stejné číslo jako je defaultní port Flasku). Port si nastavte explicitně z toho důvodu, že se vám může nějaká aplikace na portu bouchat s vaší za určitých okolností a chcete rychle vědět bez googlení, jak port změnit. Ip adresu nastavte na samé nuly a to z toho důvodu, že Docker, který budeme později používat, má problém spouštět Flask aplikace na jiné IP adrese.

```
from flask import Flask, render_template

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```

### Úkol 1.4 Koncové body:

Webové aplikace využívají principu koncových bodů. V případě, že napíše uživatel do webového prohlížeče URL obsahující adresu serveru, tak může aktivovat určitý koncový bod dodáním symbolu lomítka a následně názvu koncového bodu. Koncový bod je v Pythonu realizován pomocí dekorátoru, který naslouchá na HTTP metody GET, POST, PUT, DELETE a spouští pythonovskou metodu. Tato metoda pak provádí již určitou službu. typicky při HTTP metodě GET vrátí nějakou webovou stránku, při HTTP metodě POST naopak nahrává uživatel data z formuláře do Pythonu, PUT a DELETE se používají jen u REST API aplikací.

Podívejte se na to, jak se koncové body vytvářejí: [ZDE](https://hackersandslackers.com/your-first-flask-application/)

```
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return "<h1>Já jsem webovka s nadpisem</h1>"

@app.route("/datasets")
def datasets():
    return "<h1>Já jsem jiná webovka s nadpisem</h1><p>mám i odstavec</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```

### Úkol 1.5 Šablony:

Při obdržení požadavku HTTP GET má webový server vracet nějakou webovou stránku. Těm se říká ve Flasku šablony, jelikož mohou obsahovat nějaká data z Pythonu. Tyto data dodáváme do stránky pomocí šablonovacího jazyku, kterým je v případě Flasku jazyk Jinja2. Šablony (webové stránky) ukládáme implicitně do složky templates v projektu Flask aplikace, ale tato složka se dá nastavit parametrem template_folder. Šablony mohou mít i své šablony, které jsou pak rozšiřované. 

Podívejte se na to, jak se tvoří a vrací šablony uživateli: [ZDE](https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application)

**app.py**
```
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/datasets")
def datasets():
    return render_template("datasets.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```

**šablona pro webovky template.html**
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Myweb-{% block subtitle %}{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Name of my website</h1>
    </header>
    <nav>
        <ul>
            <li>
                <a href="{{ url_for('index') }}">About</a>
            </li>
            <li>
                <a href="{{ url_for('datasets') }}">Datasets</a>
            </li>
            <li>
                <a href="{{ url_for('contact') }}">Contact</a>
            </li>
        </ul>
    </nav>
    <main>
        {% block main %}{% endblock %}
    </main>
    <footer>
        <p>&copy;Beránek Pavel, UJEP, 2023</p>
    </footer>
</body>
</html>
```

**konkrétní stránka index.html**
```
{% extends "template.html" %}

{% block subtitle %}
About
{% endblock %}

{% block main %}
<p>My homepage</p>
{% endblock %}
```

### Úkol 1.6 Kaskádové styly:

Pokud bychom pro tvorbu šablon použili pouze jazyk HTML5, tak jsme sice vytvořili strukturu stránek, ale jejich vzhled by nebyl příliš lákavý. Řešením je využít kaskádových stylů. Je zvykem dávat css soubory do složky static.

Podívejte se na to, jak dodat CSS do Flask aplikace: [ZDE](https://hackersandslackers.com/flask-assets)

**nahrání css do template.html**
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Myweb-{% block subtitle %}{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <header>
        <h1>Name of my website</h1>
    </header>
    <nav>
        <ul>
            <li>
                <a href="{{ url_for('index') }}">About</a>
            </li>
            <li>
                <a href="{{ url_for('datasets') }}">Datasets</a>
            </li>
            <li>
                <a href="{{ url_for('contact') }}">Contact</a>
            </li>
        </ul>
    </nav>
    <main>
        {% block main %}{% endblock %}
    </main>
    <footer>
        <p>&copy;Beránek Pavel, UJEP, 2023</p>
    </footer>
</body>
</html>
```

**obsah css**
```
body{
    background-color: antiquewhite;
}

#view_count{
    font-size: larger;
    font-weight: bolder;
    color:rgb(165, 55, 55);
}
```

## Domácí cvičení 1

### Úkol HW1.1 HTML5:

Váš výsledný produkt bude využívat HTML5 standard jazyka. Ne všichni programátoři využívají HTML5 možnosti do maximální míry. Projděte si tutorial na w3schools, který vám ukáže možnosti HTML5 [ZDE](https://www.w3schools.com/html/default.asp).

Zaměřte se určitě na následující:
1. Jaký je rozdíl mezi HEAD a BODY
2. Co jsou to METAdata?
3. Jaká se sémantická struktura webové stránky (HEADER, FOOTER, NAV, MAIN, ASIDE, SECTION, ARTICLE)
4. Jak se tvoří odstavce P a nadpisy H
5. Jak se tvoří setříděné OL a nesetříděné seznamy UL a jejich prvky LI
6. Jak se tvoří hyperlinkové odkazy A na dokumenty uvnitř webovky a mimo webovku
7. Jak se tvoří sémantická tabulka pomocí záhlaví, zápatí, těla, řádků a buněk
8. Jak se tvoří formuláře pomocí FORM, FIELDSET, INPUT (a jejich typy) a tlačítka BUTTON
9. Jak používat entity
10. Jak vkládat multimediální prvky jako plátno, video, audio, obrázky aj.

## Úkol HW1.2 CSS3:

Vaše stránka zatím nevypadá příliš vábně. Zkuste si ji malinko ostylovat pomocí kaskádových stylů. Na následujícím odkazu najdete důležitou sadu operátorů a struktur, které můžete používat pro výběr určitých prvků, které chcete nastylovat. [ZDE](https://www.w3schools.com/cssref/css_selectors.php). Podívejte se pak ještě dál na nějaké ukázky a zkuste si ostylovat hezky navigační lištu.

### Video týdne 1: Flask

Projděte si následující tutoriál na framework flask [ZDE](https://www.youtube.com/watch?v=Z1RJmh_OqeA).