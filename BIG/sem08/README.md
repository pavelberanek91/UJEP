# Datová úložiště a nástroje pro Big Data (KI/BIG)

## Seminář 8 - Ekosystém Hadoop

#### S8.1 - Další nástroje pro Hadoop
BUDE DOPLNĚNO

#### S8.2 - HiveQL (Hive Query Language)

HiveQL je dotazovací jazyk nástroje Apache Hive, který umožňuje dotazovat se analytovat data uložená v HDFS. Jazyk je podobný jazyku SQL, což si můžeme ukázat na následujícím příkladu:
```
SELECT country, COUNT(*) as user_count
FROM users
GROUP BY country;
```
HiveQL tento dotaz přeloží do MapReduce úlohy a spustí. Tímto způsobem je možné snadno vytvářet různé reporty v oblasti dolování veledat z Hadoop klastru.

Hive dotazy je možné pouštět pomocí Python Knihovny PyHive.

#### S8.3 - Apache Pig
BUDE DOPLNĚNO

ETL (Extract-Transform-Load) je sada fází, které se typicky nachází při analýze dat, které jsou uloženy v datovém skladu. Jedná se o myšlenkový a procesní pracovní rámec, který pomáhá analytikům vytvářet analyzující programy.
1. Extract - získá data z datového úložiště
2. Transform - změní data a získá z nich nějakou podnikovou hodnotu (program napsaný pomocí MapReduce)
3. Load - uloží data do datového úložiště

Tyto fáze představují jednu datovou rouru pro zpracování dat. Apache Pig je jazyk, který umožňuje psát komplexní programy a můžeme si tyto programy obohatit o vlastní uživatelem definované funkce v mnoha jazykých včetně jazyka Python. Tento jazyk nám pomůže psát takové ETL roury.

https://en.wikipedia.org/wiki/Apache_Pig

#### S8.4 - Apache Kafka
BUDE DOPLNĚNO

#### S8.5 - Správa pracovních toků

Pracovní datoky (nebo také datové roury-pipelines) jsou automatizované pracovní postupy, které zahrnují získání dat (extrakce), zpracování dat (transformace) a jejich uložení (load). Takové toky potřebujeme volat opakovaně v čase, efektivně s případnou možností škálování. 

Z toho důvodu existují nástroje pro správu a monitoring toků. Mezi nejznámější nástroje patří Apache Airflow, Prefect, Google Cloud Dataflow a Luigi workflows.

Mezi hlavní vlastnosti těchto správců toků patří:
1. Automatizace: složité kroky z více procesů se spouští automatizovaně od získání dat až po jejich vizualizaci
2. Správa závislostí: toky mohou být na sobě závislé a správce se postarají o návaznost výsledků ve formě grafové struktury
3. Detekce stavu toku: správci umí hlídat, které úkoly ještě nebyly splněné a které jo. Hotové úkoly již nebude spouštět.
4. ETL rámce: správci podporují myšlenky Extract-Transform-Load pracovního rámce datových analytiků
5. Logování a monitoring: správci mají obyčejně přehledné datové dashboardy a logovací mechanismy pro průběhy procesů a jejich problémy
6. Toky a strojové učení: velké modely strojového učení se učí z mnoha dat, která jsou získávána toky. Správci umožní takové učení z dat systematizovat.

### Cvičení

#### C8.1 - HiveQL

TATO ČÁST KURZU BUDE JEDNOHO DNE DODĚLANÁ :) 

#### C8.2 - PyHive - ZATÍM NEFUNGUJE

TATO ČÁST KURZU BUDE JEDNOHO DNE DODĚLANÁ :) 

Pro dotazy nad HDFS můžeme využít technologie Hive. Pro využití Hive musíme upravit náš docker-compose a přidat tam další uzly:
* Hive server - Používá se pro dotazování nad HDFS
* Metastore server - Spravuje metadata, která používá Hive Server
* MySQL pro ukládání metadat - Ukládá metadata pro Metastore server

