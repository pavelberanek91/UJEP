# Datová úložiště a nástroje pro Big Data (KI/BIG)

## Seminář 2 - Tvorba unifikovaných izolovaných prostředí: Docker, CoreOS, rkt

### Samostudium

#### S2.1 - Orchestrace

Jakmile se začne růst počet kontejnerů vaší aplikace, tak začne vznikat velké množství problémů:
1. Jak automatizuji životní cyklus kontejnerů?
2. Jak můžeme systém škálovat (nahoru i dolu)?
3. Jak zajistíme znovuspuštění kontejnerů, pokud z nějakého důvodu dojde k jejich pádu při běhu?
4. Jak můžeme můžeme nasadit změny systému do provozu bez přerušení běhu (tzv. blue-green deployment)?
5. Jak zajistíme komunikaci mezi hardwarovými uzly přes virtuální sítě?
6. Jak můžeme ukládat a doručovat klíče, hesla a jiná tajemství do správných kontejnerů?

Tyto situace řeší orchestrační nástroje, jako je Docker Swarm nebo Kubernetes. Orchestrace je termín, který představuje proces automatické konfigurace, koordinace spolupráce a řízení softwaru. V kontextu kontejnerů se tím myslí schopnost řídit životní cyklus kontejnerů.

Docker Swarm řeší orchestraci tím způsobem, že rozděluje uzly v síti na 2 typy - manažeři a dělníci (manažeři mohou být zároveň dělníky). Manažeři řídí životní cyklus dělníků.

#### S2.2 - CoreOS, Fedora CoreOS a Flatcar Linux

#### S2.3 - Nasazení obrazů

#### S2.4 - Monitorování obrazů

### Cvičení

#### C2.1 - Nginx

**1. Reverzní proxy**
1. Vytvořte Dockerfile pro Python
2. Nahrajte do Dockerfilu jednoduchou Flask aplikaci
3. Vytvořte Nginx konfigurační soubor a nastavte ho jako reverzní proxy na portu 80
4. Spojte Dockerfile se stáhnutým Docker obrazem Nginx pomocí dockercompose
5. Spusťte a otestujte pomocí logs v docker-compose

**2. Bezpečnost**
1. Vyzkoušejte, že curl http://localhost vrací obsah z backendu, ale curl -I http://localhost vrací jako server nginx
2. Přidejte do nginx ochranu proti DDoS útokům omezením rychlosti požadavků a otestujte skriptem.

**3. Load balacing**
1. Přidejte do flask kódu kód, který bude identifikovat, ze kterého serveru se vrací odevzda, např.: return f'Hello from {os.environ["HOSTNAME"]}!'
2. Vytvořte více instance flask backendu na různých portech v docker-compose
3. Nastavte nginx jako loadbalacner mezi instantizovanými kontejnery v nginx.conf
4. Otestujte load balancing

**4. Cachování**
1. Přidejte do konfiguje nginx cestu ke cachování odpovědí
2. Ověřte, že se odpovědi vrací z cache

#### C2.2 - Docker Swarm

Pojďme nejprve zapnout Docker Swarm (implicitně je neaktivní, což zjistíte pomocí docker info příkazu). Následující příkaz vytvoří hejno s bezpečnostním certifikátem a tokeny pro připojení do hejna.

```
docker swarm init
```

Pojďme si vypsat všechny existující uzly. Ve výpisu vidíme jeden existující, jehož status je Leader. Vůdce může být v celém hejnu pouze jeden. 
```
docker node ls
```

Příkaz node slouží pro různé administrační záležitosti jako změna stavu uzlu z manažera na dělníka a naopak nebo odstranění uzlu z hejna.
```
docker node --help
```

Pro řízení samotného hejna slouží příkaz swarm, kterým můžeme připojovat uzly do hejna.
```
docker swarm --help
```

V hejnu se již nevyužívá příkaz docker run, ale hejnový příkaz docker service. Tento příkaz slouží pro vytváření služeb hejna a škálování.
```
docker service --help
```

Pojďme vytvořit naší první službu hejna. Vytvoříme službu, která vezme alpine linux obrazy a zavolá příkaz ping v terminálu aby pingnul server Googlu.
```
docker service create alpine ping 8.8.8.8
```

Službu si můžeme prohlédnout pomocí následující příkazu.
```
docker service ls
```

#### C2.3 - Kontejnerizace aplikace pomocí RKT

#### C2.4 - Flatcar Linux

#### C2.5 - Monitorování pomocí Prometheus a Grafana

#### D2.3 - lorem

#### D2.4 - lorem

#### D2.5 - lorem
