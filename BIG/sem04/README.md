# Datová úložiště a nástroje pro Big Data (KI/BIG)

## Seminář 4 - NoSQL databáze a BigData (Neo4j)

### Samostudium

#### S4.1 - Neo4j

Neo4j je grafová databáze navržená speciálně pro ukládání, správu a dotazování na data, která mají složité vztahy mezi entitami. Data jsou ukládána ve formě grafů do uzlů (node) a vztahů mezi nimi (edge). Každý uzel a hrana mají své vlastnosti (property) modelované jako množina dvojic typu klíč-hodnota.

Neo4j je navržena pro ukládání a práci s daty, která mají složité vztahy mezi jednotlivými entitami, což je častý rys veledat. Mezi její výhody z pohledu našeho kurzu jsou:
1. Neo4j je optimalizován pro dotazy na grafové struktury, což umožňuje efektivní analýzu vztahů (např. sociální sítě, obchodní transakce, logistika), které by byly v relačních databázích mnohem pomalejší a náročnější. Jeho rychlost se ukazuje tak efektivní, že je vhodný i pro práci v reálném čase (detekce podvodů analýzou transakcí).
2. Neo4j podporuje horizontální škálování, což je klíčové pro efektivní práci s obrovským množstvím dat (volume vlastnost).
3. Neo4j dovoluje dynamicky přidávat nové typy vztahů nebo uzlů, aniž by bylo nutné měnit strukturu databáze, což je výhodné při práci s neustále se měnícími veledaty (variety vlastnost).
4. Neo4j se často používá ve spojení s big data ekosystémem (Apache Hadoop, Apache Spark), které mohou předzpracovávat velké objemy dat, než jsou uloženy nebo analyzovány v Neo4j. Tyto integrace umožňují vytvořit robustní řešení pro analýzu veledat.


#### S4.2 - Cypher Query Language (CQL)

Neo4j používá dotazovací jazyk zvaný Cypher, který umožňuje jednoduše a čitelně psát dotazy na grafová data. Pojďme se podívat na základní operace v jazyce Cypher (CRUD operace - Create, Read, Update, Delete, slučovací a agregační dotazy).

**Create: Vytvoření uzlu**
Dotaz vytvoří uzel se značkou (label) Person a vlastnostmi name a age.
```cypher
CREATE (p:Person {name: 'John Doe', age: 30})
```

**Create: Vytvoření uzlu a vztahu**
Dotaz vytvoří dva uzly Person s vlastnostmi name a propojí je vztahovým typem FRIENDS_WITH.
```cypher
CREATE (p1:Person {name: 'Alice'}), (p2:Person {name: 'Bob'})
CREATE (p1)-[:FRIENDS_WITH]->(p2)
```

**Read: Vyhledání všech uzlů určitého typu**¨
Najde všechny uzly se značkou Person a vrátí je.
```cypher
MATCH (p:Person) RETURN p
```

**Read: Vyhledání uzlu podle vlastnosti**
Najde všechny uzly Person, kde name je John Doe, a vrátí je.
```cypher
MATCH (p:Person {name: 'John Doe'}) RETURN p
```

**Read: Vyhledání vztahů**
Najde všechny vztahy FRIENDS_WITH mezi uzly Person.
```cypher
MATCH (p1:Person)-[r:FRIENDS_WITH]->(p2:Person) RETURN p1, r, p2
```

**Read: Cesta mezi uzly**
Najde cestu mezi Alice a Eve, kde je libovolný počet (včetně nuly) vztahů FRIENDS_WITH.
```cypher
MATCH path = (p1:Person {name: 'Alice'})-[:FRIENDS_WITH*]->(p2:Person {name: 'Eve'}) RETURN path
```

**Update: Vytvoření uzlu**
Najde uzel Person s name John Doe, aktualizuje jeho věk na 31.
```cypher
MATCH (p:Person {name: 'John Doe'})
SET p.age = 31
RETURN p
```

**Update: Přidání nových vlastností**
Přidá vlastnost email do uzlu John Doe.
```cypher
MATCH (p:Person {name: 'John Doe'})
SET p.email = 'johndoe@example.com'
RETURN p
```

**Update: Aktualizace značky**
Přidá uzlu John Doe nový label Employee.
```cypher
MATCH (p:Person {name: 'John Doe'})
SET p:Employee
RETURN p
```

**Delete: Smazání uzlu (bez vztahů)**
```cypher
MATCH (p:Person {name: 'John Doe'})
DELETE p
```

**Delete: Smazání uzlu s jeho vztahy**
Odstraní uzel John Doe i se všemi jeho vztahy.
```cypher
MATCH (p:Person {name: 'John Doe'})
DETACH DELETE p
```

**Delete: Odstranění vlastnosti**
Odstraní vlastnost email z uzlu John Doe.
```cypher
MATCH (p:Person {name: 'John Doe'})
REMOVE p.email
RETURN p
```

**Použití podmínek**
Najde všechny uzly Person s věkem větším než 25 a vrátí jejich vlastnostni name a age.
```cypher
MATCH (p:Person)
WHERE p.age > 25
RETURN p.name, p.age
```

**Vrácení hodnot s tříděním**
Vrátí seznam osob seřazený podle věku sestupně.
```cypher
MATCH (p:Person)
RETURN p.name, p.age
ORDER BY p.age DESC
```

**Spočítání uzlů**
Spočítá počet uzlů se značkou Person.
```cypher
MATCH (p:Person)
RETURN count(p)
```

**Spočítání vztahů určitého typu**
Spočítá počet vztahů FRIENDS_WITH.
```cypher
MATCH ()-[r:FRIENDS_WITH]->()
RETURN count(r)
```

**Seskupení a agregace**
Sesbírá uzly Person a spočítá, kolik jich je podle věku.
```cypher
MATCH (p:Person)
RETURN p.age, count(p) AS count_by_age
```

#### S4.3 - Pokročilé příkazy CQL

**Slučování uzlů**
MERGE je podobný CREATE, ale pouze vytvoří uzel nebo vztah, pokud ještě neexistuje. Pokud uzel nebo vztah existuje, použije jej. Tento dotaz vyhledá nebo vytvoří uzel Person s name John Doe. Pokud uzel neexistuje, nastaví věk na 30. Pokud uzel existuje, aktualizuje lastLogin na aktuální časové razítko.
```cypher
MERGE (p:Person {name: 'John Doe'})
ON CREATE SET p.age = 30
ON MATCH SET p.lastLogin = timestamp()
RETURN p
```

**Slučování vztahů**
Vyhledá (nebo vytvoří, pokud neexistuje) vztah FRIENDS_WITH mezi Alice a Bobem.
```cypher
MATCH (p1:Person {name: 'Alice'}), (p2:Person {name: 'Bob'})
MERGE (p1)-[r:FRIENDS_WITH]->(p2)
RETURN p1, r, p2
```

