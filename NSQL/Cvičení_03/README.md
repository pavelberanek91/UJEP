# NoSQL databázové systémy

## On-site cvičení 3

### Úkol 3.1 Docker:

lorem

### Úkol 3.2 Dockerizace aplikace:

Jako první budeme muset vyexportovat všechny nainstalované moduly v jazyce Python, které pak nainstalujeme dovnitř prázdného image s Alpine Linuxem a interpretrem Pythonu.

```
pip freeze > requirements.txt
```

Následně vytvoříme soubor s názvem Dockerfile. Dockerfile je soubor, ve kterém se nahrává základní obraz (linux s nainstalovanou aplikací) a my do něj můžeme nakopírovat náš zdrojový kód a zadat příkazy pro instalaci závislostí (moduly z requirements.txt).

```
FROM python:3.10-alpine
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt --no-cache-dir
COPY ./code /code
CMD python app.py
```

* FROM - z jakého základního obrazu vycházíme, ten se stahuje z webového portálu Dockerhub.com
* WORKDIR - vytvoří pracovní adresář v obrazu
* COPY - zkopíruju z mého pracovního adresáře do zadané složky v obrazu soubory/adresáře
* RUN - spusť příkazy, které jsou součástí připravy obrazu, v tomto případě instalace všech balíčků pythonu z requirements souboru a nevytvářej bordel (no-cache)
* CMD - poté, co je obraz hotov, tak proveď operace v příkazové řádce (spusť naší flask appku)

Následně musíme takový obraz definovaný souborem sestavit (Dockerfile je návod na sestavení).
```
docker build -t nsql:flask .  
```

Teď už jen stačí rozeběhnout náš obraz do běžící instance = kontajner.
```
docker run -p 5000:5000 nsql:flask
```


### Úkol HW3.3 Docker-compose a PostgreSQL:

Jedním z prvních úkolů v projektu bude vytvořit přihlašovací systém, který bude využívat relační databázi pro správu uživatelů. Přihlašování bude probíhat pomocí formuláře. 

Podívejte se, jak se tvoří a zpracovává formulář: [ZDE](https://hackersandslackers.com/flask-wtforms-forms)

### Úkol 3.4 SQLAlchemy:

Pro připojení do databáze budeme používat balíček SQLAlchemy. Budeme s ním pracovat příští hodinu. Zprovozněte si SQLAlchemy podle následujícího tutoriálu [ZDE](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#installation).

### Úkol HW3.5 Objektově-relační mapování:

V tutoriálu z HW2.3 jste si mohli všimnout, že využívají tříd pro práci s databází. Tomuto konceptu se říká objektově-relační mapování. Na následující stránce se dočtete, co je to vlastně ORM [ZDE](https://docs.sqlalchemy.org/en/14/orm/tutorial.html)

**Video týdne 1: ORM**

ORM má své výhody i nevýhody. Podívejte se na následující video [ZDE](https://www.youtube.com/watch?v=3EvhK7-DlZA).