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

1. Zprovozněte si prostředí Sparku, nejprve zvlášť a zkuste si nějaký hello-world příklad. 
2. Integrujte Spark do Vašeho stávajícího Hadoop ekosystému pro využívání dat z HDFS. Vyzkoušejte na příkladu, kdy vstupní data jsou uložena v HDFS.
3. Volitelně - zprovoznění do Kubernetes klastru

Nápomocné tutoriály:
* [SPARKBYEXAMPLES - SPARK V DOCKER-COMPOSE](https://sparkbyexamples.com/pyspark-tutorial)
* [MEDIUM - SPARK V DOCKER-COMPOSE](https://medium.com/@SaphE/testing-apache-spark-locally-docker-compose-and-kubernetes-deployment-94d35a54f222)
* [MEDIUM - SPARK LOKÁLNĚ](https://medium.com/@marcelopedronidasilva/how-to-install-and-run-pyspark-locally-integrated-with-vscode-via-jupyter-notebook-on-windows-ff209ac8621f)
* [MEDIUM - SPARK KUBERNETES](https://medium.com/@SaphE/deploying-apache-spark-on-a-local-kubernetes-cluster-a-comprehensive-guide-d4a59c6b1204)

**Řešení Docker-compose**
Mé řešení vzniklo na základě druhého tutoriálu MEDIUM - SPARK V DOCKER-COMPOSE. Neprve vytvoříme adresář s názvem `docker-compose-way`, do kterého uložíme všechny potřebné soubory pro běh Spark klastru.

Prvním souborem v adresáři bude Dockerfile s následujícím obsahem.
```Dockerfile
# Základní Java obraz, ze kterého vyjdeme, jelikož budeme později odkazovat na tento obraz, tak mu dáme kratší alias
FROM openjdk:11.0.11-jre-slim-buster as builder

# Instalace všech závislostí včetně Pythonu a jeho modulů (numpy, scipy, matplotlib) pro PySpark, ssh a net-tools pro komunikaci mezi Spark uzly a curl a wget pro stahování dodatečných souborů
RUN apt-get update && apt-get install -y curl vim wget software-properties-common ssh net-tools ca-certificates python3 python3-pip python3-numpy python3-matplotlib python3-scipy python3-pandas python3-simpy

# Vytvoření aliasu python pro python3 (skutečná binárka) pro zajištění kompatibility skritpů, volající python3 pod aliasem python
RUN update-alternatives --install "/usr/bin/python" "python" "$(which python3)" 1

# Potřebné konstanty pokud využíváme Python 3.3 a větší - verze Sparku, verze Hadoopu, kořenový adresář kam se Spark nainstaluje a fixní seed pro paralelní zpracování dat
ENV SPARK_VERSION=3.4.0 \
HADOOP_VERSION=3 \
SPARK_HOME=/opt/spark \
PYTHONHASHSEED=1

# Stáhnutí a rozbalení Sparku do adresáře /opt/spark
RUN wget --no-verbose -O apache-spark.tgz "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" \
&& mkdir -p /opt/spark \
&& tar -xf apache-spark.tgz -C /opt/spark --strip-components=1 \
&& rm apache-spark.tgz


# Obalíme částečně sestrojený obraz dalším kódem a dáme nové vrstvě alias apache-spark
FROM builder as apache-spark

# Nastavení pracovního adresáře
WORKDIR /opt/spark

# Nastavení portů Sparku, adresářů pro logy Master a Workerů, URI pro Spark Mastera a typ uzlu jako Master (může být ještě Worker)
ENV SPARK_MASTER_PORT=7077 \
SPARK_MASTER_WEBUI_PORT=8080 \
SPARK_LOG_DIR=/opt/spark/logs \
SPARK_MASTER_LOG=/opt/spark/logs/spark-master.out \
SPARK_WORKER_LOG=/opt/spark/logs/spark-worker.out \
SPARK_WORKER_WEBUI_PORT=8080 \
SPARK_WORKER_PORT=7000 \
SPARK_MASTER="spark://spark-master:7077" \
SPARK_WORKLOAD="master"

# Odhalené porty: 8080 = webové UI Masteru, 7077 = Port pro komunikaci s Masterem, 6066 = pro REST API Spark Mastera
EXPOSE 8080 7077 6066

# Vytvoření logovacích adresářů a nastavení výpisů na standardní výstup z důvodu viditelnosti v Docker logu
RUN mkdir -p $SPARK_LOG_DIR && \
touch $SPARK_MASTER_LOG && \
touch $SPARK_WORKER_LOG && \
ln -sf /dev/stdout $SPARK_MASTER_LOG && \
ln -sf /dev/stdout $SPARK_WORKER_LOG

# Spouštěcí skript, který představuje vstupní bod kontejneru.
COPY start-spark.sh /

CMD ["/bin/bash", "/start-spark.sh"]
```

Následně vytvoříme skript, který bude sloužit jako vstupní bod klastru při spuštění (byl na konci předchozího Dockerfilu). Skript slouží ke spouštění klastrů (vstupní bod) a rozlišuje nastavení uzlu podle proměnné SPARK_WORKLOAD.
```start-spark.sh
#start-spark.sh
#!/bin/bash

# Načte proměnné prostředí ze souboru load-spark-en.sh, který je součástí instalace Sparku. Jsou v něm defaultní cesty jako SPARK_HOME.
. "/opt/spark/bin/load-spark-env.sh"

# Pokud je uzel nastaven na úlohu Master
if [ "$SPARK_WORKLOAD" == "master" ];
then
# nastaví hosta na sebe (aktuální uzel je Master)
export SPARK_MASTER_HOST=`hostname`
# spustí Master proces (Java třída), nastaví IP adresu na hostname, port a web UI port a přesměruje výstup do logovacího souboru
cd /opt/spark/bin && ./spark-class org.apache.spark.deploy.master.Master --ip $SPARK_MASTER_HOST --port $SPARK_MASTER_PORT --webui-port $SPARK_MASTER_WEBUI_PORT >> $SPARK_MASTER_LOG

# Pokud je uzel nastaven na úlohu Worker
elif [ "$SPARK_WORKLOAD" == "worker" ];
# spustí Worker proces (Java třída), nastaví web UI port Workeru, URI na Master a přesměruje výstup do logovacího souboru
cd /opt/spark/bin && ./spark-class org.apache.spark.deploy.worker.Worker --webui-port $SPARK_WORKER_WEBUI_PORT $SPARK_MASTER >> $SPARK_WORKER_LOG

# Pokud je uzel nastaven na zasílání úloh do výpočetního klastru. V else je možnost rozšíření klastru o automatizované výpočty. Skript je připraven právě na takové situace, kdy existuje dedikovaný Submit uzel pro úlohy. Běžné je však pouštět úlohy na Masterovi.
elif [ "$SPARK_WORKLOAD" == "submit" ];
then
    echo "SPARK SUBMIT"
else
    echo "Undefined Workload Type $SPARK_WORKLOAD, must specify: master, worker, submit"
fi
```

Teď vytvoříme Docker obraz z Dockerfilu (musíme být ve složce docker-compose-way).
```bash
docker build -t our-own-apache-spark:3.4.0 .
```

Následně provedeme sestavení výpočetního klastr z jednoho hlavního Master uzlu a dvou výpočetního uzlů pomocí Docker-compose.
```docker-compose.yml
version: "3.3"
services:
  spark-master: #tvorba kontejneru, který bude Spark Master uzel
    image: our-own-apache-spark:3.4.0 #použijeme náš vlastní sestrojený obraz z minulých kroků
    ports:
      - "9090:8080" #webové rozhraní Sparku
      - "7077:7077" #port pro komunikaci Mastera s Workery
    volumes:
       - ./apps:/opt/spark-apps #vytvoření sdíleného adresáře mezi lokálním PC a kontejnerem Masteru pro naše aplikace
       - ./data:/opt/spark-data #vytvoření sdíleného adresáře mezi lokálním PC a kontejnerem Masteru pro data pro naše aplikace
    environment:
      - SPARK_LOCAL_IP=spark-master #IP adresa Spark služby je IP adresa Mastera
      - SPARK_WORKLOAD=master #nastavení typu úlohy na Master (pro spouštěcí skript)
  spark-worker-a: #Vytvoření prvního Workera, který počítá úlohy
    image: our-own-apache-spark:3.4.0
    ports:
      - "9091:8080" #webové rozhraní Workera
      - "7000:7000" #port pro komunikaci Workera
    depends_on:
      - spark-master
    environment:
      - SPARK_MASTER=spark://spark-master:7077 # adresa na Master uzel, ke kterému se Worker připojí do výpočetního klastru
      - SPARK_WORKER_CORES=1 # Počet CPU jader, který bude Workerovi přidělen
      - SPARK_WORKER_MEMORY=1G # Maximální paměť pro Worker pro výpočetní úlohy
      - SPARK_DRIVER_MEMORY=1G # Maximální paměť pro klientské úlohy (tzv. driver)
      - SPARK_EXECUTOR_MEMORY=1G # Maximální paměť pro spouštěče úloh
      - SPARK_WORKLOAD=worker #určení typu uzlu jako výpočetního
      - SPARK_LOCAL_IP=spark-worker-a #nastavení IP adresy workera
    volumes:
       - ./apps:/opt/spark-apps #stejné jako u Mastera, sdílený disk pro aplikace a data
       - ./data:/opt/spark-data
  spark-worker-b: #totožné sestrojení druhého výpočetního uzlu
    image: our-own-apache-spark:3.4.0
    ports:
      - "9092:8080"
      - "7001:7000"
    depends_on:
      - spark-master
    environment:
      - SPARK_MASTER=spark://spark-master:7077
      - SPARK_WORKER_CORES=1
      - SPARK_WORKER_MEMORY=1G
      - SPARK_DRIVER_MEMORY=1G
      - SPARK_EXECUTOR_MEMORY=1G
      - SPARK_WORKLOAD=worker
      - SPARK_LOCAL_IP=spark-worker-b
    volumes:
        - ./apps:/opt/spark-apps
        - ./data:/opt/spark-data
```

Klastr spustíme pomocí `docker-compose up`

Následně se připojíme do Spark-Master uzlu, který ovládá výpočetní Spark klastr. Který z kontejnerů je Master uzel Sparku zjistíte podle názvu pokud si vypíšete všechny běžící kontejnery příkazem Docker ps. Měl by se jmenovat docker-compose-way-spark-master-1. Zapamatujte si jeho hash.
```bash
docker ps
docker exec -i -t <hash pro spark-master> /bin/bash
#v me instanci: docker exec -i -t 0766d76b9da7 /bin/bash
```

Přejdeme do složky s ukázkovými příklady v jazyce Python, které si můžeme prohlédnout a pochopit zhruba, jak funguje Spark.
```bash
cd /opt/spark/examples/src/main/python
```

Po prohlednutí zkusíme vytvořit nějaký vlastní ukázkový příklad. V editoru Vi vytvoříme nějaký jednoduchý hello-world příklad pro vyzkoušení funkčnosti. Nejprve vytvořte prázdný soubor pomocí Vi.
```bash
vi test.py
```

Zmáčknutím klávesy `i` přejdete do editačního režimu. Můžete vložit následující kód do souboru:
```test.py
from pyspark.sql import SparkSession

# Inicializace SparkSession
spark = SparkSession.builder.appName("HelloWorldApp").getOrCreate()

# Vytvoření jednoduchého RDD
rdd = spark.sparkContext.parallelize(["Hello", "World", "from", "PySpark"])

# Transformace dat - převod na velká písmena
transformed_rdd = rdd.map(lambda x: x.upper())

# Akce - sběr výsledků
result = transformed_rdd.collect()

# Zápis do souboru
output_path = "/tmp/output.txt"
with open(output_path, "w") as file:
    file.write(" ".join(result))

print(f"Výsledek byl zapsán do souboru: {output_path}")

# Ukončení SparkSession
spark.stop()
```

Zmáčknutím klávesy escape můžete zadávat příkazy programu Vi. Zmáčkněte klávesu `:` a napište `wq` (write, quit) a tím uložíte zapsaný text a program ukončíte.

Teď stačí kód spustit a přečíst si výsledky (jsou vidět i ve výpisech, ale výpisy jsou tak husté, že je to lehce přehlédnutelné). Pro spuštění musíme přejít do složky se binárními soubory Sparku a spustit aplikaci pro spouštění úloh (Sparl Submit) s uvedením cesty k našemu kódu.
```bash
cd /opt/spark/bin
./spark-submit --master spark://0.0.0.0:7077 --name mujprogram /opt/spark/examples/src/main/python/test.py
```

Výsledek si můžeme stáhnout z Spark Master kontejneru pomocí Docker Copy (předpokládám, že jste příkazem exit ukončili běh bash ve Spark Master kontejneru a jste zpátky ve svém hostitelském počítači).
```bash
docker cp <hash master kontejenru>:/tmp/output.txt ./output.txt
#v me instanci: docker cp 0766d76b9da7:/tmp/output.txt .output.txt
```

Vzhledem k tomu, že jsme si v Docker-compose definovali sdílené složky, tak můžeme pro výpočty s daty využít tuto složku. V lokálním počítači vytvoříme následující kód pro shlukování dat metodou Kmeans, který uložíme do sdílené složky apps. Pozor na to, že je potřeba používat starý Pandas. Generativní AI Vám bude generovat pravděpodobně kód nový. Budete muset iterovat.
```apps/kmeans_clustering.py
from pyspark.sql import SparkSession
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import VectorAssembler
import matplotlib.pyplot as plt

# Inicializace SparkSession
spark = SparkSession.builder.appName("KMeansClustering").getOrCreate()

# Načtení dat ze sdílené složky
data_path = "/opt/spark-data/artificial_data.csv"
df = spark.read.csv(data_path, header=True, inferSchema=True)

# Převod sloupců na vektory pro clustering
vec_assembler = VectorAssembler(inputCols=["x", "y"], outputCol="features")
vec_df = vec_assembler.transform(df)

# KMeans clustering
kmeans = KMeans(k=3, seed=1)  # 3 clustery
model = kmeans.fit(vec_df)
transformed = model.transform(vec_df)

# Převod výsledků do seznamu Python objektů
data = transformed.select("x", "y", "prediction").collect()

# Rozdělení dat do clusterů
clusters = {0: [], 1: [], 2: []}  # Očekáváme 3 clustery
for row in data:
    clusters[row["prediction"]].append((row["x"], row["y"]))

# Vykreslení výsledků pomocí matplotlib
plt.figure(figsize=(8, 6))
colors = ['blue', 'green', 'red']
for cluster_id, points in clusters.items():
    x_vals, y_vals = zip(*points)
    plt.scatter(x_vals, y_vals, label=f"Cluster {cluster_id}", color=colors[cluster_id])
plt.title("KMeans Clustering")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
output_path = "/opt/spark-data/output.png"
plt.savefig(output_path)
print(f"Výsledek byl uložen do: {output_path}")

# Ukončení SparkSession
spark.stop()
```

Pro kód vytvoříme nějaká umělá data.
```data/artificial_data.csv
x,y
1.0,1.0
1.5,1.8
5.0,8.0
8.0,8.0
1.0,0.6
9.0,11.0
8.0,2.0
10.0,2.0
9.0,3.0
4.0,7.0
2.0,2.0
6.0,5.0
```

Přihlásíme se do Master nodu a úlohu spustíme. V lokální složce data bychom měli vidět výsledek - output.png.
```bash
docker exec -it <hash master kontejenru> bash
cd /opt/spark/bin
./spark-submit --master spark://spark-master:7077 /opt/spark-apps/kmeans_clustering.py
```

**Řešení integrace do Hadoop**
```Dockerfile

```
```docker-compose.yml

```

```test.py
from pyspark.sql import SparkSession

# Inicializace SparkSession
spark = SparkSession.builder.appName("HelloWorldApp").getOrCreate()

# Vytvoření jednoduchého RDD
rdd = spark.sparkContext.parallelize(["Hello", "World", "from", "PySpark"])

# Transformace dat - převod na velká písmena
transformed_rdd = rdd.map(lambda x: x.upper())

# Zápis výsledku na HDFS
output_path = "hdfs://namenode:8020/user/output"
transformed_rdd.saveAsTextFile(output_path)

print(f"Výsledek byl uložen na HDFS do: {output_path}")

# Ukončení SparkSession
spark.stop()
```

**Řešení Kubernetes**
```Dockerfile

```
```docker-compose.yml

```

#### C7.2 - Vlastní projekt využívající ML pro klasifikaci

Nahrajte na HDFS nějaká data z Kaggle a zkuste si pomocí MLlib naučit model klasifikovat (například obrázky psů a koček).

#### C7.3 - Vlastní projekt využívající grafová data

Nahrajte na HDFS nějaká grafová data (můžete je nagenerovat) a zkuste si provést analýzu grafových dat pomocí nějakého algorimu z GraphX

#### C7.4 - Vlastní projekt využívající detekci odchylky v real-time datech

Vytvořte si nějaký real-time datový zdroj, který zasílá do Sparku data (například simulace teploty) a detekujte v datech odchylky s využitím Spark Streaming. Data může generovat skript, který dává data do databáze (můžete využít i Apache Kafka z tutoriálu) a s nějakou malou pravděpodobností vygeneruje do dávky statistickou odchylku. Statistickou odchylku můžete reprezentovat jako číslo větší než 3*sigma.

