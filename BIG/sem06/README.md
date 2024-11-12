# Datová úložiště a nástroje pro Big Data (KI/BIG)

## Seminář 6 - MapReduce framework a jeho použití

### Samostudium

MapReduce bychom měli chápat na základě minulého cvičení. V tomto cvičení budeme jen zlepšovat naše dovednosti. 

Úlohy můžete psát pomocí MrJob (který si můžete pouštět lokálně) nebo nativně pro Hadoop v Javě. Doporučuji si alespoň pár úloh pro procvičení workflow s Hadoop spustit na klastru.

### Cvičení

Některá cvičení naleznete v balíku programů z minulé lekce. Přesto doporučuji si je napsat svépomocí. Pro tyto úlohy budete potřebovat i vstupní data, která si vygeneruje vlastním skriptem nebo použijte generativní AI.

#### C6.1 - Počet slov
Napište program, který spočítá počet výskytů slov v textovém souboru.
* Mapper: Rozdělte každý řádek textu na slova a přiřaďte každému slovu klíč s hodnotou 1.
* Reducer: Sečtěte hodnoty pro každý klíč (slovo) a vypište výsledný počet.

**Příklad vstupu**
```
hello world
hello Hadoop
```

**Očekávaný výstup**
```
hello   2
world   1
Hadoop  1
```

**Řešení**
```py
from mrjob.job import MRJob

class WordCount(MRJob):
    def mapper(self, _, line):
        for word in line.split():
            yield word, 1

    def reducer(self, word, counts):
        yield word, sum(counts)
```

#### C6.2 - Maximální hodnota v datasetu
Vyhledejte maximální hodnotu v datasetu (např. nejvyšší prodejní hodnotu, maximální teplotu apod.).
* Mapper: Pro každou hodnotu v datasetu emitujte klíč (např. "max") s hodnotou.
* Reducer: Najděte maximum z hodnot pro každý klíč.

**Příklad vstupu**
```
23
45
67
12
```

**Očekávaný výstup**
```
max   67
```

**Řešení**
```py
class MaxValue(MRJob):
    def mapper(self, _, line):
        value = int(line.strip())
        yield "max", value

    def reducer(self, key, values):
        yield key, max(values)
```

#### C6.3 - Počet unikátních slov
Vypočítejte počet unikátních slov v textovém souboru. 
* Mapper: Emitujte každé slovo jako klíč s hodnotou 1.
* Reducer: Použijte set nebo unikátní klíče ke spočítání unikátních slov.

**Příklad vstupu**
```
apple banana apple
banana cherry
```

**Očekávaný výstup**
```
apple   2
banana  2
cherry  1
```

**Řešení**
```py
class UniqueWordsCount(MRJob):
    def mapper(self, _, line):
        for word in set(line.split()):
            yield word, 1

    def reducer(self, word, counts):
        yield word, sum(counts)
```

#### C6.4 - Průměr hodnot v datasetu
Spočítejte průměr hodnot pro každý klíč (např. průměrné hodnocení produktu).
* Mapper: Emitujte každý klíč s hodnotou (např. hodnocení produktu).
* Reducer: Sečtěte hodnoty a vydělte počtem výskytů pro každý klíč.

**Příklad vstupu**
```
A 100
B 200
A 300
B 400
```

**Očekávaný výstup**
```
A   200.0
B   300.0
```

**Řešení**
```py
class AverageValue(MRJob):
    def mapper(self, _, line):
        key, value = line.split()
        yield key, int(value)

    def reducer(self, key, values):
        values = list(values)
        yield key, sum(values) / len(values)
```

#### C6.5 - Počet řádků v datasetu
Prostudujte, jak počítat celkový počet řádků v datasetu, což je jednoduché cvičení na práci s klíči a hodnotami.
* Mapper: Emitujte klíč (např. "count") s hodnotou 1 pro každý řádek.
* Reducer: Sečtěte všechny hodnoty pro klíč "count".

**Příklad vstupu**
```
row1
row2
row3
```

**Očekávaný výstup**
```
lines   3
```

**Řešení**
```py
class LineCount(MRJob):
    def mapper(self, _, line):
        yield "lines", 1

    def reducer(self, key, counts):
        yield key, sum(counts)
```

