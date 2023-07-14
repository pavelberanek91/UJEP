# Datová úložiště a nástroje pro Big Data (KI/BIG)

## Seminář 6 - Spark a jeho architektura

### Samostudium

https://www.oreilly.com/content/hadoop-with-python/


#### S6.1 - Apache Spark

Apache Spark je univerzální volatilní (in-memory) analytický engine pro distrubované zpracování veledat a provádění úkonů strojového učení. Jedná se o výkonnou platformu, která provádí operace nad veledaty zhruba 100x rychleji než tradiční Python. Zdrojem veledat může být Apache Hadoop, Amazon S3 server a mnoho dalších souborových systémů. Dále umožňuje zpracování dat z datových proudů (stream) v reálném čase z platformy Apache Kafka.

Architektura Sparku je realizována architektonickým vzorem master-slave. Master nazýváme ve Spark terminologii Driver a slavy nazýváme Workers. Úkolem Driveru je tvorba kontextu aplikace a úkolem Workers je provádění všech transformačních operací. O výpočetní zdroje se stará tzv. Cluster Manager.

<img src="cluster-overview.png" alt="Architecture Apache Spark klastru" />

#### S6.2 - Resilient Distributed Datasets (RDD)

#### S6.3 - PySpark

PySpark je modul pro jazyk Python, který zprostředkovává API komunikaci se Sparkem.

#### S6.4 - RDD operace

#### S6.5 - Apache Kafka

### Cvičení

#### C6.1 - lorem

#### C6.2 - lorem

#### C6.3 - lorem

#### C6.4 - lorem

#### C6.5 - lorem

### Domácí úkoly

#### D6.1 - lorem

#### D6.2 - lorem

#### D6.3 - lorem

#### D6.4 - lorem

#### D6.5 - lorem
