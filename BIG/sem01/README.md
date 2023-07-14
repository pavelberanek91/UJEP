# Datová úložiště a nástroje pro Big Data (KI/BIG)

## Seminář 1 - Principy virtualizace a přehled nástrojů

### Samostudium

#### S1.1 - Veledata

Tento kurz je zaměřen na zpracování veledat pomocí efektivních nástrojů, na které samotné jazyky a standardní moduly/knihovny nestačí. Proto je nutné si jako první definovat, co jsou vlastně veledata, abyste měli na paměti, kdy je vhodné začít uvažovat o použití vyučovaných technologií.

Jedná z vhodných definic zní následovně: "Veledata (bigdata) jsou taková data, jejichž zpracování je problém sám o sobě." Tato data se vyznačují 3 vlastnostmi, ve kterých dosahují vysokých hodnot:
1. Volume (objem) - data mají v krátkém čase velkou kapacitu (GB, TB),
2. Variety (různorodost) - data mají různé datové formáty (text, audio, GPS souřadnice) a mohou být jak úplná, tak některé položky mohou chybět,
3. Velocity (rychlost) - data přicházejí velmi rychle (sekundy, mikrosekundy).

Někdo k těmto tzv. 3V přidává další 3V:
4. Veracity (důvěryhodnost) - spolehlivost na správné informace v datech (přesnost, zkreslení),
5. Variability (proměnlivost) - změna v hodnotách a formátu dat v čase,
6. Value (hodnota) - business hodnota získaná z analýzy dat.

Může se jednat o následující typy aplikací:
1. záznamy z velkých informačních systémů (cestování, trh akcií),
2. data z IoT (internet věcí) zařízení a senzorů,
3. příspěvky na sociálních sítích,
4. videherní servery a multimediální streamy.

Tato data se zpracovávají specializovanými nástroji. Mezi nejpoužívanější patří:
1. Apache Hadoop - systém pro práci s veledaty v dávkové podobě,
2. Apache Spark - systém pro práci s veledaty včetně streamů,
3. Apache Kafka - systém pro tvorbu streamovacích potrubí (stream pipeline) ,
4. NoSQL Databáze - databáze, které jsou efektivnější pro veledata než tradiční relační tabulkové databáze,
5. specializované moduly programovacích jazyků - moduly pro rychlé vektorové operace a strojové učení (numpy, pandas, scikit-learn).

#### S1.2 - Distribuované zpracování dat

Zpracování veledat vyžaduje velký výpočetní výkon. Výpočety se provádí na počítačích, kterým budeme říkat uzly. Zvyšování výkonu uzlů se provádí dvěmi způsoby:
1. vertikální škálování - změna součástek výpočetního uzlu za výkonější,
2. horizontální škálování - přidávání dalších výpočetních uzlů.

Vertikální škálování je velice drahé a brzo dojdeme i na samotnou technologickou mez výkonu uzlu. Proto v případě veledat musíme škálovat horizontálně. Každý uzel si vezme část z příchozích dat na starost ke zpracování. To přináší komplikace ve formě nutnosti data zpětně synchronizovat a složit do jednotného celku. To se nejčastěji řeší dedikovaným uzlem, kterýmu se říká master (pán). Ten má za úkol zadávat úkoly ostatním uzlům (slaves, otroci) a získávat od nich výsledky v požadové synchronicitě (časovém sledu).

<img src="dataprocessing.jpg" alt="schéma distribuované architektury" />

Pro distribuované zpracování dat na uzlech je nutné psát sofistikované programy pro zpracování dat, které mají několik vrstev zpracování. Vzhledem k legislativě mohou některé data mít behaviorální charakter a jejich únik by porušil GDPR. Proto musí takové programy řídit i zabezpečení. Z dat musí také podniky nějakou hodnotu, která je typicky získaná z informací z dat, podle kterých se management informovaně rozhoduje. Aplikace tedy musí mít i komponenty pro analýzu dat (tvorba informací) a vizualizaci dat pro získání vhledu do problematiky. Kvalita dat také ovlivňuje celkovou analýzu a proto je nutné data často preprocesovat. Z toho důvodu existují celé pracovní rámce (frameworky) pro distribuované výpočty (Hadoop, Spark aj.). Programovat si vlastní distribuované výpočtní systémy by bylo neskutečně náročné.

<img src="datalayers.jpg" alt="vrstvy zpracování distribuovaných dat" />

#### S1.3 - Virtualizované kontejnery

#### S1.4 - lorem

#### S1.5 - lorem

### Cvičení

#### C1.1 - lorem

#### C1.2 - lorem

#### C1.3 - lorem

#### C1.4 - lorem

#### C1.5 - lorem

### Domácí úkoly

#### D1.1 - lorem

#### D1.2 - lorem

#### D1.3 - lorem

#### D1.4 - lorem

#### D1.5 - lorem