**Použití ON CREATE a ON MATCH**
Pokud uzel neexistuje, vytvoří ho s vlastnostmi name a createdAt. Pokud uzel existuje, aktualizuje lastLogin.
```cypher
MERGE (p:Person {email: 'alice@example.com'})
ON CREATE SET p.name = 'Alice', p.createdAt = timestamp()
ON MATCH SET p.lastLogin = timestamp()
RETURN p
```
**Agregace s využitím COLLECT**
Vrátí seznam přátel pro každou osobu pomocí funkce COLLECT, která shromažďuje data do seznamu.
```cypher
MATCH (p:Person)-[:FRIENDS_WITH]->(friend:Person)
RETURN p.name AS person, COLLECT(friend.name) AS friends
```

**Skupinová agregace s SUM, AVG, MAX, MIN**
Vrátí počet osob, průměrný věk, maximální a minimální věk pro každou skupinu osob podle věku.
```cypher
MATCH (p:Person)
RETURN p.age AS age_group, COUNT(p) AS count, AVG(p.age) AS avg_age, MAX(p.age) AS max_age, MIN(p.age) AS min_age
```

**Použití spojení dat s UNION**
UNION umožňuje sloučit výsledky dvou nebo více dotazů do jedné odpovědi. Tento dotaz vrátí kombinované výsledky obou dotazů, tedy data o Alice i Bobovi.
```cypher
MATCH (p:Person {name: 'Alice'}) RETURN p.name AS name, p.age AS age
UNION
MATCH (p:Person {name: 'Bob'}) RETURN p.name AS name, p.age AS age
```

**Rozvinutí seznamů**
Rozvine seznam jmen a pro každé vytvoří nový uzel Person.
```cypher
UNWIND ['Alice', 'Bob', 'Charlie'] AS name
CREATE (:Person {name: name})
```

**Cyklické vztahy**
Najde všechny osoby, které mají cyklické přátelské vztahy (přátelí se samy se sebou přes jednu či více osob).
```cypher
MATCH (p:Person)-[:FRIENDS_WITH*]->(p)
RETURN p.name
```

**Hledání cyklů v grafech**
Hledání cyklů může být užitečné v různých scénářích, jako je detekce smyček nebo sledování vztahů. Najde všechny cykly začínající a končící u Alice.
```cypher
MATCH (p:Person {name: 'Alice'})-[*]->(p)
RETURN p
```

**Výpočet vzdáleností**
Vypočítá vzdálenosti mezi všemi dvojicemi lokací.
```cypher
MATCH (p1:Location), (p2:Location)
WHERE id(p1) <> id(p2)
RETURN p1.name, p2.name, distance(p1.coordinates, p2.coordinates) AS distance
ORDER BY distance ASC
```

**Zjišťování krátkých cest**
Neo4j umožňuje najít nejkratší cestu mezi dvěma uzly pomocí shortestPath.
```cypher
MATCH (p1:Person {name: 'Alice'}), (p2:Person {name: 'Bob'})
MATCH path = shortestPath((p1)-[*]-(p2))
RETURN path
```

**Zpracování více úrovní vztahů**
Cypher umožňuje prohledávat více úrovní vztahů a efektivně zjišťovat hierarchické a složité struktury. Tento dotaz najde všechny přátele Alice až do třetí úrovně vztahů FRIENDS_WITH.
```cypher
MATCH (p:Person {name: 'Alice'})-[:FRIENDS_WITH*1..3]->(friend)
RETURN friend.name
```

**Poddotazy (Subqueries)**
Cypher podporuje poddotazy, které jsou užitečné pro složitější operace v dotazech. Tento dotaz použije poddotaz k vyhledání přátel Alice a jejich věku.
```cypher
MATCH (p:Person {name: 'Alice'})
CALL {
  WITH p
  MATCH (p)-[:FRIENDS_WITH]->(friend)
  RETURN friend.name AS friend_name, friend.age AS friend_age
}
RETURN friend_name, friend_age
```

**Použití vzorců pro prohledávání struktur v grafech**
Lze najít složité struktury pomocí specifických vzorců vztahů. Tento dotaz najde všechny osoby, které spravují zaměstnance pracující na konkrétních projektech, a vrátí příslušná data.
```cypher
MATCH (manager:Person)-[:MANAGES]->(employee:Person)-[:WORKS_ON]->(project:Project)
RETURN manager.name, employee.name, project.name
```

**Podmíněné přidání nebo aktualizace dat**
Podmínky lze použít pro flexibilnější manipulaci s daty. Tento dotaz kategorizuje osoby do skupin podle věku: minor, adult, senior.
```cypher
MATCH (p:Person)
RETURN p.name, 
       CASE 
         WHEN p.age < 18 THEN 'minor'
         WHEN p.age >= 18 AND p.age < 65 THEN 'adult'
         ELSE 'senior'
       END AS age_category
```

**Transakční dotazy**
Aktualizuje věk Alice a zaznamená čas aktualizace v jedné transakci.
```cypher
BEGIN
MATCH (p:Person {name: 'Alice'})
SET p.age = p.age + 1
CREATE (p)-[:UPDATED_ON]->(t:Timestamp {time: timestamp()})
COMMIT
```

**Projekce vlastností**
Vrátí pouze vybrané vlastnosti uzlu Person.
```cypher
MATCH (p:Person)
RETURN p { .name, .age } AS personData
```

**Práce s definovaným podgrafem**
Vytvoří podgraf přátelství a pak vrátí seznam přátel pro každou osobu.
```cypher
CALL {
  MATCH (p:Person)-[:FRIENDS_WITH]->(friend)
  RETURN p, friend
}
RETURN p.name, collect(friend.name) AS friends
```

**Vzory s konkrétními podmínkami**
Najde přátele nebo kolegy do 2 stupňů, kteří nejsou zablokováni.
```cypher
MATCH (p:Person)-[r:FRIENDS_WITH|COLLEAGUE_OF*1..2]-(friend)
WHERE NOT (p)-[:BLOCKED]-(friend)
RETURN DISTINCT friend.name
```

**Použití CASE**
Klasifikuje osoby do věkových skupin.
```cypher
MATCH (p:Person)
RETURN p.name,
CASE
  WHEN p.age >= 18 THEN 'Dospělý'
  ELSE 'Nezletilý'
END AS věková_skupina
```

**Filtrace s EXISTS**
Najde osoby, které pracují ve společnosti Neo4j.
```cypher
MATCH (p:Person)
WHERE EXISTS {
  MATCH (p)-[:WORKS_AT]->(:Company {name: 'Neo4j'})
}
RETURN p.name
```

**Práce s percentily**
Vypočítá medián věku osob.
```cypher
MATCH (p:Person)
RETURN percentileDisc(p.age, 0.5) AS medianAge
```

**Dávková aktualizace uzlů pomocí FOREACH**
Nastaví věk 30 pro všechny osoby, které nemají nastavenou hodnotu age.
```cypher
MATCH (p:Person) WHERE p.age IS NULL
WITH collect(p) AS persons
FOREACH (person IN persons |
  SET person.age = 30
)
```

**Vytváření indexů**
Vytvoří index na vlastnosti email pro uzly Person.
```cypher
CREATE INDEX FOR (p:Person) ON (p.email)
```

**Vytváření unikátních omezení**
Zajistí, že hodnota email je unikátní mezi všemi uzly Person.
```cypher
CREATE CONSTRAINT ON (p:Person) ASSERT p.email IS UNIQUE
```

**Full-textové vyhledávání**
Nastavení full-textového indexu
```cypher
CALL db.index.fulltext.createNodeIndex("personNames", ["Person"], ["name"])
```

Použití full-textového vyhledávání pro vyhledání všech osob,  jejichž jméno začíná na "Al".
```cypher
CALL db.index.fulltext.queryNodes("personNames", "Al*")
YIELD node, score
RETURN node.name, score
```

**Práce s datem a časem**
Najde osoby vytvořené před více než jedním rokem.
```cypher
MATCH (p:Person)
WHERE p.createdAt < date() - duration('P1Y')
RETURN p.name
```

**Použití APOC funkcí**
APOC (Awesome Procedures On Cypher) je knihovna rozšiřující možnosti Cypheru. Tento příklad vygeneruje jedinečné UUID a přiřadí ho uzlu Alice.
```cypher
CALL apoc.create.uuid()
YIELD uuid
MATCH (p:Person {name: 'Alice'})
SET p.id = uuid
RETURN p
```

**Výpočet PageRank**
Pokud máte nainstalovanou knihovnu Graph Data Science, můžete využít různé algoritmy. Následující dotaz vypočítá PageRank skóre pro uzly Person na základě vztahů FRIENDS_WITH.
```cypher
CALL gds.pageRank.stream({
  nodeProjection: 'Person',
  relationshipProjection: 'FRIENDS_WITH'
})
YIELD nodeId, score
RETURN gds.util.asNode(nodeId).name AS name, score
ORDER BY score DESC
```

#### S4.4 - Knihovny pro neo4j
Pro rozšíření možností práce s Neo4j existuje několik dodatečných knihoven, které obohacují Cypher a umožňují pokročilé operace, analýzu a manipulaci s daty.

**APOC (Awesome Procedures on Cypher)**
APOC je jedna z nejpoužívanějších knihoven pro Neo4j, která obsahuje stovky předdefinovaných funkcí a procedur, které zjednodušují a rozšiřují možnosti Cypheru. APOC je obvykle již integrovaný do Neo4j, ale pokud není, můžete ho přidat jako doplněk stažením z APOC GitHub.

* Manipulace s daty: Rozšiřuje CQL o funkce pro práci se seznamy, mapami a textovými řetězci, jako jsou procedury pro transformaci a formátování.
* Integrace s API: Podporuje volání vzdálených API, načítání JSON nebo XML dat do grafu.
* Import a export: Umožňuje import dat z různých formátů, jako jsou CSV, JSON a XML, a export dat zpět do těchto formátů.
* Správa grafů: Obsahuje nástroje pro vytváření, mazání a manipulaci s grafovými strukturami, včetně procedur pro správu uzlů a vztahů.
* Pokročilé agregace a analýzy: Poskytuje agregované a analytické funkce, které nejsou běžně dostupné v Cypheru, jako například metriky centrality.

APOC je velmi používaná knihovna, tak si vypíšeme, co vše umí:
* apoc - nápověda a verze APOC knihovny
* agg - agregační funkce (první, poslední, medián, percentily, součin, statistiky)
* algo - algoritmy nad grafem (A*, Dijkstra, cesty)
* any - nástroje pro práci s virtuálními uzly a vztahy
* atomic - nástroje pro atomické operace (přidej, připoj, vlož, odstraň, odečti, uprav)
* bitwise - nástroje pro bitové operace
* bolt - nástroje pro přístup z Neo4J do jiných databází přes Bolt protokol
* cluster - pro shlukování uzlů v grafu
* coll - nástroje pro práci s kolekcemi (obsahuje, průměr z kolekce, rozdělení, zipování, kombinace, množinové operace, míchání apod.)
* config - nástroje pro práci s nastavením databáze
* convert - nástroje pro konverzi datových typů (na strom, na čísla, na množiny a jiné kolekce)
* couchbase - nástroje pro práci s CouchBase databází
* create - nástroje pro tvorbu a odstraňování uzlů, vztahů, virtuálních cest, uuid a pod.
* custom - nástroje pro tvorbu vlastních procedur a funkcí
* cypher - nástroje pro spouštění Cypher dotazů ze souborů, paralelně, sekvenčně apod.
* data - nástroje pro práci se síťovou cestou (doména, email, URL)
* date - nástroje pro práci s datumy (expirace, konverze, parsing, standardy, časové zóny)
* dv - nástroje pro práci s virtuálními daty (nejsou přímo v Neo4J, ale v jiném datovém zdroji)
* es - nástroje pro práci s Elastic Search (get, post, query)
* examples - databáze datasetů k hraní si (toy-datasets), má zatím jen jednu databázi a to movies
* export - nástroje pro export dat z Neo4J do jiných datových formátů (csv, cypher, graphml, json, xls)
* generate - nástroje pro generování náhodných grafů podle různých modelů (Barabasi-Alber, Erdos-Renyi, Watts-Strogatz)
* gephi - nástroje pro práci s daty v Gephi formátu (jedna z nejpopulárnější vizualizačních platforem pro grafová data)
* get - nástroje pro získání uzlů a vztahů podle ID
* graph - nástroje pro tvorbu grafu z dokumentů, dat a cypher dotazu
* hashing - funkce pro výpočet hash otisků
* import - nástroje pro nahrání dat ze souborů s grafovou strukturou a slouží oproti apoc.load pro velké množství dát naráz (CSV, JSON, XML, GraphML)
* json - nástroje pro traverzaci (cestování) po cestách v JSON souboru
* label - zjišťování existence značky (label) v grafu
* load - nástroje pro nahrání dat ze souborů různých formátů (CSV, JSON, HTML, JDBC, XML, XLS), data nemusí mít grafovou strukturu a funkce si s nimi poradí (robustnější oproti import)
* lock - nástroje pro uzamykání přístupů k uzlům a vztahům
* log - nástroje pro logování informací (chyby, upozornění)
* map - nástroje pro úpravu hodnot (zploštění, shlukování, odstranění hodnot)
* math - matematické funkce (harmonické funkce, regrese, min a max číselných datových typů)
* merge - nástroje pro slučování uzlů a vztahů
* meta - nástroje pro meta informaci o grafu (tabulková podoba, podgrafy, datové typy, počty uzlů)
* metrics - nástroje pro získání a ukládání systémových metrik (start transakce, rollbacky)
* model - nástroje pro práci s relační databází (přes JDBC - Java Database Connectivity)
* mongo - nástroje pro komunikaci s MongoDB (CRUD operace)
* mongodb - to samé co apoc.mongo, ale deprecated
* monitor - vrací informace o zátězi na výpočetní prostředky
* neighbors - nástroje pro práci se soudeními uzly vybraného uzlu (vrátí uzly z/do určité vzdálenosti)
* nlp - nástroje pro zpracování přirozeného jazyka (fráze, nálada, detekce entit, klasifikace)
* node - nmástroje pro zjišťování informací o jednom uzlu (vstupní a výstupní stupně, značky, vztahy)
* nodes - nástroje pro práci s uzly (kolapsování, detekce cyklů, zjišťování exitence napojených vztahů apod.)
* number - nástroje pro převod čísel na jiné datové typy a formáty
* path - nástroje pro práci s cestami a podgrafy (řezání, rozšířování, směšování)
* periodic - nástroje pro dávkové zpracování dat
* redis - nástroje pro komunikaci s Redis databází
* refactor - nástroje pro refaktorizaci grafu (odstraň uzly a přepoj cestu apod.)
* rel - nástroje pro práci se vztahy v grafu (typ, počáteční a koncový uzel)
* schema - nástroje pro práci s databázovým schématem (ověření, vztahy, omezení)
* scoring - algoritmy pro hodnocení grafu (existence uzlů, Pareto)
* search - nástroje pro paralelní prohledávání uzlů
* spatial - nástroje pro práci s prostorovými (geo) daty
* static - nástroje pro práci se statickými soubory (klíče na serveru apod.)
* stats - statistické funkce (zatím jen degress)
* systemdb - práce s metadaty grafu a spouštění DDL příkazů
* temporal - nástroje pro práci s časovou zónou
* text - nástroje pro práci s textem (kapitalizace, fonezitace, čištění, vzdálenosti, fuzzy logika, regexy, rozdělení, kódování)
* trigger - nástroje pro práci s databázovými triggery
* ttl - nástroje pro práci s Tíme-to-Live (TTL), tedy časem expirace záznamu
* util - nástroje pro práci s hashováním a kompresí/dekompresí informací
* uuid - pro práci s univerzálně jedinečnými identifikátory ve formě 128 bitového čísla
* warmup - pro rychlé nahrání uzlů a vztahů do paměti
* xml - poskytuje algoritmy pro práci nad XML soubory

