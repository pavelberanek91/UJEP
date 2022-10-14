# NoSQL databázové systémy

**Obsah přednášky 1**:
1. Vymezení a cíle NoSQL databázových systémů

**Obsah cvičení 1**:
* Co jsou to NoSQL databáze
* BASE model konzistence
* Veledata

## On-site cvičení 1

### Cognitive apprenticeship

### Úkol OS1.1 NoSQL Databáze:

Databáze je množina dat, která má určitý formát (tabulka, slovník, XML soubor). Tyto databáze spravujeme pomocí aplikací, kterým se říká systémy řízení báze dat (anglicky database management systems, DBMS). Existují dvě hlavní kategorie DBMS:
* SQL
* NoSQL

SQL DBMS jsou typické tím, že databáze představuje tabulky, které mají mezi sebou určitý vztah (relaci). Do tabulek zaznamenáváme informace (atributy) o reálných objektech v našem světě (entity). Atributy entit je možné rozdělit do více tabulek. Jeden řádek v tabulce se nazývá záznam. Z toho vyplývá jeden určitý problém, že entita je rozprostřená mezi tabulkami a musíme ji skládat zpět. To napovídá, že by bylo vhodnější určité problémy řešit jiným modelem databází. NoSQL DBMS jsou řešením některých problému tradičních SQL databází.

Mezi nejpoužívanější NoSQL DBMS patří:
1. Redis: klíč-hodnota orientovaná DB
2. MongoDB: dokumentově orientovaná DB
3. Apache Cassandra: sloupcově orientovaná DB
4. Neo4J: grafově orientovaná DB

### Úkol OS1.2 CAP teorém (Eric Brewer):

CAP teorém tvrdí, že není možné, aby DBMS plnil všechny z následujících tří vlastností:
1. Consistency - všichni vidí ve stejném čase stejná data
2. Availability - systém operuje i tehdy, dojde-li k výpadku serveru
3. Partititon Tolerance - systém operuje i tehdy, dojde-li k přeřušení spojení serverů

Konzistence v CAP teorému představuje splnění linearizovatelnosti operací. Mějme 2 transakce A a B. Nejprve se úspěšně provede transakce A a poté se provede transakce B. Pokud je DBMS konzistentní, pak transakce B vidí taková data, jaká měla na svém výstupu transakce. Konzistence je typický pro SQL DBMS. 

Availability v CAP teorému představuje dostupnost v případě požadavku. Každá databáze, která neselhala (server s instancí DB běží), tak musí při mém požadavku úkol provést. 

Partition Tolerace v CAP teorému představuje odolnost pri chybám v síti, kdy se přeruší propojení serverů.

Důkaz CAP teorému spočívá v následující úvaze. Představme si, že máme dva servery a na nich bězí dvě kopie databáze. Jeden server je například v Americe a druhý v Evropě. Tyto servery si spolu vyměňují data, jakmile někdo provede na jednom z nich transakci. Jsou tedy konzistentní. Pak nastane problém a jejich spojení se přeřuší. Servery dále běží, avšak již si nemohou zaslat transakce, které způsobí jejich konzistenci. V takovém případě jsou dvě možnosti, jak se situací vypořádat:
1. Aplikace budou i nadále dostupné a odolné proti výpadkům, jen bude každý server mít trošku jiná data od doby výpadku propojení.
2. Aplikace se musí zastavit a počkat, než se propojení obnoví, ať neztratíme konzistenci dat. Tím přestává být systém dostupný.


Podle těchto písmen rozdělujeme DBMS do tří kategorií:
* AP = Tyto DB jsou v případě síťového přerušení stále k dispozici, ačkoliv některé servery mají stará data (nekonzistentní). Po obnovení spojení se data dostávají do konzistentního stavu. Př.: Apache Cassandra, CouchDB
* CP = Tyto DB zůstavají v případě síťového přerušení konzistentní, avšak ne všechny servery jsou dostupné. DBMS musí odpojený server vypnout. Po přopojení si konzistenci obnoví od ostatních Př.: MongoDB, Redis
* CA = Tyto DB nemohou z principu být P-tolerantní, jelikož nelze v případě síťového výpadku zajistit, že se do pevného disku uloží všude stejná data. Jedná se tedy pouze o nesíťové DB, kde není co přerušovat (takže klasické DB). Př.: MariaDB, MS SQL Server, SQLite3

### Úkol OS1.3 ACID vs. BASE:

Hlavní vlastnost, která odlišuje SQL a NoSQL databáze od sebe je model konzistence dat. SQL používají model ACID, kde je hlavní důraz kladen na integritu dat. NoSQL databáze používají model konzistence BASE, kde je primární vlastností dostupnost dat.