Nový docker-compose bude vypadat takto:
```yml
version: "3"

services:
  namenode:
    image: bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8
    container_name: namenode
    restart: always
    ports:
      - 9870:9870
      - 9000:9000
    volumes:
      - hadoop_namenode:/hadoop/dfs/name
    environment:
      - CLUSTER_NAME=test
    env_file:
      - ./hadoop.env

  datanode:
    image: bde2020/hadoop-datanode:2.0.0-hadoop3.2.1-java8
    container_name: datanode
    restart: always
    volumes:
      - hadoop_datanode:/hadoop/dfs/data
    environment:
      SERVICE_PRECONDITION: "namenode:9870"
    env_file:
      - ./hadoop.env
  
  resourcemanager:
    image: bde2020/hadoop-resourcemanager:2.0.0-hadoop3.2.1-java8
    container_name: resourcemanager
    restart: always
    environment:
      SERVICE_PRECONDITION: "namenode:9000 namenode:9870 datanode:9864"
    env_file:
      - ./hadoop.env

  nodemanager1:
    image: bde2020/hadoop-nodemanager:2.0.0-hadoop3.2.1-java8
    container_name: nodemanager
    restart: always
    environment:
      SERVICE_PRECONDITION: "namenode:9000 namenode:9870 datanode:9864 resourcemanager:8088"
    env_file:
      - ./hadoop.env
  
  historyserver:
    image: bde2020/hadoop-historyserver:2.0.0-hadoop3.2.1-java8
    container_name: historyserver
    restart: always
    environment:
      SERVICE_PRECONDITION: "namenode:9000 namenode:9870 datanode:9864 resourcemanager:8088"
    volumes:
      - hadoop_historyserver:/hadoop/yarn/timeline
    env_file:
      - ./hadoop.env

  mysql:
    image: mysql:5.7
    container_name: mysql
    environment:
      MYSQL_ROOT_PASSWORD: root_password
      MYSQL_DATABASE: hive
      MYSQL_USER: hive
      MYSQL_PASSWORD: hive_password
    volumes:
      - mysql_data:/var/lib/mysql

  hive-metastore:
    image: bde2020/hive:2.3.2-postgresql-metastore
    container_name: hive-metastore
    environment:
      HIVE_METASTORE_URI: thrift://hive-metastore:9083
      METASTORE_DB_TYPE: mysql
      MYSQL_HOST: mysql
      MYSQL_PORT: 3306
      MYSQL_USER: hive
      MYSQL_PASSWORD: hive_password
    depends_on:
      - mysql
    ports:
      - 9083:9083

  hive-server:
    image: bde2020/hive:2.3.2
    container_name: hive-server
    environment:
      SERVICE_PRECONDITION: "namenode:9000 datanode:9864"
      HIVE_METASTORE_URI: thrift://hive-metastore:9083
      HIVE_SERVER2_THRIFT_PORT: 10000
    depends_on:
      - hive-metastore
    ports:
      - 10000:10000
  
volumes:
  hadoop_namenode:
  hadoop_datanode:
  hadoop_historyserver:
  mysql_data:
```

Do našeho lokálního počítače si nainstalujeme potřebné moduly
```bash
pip install pyhive
pip install thrift
pip install thrift_sasl
```

Připojme se Python skriptem na HiveServer a požádejme o výsledek dotazu nad HDFS:
```py
from pyhive import hive

conn = hive.Connection(host="localhost", port=10000, username="hive")
cursor = conn.cursor()
cursor.execute("SHOW DATABASES")
for db in cursor.fetchall():
    print(db)
```

#### C8.3 - Pig s UDF v Pythonu

#### C8.4 - Kafka 

#### C8.5 - Luigi workflows

Datové roury často běží opakovaně v periodických intervalech. Pokud nám neustále přichází nová data, potřebujeme neustále nové analýzy. Pokud jsou kódy dostatečně univerzální, můžeme je spouštět opakovaně. 

Takové vymazlené roury budeme muset řídit a sledovat jejich stav. K tomu nám mohou pomocí nástroje pro zprácu datových rour nebo také pracovních toků. Jedním z takových nástrojů je Luigi.

https://medium.com/@prasanth_lade/luigi-all-you-need-to-know-f1bc157b20ed