**Graph Data Science (GDS)**
Graph Data Science je knihovna zaměřená na pokročilé grafové algoritmy a analýzy pro strojové učení, doporučovací systémy a datovou vědu. GDS umožňuje provádět složité analýzy přímo v databázi, což je ideální pro aplikace, kde jsou data silně propojena. Knihovna GDS je k dispozici jako oficiální doplněk Neo4j. Lze ji nainstalovat přímo ze stránky Graph Data Science Library.

* Grafové algoritmy: Obsahuje algoritmy pro analýzu grafů, jako jsou algoritmy pro nalezení nejkratší cesty, centrality, komunity (např. Louvain nebo Label Propagation) a další.
* Analýza podobnosti a doporučování: Umožňuje doporučování na základě podobnosti nebo sousedství uzlů.
* Strojové učení a embeddingy: Nabízí funkce pro tvorbu grafových embeddingů, které slouží jako vstupní data pro modely strojového učení.
* Správa a projekce subgrafů: Umožňuje vytváření a práci s projekcemi grafů, což usnadňuje práci s velkými grafovými strukturami.

GDS je velmi používaná knihovna, tak si vypíšeme, jaké algoritmy poskytuje:
* Centralita
  * Article Rank
  * Articulation Points
  * Betweenness Centrality
  * Bridges
  * CELF
  * Closeness Centrality
  * Degree Centrality
  * Eigenvector Centrality
  * Page Rank
  * Harmonic Centrality (alfa verze)
  * HITS (alfa verze)
* Detekce komunit
  * Conductance metric
  * K-Core Decomposition
  * K-1 Coloring
  * K-Means Clustering
  * Label Propagation
  * Leiden
  * Local Clustering Coefficient
  * Louvain
  * Modularity metric
  * Modularity Optimization
  * Strongly Connected Components
  * Triangle Count
  * Weakly Connected Components
  * Approximate Maximum k-cut (alfa verze)
  * Speaker-Listener Label Propagation (alfa verze)
* Podobnost
  * Node Similarity
  * Filtered Node Similarity
  * K-Nearest Neighbors
  * Filtered K-Nearest Neighbors
* Hledání cesty
  * Delta-Stepping Single-Source Shortest Path
  * Dijkstra Source-Target Shortest Path
  * Dijkstra Single-Source Shortest Path
  * A* Shortest Path
  * Yen’s Shortest Path
  * Breadth First Search
  * Depth First Search
  * Random Walk
  * Bellman-Ford Single-Source Shortest Path
  * Minimum Weight Spanning Tree
  * Minimum Directed Steiner Tree (beta verze)
  * Minimum Weight k-Spanning Tree (alfa verze)
  * All Pairs Shortest Path (alfa verze)
  * Longest Path for DAG (alfa verze)
* Orientovaný acyklický graf (DAG)
  * Topological Sort (alfa verze)
  * Longest Path (alfa verze)
* Embdeddings pro uzly
  * FastRP
  * GraphSAGE (beta verze)
  * Node2Vec (beta verze)
  * HashGNN (beta verze)
* Predikce topologických vazeb
  * Adamic Adar (alfa verze)
  * Common Neighbors (alfa verze)
  * Preferential Attachment (alfa verze)
  * Resource Allocation (alfa verze)
  * Same Community (alfa verze)
  * Total Neighbors (alfa verze)
* Pregel API - pro vlastní funkce

**Neo4j Bloom**
Neo4j Bloom je vizualizační nástroj, který umožňuje interaktivní procházení grafů a vizualizaci dat v Neo4j. Bloom je vhodný pro ne-techniké uživatele, kteří potřebují snadno prozkoumat grafová data. Bloom je samostatný doplněk, dostupný jako součást Neo4j Desktop nebo Enterprise Edition.

* Vizualizace dat: Umožňuje vizuálně procházet graf a snadno vyhledávat uzly a vztahy na základě jednoduchých dotazů.
* Filtry a styly: Poskytuje možnosti filtrování dat a úpravy vizuálního zobrazení uzlů a vztahů.
* Předdefinované pohledy: Umožňuje ukládání pohledů na grafy pro snadné sdílení a prezentaci.

**Full-text Search Index**
Neo4j podporuje full-textové vyhledávání, což rozšiřuje základní možnosti Cypheru o pokročilé textové vyhledávání. To je užitečné pro aplikace, které potřebují najít uzly nebo vztahy na základě textového obsahu, jako jsou aplikace pro doporučování nebo vyhledávání informací.

Vytvoření full-textového indexu:
```cypher
CALL db.index.fulltext.createNodeIndex("personNames", ["Person"], ["name"])
```

Vyhledání s full-textovým indexem:
```cypher
CALL db.index.fulltext.queryNodes("personNames", "Al*")
YIELD node, score
RETURN node.name, score
```

**Neuler Plugin**
Neuler je plugin pro Neo4j zaměřený na usnadnění práce s grafovými algoritmy a vizualizaci grafů přímo z Neo4j Desktop. Pomáhá uživatelům provádět složitou analýzu bez nutnosti psát Cypher dotazy pro každý algoritmus. Neuler lze nainstalovat přímo z Neo4j Desktop jako rozšíření.

