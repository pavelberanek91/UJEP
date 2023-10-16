# NoSQL databázové systémy

## On-site cvičení 3

### Úkol 3.1 Docker:

V moderním světe vývoje softwaru je slušným zvykem své aplikace zapouzdřit do tzv. kontejnerů. Kontejner je spustitelná digitální jednotka, která obsahuje kód aplikace se v šmi digitálními aktivy a závislostmi pro běh. Tyto kontejnery zajišťují (nebo by měly zajišťovat) multiplatformní běh aplikací.

Docker je v aktuální době nejpopulárnější virtualizační nástroj pro kontejnery. Jeho způsob sestavování obrazů (předloh) pro kontejnery se stal standardem, kterému říkám OCI. Pro používání Dockeru si musíte stáhnout nejprve samotný Docker a to ideálně v desktopové verzi, kterou budu na hodinách využívat. [ZDE](https://www.docker.com/products/docker-desktop/).

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

Následně musíme takový obraz definovaný souborem sestavit (Dockerfile je návod na sestavení). Příznak -t dává sestavovanému obrazu název (značku, tag). Bez něj bychom obraz neviděli v Docker Desktopu. Tečka na konci představuje cestu k Dockerfilu a pokud napíšeme tečku, tak tím myslíme aktuální pracovní adresář terminálu.
```
docker build -t nsql:flask .  
```

Teď už jen stačí rozeběhnout náš obraz do běžící instance = kontejner.
```
docker run -p 5000:5000 nsql:flask
```


### Úkol 3.3 Docker-compose:

Již umíme vytvořit vlastní obraz, který umíme spustit v kontejner. Teď zbývá ještě stáhnout a spustit obrazy pro všechny NSQL databázové systémy v tomto kurzu. K tomu nám pomůže docker-compose program (nově již součástí Dockeru), který umí jednotlivé stažené služby propojit a nakonfigurovat. Vytvoříme soubor s názvem docker-compose.yml (nebo .yaml), který představuje konfigurační příkazy v YAML formátu pro Docker. 

Compose soubory začínají uvozením verze (aktuálně 3). Poté následuje výčet služeb, které compose souborem vytváříme. Název je zcela na nás. V mém compose souboru je služba s názvem Flask vytvořená vlastním Dockerfilem, což poznáme podle příkazu build, za kterým následuje cesta k Dockerfilu (tečka znamená stejný adresář, jako v kterém je compose souboru). Build vyžaduje i značku jako v předchozích příkladech, příkazem container_name pojmenujeme budovaný obraz. Poté nastavíme porty a propojíme adresářový systém z našeho pracovního adresáře s adresářem v Docker obrazu. V mém compose souboru je adresář code z aktuálního pracovního adresáře propojen s adresářem code v Docker obrazu. Pokud chcem vyjádřit pořadí spouštění se závislostí běhu, tak to můžeme vyjádřit příkazem depends_on. Všechny ostatní služby (jednotlivé NSQL databáze v tomto kurzu) jsou v mém compose souboru stažené přímo z Dockerhubu a jen některé z nich nastavuji (například login a heslo administrátora nebo porty).

```
version: '3'
services:
  flask:
    build: .
    container_name: flask
    ports:
      - "5000:5000"
    volumes:
      - ./code:/code
    depends_on:
      - redis

  redis:
    image: redislabs/redismod
    container_name: redis
    ports:
      - "6379:6379"

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

## Domácí cvičení 3

### Úkol HW3.1 SQLAlchemy:

Pro připojení do databáze budeme používat balíček SQLAlchemy. Budeme s ním pracovat příští hodinu. Zprovozněte si SQLAlchemy podle následujícího tutoriálu [ZDE](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#installation).

### Úkol HW3.2 Objektově-relační mapování:

V tutoriálu z HW2.3 jste si mohli všimnout, že využívají tříd pro práci s databází. Tomuto konceptu se říká objektově-relační mapování. Na následující stránce se dočtete, co je to vlastně ORM [ZDE](https://docs.sqlalchemy.org/en/14/orm/tutorial.html)

### Video týdne 1: ORM

ORM má své výhody i nevýhody. Podívejte se na následující video [ZDE](https://www.youtube.com/watch?v=3EvhK7-DlZA).