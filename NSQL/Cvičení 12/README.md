# NoSQL databázové systémy

## Cvičení 12 - Grafová databáze Neo4J

### Zadání

Nainstalujte si grafovou databázi Neo4j pomocí docker-compose. Dále si nainstalujte ovladač pro práci s neo4j v pythonu a zkuste si hello world program z oficiální dokumentace: [ZDE](https://neo4j.com/docs/python-manual/current/get-started/).

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