* Uživatelské rozhraní pro GDS: Zjednodušuje používání knihovny Graph Data Science pomocí GUI, kde lze přímo vybrat algoritmy a zpracovávat výsledky.
* Vizualizace algoritmů: Poskytuje vizualizační nástroje pro analýzu výsledků algoritmů.

**Liquigraph**
Liquigraph je nástroj pro správu migrací databází v Neo4j. Tento nástroj umožňuje verziování a správu změn v grafech podobně jako nástroje Liquibase nebo Flyway v relačních databázích.  Liquigraph je open-source nástroj dostupný na GitHubu a lze jej použít jako samostatnou aplikaci nebo knihovnu.

* Verzování grafových migrací: Umožňuje spravovat a provádět migrace grafových schémat.
* Automatizace změn: Pomáhá automatizovat změny ve struktuře grafu během vývoje.

**Neo4j Streams**
Neo4j Streams je rozšíření pro integraci Neo4j s Apache Kafka. Umožňuje přenos a synchronizaci dat mezi Neo4j a Kafkou, což je užitečné pro aplikace pracující s reálnými daty nebo pro distribuované systémy. Neo4j Streams je open-source a je k dispozici na GitHubu.

* Streamování událostí: Umožňuje streamování událostí z Neo4j do Kafky a naopak.
* Integrace s datovými pipelinami: Vhodné pro integraci Neo4j s datovými pipelinami, jako jsou Apache Spark nebo Hadoop.

**GraphQL for Neo4j**
GraphQL for Neo4j umožňuje přímou práci s daty v Neo4j pomocí rozhraní GraphQL, což usnadňuje práci s grafovými daty ve webových aplikacích. GraphQL pro Neo4j je k dispozici jako rozšíření na GitHubu a jako Neo4j GraphQL Toolbox.

* Automatická generace API: Generuje GraphQL API přímo z Neo4j dat.
* Interaktivní dotazy: Umožňuje provádět dotazy a mutace přímo z GraphQL rozhraní.

#### S4.5 - Optimalizaci výkonu a škálovatelnosti v Neo4j
Zde je několik konkrétních postupů a doporučení, které mohou pomoci při optimalizaci výkonu a škálování v Neo4j.

**Indexování**
* Vytvoření indexů: V Neo4j je možné vytvářet indexy pro specifické vlastnosti (atributy) uzlů, což významně zrychluje dotazy, které tyto vlastnosti filtrují. Doporučuje se indexovat vlastnosti, které jsou často používány v dotazech typu WHERE nebo MATCH.
* Unikátní omezení: Definování unikátních omezení (constraints) nejen zajišťuje jedinečnost dat, ale také automaticky vytváří indexy, což zlepšuje výkon dotazů.

**Profilování a optimalizace dotazů**
* PROFILING dotazů: Neo4j umožňuje použití příkazu PROFILE nebo EXPLAIN, které zobrazí, jak je dotaz vykonáván a kolik zdrojů spotřebovává. Tento nástroj umožňuje identifikovat úzká místa, která lze optimalizovat.
* Vyhýbání se kaskádovým operacím: Je třeba se vyhnout dotazům, které vyžadují plné procházení grafu, pokud to není nezbytné. U dlouhých dotazů lze použít specifické podmínky nebo indexy ke snížení počtu uzlů, které je třeba prohledat.
* Dávkování operací: Při provádění velkých změn v databázi (např. vytváření nebo aktualizace uzlů) je vhodné provádět tyto změny v dávkách (batch), aby se zabránilo přetížení paměti.

**Paměť a cache**
* Konfigurace paměti: Optimalizace konfigurace paměti je zásadní pro rychlý výkon Neo4j. Je nutné správně nakonfigurovat page cache (pro rychlý přístup k datům uloženým na disku) a heap memory (pro provádění dotazů). Velikost page cache by měla odpovídat velikosti datové sady nebo alespoň často používaným částem dat.
* Caching: Neo4j využívá caching pro často opakované dotazy a části grafu. Pro zlepšení výkonu se ujistěte, že klíčové části grafu jsou často přístupné v paměti díky efektivnímu cachingu.

**Použití APOC a GDS knihoven**
* APOC: Pro agregační funkce a různé výpočty používejte knihovnu APOC, díky které budou dotazy výpočetně efektivní a čisté než když si je budete psát pomocí vlastných Cypher dotazů.
* GDS: Pro výpočet grafových algoritmů, jako jsou algoritmy pro hledání nejkratší cesty nebo komunitní detekce, je vhodné použít knihovnu GDS, která je optimalizovaná pro takové výpočetně náročné úkony.

**Škálování**
* Vertikální škálování: Jednodušší způsob, jak škálovat Neo4j, je navýšit prostředky (RAM, CPU) na jednom serveru. Pro velké grafy s náročnými dotazy je dostatek paměti a výpočetního výkonu klíčový. To se však prodražuje s mírou škálování.
* Horizontální škálování (clustering): Neo4j Enterprise Edition podporuje clustering, což umožňuje rozdělit zátěž na více uzlů (serverů). Databáze se tak stává výkonově robustnější a dostupnější. Dostupnost se dá zlepšit využitím architektury Master-slave s více replikami.

**Optimalizace modelu grafu**
* Minimalizace vztahů: Přestože jsou vztahy v grafu klíčové, příliš mnoho nebo zbytečných vztahů může zhoršit výkon. Doporučuje se udržovat graf jednoduchý, s minimálním počtem vztahů, které zajišťují potřebné spojení.
* Správné rozdělení dat: Pokud je graf příliš složitý, je vhodné zvážit rozdělení na více menších, propojených grafů nebo přizpůsobení modelu tak, aby bylo snazší provádět specifické dotazy s minimálním přecházením mezi uzly.

**Správa a monitoring**
* Neo4j Management Tools: Neo4j poskytuje nástroje pro monitoring výkonu databáze, které mohou pomoci s identifikací problémů s výkonem, jako je např. Neo4j Ops Manager.
* Logování a analytika: Udržování logů dotazů a jejich analýza umožňuje identifikovat časté a pomalé dotazy, které lze optimalizovat.

### Cvičení

V tomto cvičení budete analyzovat data ze sociální sítě.

#### C4.1 - Příprava prostředí v Docker

Připravite si docker-compose.yml soubor, kterým zprovozníte aplikaci. Stačí jen vlastní Dockerfile s pythonem a obraz pro Neo4j. Pozor na to, že neo4j dlouho startuje a bude nutné počkat pro závislé kontejnery. Lze to řešit tím, že počkáte určitou dobu nebo pomocí kontroly zdraví kontejneru (healthcheck) počkáte do doby provozu kontejneru.

**Řešení úkolu**
V tomto docker-compose souboru je jen neo4j a kontejner pro python skript, který budu následně používat.
```cypher
version: '3.8'

services:
  python-app:
    build: .
    container_name: python-app
    depends_on:
      neo4j:
        condition: service_healthy

  neo4j:
    image: 'neo4j:latest'
    ports:
      - '7474:7474'
      - '7687:7687'
    environment:
      NEO4J_AUTH: 'neo4j/adminpass'
    healthcheck:
      test: cypher-shell --username neo4j --password adminpass 'MATCH (n) RETURN COUNT(n);' # Checks if neo4j server is up and running
      interval: 10s
      timeout: 10s
      retries: 5
```

