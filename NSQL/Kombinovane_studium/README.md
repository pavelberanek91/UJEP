# NoSQL Databáze

Vítejte na kurzu NoSQL databází. Cílem tohoto kurzu je vyzkoušet si vybrané typy NoSQL databází a jejich typické zástupce. Pro kombinované studium jsem vybral:
1. Databázi typu klíč-hodnota: Redis
2. Dokumentovou databázi: MongoDB
3. Grafovou databázi: Neo4j

### Podmínky zápočtu

Zápočet bude udělen za vhodně použitou NoSQL databázi v nějakém menším webovém projektu. Typ projektu je na vás, avšak nesmí se jednat o plagiát z internetu. Zkuste si vymyslet vlastní unikátní projekt. Zápočet mi přijdete ukázat v zápočtovém týdnu na vypsané termíny. Můžete se zapsat i na termíny spolu s prezenčními studenty.

## Kombinované studium

V kombinovaném studiu je naplánováno pouze jedno krátké setkání na přednášku a cvičení. Cílem cvičení je zprovoznit si technickou infrastrukturu pro vaše seminární práce. Práce se samotnými typy databázi bude již na vašem samostudiu. V sekci materiály naleznete všechny potřebné zdroje informací pro začátek vašich projektů.

### Materiály

1. Příkazy Redis: [ZDE](https://www.tutorialspoint.com/redis/index.htm)
2. Redis v Pythonu: [ZDE](https://realpython.com/python-redis/)
3. Příkazy MongoDB: [ZDE](https://www.tutorialspoint.com/mongodb/index.htm)
4. MongoDB v Pythonu: [ZDE](https://realpython.com/introduction-to-mongodb-and-python/)
5. Příkazy Neo4j: [ZDE](https://www.tutorialspoint.com/neo4j/index.htm)
6. Neo4j v Pythonu: [ZDE](https://marcobonzanini.com/2015/04/06/getting-started-with-neo4j-and-python/)

### On-site cvičení

Cvičení bude mít následující kroky:
1. Vytvoření Lokálního hello world programu.
2. Vytvoření základního docker obrazem pro náš projekt.
3. Stažení obrázů všech NoSQL databází a propojení s naším docker obrazem pro vzájemnou komunikaci
4. Vytvoření jednoduché webové aplikace v docker obrazu pomocí mikroframeworku Flask
5. Komunikace z Flask aplikace s Redis databází
6. Komunikace z Flask aplikace s MongoDB databází
7. Komunikace z Flask aplikace s Neo4j databází
8. Rozloučení se :)

#### 1. Hello World Flask

Otevřete si nějaký váš oblíbený editor (např. VS Code) a otevřete si nějakou pracovní složku. Já ji pojmenuji jako nosql_projekt. Pokud nemáte žádný vhodný editor nainstalován, tak doporučuji Visual Studio Code [ZDE](https://code.visualstudio.com/download). Do tohoto adresáře vložte soubor s názvem Dockerfile. Dockerfile je soubor, který se spustí aplikací docker v příkazové řádce a vytvoří nám z docker obraz, který představuje naší hotovou webovou aplikaci, která komunikuje s jinými obrazy (resp. tzv. kontejnery = běžící obrazy).

Nejprve budeme potřebovat vůbec nějaký kód, který můžeme spustit. Do vámi vytvořeného pracovního adresáře vytvořte soubor app.py a vložte do něj následující kód:

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def uvodni_stranka():
    return '<h1>Muj NoSQL projekt</h1>'

if __name__ == "__main__":
    app.run(debug=True)
```

Tento kód vytvoří instanci webového serveru Flask a na koncovém bodě "/" bude naslouchat na HTTP požadavky. V případě obdržení požadavku typu GET se spoustí funkce uvodni_stranka(), která vrátí vašemu prohlížeči HTML kód s nadpisem první úrovně. Argument True pro parametr debug si v ostrém provozu vypnete. Jedná se o vlastnost Flasku, která umožní vidět změny na webovém projektu okamžitě po uložení změny kódu. Není nutné Flask restartovat.

Abychom mohli spustit tento kód, tak si nejprve musíme také Flask nainstalovat. Otevřete si ve visual studio code terminál (klávesová zkratka ctrl(cmd) + J). Do terminálu zadáme následující příkaz pro vytvoření virtuálního prostředí:

```
python -m venv venv
```

Pokud vám příkaz nefunguje, pak musíte zjistit, jak se jmenuje alias pro váš python v příkazové řádce. Pokud nemáte Python vůbec nainstalován, tak si ho nainstalujte z následující stránky: [ZDE](https://www.python.org/downloads/). Tento příkaz v příkazové řádce udělá to, že zavolá pythonovský modul venv a vytvoří složku pro virtuální prostředí s názvem venv (ten druhá venv v pořadí, je možné zvolit jiný název).

Toto virtuální prostředí si musíme aktivovat. Ve Windowsu to provedeme následujícím příkazem:

```
\venv\Scripts\activate
```

V Linuxu a MacOS to provedeme následujícím příkazem:

```
source venv/bin/activate
```

Pokud byste chtěli prostředí deaktivovat, tak se to ve všech operačních systémech provede příkazem:

```
deactivate
```

Následně si do virtuálního prostředí nainstalujeme balíček flask (oveřte si, že se moduly nainstalovaly do vaší lib složky ve složce s virtuálním prostředím):

```
pip install flask
```

Aby kdokoliv mohl používat nás projekt, je nutné, aby si také nainstaloval všechny balíčky, se kterými pracujeme. Export seznamu nainstalovaných balíčků se provádí následujícím příkazem (je zvykem nazývat takový soubor requirements.txt):

```
pip freeze > requirements.txt
```

Projekt můžeme zkusit spustit pro kontrolu, zda funguje alespoň lokálně na našem PC:

```
python app.py
```

#### 2. Docker

Dalším krokem je instalace Docker na vašem operačním systému:

* Windows: [ZDE](https://docs.docker.com/desktop/install/windows-install/)
* Debian: [ZDE](https://docs.docker.com/desktop/install/debian/)
* Fedora: [ZDE](https://docs.docker.com/desktop/install/fedora/)
* Ubuntu: [ZDE](https://docs.docker.com/desktop/install/ubuntu/)
* Arch: [ZDE](https://docs.docker.com/desktop/install/archlinux/)
* MacOS: [ZDE](https://docs.docker.com/desktop/install/mac-install/)

 Do Dockerfilu vložte následující příkazy:

```
# syntax=docker/dockerfile:1

FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
```

1. Příkaz FROM stáhne z oficiálního repozitáře obrazů (Dockerhub) obraz Python3, což je malý předpřipravený virtualizovaný počítač pouze s pythonem (nejnovější verze). 
2. Příkaz WORKDIR vytvoří adresář (mkdir) uvnitř staženého obrazu (python:3) a přesune se do něj (cd).
3. Příkaz COPY zkopíruje vybraný soubor z vašeho aktuálního pracovního adresáře (u mě nosql_projekt) a zkopíruje můj soubor do aktuálního pracovního adresáře v obraze (WORKDIR cesta). Do obrazu kopírujeme soubor requirements, který slouží k tomu, abych mohli nainstalovat všechny potřebné moduly python pro běh aplikace.
4. Příkaz RUN spustí příkaz z příkazové řádky uvnitř obrazu. Zde nejprve pomocí balíčkovacího systému pip nainstalujeme všechny potřebné moduly pro náš python projekt.
5. Příkazem COPY následně zkopírujeme všechno z aktuálního adresáře (zdrojové kódy) do pracovního adresáře uvnitř obrazu.
6. Příkazem CMD spustíme příkaz python a pomocí něj flask an vybrané adrese. Rozdíl mezi RUN a CMD je ten, že RUN se spouští během sestavování obrazu (příprava) zatímco CMD se spouští když už je obraz sestaven (spouštění aplikací.)

Následně můžeme tento obraz dát dohromady (build) pomocí příkazu:

```
docker build --tag flask .
```

Ve výpisu obrazů bychom měli vidět nás docker obraz pod názvem flask:

```
docker images
```

Zkusme teď spustit náš docker obraz:

```
docker run -d -p 5000:5000 flask
```

Příznak -d říká, že se má obraz spustit v tzv. detach modu, tj. bude na pozadí a máme volný terminál pro další prác. Příznakem -p vybereme na jakém portu na našem lokálním PC se mají objevit data z portu z obrazu.

Pokud by něco nefungovalo, můžete všechny spuštěné kontejnery zastavit a smazat následující dvojicí příkazů:

```
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

Pokud zadáte do vašeho prohlížeče adresu: ```http://localhost:5000```, tak by se měla objevit webová stránka s vaším flask projektem z docker obrazu. Pokud vám docker psal konflikt na portech, pak změňte port, na který si posíláte data, např.: ```docker run -d -p 5001:5000 flask```. Pak zavoláte na vašem localhostovi aplikaci pod novým portem: ```http://localhost:5001```.

#### 3. Flask

V této fázi můžeme vytvořit nějakou menší webovou aplikaci ve Flask frameworku. V této sekci vás provedu základními možnostmi Flask frameworku.

Do našeho pracovního adresáře vytvoříme dvě složky:
1. Templates: do tohoto adresáře vkládáme html stránky (název je pevně nastaven).
2. Static: do tohoto adresáře vytvořte ještě adresáře css, js a imgs (názvy se mohou lišit).
3. CSS: do tohoto adresáře vkládáme kaskádové styly, které graficky upraví vzhled našich stránek.
4. JS: do toho adresáře vkládáme kód v jazyce javascript nebo jiné skripty spouštěné na straně uživatele.
5. IMGS: do tohoto adresáře vkládáme obrázky.

Pojďme upravit náš soubor app.py (vysvětlení je v komentářích v kódu):

```
#Flask je třída, jejíž instance představuje zhmotnění (instantizování) naší webové aplikace
#render_template slouží pro vrácení webové stránky ze složky templates uživateli
#request slouží pro získání dat z formuláře a zjištění http metody (GET, POST, PUT, DELETE)
from flask import Flask, render_template, request

#slovník db představuje naší falešnou databázi (prozatím, vy implementujete nějakou NoSQL)
db = {
    'jana@email.com': 'Co ze sem mam napsat?',
    'pepa@gmail.com': 'Ahoj. Chci se zeptat, jestli mi prodas vas produkt za kafe.',
    'johana@seznam.cz': 'johana@seznam.cz'
}

#instantizace webové aplikace
app = Flask(__name__)

#vytvoření endpointu root, který vrací webovou stránku index.html s kontextem databaze
#kontext je sada proměnných, jejichž hodnoty můžeme v html stránkách (=šablonách) využívat
@app.route('/')
def index():
    return render_template('index.html', databaze=db)

#další endpoint, který přijímá jak GET tak i POST HTTP požadavky
#pokud přijde požadavek typu POST, tak uživatel nahrál data na naší webovou stránku (formulář), tak je zpracujeme
#pokud přijde požadavek typu GET, tak uživatel chce jen po nás webovou stránku z formulářem
@app.route('/kontakt', methods=['GET', 'POST'])
def kontakt():
    if request.method == "GET":
        return render_template('kontakt.html')
    elif request.method == "POST":
        email = request.form['email']
        dotaz = request.form['dotaz']
        db[email] = dotaz
        return render_template('kontakt.html', vzkaz="Dotaz byl prijat. Dekujeme!")

#kód, který spouští naší instanci webové aplikace
if __name__ == "__main__":
    app.run(debug=True)

```

#### 4. Docker-compose

Dalším krokem je instalace Docker-compose. Tato aplikace nám umožní stáhnout další obrazy (předpřipravené z dockerhubu) a propojit je s naším obrazem. Naše výsledná aplikace se bude skládat z menšího množství vzájemně komunikujících obrazů.

V našem pracovním adresáři vytvoříme soubor s názvem docker-compose.yaml. Do něj vložíme následující kód:

```
version: '3'
services:
  web:
    build: .
    ports:
     - "5000:5000"
  redis:
    image: redis:latest
  mongodb:
    image: mongo:latest
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: admin
    ports:
      - 27017:27017
  neo4j:
    image: neo4j:latest
    ports:
      - "7474:7474"
      - "7687:7687"
```

#### 5. Redis

#### 6. MongoDB

#### 7. Neo4J

#### 8. Závěr
