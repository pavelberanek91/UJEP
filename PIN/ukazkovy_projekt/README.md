# 1. Jazyk XML

Jazyk XML představuje důležitý standard pro přenos dat napříč ruznorodými systémy a pro otevřená data. V tomto cvičení se naučíte navrhnout si vlastní XML soubor na
papíře, napsat k němu XML kód, popsat jeho datové schéma pomocí dvou standardů a vymyslet službu, která by takové XML soubory generovala a konzumovala.

Pro všechna cvičení na XML vám bude stačit následující tutorial na W3 schools: [W3Schools XML Tutorial](https://w3schools.com/xml/default.asp)

## On-site cvičení

### Cv1.1 XML kód (30 minut)

Pravděpodobně jste se již někdy setkali s XML kódem a pokud ne, tak jste si ještě pravděpodobněji setkali s HTML kódem, který představuje podmnožinu XML. Jazyk XML
představuje standard pro počítačová data, které je možné vyměňovat mezi různými platformami. Mohu například stáhnout data z databáze a zobrazit je na mobilní aplikaci,
webové stránce, textovém dokumentu nebo si je ponechat v raw podobě.

Prohlédněte si ukázku XML kódu pro popis dat na následujícím odkazu: [W3Schools XML Introduction](https://w3schools.com/xml/xml_whatis.asp)

Každý xml kód se zkládá z elementů, které představují dvojici data a značka (tag): [W3Schools XML Elements](https://w3schools.com/xml/xml_elements.asp)

K datům je dále možné přidat atributy, které přidávají dodatečnou informaci: [W3Schools XML Attributes](https://w3schools.com/xml/xml_attributes.asp)

Místo atributů je možné využít další element a neexistuje žádný standard k tomu, jaká informace by měla být dodána jako element a jaká jako atribut. Já osobně 
doporučuji, aby elementy byly informace pro čtenáře a atributy informy pro aplikaci, kterou XML soubor zpracováváte. To ovšem může způsobat problém s tzv. validací.
Více o problematice elementy vs. atributy naleznete na [W3Schools Elements vs. Attr](http://w3schools.com/xml/xml_dtd_el_vs_attr.asp)

Jelikož mohou mít XML elementy stejné názvy, ale zcela jiný význam, mohly by se elementy při zpracování aplikací plést. Z toho důvodu je možné k elementům přidat
prefix, který elementy dále kategorizuje do jmenných prostorů. Příklad může být problém table jako stolu a table jako tabulky: [W3Schools XML Namespaces](https://w3schools.com/xml/xml_namespaces.asp)

Vaším úkolem je vytvořit vlastní XML soubor, podle následující specifikace klienta:
> Naše aplikace pro učitele na základní a střední škole, sloužící pro vyhledávání návodů na fyzikální pokusy, bude používat pro ukládání dat o pokusech XML soubory.
> Každý pokus bude v jednom XML souboru a potřebuje mít v sobě uložené následující informace: název experimentu, jméno autora, vhodné ročníky pro demonstraci, pomůcky,
> návod. Každá pomůcka by měla být element sám o sobě. Ročníky budou zpracované jen strojově při filtrování a vyhledávání v databázi a klient tuto informace neuvidí.
> Navrhněte jeden ukázkový XML soubor podle této specifikace.


### Cv1.2 Well Formed XML (20 minut)

XML představuje velice jednoduchý formát kódu, jelikož je struktura téměr celá na vás. Existuje pouze pár pravidel [W3Schools XML Syntaxe](https://w3schools.com/xml/xml_syntax.asp). Pokud je dodržíte, pak je váš XML dokument považován za tzv. "Well Formed":
1. XML dokument musí obsahovat kořenový element (nemá sourozence, jen děti)
2. Pokud má XML dokument prolog (používáme pro specifikaci kódování, defaultně UTF-8), pak musí být prvním řádkem souboru
3. Všechny elementy musí být uzavřené (výjimku tvoří prolog)
4. Elementy jsou case sensitive
5. Elementy musí být řádně zanořené
6. Hodnoty atributů musí být v uvozovkách
7. Některé znaky mají speciální význam a proto musí být vloženy jako entity
8. Komentáře nesmí obsahovat dvě pomlčky jinde, než na konci komentáře
9. Bílé znaky nejsou ořezávány
10. Zalomení na nový řádek je znak LF (line feed) - nutné řešit při problémech s parsováním ve Windows

Zda je XML "Well Formed" lze otestovat pomocí XML validátorů: [W3Schools XML Validator](https://w3schools.com/xml/xml_validator.asp)

Vaším úkolem je prohlédnout si následující XML kód a opravit ho tak, aby byl "Well Formed" a otestovat validátorem:

```
<kniha>
    <!-- každá kniha obsahuje dva názvy a to český a anglický -- specifikováno atributem -->
    <název jazyk=cz>Epos o Berygamešovi
    <název jazyk=en>Epic of Berygamesh
    <Autor>Jiří Fišer</autor>
    <postavy><postava>Berygameš</postava><postava>Škvorkidu<postavy/></postava>
</kniha>
<kniha>
    <název jazyk=cz>Pán prstenů: návrat Fišera
    <název jazyk=en>Lord of the rings: return of Fišer
    <Autor>Beránek Pavel</autor>
    <popis>
        Kniha o partě ajťáků, kteří se chystají na výpravu na zápočet na Fakultu Osudu.
    </popis>
</kniha>
<?xml version="1.0" encoding="UTF-8"?>
```

### Cv1.3 XML služby (10 minut)

XML se používá jako jazyk pro popis dat, který vyžadují klientské aplikace od serveru. Takové servery tedy pro klienty poskytují služby. Mezi základní XML formáty, 
které používají serverové služby řadíme:
1. [XML WSDL](https://w3schools.com/xml/xml_wsdl.asp) - formát pro popis webových služeb (endpointy, funkcionalita), používá se společně se SOAP
2. [XML SOAP](https://w3schools.com/xml/xml_soap.asp) - formát pro zasílání dat pomocí HTTP požadavků mezi systémy čistě v XML oproti jiným typům služeb (CORBA atd.)
3. [XML RDF](https://w3schools.com/xml/xml_rdf.asp) - formát pro grafová data; pokud služby poskytují data v XML RDF, pak jsou tzv. 4. úrovně otevřenosti
4. [XML RSS](https://w3schools.com/xml/xml_rss.asp) - formát pro zasílání krátkých upozornění odběratelům (typicky na aplikace typu RSS čtečka)

Více o RSS (Really Simple Syndication): [mnot.net](https://mnot.net/rss/tutorial)

Více o WSDL (Web Services Description Language): [tutorialspoint.com](https://tutorialspoint.com/wsdl/wsdl_introduction.htm) a ukázka [wiki](https://en.wikipedia.org/wiki/Web_Services_Description_Language)

Více o SOAP (Simple Object Access Protocol): [guru99.com](https://guru99.com/soap-simple-object-access-protocol.html) a [tutorial z MUNI](https://dior.ics.muni.cz/~makub/soap/tutorial.html)

Více o RDF (Resource Description Framework): [linkeddatatools.com](https://linkeddatatools.com/semantic-web-basics) a [5star open data](https://5stardata.info/en/)

Vyzkoušejte si RSS čtečku:
> Stáhněte si do mobilního zařízení nějakou RSS čtečku (pro Android např.: Feedly) a přidejte si RSS feed na mojí stránku pavelberanek.com. Pokud vydám nový článek
na mé webové stránce, přijde vám upozornění.

### Cv1.4 Návrh XML stromu (10 minut)

XML nemá žádný model pro grafickou reprezentaci, jako například třídy v OOP jako diagramy tříd z jazyka UML. Přesto by se nám nějaký alespoň primitivní grafický model
pro přemýšlení nad návrhem, komunikaci o datovém modelu v týmu nebo dokumentaci hodil. Jelikož XML představuje datovou strukturu, kde nalezneme prvotní značku (kořen), 
značky, obsahující další značky, (větve) a značky, neobsahující žádné další značky, (listy), tak se nabízí možnost zakreslit XML jako stromovou strukturu.

Na stránce [W3 Schools XML Tree](https://w3schools.com/xml/xml_tree.asp) vidíte grafickou reprezentaci xml kódu pomocí stromové struktury. Pod obrázkem naleznete
kód k příslušnému stromu. Vaším úkolem je vytvořit návrh struktury xml dokumentu podle následující klientské specifikace:
> Chtěl bych vytvořit webovou aplikaci pro receptář alkoholových koktejlů. Kdokoliv, kdo otevře webovou stránku, tak může nahrát XML soubor s vlastním receptem.
> Klient může naráz nahrát více receptů a o každém receptu budu potřebovat ukládat stejné informace, jako jsou na následující webové stránce: [Míchané drinky](https://michanedrinky.cz).

### Cv1.5 Validní XML (40 minut)

Ve cvičení 1.Cv2 jste zkoušeli upravit XML soubor tak, aby byl "Well formed". Kromě "Well formed" by měl být XML soubor ještě validní. Aby byl dokument XML dokument
validní, pak se musí jeho struktura řídit šablonou ve formátu DTD (Document Type Definition) nebo XML Schema (novější typ šablony, která je sama o sobě XML). 
Představit si to lze obdobně jako v objektově orientovaném programování, kde v našem případě šablona odpovídá třídě a XML dokument odpovídá objektu (instanci třídy).

Ukázku DTD naleznete na stránce: [W3Schools XML DTD](https://w3schools.com/xml/xml_dtd.asp)

Každý DTD dokument se skládá ze stavebních bloků: [W3Schools XML DTD Building Blocks](https://w3schools.com/xml/xml_dtd_building.asp) a DTD představuje strukturu
na sebe navazujících bloků - co každý blok obsahuje za potomky a jaké má příbuzné.

1. Elementy [W3Schools XML DTD Elements]() - mohou být prázdné, s daty, s potomky, libovolnými bloky (element, data) a o různém počtu bloků (právě 1, alespoň 1, nula a více, nula nebo jeden) nebo s výčtem konkrétních bloků pomojí spojky OR.
2. Atributy [W3Schools XML DTD Attributes]() - atributy mají typy (data, výčet, ID, odkaz na ID, entita, atd.) a hodnoty (pevně dané, povinné a volitelné)
3. Entity [W3Schools XML DTD Entities]() - zkratky za konstantní hodnoty, které často využíváte
4. Parsovaná data - data mezi elementy, která budou zpracována parserem a entity budou rozvinuty
5. Znaková data - data mezi elementy, která se berou doslovně a nejsou nijak zpracována (entity nebudou rozvinuty a v obsahu zůstane jejich alias)

Váš úkol zní:
> Vytvořte DTD schéma ke stromu ze cvičení 1CV4 na míchané drinky. 

## Domácí cvičení

Domácí cvičení nejsou nijak hodnoceny a je to pouze na vaší vlastní odpovědnosti, zda je vykonáte či nikoliv. Znalosti z těchto úkolů budou vyžadovány u zápočtu.
Pokud se zaseknete u nějakého úkolu, tak napište na Discordu do příslušné kategorie předmětu a může vám spolužák nebo já poradit.

### U1.1 XML splňující DTD

Při On-site výuce jste vytvářeli DTD pro určitá XML. Zkuste si to teď obráceně, tzn. napište XML, které je validní vúči konkrétnímu DTD, a ověřte jeho validnost
pomocí online validátoru: [xmlvalidation.com](http://xmlvalidation.com)

> Na stránce [W3Schools XML DTD Examples](https://w3schools.com/xml/xml_dtd_examples.asp) naleznete 2 DTD schémata (televizní program a novinový článek). Napište
> k nim validní XML.

### U1.2 Lorem

### U1.3 Lorem