#### C6.6 - Počet slov podle délky
Spočítejte, kolik slov má každou délku (např. kolik slov má 3 písmena, 4 písmena atd.).
* Mapper: Emitujte délku slova jako klíč a hodnotu 1.
* Reducer: Sečtěte výskyty pro každý klíč (délku slova).

**Příklad vstupu**
```
cat dog elephant
horse
```

**Očekávaný výstup**
```
3   2
8   1
5   1
```

**Řešení**
```py
class WordLengthCount(MRJob):
    def mapper(self, _, line):
        for word in line.split():
            yield len(word), 1

    def reducer(self, length, counts):
        yield length, sum(counts)
```

#### C6.7 - Top N položek podle hodnoty
Najděte top N položek (např. nejdražší produkty nebo nejsledovanější videa).
* Mapper: Emitujte klíč s hodnotou (např. název produktu a jeho hodnocení).
* Reducer: V Reduceru seřaďte hodnoty a vyberte N nejvyšších. 

**Příklad vstupu**
```
productA 10
productB 20
productC 30
productD 40
```

**Očekávaný výstup pro N=2**
```
productD   40
productC   30
```

**Řešení**
```py
from heapq import nlargest

class TopNValues(MRJob):
    N = 3  # Nastavte hodnotu N dle potřeby

    def mapper(self, _, line):
        key, value = line.split()
        yield None, (int(value), key)

    def reducer(self, _, values):
        top_n = nlargest(self.N, values)
        for value, key in top_n:
            yield key, value
```

#### C6.8 - Spojení dat podle klíče
Načtěte dvě různé datasety a spojte je na základě společného klíče (např. spojení seznamu produktů a jejich prodejů).
* Mapper: Pro každou datovou sadu přidejte k hodnotě označení zdroje (např. "A" nebo "B").
* Reducer: Spojte záznamy podle klíče, kde oba zdroje existují, a sloučte hodnoty.

**Příklad vstupu**
```
A 1 value1
B 1 value2
A 2 value3
```

**Očekávaný výstup**
```
1   [("A", "value1"), ("B", "value2")]
2   [("A", "value3")]
```

**Řešení**
```py
class JoinData(MRJob):
    def mapper(self, _, line):
        source, key, value = line.split()
        yield key, (source, value)

    def reducer(self, key, values):
        values = list(values)
        if len(values) == 2:
            yield key, values
```

#### C6.9 - Inverzní index pro dokumenty
Vytvořte inverzní index pro dokumenty (např. pro vyhledávač), kde každý dokument obsahuje seznam slov.
* Mapper: Emitujte každé slovo jako klíč s hodnotou obsahující ID dokumentu.
* Reducer: Vytvořte seznam dokumentů pro každý klíč (slovo).

**Příklad vstupu**
```
doc1  hello world
doc2  hello Hadoop
```

**Očekávaný výstup**
```
hello   [doc1, doc2]
world   [doc1]
Hadoop  [doc2]
```

**Řešení**
```py
class InvertedIndex(MRJob):
    def mapper(self, _, line):
        doc_id, content = line.split('\t', 1)
        for word in content.split():
            yield word, doc_id

    def reducer(self, word, doc_ids):
        yield word, list(set(doc_ids))
```

#### C6.10 - Sekundární třídění podle dvou kritérií
Seřaďte data nejprve podle prvního klíče a následně podle druhého (např. jméno a příjmení).
* Mapper: Emitujte složený klíč (např. [příjmení, jméno]) s hodnotou.
* Reducer: Seřaďte hodnoty podle druhého kritéria.

**Příklad vstupu**
```
Smith John
Smith Alice
Brown John
```

**Očekávaný výstup**
```
Brown   [John]
Smith   [Alice, John]
```

**Řešení**
```py
class SecondarySort(MRJob):
    def mapper(self, _, line):
        last_name, first_name = line.split()
        yield last_name, first_name

    def reducer(self, last_name, first_names):
        yield last_name, sorted(first_names)
```

#### C6.11 - Společný výskyt slov
Najděte, jak často se dvě slova vyskytují společně v dokumentech.
* Mapper: Emitujte každou dvojici slov z dokumentu jako klíč s hodnotou 1.
* Reducer: Sečtěte výskyty pro každou dvojici.

