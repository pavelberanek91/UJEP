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

Pokud byste spustili docker kontejner se jménem, se kterým nejste spokojeni, pak můžete docker kontejner zastavit pomocí příkazu: ```docker stop muj_redis``` 

========== dodělat

a případně smazat kontejner příkazem ```docker rmi $(docker image | grep 'muj_redis')```. Pokud byste chtěli smazat stažený obraz, pak použijte příkaz: ```docker rmi $(docker image | grep 'muj_redis')```.

Pokud byste chtěli smazat všechny stažené obrazy, pak to provedete příkazem ```docker rmi $(docker images -q)```.

========== 

Pro využívání CLI příkazů na obrazu Redis si zapneme interaktivní mód a zapneme shell: ```docker exec -it muj_redis sh```.

V shellu Redis kontajneru můžeme zapnout aplikace redis-cli pro práci s Redis databází v příkazové řádce: ```redis-cli```.

### Úkol OS6.2 Komunikace s Redis pomocí redis-py:


### Úkol OS6.3 Lorem:


### Úkol OS6.4 Využití Redis jako rychlé in-memory databáze:


### Úkol OS6.5 Využití Redis jako cachovací databáze:


## Domácí cvičení 1

### Úkol HW6.1 Lorem:

### Úkol HW6.2 Lorem:

### Úkol HW6.3 Lorem:

### Úkol HW6.4 Lorem:

### Úkol HW6.5 Lorem:

