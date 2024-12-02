# Datová úložiště a nástroje pro Big Data (KI/BIG)

## Seminář 7 - Spark a jeho moduly - MLlib, GraphX, Spark Streaming

https://www.analyticsvidhya.com/blog/2022/08/complete-guide-to-run-machine-learning-on-spark-using-spark-mllib/
https://github.com/Marcel-Jan/docker-hadoop-spark

### Samostudium

#### S7.1 - Apache Spark

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

#### S7.2 - Resilient Distributed Datasets (RDD)

RDD je jeden z nejdůležitějších konceptů Sparku. Představuje základní datovou strukturu Sparku, která je distribuovaná, nemutabilní a odolná proti selhání (fault-tolerant). Tato datová struktura obaluje datové sady, nad kterými je možné na různých uzlech provádět výpočty.

RDD vznikají dvěma způsoby:
1. paralelizací existující kolekce v Driver programu,
2. referencí na data v externím datovém úložišti (HDFS, HBase, Cassandra, Amazon S3).

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

#### S7.3 - MLlib

MLlib je knihovna strojového učení pro Apache Spark, která poskytuje škálovatelné a distribuované algoritmy strojového učení, nástroje a užitečné utility a je dostupná ihned po instalace Sparku. Je navržena tak, aby zjednodušila implementaci strojového učení na velkých datových souborech, které jsou distribuovány na výpočetním klastru jako je Hadoop. MLlib nabízí flexibilní API pro programování ve Scale, Pythonu, Javě i R, avšak není tak rozšířen jako využití modulů scikit-learn nebo tensorflow/pytorch ve světe strojového učení. Důvodem je i značnější složitost vlivem zamýšleném využití na výpočetním klastru.

MLlib podporuje následující typy ML algoritmů:
* Klasifikaci: Například logistická regrese, podpora vektorových strojů (SVM).
* Regresi: Lineární regrese, Lasso, Ridge regrese.
* Shlukování: K-means, Gaussian Mixture Models (GMM).
* Redukci dimenzionality: Principal Component Analysis (PCA), Singular Value Decomposition (SVD).
* Doporučovací systémy: Alternating Least Squares (ALS) pro doporučování na základě kolaborativního filtrování.
* Hodnocení modelů: Metody jako ROC křivky, přesnost, MSE, apod.

Následuje ukázka práce s modulem PySpark, který přes API volá Spark.

**Načtení dat:**
```
from pyspark.ml.linalg import Vectors
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("MLlibExample").getOrCreate()
data = [(Vectors.dense([0.0, 1.1, 0.1]), 1.0),
        (Vectors.dense([2.0, 1.0, -1.0]), 0.0),
        (Vectors.dense([2.0, 1.3, 1.0]), 1.0)]
df = spark.createDataFrame(data, ["features", "label"])
```

**Vytvoření a trénování modelu:**
```
from pyspark.ml.classification import LogisticRegression

lr = LogisticRegression(maxIter=10, regParam=0.01)
model = lr.fit(df)
```

**Predikce:**
```
predictions = model.transform(df)
predictions.show()
```

**Evaluace modelu:**
```
from pyspark.ml.evaluation import BinaryClassificationEvaluator

evaluator = BinaryClassificationEvaluator()
accuracy = evaluator.evaluate(predictions)
print(f"Accuracy: {accuracy}")
```


#### S7.4 - GraphX

GraphX je komponenta Apache Spark, která je navržena pro zpracování a analýzu grafových dat a využívá jako základní datové struktury RDD. Umožňuje manipulaci s orientovanými i neorientovanými grafy a provádění grafových algoritmů na distribuovaných datových sadách. Využívá výhod in-memory zpracování a distribuovaných výpočtů v rámci Spark ekosystému. Případy užití jsou totožné s MLlib, tedy využíváme v případech, kdy máme veledata na distribuovaném úložišti a potřebujeme provést výpočty. Pro malé grafy je lepší využít dedikované lokální moduly Pythonu, pro střední Neo4j (který je škálovatelný) a pro datově nejobjemnější případy práve GraphX.

Podporované algoritmy:
* Subgrafy: Vytváření podgrafů na základě filtrů.
* Join: Propojení grafů s dalšími daty.
* Transformace: Modifikace vrcholů a hran.
* PageRank: Hodnocení významu vrcholů v grafu.
* Connected Components: Detekce propojených komponent v grafu.
* Triangle Count: Počítání trojúhelníků (kliky o třech vrcholech).
* Shortest Path: Nejkratší cesta mezi uzly.

GraphX se používá primárně v Javě, avšak pokud chcete použít Python, tak existuje wrapper [GRAPHFRAMES](https://graphframes.github.io/graphframes/docs/_site/quick-start.html).
```
from graphframes import *

# Create a Vertex DataFrame with unique ID column "id"
v = sqlContext.createDataFrame([
  ("a", "Alice", 34),
  ("b", "Bob", 36),
  ("c", "Charlie", 30),
], ["id", "name", "age"])

# Create an Edge DataFrame with "src" and "dst" columns
e = sqlContext.createDataFrame([
  ("a", "b", "friend"),
  ("b", "c", "follow"),
  ("c", "b", "follow"),
], ["src", "dst", "relationship"])
# Create a GraphFrame
g = GraphFrame(v, e)

# Query: Get in-degree of each vertex.
g.inDegrees.show()

# Query: Count the number of "follow" connections in the graph.
g.edges.filter("relationship = 'follow'").count()

# Run PageRank algorithm, and show results.
results = g.pageRank(resetProbability=0.01, maxIter=20)
results.vertices.select("id", "pagerank").show()
```

#### S7.5 - Spark Streaming

Spark Streaming je modul Apache Spark navržený pro zpracování datových toků v reálném čase a je dostupný ihned po instalaci Sparku. Umožňuje analyzovat a zpracovávat data přicházející z různých zdrojů, jako jsou senzory, logy, sociální sítě, databáze nebo služby pro sběr dat. Namísto zpracování jednotlivých událostí v reálném čase Spark Streaming rozdělí tok dat do malých časových úseků (např. každých 1 sekundu). Spark Streaming je postaven na Spark Core a integruje se se Spark ekosystémem (např. Spark SQL pro dotazování se, GraphX pokud přicházejí grafová data, MLlib pro využití strojového učení nad daty přicházejícími v reálném čase).

Algoritmus práce Spark Streaming:
1. Příjem datového toku: Data jsou přijímána ze zdroje (např. Kafka, socket).
2. Transformace na DStream: Data jsou reprezentována jako DStream (Discretized Stream), což je sekvence RDD (Resilient Distributed Dataset).
3. Transformace a analýza: Operace na DStreamech (např. map, filter, reduce).
4. Výstup: Zpracovaná data mohou být uložena do HDFS, databáze nebo použita pro další analýzu.

```
from pyspark.streaming import StreamingContext
from pyspark import SparkContext

# Vytvoření Spark kontextu
sc = SparkContext("local[2]", "NetworkWordCount")
ssc = StreamingContext(sc, 1)  # Interval mikro-batch (1 sekunda)

# Přijetí datového toku ze socketu na portu 9999
lines = ssc.socketTextStream("localhost", 9999)

# Zpracování dat (počítání slov)
words = lines.flatMap(lambda line: line.split(" "))
wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

# Výstup výsledků do konzole
wordCounts.pprint()

# Spuštění streamingu
ssc.start()
ssc.awaitTermination()
```

### Cvičení

#### C7.1 - Tutoriál a zprovoznění ekosystému

Projděte si následující tutoriál a zprovozněte nástroje Spark a Graphx s případnými Python moduly pro Váš Hadoop docker-compose: [TUTORIAL](https://sparkbyexamples.com/pyspark-tutorial/). Vyzkoušejte si zmíněné příklady.

#### C7.2 - Vlastní projekt využívající ML pro klasifikaci

Nahrajte na HDFS nějaká data z Kaggle a zkuste si pomocí MLlib naučit model klasifikovat (například obrázky psů a koček).

#### C7.3 - Vlastní projekt využívající grafová data

Nahrajte na HDFS nějaká grafová data (můžete je nagenerovat) a zkuste si provést analýzu grafových dat pomocí nějakého algorimu z GraphX

#### C7.4 - Vlastní projekt využívající detekci odchylky v real-time datech

Vytvořte si nějaký real-time datový zdroj, který zasílá do Sparku data (například simulace teploty) a detekujte v datech odchylky s využitím Spark Streaming. Data může generovat skript, který dává data do databáze (můžete využít i Apache Kafka z tutoriálu) a s nějakou malou pravděpodobností vygeneruje do dávky statistickou odchylku. Statistickou odchylku můžete reprezentovat jako číslo větší než 3*sigma.

