# NoSQL databázové systémy

## Cvičení 12 - Grafová databáze Neo4J

### Zadání
V tomto cvičení si budeme hrát s grafovou databází Neo4J bez kódu v jazyce Python. Vyzkoušíme si pomocí jazyka Cypher budovat grafovou databázi. 

#### Úkoly
Tyto úkoly zkuste splnit bez koukání se do mého řešení. Pokud byste měli velký problém s chápáním návodů na internetu, tak se můžete do řešení podívat.

1. Napište si docker-compose.yml soubor, který stáhne neo4j obraz, nastaví porty na databázi a protokol pro komunikaci bolt a nastaví přístupové údaje.
2. Otevřete si Neo4j databázi v prohlížeči a přihlašte se do systému (db nemusíte volit a nechat prázdné).
3. Vytvořte uzel v databázi pomocí Cypher jazyka. Uzel se bude jmenovat Katedra a jeho vlastnosti budou adresa a patro. Vyplňte do adresy adresu budovy CPTO a do patra číslo 6.
4. Vytvořte druhý uzel v databázi pomocí Cypher Jazyka. Uzel se bude jmenovat Vedoucí a jeho vlastnosti budou jméno, tituly, kancelář, telefon a email. Vyplňte informace podle následujícího odkazu [ZDE](https://ki.ujep.cz/cs/personalni-slozeni/jiri-skvor/).
5. Vytvořte vztah mezi těmito uzly. Vztah bude mít název: vede katedru.
6. Prohlédněte si ve webové vizualizaci vytvořenou grafovou databázi.
7. Doplňte zaměstnance a dej jim řádné vztahy ke katedře (stačí pár příkladů).
8. Rozšiřte příklad o fakultu a katedry (stačí pár příkladů).
9. Rozšiřte příklad o univerzitu a fakulty (stačí pár příkladů).
10. Vytvořte Cypher dotaz, který vypíše názvy všech fakult.
11. Vytvořte Cypher dotaz, který vypíše názvy všech kateder na všech fakultách.
12. Vytvořte Cypher dotaz, který vypíše všechny telefony vedoucích kateder.
13. Vytvořte Cypher dotaz, který vypíše všechny emaily zaměstnanců kateder přírodovědecké fakulty.

**Řešení úkolu 1**
```
version: '3'

services:
  neo4j:
    image: 'neo4j:latest'
    ports:
      - '7474:7474'
      - '7687:7687'
    environment:
      NEO4J_AUTH: 'neo4j/adminpass'
```

Následně pomocí příkazu ```docker-compose up``` v terminálu spustím.

**Řešení úkolu 2**

Stačí otevřít v prohlížeči adresu localhost s portem podle docker-compose.yml souboru. Implicitně je to port 7474. Pak zadáte svoje údaje z docker-compose souboru a prihlásíte se. Jméno databáze zvolte například test.

**Řešení úkolu 3**

V prohlížeči nalezneme horní příkazovou lištu a zadáme tam příkaz pro vytvoření uzlu:
```
CREATE(k1:Katedra{jméno: "Katedra Informatiky", adresa: "Pasteurova 3632/15, 400 96 Ústí nad Labem", patro: 6})
```

**Řešení úkolu 4**

```
CREATE(v1: Vedoucí{jméno: "Jiří Škvor", tituly: "RNDr., Ph.D.", kancelář: "6.01", telefon: "+420 475 286 711", email:"jiri.skvor@ujep.cz"})
```

**Řešení úkolu 5**

```
MATCH
  (v1: Vedoucí),
  (k1: Katedra)
CREATE (v1)-[: vede]->(k1)
```

**Řešení úkolu 6**
```
MATCH (n) RETURN n
```

**Řešení úkolu 7**

**Řešení úkolu 8**

**Řešení úkolu 9**

**Řešení úkolu 10**

### Domácí úkoly

Za domácí úkol si doděláte docker-compose soubor, kterým se připojíte k vaší budované databázi a vyzkoušíte si alespoň jeden dotaz nad ní.

Docker compose:

```
neo4j:
    image: neo4j:latest
    env_file:
      - '.env'
      - '.testenv'
    ports:
      - '7475:7475'
      - '7688:7688'
    volumes:
      - 'testdb:/data'
```

Python konektor:

```
pip install neo4j
```

Hello world aplikace:

```
from neo4j import GraphDatabase

class HelloWorldExample:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def print_greeting(self, message):
        with self.driver.session() as session:
            greeting = session.execute_write(self._create_and_return_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]


if __name__ == "__main__":
    greeter = HelloWorldExample("bolt://localhost:7687", "neo4j", "password")
    greeter.print_greeting("hello, world")
    greeter.close()
```

Než začnete (pro případ problémů):
1. Zjistěte si, jaké všechny porty potřebujete v docker-compose nastavit pro Neo4j
2. Vyzkoušejte si raději předpřipravený docker-image pro neo4j od bitnami
3. Vyzkoušejte pomocí cypheru (CQL) dotaz do neo4j: [ZDE](https://www.tutorialspoint.com/neo4j/index.htm)
4. Připojte neo4j pomocí docker-compose k vaší aplikaci a vyzkoušejte.