**Příklad vstupu**
```
apple banana apple
banana cherry
```

**Očekávaný výstup**
```
(apple, banana)   2
(apple, cherry)   1
(banana, cherry)  1
```

**Řešení**
```py
class WordCooccurrence(MRJob):
    def mapper(self, _, line):
        words = line.split()
        for i, word1 in enumerate(words):
            for word2 in words[i + 1:]:
                yield (word1, word2), 1

    def reducer(self, word_pair, counts):
        yield word_pair, sum(counts)
```

#### C6.12 - Analýza sentimentu v recenzích
Klasifikujte sentiment (pozitivní/negativní) v textových recenzích pomocí jednoduchých pravidel nebo slovníku.
* Mapper: Emitujte klíč (např. ID recenze) s hodnotou obsahující kladný/negativní sentiment.
* Reducer: Spočítejte počet kladných a negativních recenzí.

**Příklad vstupu**
```
review1 good product
review2 bad quality
review3 excellent service
```

**Očekávaný výstup**
```
positive   2
negative   1
```

**Řešení**
```py
class SentimentAnalysis(MRJob):
    positive_words = {"good", "great", "excellent"}
    negative_words = {"bad", "poor", "terrible"}

    def mapper(self, _, line):
        sentiment = "neutral"
        if any(word in line for word in self.positive_words):
            sentiment = "positive"
        elif any(word in line for word in self.negative_words):
            sentiment = "negative"
        yield sentiment, 1

    def reducer(self, sentiment, counts):
        yield sentiment, sum(counts)
```

#### C6.13 - Výpočet PageRanku
Implementujte PageRank algoritmus pro jednoduchý graf (např. webové stránky a jejich odkazy).
* Mapper: Emitujte uzel a jeho váhu pro každý sousední uzel.
* Reducer: Sečtěte přispívající váhy pro každý uzel, normalizujte a znovu rozdělte.

**Příklad vstupu**
```
A   B C
B   C
C   A
```

**Očekávaný výstup**
```
A   0.333
B   0.333
C   0.333
```

**Řešení**
```py
class PageRank(MRJob):
    def mapper(self, _, line):
        node, *links = line.split()
        yield node, links
        rank = 1.0 / len(links)
        for link in links:
            yield link, rank

    def reducer(self, node, values):
        rank = 0.15 + 0.85 * sum(values)
        yield node, rank
```

#### C6.14 - Identifikace anomálií v datových tocích
V datasetu transakcí vyhledejte anomálie, jako jsou neobvykle vysoké hodnoty.
* Mapper: Emitujte klíč s hodnotou (např. transakce a její hodnota).
* Reducer: Spočítejte průměr a směrodatnou odchylku, hledejte odlehlé hodnoty.

**Příklad vstupu**
```
t1 100
t2 200
t3 1000
t4 150
```

**Očekávaný výstup**
```
mean      362.5
std_dev   370.56
```

**Řešení**
```py
class AnomalyDetection(MRJob):
    def mapper(self, _, line):
        transaction, value = line.split()
        yield "value", int(value)

    def reducer(self, key, values):
        values = list(values)
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        yield "mean", mean
        yield "std_dev", variance ** 0.5
```

#### C6.15 - K-means clustering
Implementujte algoritmus K-means clustering pro seskupení bodů ve 2D prostoru.
* Mapper: Pro každý bod spočítejte vzdálenost od centroidů a přiřaďte k nejbližšímu.
* Reducer: Sečtěte hodnoty bodů a aktualizujte centroidy. Opakujte iterace.

**Příklad vstupu**
```
1 1 2
2 2 3
3 8 8
4 9 9
```

**Očekávaný výstup**
```
(1.5, 2.5)
(8.5, 8.5)
```

**Řešení**
```py
class KMeans(MRJob):
    def mapper(self, _, line):
        point_id, x, y = line.split()
        x, y = float(x), float(y)
        centroid = min(self.centroids, key=lambda c: (x - c[0]) ** 2 + (y - c[1]) ** 2)
        yield centroid, (x, y)

    def reducer(self, centroid, points):
        points = list(points)
        mean_x = sum(p[0] for p in points) / len(points)
        mean_y = sum(p[1] for p in points) / len(points)
        yield centroid, (mean_x, mean_y)
```