#### C4.2 - Vygenerujte do databáze falešná data
Vygenerujte do databáze umělá data skriptem. Můžete použít můj skript, který generuje umělá data o sociální síti. Data zahrnují uživatele a jejich vztahy, příspěvky a komentáře.

```
import random
from faker import Faker
from py2neo import Graph, Node, Relationship

fake = Faker()
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

# Nastavení počtu uživatelů, příspěvků a vztahů
NUM_USERS = 1000
NUM_POSTS = 5000
NUM_RELATIONSHIPS = 2000

# Vymazání existujících dat
graph.run("MATCH (n) DETACH DELETE n")

# Vytváření uživatelů
users = []
for i in range(NUM_USERS):
    user = Node("User", name=fake.name(), age=random.randint(18, 70), location=fake.city())
    graph.create(user)
    users.append(user)

# Vytváření příspěvků
posts = []
for i in range(NUM_POSTS):
    user = random.choice(users)
    post = Node("Post", content=fake.text(), created_at=fake.date_time_this_year())
    graph.create(post)
    graph.create(Relationship(user, "CREATED", post))
    posts.append(post)

# Vytváření vztahů mezi uživateli (FOLLOWING)
for i in range(NUM_RELATIONSHIPS):
    user_a = random.choice(users)
    user_b = random.choice(users)
    if user_a != user_b:
        graph.create(Relationship(user_a, "FOLLOWS", user_b))

# Vytváření komentářů
for i in range(NUM_POSTS // 2):
    user = random.choice(users)
    post = random.choice(posts)
    comment = Node("Comment", content=fake.sentence(), created_at=fake.date_time_this_year())
    graph.create(comment)
    graph.create(Relationship(user, "COMMENTED", comment))
    graph.create(Relationship(comment, "ON", post))

print("Data byla úspěšně vygenerována.")
```

Python skript bude v kontejneru, který je sestaven následujícícm Dockerfilem:
```Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY synthetic_data.py /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
CMD ["python", "synthetic_data.py"]
```
Tento Dockerfile je právě tím, který builduji v souboru z předchozího cvičení.

Zobrazte si výslednou sociální síť v základním webovém rozhraní neo4j (Neo4j Browser). Implicitně běží na portu 7474 a zobrazit celou síť (bude problém, pokud vygenerujete hodně dat) můžete příkazem:

```cypher
MATCH (uzel) RETURN uzel
```

#### C4.3 - Základní operace
Vyzkoušejte si nad daty následující jednoduché analýzy:
1. Vyhledejte prvních 10 uživatelů v databázi.
2. Najděte všechny uživatele, kteří žijí v nějakém zadaném městě.
3. Vytvořte vztah, kde "Alice" sleduje "Boba".
4. Zobrazte 5 uživatelů s největším počtem příspěvku.
5. Zobrazte prvních 10 vztahů, kde jeden uživatel sleduje jiného.
6. Zobrazte 10 příspěveků a jejich komentáře.
7. Odstraňte vztah, kde "Alice" sleduje "Boba"
8. Najděte 5 uživatelů s největším počtem sledujících.
9. Najděte uživatele, kteří komentovali příspěvek jiného uživatele, a zobrazte obsah příspěvku.

**Řešení úkolu 1**
Vyhledejte prvních 10 uživatelů v databázi.
```cypher
MATCH (u:User)
RETURN u
LIMIT 10;
```

**Řešení úkolu 2**
Najděte všechny uživatele, kteří žijí v nějakém vybraném městě.
```cypher
MATCH (u:User {location: "New Staceyview"})
RETURN u;
```

**Řešení úkolu 3**
Vytvořte vztah, kde "Alice" sleduje "Boba".
```cypher
MERGE (a:User {name: "Alice"}) ON CREATE SET a.age = 30, a.location = "Not specified"
MERGE (b:User {name: "Bob"}) ON CREATE SET b.age = 30, b.location = "Not specified"
MERGE (a)-[:FOLLOWS]->(b);
```
A prohlédnutí úspěšného dotazu.
```cypher
MATCH (a:User {name: "Alice"}), (b:User {name: "Bob"})
RETURN a, b;
```

**Řešení úkolu 4**
Zobrazte 5 uživatelů s největším počtem příspěvků.
```cypher
MATCH (u:User)-[:CREATED]->(p:Post)
RETURN u, COUNT(p) AS num_posts
ORDER BY num_posts DESC
LIMIT 5;
```

**Řešení úkolu 5**
Zobrazte prvních 10 vztahů, kde jeden uživatel sleduje jiného
```cypher
MATCH (u1:User)-[f:FOLLOWS]->(u2:User)
RETURN u1, f, u2
LIMIT 10;
```

**Řešení úkolu 6**
Zobrazte 10 příspěvků a jejich komentáře
```cypher
MATCH (p:Post)<-[:ON]-(c:Comment)
RETURN p, COLLECT(c) AS comments
LIMIT 10;
```

**Řešení úkolu 7**
Odstraňte vztah, kde "Alice" sleduje "Boba"
```cypher
MATCH (a:User {name: "Alice"})-[f:FOLLOWS]->(b:User {name: "Bob"})
DELETE f;
```

A prohlédnutí úspěšného dotazu.
```cypher
MATCH (a:User {name: "Alice"}), (b:User {name: "Bob"})
RETURN a, b;
```

**Řešení úkolu 8**
Najděte 5 uživatelů s největším počtem sledujících
```cypher
MATCH (u:User)<-[:FOLLOWS]-(follower:User)
RETURN u, COUNT(follower) AS num_followers
ORDER BY num_followers DESC
LIMIT 5;
```

**Řešení úkolu 9**
Najděte uživatele, kteří komentovali příspěvek jiného uživatele, a zobrazte obsah příspěvku
```cypher
MATCH (u1:User)-[:COMMENTED]->(c:Comment)-[:ON]->(p:Post)<-[:CREATED]-(u2:User)
WHERE u1 <> u2
RETURN u1.name AS commenter, u2.name AS post_owner, p.content AS post_content;
```

#### C4.4 - Pokročilé dotazy
Vyzkoušejte si následující složitější dotazy s využitím knihovny APOC a GDS. Aby Vám knihovny fungovaly, musíte si je nainstalovat/aktivovat. Budeme používat knihovny APOC a GDS. Do docker-compose musíte přidat do ENV proměnných aktivované moduly:
```
version: '3.8'

services:
  python-app:
    build: .
    container_name: python-app
    depends_on:
      neo4j:
        condition: service_healthy

  neo4j:
    image: 'neo4j:latest'
    ports:
      - '7474:7474'
      - '7687:7687'
    environment:
      NEO4J_AUTH: 'neo4j/adminpass'
      NEO4J_PLUGINS: '["apoc", "graph-data-science"]'
    healthcheck:
      test: cypher-shell --username neo4j --password adminpass 'MATCH (n) RETURN COUNT(n);' # Checks if neo4j server is up and running
      interval: 10s
      timeout: 10s
      retries: 5
```

**Úkoly:**
1. Vytvořte vztah "KNOWS" mezi dvěma uživateli pomocí APOC procedury, kde vztah má atribut "since" a jeho význam je, že se znají od nějakého roku.
2. Rozdělete uživatele do věkových skupin po deseti letech a spočítejte, kolik příspěvku v každé skupině bylo vytvořeno
3. Zobrazte příspěvky s počtem komentářů a průměrným věkem uživatelů, kteří je komentovali.
4. Pomocí APOC vytvořte vztah "SHARED_FOLLOW" mezi uživateli, kteří sledují stejného uživatele.
5. Konsolidujte uživatele podle jejich lokace a zkombinujte vlastnosti.
6. Spočítejte celkový počet interakcí každého uživatele a zobrazte 5 nejaktivnějších uživatelů.
7. Použijte apoc.periodic.iterate pro iteraci uživatelů a aktualizaci atributu active v dávkách po 50, což simuluje efekt transakce a škálované zpracování.
8. Pomocí GDS knihovny vypočítejte PageRank pro uživatele a zobrazte 5 uživatelů s nejvyšším skóre, což jsou ti, kteří mají největší vliv v grafu na základě vztahu "FOLLOWS".
9. Použijte Louvain algoritmus k detekci komunit mezi uživateli.
10. Pomocí Dijkstra algoritmu vypočítejte nejkratší cestu mezi dvěma uživateli.
11. Spočítejte betweenness centrality pro uživatele a zobrazte 5 nejvlivnějších uživatelů.
12. Pomocí Jaccard Similarity zjistěte, kteří uživatelé mají nejpodobnější sledující.
13. Pomocí Harmonic Centrality zjistěte, kteří uživatelé jsou nejvíce propojení v rámci sítě.
14. Pomocí Label Propagation algoritmu zjistěte, do kterých komunit uživatelé patří.


**Řešení úkolu 1**
Vytvořte vztah "KNOWS" mezi dvěma uživateli pomocí APOC procedury, kde vztah má atribut "since" a jeho význam je, že se znají od nějakého roku.

Jelikož nám generátor asi nevytvořil Alice a Boba nebo jsme si předchozí uzly smazali, tak si je vytvoříme znovu.
```cypher
CREATE (a:User {name: "Alice"});
CREATE (b:User {name: "Bob"});
```

Provete tvorbu vztahu pomocí APOC knihovny.
```cypher
MATCH (a:User {name: "Alice"}), (b:User {name: "Bob"})
CALL apoc.create.relationship(a, "KNOWS", {since: 2023}, b) YIELD rel
RETURN rel
```

Ověříme existenci vztahu.
```
MATCH (a:User {name: "Alice"})-[r:KNOWS]->(b:User {name: "Bob"})
RETURN a, r, b
```

**Řešení úkolu 2**
Rozdělete uživatele do věkových skupin po deseti letech a spočítejte, kolik příspěvku v každé skupině bylo vytvořeno pomocí APOC partition.
```cypher
MATCH (u:User)-[:CREATED]->(p:Post)
WITH (u.age / 10) * 10 AS age_group, COUNT(p) AS num_posts
RETURN age_group, SUM(num_posts) AS total_posts
ORDER BY age_group
```

**Řešení úkolu 3**
Zobrazte příspěvky s počtem komentářů a průměrným věkem uživatelů, kteří je komentovali.
```cypher
MATCH (p:Post)<-[:ON]-(c:Comment)<-[:COMMENTED]-(u:User)
WITH p, COUNT(u) AS num_comments, AVG(u.age) AS avg_age
RETURN p.content AS post_content, num_comments, avg_age
ORDER BY num_comments DESC
LIMIT 10
```

**Řešení úkolu 4**
Pomocí APOC vytvořte vztah "SHARED_FOLLOW" mezi uživateli, kteří sledují stejného uživatele.
```cypher
MATCH (u1:User)-[:FOLLOWS]->(u:User)<-[:FOLLOWS]-(u2:User)
WHERE u1 <> u2
CALL apoc.create.relationship(u1, 'SHARED_FOLLOW', {}, u2) YIELD rel
RETURN u1.name, u2.name
LIMIT 10
```

Ověřím, že se povedlo.
```
MATCH (u1:User)-[:SHARED_FOLLOW]->(u2:User)
MATCH (u1)-[:FOLLOWS]->(u:User)<-[:FOLLOWS]-(u2)
RETURN u1.name AS follower1, u2.name AS follower2, u.name AS sharedFollowedUser
LIMIT 10
```

**Řešení úkolu 5**
Konsolidujte pomocí knihovny APOC a příkazu refactor.mergeNodes uživatele podle jejich lokace a zkombinujte vlastnosti. Konsolidace je proces sloučení uzlů se shodnou hodnotou vybraného atributu (v tomto případě lokace). Tato úloha je v praxi důležitá pro slučování duplicitních uzlů. Pro ověření funkčnosti přejmenuju uzly podle konsolidovaného atributu - lokace.

```cypher
MATCH (u:User)
WITH u.location AS loc, COLLECT(u) AS users
CALL apoc.refactor.mergeNodes(users, {properties: "combine"}) YIELD node
SET node.name = loc
RETURN node
```

**Řešení úkolu 6**
Spočítejte celkový počet interakcí každého uživatele a zobrazte 5 nejaktivnějších uživatelů. Pro správné počítání musíme použít OPTIONAL MATCH namísto MATCH. MATCH by vynechal uživatele, kteří nemají takový vztah vytvořený (nemají hranu daného typu). OPTINAL MATCH je nevynechá a dá jim šanci získat své počty interakcí v jiné kategorii (tím myslím post, koment, follow).

```cypher
MATCH (u:User)
OPTIONAL MATCH (u)-[:CREATED]->(p:Post)
WITH u, COUNT(p) AS post_count
OPTIONAL MATCH (u)-[:COMMENTED]->(c:Comment)
WITH u, post_count, COUNT(c) AS comment_count
OPTIONAL MATCH (u)-[:FOLLOWS]->(f:User)
WITH u, post_count, comment_count, COUNT(f) AS follow_count
RETURN u.name, (post_count + comment_count + follow_count) AS total_interactions
ORDER BY total_interactions DESC
LIMIT 5
```

**Řešení úkolu 7**
Použijte apoc.periodic.iterate pro iteraci uživatelů a aktualizaci atributu active v dávkách po 50, což simuluje efekt transakce a škálované zpracování.
```cypher
CALL apoc.periodic.iterate(
  "MATCH (u:User) RETURN u",
  "SET u.active = true",
  {batchSize: 50, iterateList: true}
) YIELD batches, total
RETURN batches, total
```

Můžeme spočítat, jestli se opravdu provedl příkaz u dávky uživatelů. Číslo by mělo odpovídat velikosti dávky (tedy pokud máte dostatek uživatelů).
```
MATCH (u:User)
WHERE u.active = true
RETURN COUNT(u) AS active_users
```

**Řešení úkolu 8**
Pomocí algoritmu PageRank (příkaz pageRanek.stream) z knihovny GDS zjistěte, kteří uživatelé mají největší vliv v grafu na základě vztahu "FOLLOWS". Budete si muset nejprve vytvořit grafovou projekci příkazem graph.project.cypher.

PageRank je algoritmus původně navržený k hodnocení webových stránek na základě počtu a kvality odkazů. PageRank přiřazuje každému uzlu skóre, které odráží jeho „důležitost“ na základě toho, kolik a jaké uzly na něj směřují. V případě sociálních sítí (např. User a FOLLOWS) by PageRank skóre určilo, kteří uživatelé jsou „vlivnější“ nebo více propojení.

Grafová projekce je dočasná struktura, která slouží k optimalizaci výpočtů grafových algoritmů. Projekce vytváří pohled na data v databázi bez nutnosti změny nebo kopírování původních dat.

Vytvořil jsem grafovou projekci s názvem userGraph (jméno potřebujeme pro pageRank), která vyhledá všechny uživatele a jejich vztahy typu FOLLOWS. Tyto informace potřebuje PageRank algoritmus.

```cypher
CALL gds.graph.project.cypher(
  'userGraph',
  'MATCH (u:User) RETURN id(u) AS id',
  'MATCH (u1:User)-[:FOLLOWS]->(u2:User) RETURN id(u1) AS source, id(u2) AS target' 
)
```

Zde aplikuji PageRank algoritmus na projekci userGraph a vrátím top5 uživatelů s nejvyšším PageRank skórem a jména těchto vlivných uživatelů. MaxIterations říká, kolikrát se má algoritmus opakovat (je tam stochasticita, tak chceme opakovat kvůli statistice). DampingFactor ovlivňuje stochasticitu. Jedná se o pravděpodobnost, že uživatel klikne na další odkaz (u webových stránek). V našem kontextu to znamená, že půjdeme na další napojený uzel. Pokud je DampingFactor 0.85, tak uživatel na 85 % bude následovat hranu do dalšího uzlu a na 15 % přejde na náhodný jiný uzel (na webu odkaz).

```cypher
CALL gds.pageRank.stream('userGraph', {
  maxIterations: 20,
  dampingFactor: 0.85
})
YIELD nodeId, score
RETURN gds.util.asNode(nodeId).name AS user, score
ORDER BY score DESC
LIMIT 5
```

Grafovou projekci můžeme po dokončení hraní si odstranit ať nezabírá zbytečně paměť (u veledat to může být opravdu velký problém).
```
CALL gds.graph.drop('userGraph')
```

**Řešení úkolu 9**
Použijte Louvain algoritmus k detekci komunit mezi uživateli. Cílem je najít skupiny uzlů (nebo komunit), které mají mezi sebou více spojení než s uzly mimo jejich skupinu. Tento algoritmus se často využívá v sociálních sítích, kde může odhalit například skupiny přátel nebo skupiny uživatelů s podobnými zájmy a nákupními preferencemi (doporučovací systémy). Matematicky využívá princip výpočtu modularity (míry kvality komunitní struktury), jejíž hodnotu se snaží algoritmus maximalizovat přesouváním uzlů mezi komunitami. Uzly jsou slučovány do větších komunit, dokud se modularita dále nezvyšuje.

Opět si vytvoříme stejně jako v předešlém cvičení grafovou projekci.
```cypher
CALL gds.graph.project(
  'userGraph',
  'User',
  'FOLLOWS'
)
```

Teď již můžeme spoustit Louvain algoritmus nad vytvořenou projekcí. V YIELD zadáme, že chcem vrátit z algoritmu ID uzlu a ID komunity, do které ho algoritmus zařadil. V RETURN pak uvedeme, že chcem převést ID uzlu na uzel v naší databázi.
```cypher
CALL gds.louvain.stream('userGraph')
YIELD nodeId, communityId
RETURN gds.util.asNode(nodeId).name AS user, communityId
ORDER BY communityId
LIMIT 5
```

Projekci můžeme posléze smazat pro uvolnění paměti.
```cypher
CALL gds.graph.drop('userGraph')
```

**Řešení úkolu 10**
Pomocí Dijkstra algoritmu vypočítejte nejkratší cestu mezi dvěma uživateli. 

Nejprve si zjistíme jména v našich uzlech.
```cypher
RETURN n.name AS name
```

Následně musím vytvořit grafovou projekci.
```cypher

```

Teď mohu vybrat konkrétní jména a zavolat z GDS Dijkstrův algoritmus (je i v APOC).
```cypher
MATCH (start:User {name: 'Chelsea Harrington'}), (end:User {name: 'Russell Sanchez'})
CALL gds.shortestPath.dijkstra.stream({
  sourceNode: id(start),
  targetNode: id(end),
  relationshipWeightProperty: 'weight'
})
YIELD totalCost, path
RETURN totalCost, path
```

Projekci můžeme posléze smazat pro uvolnění paměti.
```cypher
CALL gds.graph.drop('userGraph')
```

**Řešení úkolu 11**
Spočítejte betweenness centrality pro uživatele a zobrazte 5 nejvlivnějších uživatelů.
```cypher
CALL gds.betweenness.stream({
  nodeProjection: 'User',
  relationshipProjection: 'FOLLOWS'
})
YIELD nodeId, score
RETURN gds.util.asNode(nodeId).name AS user, score
ORDER BY score DESC
LIMIT 5
```

**Řešení úkolu 12**
Pomocí Jaccard Similarity zjistěte, kteří uživatelé mají nejpodobnější sledující.
```cypher
CALL gds.nodeSimilarity.stream({
  nodeProjection: 'User',
  relationshipProjection: 'FOLLOWS',
  similarityCutoff: 0.5
})
YIELD node1, node2, similarity
RETURN gds.util.asNode(node1).name AS user1, gds.util.asNode(node2).name AS user2, similarity
ORDER BY similarity DESC
LIMIT 10
```

**Řešení úkolu 13**
Pomocí Harmonic Centrality zjistěte, kteří uživatelé jsou nejvíce propojení v rámci sítě.
```cypher
CALL gds.alpha.closeness.stream({
  nodeProjection: 'User',
  relationshipProjection: 'FOLLOWS'
})
YIELD nodeId, centrality
RETURN gds.util.asNode(nodeId).name AS user, centrality
ORDER BY centrality DESC
LIMIT 5
```

**Řešení úkolu 14**
Pomocí Label Propagation algoritmu zjistěte, do kterých komunit uživatelé patří.
```cypher
CALL gds.labelPropagation.stream({
  nodeProjection: 'User',
  relationshipProjection: 'FOLLOWS'
})
YIELD nodeId, communityId
RETURN gds.util.asNode(nodeId).name AS user, communityId
ORDER BY communityId
```

#### C4.5 - Dashboard/Report v Pythonu

Vytvořte datový dashboard nebo nějakou jednoduchou přehledovou tabulku v Pythonu. Nemusíte to být vzhledné a nemusíte vizualizovat všechny získané informace. Cílem je pouze vyzkoušet si volání CQL dotazů v Pythonu. 