Model konzistence ACID:
* A (Atomicity) = Transakce dat je atom komunikace s DB. Pokud transakce selže, tak se pomocí mechanismu rollbacku navrací DB do předchozího stabilního stavu.
* C (Consistence) = Po provedení transakce máme jistotu, že data budou splňovat integritní omezení (správné datové typy, dodržení relací, atd.).
* I (Isolation) = Transakce jsou vzájemně izolované. DBMS zařídí jejich sekveční provedení.
* D (Durability) = Po provedení transakce jsou data nevolatilně zapsána do DB a navrát do předchozího stavu se musí dělat z logů o transakcích.

Model konzistence BASE:
* BA (Basic Availability) = Data jsou vysoce dostupná, kdykoliv je uživatel potřebuje. Nedostupná mohou být jen v případě, kdy celý systém (několik serverů) selže naráz.
* S (Soft State) = Data uložená v distribuovaném systému serverů se mohou lišit. Hodnoty atributu entity nejsou napříč systémem konzistentní.
* E (Eventual Constistency) = Data nemusí být v daném čase konzistentní, ale po nějaké době/události nakonec budou konzistentní. Taková událost je třeba požadavek na čtení dat (něž ale někdo požádá, tak nemusí být).

### Úkol OS1.4 Škálovatelnost:

Škálovatelností rozumíme schopnost systému přizpůsobit se požadovanému objemu požadavků. Základní způsoby škálovatelnosti jsou:
1. vertikální škálování: zvyšování výpočetních prostředků serveru (více RAM, lepší nebo více CPU, větší pevný disk)
2. horizontální škálování: zvyšování počtu serverů

Vertikální škálování začně být od určitého požadavku na objem požadavků finančně neúnosný a možná i nereálné k provedení na hardwaru aktuální doby. To může představovat velký problém pro SQL databáze, kde víceméně jediný způsob jak provést škálování je vertikální škálování. NoSQL databáze oproti SQL databázím nemají problém s horizontálním škálováním a cíleně využívají tohoto škálování pro zajištění vysoké dostupnosti dat.

NoSQL databáze jsou speficiké svým modelem konzistence BASE, kde je primární dostupnost dat. V případě výpadku server s DB musí existovat mechanismus, který vrátí data, ačkoliv nemusí být integritní.
1. Duplication: databáze je rozkopírovaná mezi více serverů a v případě výpadku jednoho se používá druhý se zálohou
2. Sharding: databáze je rozdělena mezi více serverů a v případě výpadku jednoho nedostane uživatel všechna data v celistvé podobně (není integrita), ale nějaká přeci jen dostane

Sharding lze provádět dvěma způsoby. Představme si DB v modelu obyčejné tabulky (jako například tabulka z aplikací tabulkových kalkulátorů):
1. vertikální sharding: sloupce tabulek jsou rozděleny do více databází, tím se zaručí, že v případě výpadku jsou dostupné všechny entity, avšak jejich informace budou omezené
2. horizontální sharding: řádky tabulek jsou rozděleny do více databází, tím se zaručí, že v případě výpadku jsou dostupné alespoň některé entity se všemi svými atributy

### Úkol OS1.5 Veledata:

Veledata představují velký problém v oblasti datový analýzy. Jedná se o data, kde práce s nima představuje problém sám o sobě. Taková data jsou typická svými V-vlastnostmi:
1. Volume: veledata jsou natolik objemná, že klasické DB nestačí
2. Velocity: veledata přicházejí tak rychlé, že klasické DB nestačí nebo jsou zbytečné
3. Variety: veledata přicházejí v různých formátech, že práce v klasické DB by byla integritně náročná
4. Valence: veledate mají variabilní počet relací, který se v čase mění nebo narůstají s každým záznamem

Někteří autoři k těmto V-vlastnostem přidávají řadí další vlastnosti (například Veracity), avšak nám budou stačit tyto. Jedná se tedy především o data z různých IoT (internet of things) zařízení jako jsou chytré senzory a telefony, u kterých ve velmi krátkém čase musíme zpracovat velký objem dat různého charakteru a relace mezi daty jsou variabilní. Z toho vyplývá, že musíme sáhnout právě po nějakých speciálních databázích, kde je prioritní dostupnost, jestli chceme výsledky dat vůbec v reálném čase používat. Těmi jsou právě NoSQL databáze.

DB pro veledata se v oboru business inteligence různě nazývají. Pojďme se na nějaké definice podívat:
1. Data ocean: jedná se o všechna možná data, které jsme schopni získat z různých zdrojů 
2. Data lake: jedná se o data z oceánu, které víme, že budeme potřebovat a čistíme je algoritmy
3. Data swamp: to samé jako jezero, jen je nečistíme, čímž si zhoršímu schopnost je využít
4. Data pond: jedná se o data, která budeme v brzké době potřebovat a proto jsou značně očištěna
5. Data puddle: jedná se o data, která zrovna teď potřebujeme a jsou očištěna - připravena 
6. Data warehouse: jedná se o skladiště dat s danou strukturou (např.: ve formě SQL tabulek)
7. Data market: funkcionálně ohraničený sklad (data jen pro logistiku nebo účetnictví, atd.)
8. Data cube (OLAP): tří dimenzionální struktura z dat marketu, která se řeže v osách
9. Data report: výsledek řezů OLAP kostky nebo jiných dat z tržiště

Přechod mezi strukturami se provádí pomocí tzv. ETL transformací (extract-transform-load). Jedná se o tři činnosti, které je nutné s datama vždy provést. Extract vezme z jedné DB data, která nás zajímají. Transform je přemění do podoby pro následnou databázi. Load je nahraje do následné databáze.

Je nutné zmínit, že velkou roli hraje strojové učení. Intenzivně se zkoumají algoritmy, které dokáží z datových oceánů najít data, která nás budou zajímat, nebo hledat mezi daty z jezera zajimavé souvislosti, které bychom jako lidé nenašli.

## Domácí cvičení 1

Pročtěte si následující tutoriály, ať se lépe konzulte příští lekce NSQL kurzu, kde si probereme strukturu Flask aplikací.

### Úkol HW1.1 Flask:

Flask je microframework pro vývoj webových aplikací v jazyce Python. Oproti například frameworku Django se jedná o jen to nejmenší nutné, aby python šlo využít pro tvorbu webových aplikací. Vytvořte si projekt ve vašem oblíbeném editoru, vytvořte virtuální prostředí v jazyce Python a balíčkovacím systémem pip si nainstalujte Flask. 

Návod naleznete zde: [ZDE](https://flask.palletsprojects.com/en/2.2.x/installation/)

### Úkol HW1.2 Koncové body:

Webové aplikace využívají principu koncových bodů. V případě, že napíše uživatel do webového prohlížeče URL obsahující adresu serveru, tak může aktivovat určitý koncový bod dodáním symbolu lomítka a následně názvu koncového bodu. Koncový bod je v Pythonu realizován pomocí dekorátoru, který naslouchá na HTTP metody GET, POST, PUT, DELETE a spouští pythonovskou metodu. Tato metoda pak provádí již určitou službu. typicky při HTTP metodě GET vrátí nějakou webovou stránku, při HTTP metodě POST naopak nahrává uživatel data z formuláře do Pythonu, PUT a DELETE se používají jen u REST API aplikací.

Podívejte se na to, jak se koncové body vytvářejí: [ZDE](https://hackersandslackers.com/your-first-flask-application/)


### Úkol HW1.3 Šablony:

Při obdržení požadavku HTTP GET má webový server vracet nějakou webovou stránku. Těm se říká ve Flasku šablony, jelikož mohou obsahovat nějaká data z Pythonu. Tyto data dodáváme do stránky pomocí šablonovacího jazyku, kterým je v případě Flasku jazyk Jinja2. Šablony (webové stránky) ukládáme implicitně do složky templates v projektu Flask aplikace. Šablony mohou mít i své šablony, které jsou pak rozšiřované. 

Podívejte se na to, jak se tvoří a vrací šablony uživateli: [ZDE](https://hackersandslackers.com/flask-jinja-templates)

### Úkol HW1.4 Kaskádové styly:

Pokud bychom pro tvorbu šablon použili pouze jazyk HTML5, tak jsme sice vytvořili strukturu stránek, ale jejich vzhled by nebyl příliš lákavý. Řešením je využít kaskádových stylů. Psaní grafického návrhu stránky pomocí kaskádových stylů je náročné. Lepší je využít nějaký vhodný pracovní rámec pro styly jako je například W3.CSS nebo Bootstrap5. 

Podívejte se na to, jak dodat CSS do Flask aplikace: [ZDE](https://hackersandslackers.com/flask-assets)

Dále si projděte si tutoriál na Bootstrap5: [ZDE](https://blog.appseed.us/bootstrap-for-beginners-with-examples/)

### Úkol HW1.5 Přihlašovací formulář:

Jedním z prvních úkolů v projektu bude vytvořit přihlašovací systém, který bude využívat relační databázi pro správu uživatelů. Přihlašování bude probíhat pomocí formuláře. 

Podívejte se, jak se tvoří a zpracovává formulář: [ZDE](https://hackersandslackers.com/flask-wtforms-forms)

**Video týdne 1: Databázová paradigmata**

Pojďme si zopakovat znalosti z hodiny na youtubovém videu :) [ZDE](https://www.youtube.com/watch?v=W2Z7fbCLSTw)

**Video týdne 2: Docker**

Pro snadné používání databází v našem vývojářském ekosystému budeme používat aplikaci Docker. Podívejte se na následující video, které vás do Dockeru zasvětí. [ZDE](https://www.youtube.com/watch?v=gAkwW2tuIqE)
