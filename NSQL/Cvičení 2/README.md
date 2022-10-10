# NoSQL databázové systémy

**Obsah cvičení 2**:
* Webové aplikace ve Flask
* Koncové body
* Šablony

## On-site cvičení 2

V této lekci si připravíte jednoduchý webový portál, který bude vracet uložené články ve formě html stránek. Dále také může kdokoliv na portál nahrát vlastní článek. Na domovské stránce uživatel vyplní do formuláře text článku, své jméno a další náležitosti. Tyto data se vezmou, vytvoří se nová webová stránka a uloží se do adresáře s ostatními články. Tato nově přidaná stránka bude k dispozici pro otevření v seznamu článku na domovské stránce.

### Úkol OS2.1 Vytvoření prostředí pro vývoj:

Pro vývoj v jazyce Flask si budeme muset Flask modul nainstalovat. Doporučuji si jako první vytvořit a aktivovat virtuální prostředí. Jako první se ujistěte, že máte mezi balíčky nainstalován balíček pro tvorbu virtuálních prostředí (např.: venv nebo virtualenv).

```
python3 -m venv
```

Dále si vytvořte virtuální prostředí s nějakým názvem do pracovního adresáře.

```
python3 -m venv venv
```

Prostředí si aktivujte postupem podle vašeho operačního systému. V operačním systému Windows se vám vygeneruje aktivační skript pro powershel a dávkový soubor .bat. Stačí tento skript jednoduše vyhledat a spustit. V operačních systémech jako je Linux nebo MacOS musíte použít příkat source.

```
source venv/bin/activate
```

Pokud máte v terminále vedle vašeho uživatelského jména v závorkách název virtuálního prostředí, tak aktivace proběhla správně.

Následně si nainstalujte mezi knihovny virtuálního prostředí balíček Flask.

```
pip install flask
```

Ve vámi vybraném editoru zvolte interpretr jazyka Python právě ten interpret z virtuálního prostředí. V prostředí VS Code stačí stisknout klávesovou zkratku cmd(ctrl)+shift+P a zvolit možnost "Python: vybrat interpret". Občas se mi ve VS Code stává, že i po vybraní cesty se mi interpret nenahraje. Pak stačí jako pracovní adresář otevřít složku, ve které je i složka s virtuálním prostředím.

### Úkol OS2.1 Vytvoření Flask projektu:

Vytvořte si adresář src, do kterého umistěte soubor s názvem app.py. Tento soubor bude prozatím obsahovat vše, co se týká jazyka Python a frameworku Flask. Později si uděláte korektní strukturu vašeho projektu. Na této stránce naleznete návod, jak spustit Flask aplikaci: [ZDE](https://www.tutorialspoint.com/flask/flask_application.htm).

Pro pohodlnost si nastavte debug režim a rovnou si nastavte i port (napište stejné číslo jako je defaultní port Flasku). Port si nastavte explicitně z toho důvodu, že se vám může nějaká aplikace na portu bouchat s vaší za určitých okolností a chcete rychle vědět bez googlení, jak port změnit.


### Úkol OS2.2 Metody pro koncové body:

Dalším úkolem je vytvoření koncových bodů. Zatím si zkuste obecně jak routování ve Flasku funguje, později přepíšete kód podle vaší semestrální práce. Jak zpracovávat data z koncových bodů naleznete: [ZDE](https://www.tutorialspoint.com/flask/flask_variable_rules.htm).

Zatím si můžeme představit, že uživatel chce vracet nějaký článek s univerzitními novinkami. Tyto články se volají přes své id v URL adrese. Zkuste si tedy odchytávat z URL adresy id.

### Úkol OS2.3 Vrácení šablon:

Flask slouží jako webový server, který zpracovává požadavky. Typickým požadavkem u běžných webových aplikací je návrat obsahu webové stránky. Na následující stránce naleznete návod, jak vrátit uživateli webovou stránku: [ZDE](https://www.tutorialspoint.com/flask/flask_templates.htm).

Zkuste vytvořit endpoint články, kterým přesměrujete uživatele na webovou stránku, obsahující seznam všech hypotetických článků na vašem serveru.

### Úkol OS2.4 Zpracování HTTP metod:

Protokol HTTP umožňuje zasílat 4 typy metod. Nejčastěji užívanou metodou je metoda GET a POST. GET se používá pro stahování webových stránek a POST pro nahrávání dat na server. Vytvořte si v HTML formulář a pomocí metody POST vložit článek nějakého textu na server. Návod na zpracování požadavků naleznete [ZDE](https://www.tutorialspoint.com/flask/flask_http_methods.htm)

Pro řádné bezpečné formuláře doporučuji využít knihovu WTF flask. Návod na její používání naleznete [ZDE](https://www.tutorialspoint.com/flask/flask_wtf.htm).

### Úkol OS2.5 Statické soubory:

Váš webový portál bude pro svou funkci vyžadovat statické soubory (kaskádové styly, javascript, obrázky). Následující odkaz vám ukáže, jak nahrát na webový portál statické soubory [ZDE](https://www.tutorialspoint.com/flask/flask_static_files.htm).

## Domácí cvičení 2

### Úkol HW2.1 HTML5:

Váš výsledný produkt bude využívat HTML5 standard jazyka. Ne všichni programátoři využívají HTML5 možnosti do maximální míry. Projděte si tutorial na w3schools, který vám ukáže možnosti HTML5 [ZDE](https://www.w3schools.com/html/default.asp).

### Úkol HW2.2 Bootstrap5/W3.CSS:

Místo kaskádových stylů svépomocí se dnes využívají hotové frameworky. Nejoblíbenějším frameworkem je Bootstrap. Alternativou od W3schools je W3.css. Podívejte se na následující tutoriály a vyzkoušejte si implementaci těchto frameworků do vaší aplikace. Návod na Bootstrap5 [ZDE](https://www.w3schools.com/bootstrap5/index.php). Návod na W3.CSS [ZDE](https://www.w3schools.com/w3css/default.asp).

### Úkol HW2.3 SQLAlchemy:

Pro připojení do databáze budeme používat balíček SQLAlchemy. Budeme s ním pracovat příští hodinu. Zprovozněte si SQLAlchemy podle následujícího tutoriálu [ZDE](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#installation).

### Úkol HW2.4 Objektově-relační mapování:

V tutoriálu z HW2.3 jste si mohli všimnout, že využívají tříd pro práci s databází. Tomuto konceptu se říká objektově-relační mapování. Na následující stránce se dočtete, co je to vlastně ORM [ZDE](https://docs.sqlalchemy.org/en/14/orm/tutorial.html)


**Video týdne 1: ORM**

ORM má své výhody i nevýhody. Podívejte se na následující video [ZDE](https://www.youtube.com/watch?v=3EvhK7-DlZA).

**Video týdne 2: Flask**

Projděte si následující tutoriál na framework flask [ZDE](https://www.youtube.com/watch?v=Z1RJmh_OqeA).
