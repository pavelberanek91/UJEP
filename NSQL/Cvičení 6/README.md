# NoSQL databázové systémy

**Obsah přednášky 6:**

1. Databáze typu klíč - hodnota (praktická ukázka REDIS)

**Obsah cvičení 6:**

* Redis-py

## On-site cvičení 6

### Úkol OS6.1 Vytvoření prostředí pro vývoj:

Redis budeme využívat přes Docker obraz. Je tedy nutné si nainstalovat Docker. V opačném případě můžete přímo nainstalovat Redis, ale to nedoporučuji pro potřeby vaší výuky. Stáhneme si předpřipravený obraz Redis z DockerHubu pomocí příkazu: ```docker pull redis```.

Kontrolu staženého obrazu provedeme pomocí příkazu: ```docker images```. Tím vypíšeme seznam všech stažených obrazů, které je možné spustit v kontajnerech.

Následně Redis obraz spustíme v kontejneru pomocí Dockeru příkazem v odpojeném módu (na pozadí) na portu 6379 (ten je i implicitní, takže to není nutné specifikovat): ```docker run -d -p 6379:6379 --name muj_redis redis ```.

Ujistíme se, že Docker kontejner běží pomocí příkazu: ```docker ps``` a zapamatujeme si port (měl by být implicitně 6379).

Pokud byste chtěli vidět stavové výpisy Redis, pak napište ```docker logs muj_redis```.

Pokud byste spustili docker kontejner se jménem, se kterým nejste spokojeni, pak můžete docker kontejner zastavit pomocí příkazu: ```docker stop muj_redis``` a případně smazat kontejner příkazem ```docker rmi $(docker image | grep 'muj_redis')```. Pokud byste chtěli smazat stažený obraz, pak použijte příkaz: ```docker rmi $(docker image | grep 'muj_redis')```.

Pokud byste chtěli smazat všechny stažené obrazy, pak to provedete příkazem ```docker rmi $(docker images -q)```.

Pro využívání CLI příkazů na obrazu Redis si zapneme interaktivní mód a zapneme shell: ```docker exec -it muj_redis sh```.

V shellu Redis kontajneru můžeme zapnout aplikace redis-cli pro práci s Redis databází v příkazové řádce: ```redis-cli```.

Vyzkoušejte si, že jste schopni s Redisem komunikovat pomocí příkazu ```PING```. Mělo by se vám ozvat ```PONG```.

### Úkol OS6.2 Komunikace s Redis pomocí redis-py:

Další fází je připojit se jazykem python do redis databáze. Nainstalujte si do virtuálního prostředí (nebo pro odvážlivce nativního prostředí) přes balíčkovací systém pip knihovnu redis ```python -m pip install redis```. Vyzkoušejte si poslat pár příkazů z přednášky do instance redisu:

```
import redis
r = redis.Redis()

r.mset({"Katedra Informatiky": "Jiří Škvor", "Katedra Fyzika": "Eva Hejnová"})
r.get("Katedra Informatiky")
```

Pokud byste potřebovali nastavit redis jinak než implicitně, pak ```r = redis.Redis(host='localhost', port=6379, db=0, password=None)```. Parametr ```db``` představuje číslo databáze. Redis si své instance označuje identifikátorem a může vám naráz běžet více instancí redis databáze. Port 6379 je implicitní a snad by se vám neměl s žádným křížit. Je však možné, že máte tento port zakázený, tak si ho povolte nebo využijte jiný povolený port.

Vyzkoušejte si nastavit dobu přežití pro nějakou položku v redis databázi:

```
from datetime import timedelta
r.setex("Děkan", timedelta(minutes=1), value="Michal Varady")
```

Pokud se na ní budete ptát, tak po minutě již nebude v databázi přítomna:

```
r.get("Děkan")
```

Dobrý tutoriál s výčtem operací rozhraní pro používání Redisu v pythonu naleznete [ZDE](https://realpython.com/python-redis/).

### Úkol OS6.3 Komunikace s Redis z Flask:

Teď již zbývá propojit redis s webovým frameworkem Flask. Návod na propojení naleznete [ZDE](https://pypi.org/project/flask-redis/).

### Úkol OS6.4 Využití Redis jako cachovací databáze:

Hlavní využití Redisu v komerčních aplikacích je redis jako cachovací databáze. Redis běží v operační paměti a je schopen vracet velice rychle data. Myšlenka je zakreslená v následujícím obrázku.

![image](https://user-images.githubusercontent.com/42642687/199008241-984f260f-b345-4cb3-b9c8-36e16c0bfac8.png)

Prověďte následující úkoly:
1. Naplňte Postgres databázi informacema o katedrách na jednotlivých fakultách (stačí pár údajů) a vyprázdněete Redis databázi. 
2. Vytvořte webovou stránku ve Flasku, kde uživatel zvolí katedru.
3. Uživatel si na stránce zvolí katedru,  Flask aplikace se nejprve podívá do redis databáze a pokud se tám katedra nachází, tak vrátí její data.
4. Pokud se tam nebude katedra nacházet, pak se podívejte do Postgres databáze a přečtěte informace z ní.
5. Tyto informace uložte do Redis databáze, ať tam jsou nacachované pro příští rychlé využití. 
6. Informace tam zůstanou nacachované maximálně minutu. 
7. Vrácená data vizualizujte šablonovacím jazykem Jinja2.
8. Změřte rychlost vracení nacachované a nenacachované hodnoty z webové aplikace.


## Domácí cvičení 1

### Úkol HW6.1 Lorem:

### Úkol HW6.2 Lorem:

### Úkol HW6.3 Lorem:

### Úkol HW6.4 Lorem:

### Úkol HW6.5 Lorem:

