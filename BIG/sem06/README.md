# Datová úložiště a nástroje pro Big Data (KI/BIG)

## Seminář 6 - Spark a jeho architektura

### Samostudium

https://www.oreilly.com/content/hadoop-with-python/
https://spark.apache.org/docs/latest/rdd-programming-guide.html


#### S6.1 - Apache Spark

Apache Spark je univerzální volatilní (in-memory) analytický engine pro distrubované zpracování veledat a provádění úkonů strojového učení. Jedná se o výkonnou platformu, která provádí operace nad veledaty zhruba 100x rychleji než tradiční Python. Zdrojem veledat může být Apache Hadoop, Amazon S3 server a mnoho dalších souborových systémů. Dále umožňuje zpracování dat z datových proudů (stream) v reálném čase z platformy Apache Kafka.

Architektura Sparku je realizována architektonickým vzorem master-slave. Master proces nazýváme ve Spark terminologii Driver a slave procesy nazýváme Workers. Úkolem Driveru je tvorba kontextu aplikace a řízení práce Workers, úkolem Workers je provádění všech transformačních operací. O výpočetní zdroje se stará tzv. Cluster Manager. Spark podporuje následující Cluster Managery:
1. Vlastní cluster manager Sparku - jednoduchý klastr samotného Sparku pro méně náročné úlohy,
2. Apache Mesos - univerzální cluster manager, ale je již deprecated,
3. Hadoop YARN - cluster manager pro Hadoop2 a Hadoop3,
4. Kubernetes - jeden z nejpoužívanějších orchestračních nástrojů.

<img src="cluster-overview.png" alt="Architecture Apache Spark klastru" />

Apache Spark má v sobě předpřipravené knihovny pro užitečné operace nad veledaty, tzv. Apache Spark Eco System. Mezi tyto knihovny patří:
1. Spark SQL
2. Spark Streaming
3. Spark MLlib
4. GraphX

Komunikace se Sparkem se provádí pomocí API, které nazýváme Apache Spark Core API. K tomuto API má Spark podporu pro následující jazyky:
1. Python
2. R
3. Java
4. Scala
5. SQL

Kromě toho je možné použít knihovny třetích stran, které naleznete [ZDE](https://spark-packages.org).

#### S6.2 - PySpark

PySpark je modul pro jazyk Python, který zprostředkovává API komunikaci se Sparkem.


#### S6.3 - Resilient Distributed Datasets (RDD)

RDD je jeden z nejdůležitějších konceptů Sparku. Představuje základní datovou strukturu Sparku, která je distribuovaná, nemutabilní a odolná proti selhání (fault-tolerant). Tato datová struktura obaluje datové sady, nad kterými je možné na různých uzlech provádět výpočty.

RDD vznikají dvěma způsoby:
1. paralelizací existující kolekce v Driver programu,
2. referencí na data v externím datovém úložišti (HDFS, HBase, Cassandra, Amazon S3).

#### S6.4 - RDD operace

RDD struktury podporují dva typy operací:
1. transformace - vytváří novou datovou sadu z existující,
2. akce - vrací hodnotu z výpočtu nad datovou sadu.

Všechna RDD operace se vyhodnocují liným způsobem, tedy až je zapotřebí výsledek. Do té doby si pouze pamatují, že se mají provést až bude potřeba. To vytváří vysokou výpočetní efektivitu Sparku.

Vybrané RDD transformace:
1. map(func) - vrátí novou datovou sadu, která vznikne aplikací mapovací funkce na prvky datové sady,
2. filter(func) - vrátí novou datovou sadu, která vznikne ,
3. join(other) - vrátí spojení dvou datových sad podle klíče na hashmapu uspořádaných ntic (tuple),
4. union(other) - vrátí spojení dvou datových sad do jedné,
5. intersection(other) - vrátí průnik dvou datových sad,
6. distinct(other) - vrátí datovou sadu obsahující rozdílné elementy ve dvou datových sadách,
7. cartesian(other) - vrátí datovou sadu všech možných párů hodnot ze dvou datových sad,
8. cogroup(other) - vrátí outer join dvou kolekcí ve formě iteratovatelných ntic, 
9. coalesce(npartitions) - sníží počet částí (partition) na zadaný počet za účelem zvýšení výkonu,
10. repartition(npartitions) - rozmíchá datovou sadu a rozdělí ji na zadaný počet částí, 

Vybrané RDD akce:
1. reduce(func) - přijme kumulativní asociativní funkce, která provede agregaci nad daty a vrátí výsledek agregace,
2. collect() - vrátí všechny data z datové sady ve formě pole do Driveru,
3. count() - vrátí počet datových položek v datové sadě,
4. first() - navrátí první element datové sady,
5. take(n) - navrátí pole n-prvních elementů datové sady,
6. takeSample(withReplacement, n) - navrátí s nahrádou nebo bez náhrady n položek náhodným výběrem,
7. countByKey() - vrátí hashmapu s frekvencí klíčů,
8. foreach(func) - aplikuje funkci na prvky datové sady, avšak umožňuje vedlejší efekty (update akumulátoru nebo interakce s externím úložištěm),
9. saveAsTextFile(path) - uloží datovou sadu do textového souboru,
10. saveAsSequenceFile(path) - uloží datovou sadu do formátu Hadoop SequenceFile

Tyto RDD akce lze optimalizovat několika způsoby:
1. výběr vhodné formy persistence - cachovaní datové sady do paměti uzlů pro následné operace,
2. sdílené proměnné - procesy ve Sparku mají vlastní kopie dat, avšak je možné využít sdílených proměnných ve formě akumulátorů a mechanismem broadcastu proměnných.

#### S6.5 - Apache Kafka

### Cvičení

#### C6.1 - Načtení externí datové sady

#### C6.2 - Analýza dat pomocí RDD operací

#### C6.3 - Optimalizace operací

#### C6.4 - Tvorba reportu

#### C6.5 - Analýza streamu

### Domácí úkoly

#### D6.1 - lorem

#### D6.2 - lorem

#### D6.3 - lorem

#### D6.4 - lorem

#### D6.5 - lorem
