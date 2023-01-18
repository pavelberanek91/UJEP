# Programování pro internet

**Obsah cvičení 2**:
* XML služby
* SMIL
* SVG
* RSS

### On-site

#### XML služby

Nad značkovacím jazykem XML bylo vybudováno spousty technologií, které poskytujou uživatelům služby. Mezi stále využíváné technologie řadíme například:
* SMIL: již obsolete, ale používají to MMS zprávy a stará HD DVDéčka pro zobrazení menu
* SVG: používají do dneš vektorové editory jako Inscape a webové stránky pro rychlé procedurální generování obrázků/ikon
* RSS: používají webové portály pro upozornění na nově vydané příspěvky nebo podcasty (např.: ve wordpressu lze snadno realizovat jen instalací pluginu)
* WSDL: Pokud jste chodili na softwarové inženýrství, tak jsem vám o něm vyprávěl. Jedná se o jazyk, kterým se popisují služby, které jsou přes své rozhraní poskytovány uživatelům.
* SOAP: Pokud jste chodili na softwarové inženýrství, tak jsem vám o něm vyprávěl. Jedná se o protokol, kterým přistupuje k službě. Má stále využití u větších systémů, avšak bylo nahrazeno jednoduším řešením ve formě REST aplikací.
* RDF: Jedná se o způsob popisu webových zdrojů (stránky, multimediální objekty, soubory) na serveru. Tento jazyk je jeden z navržených pro tvorbu otevřených dat na 4. až 5. úrovni, takže podle toho, zda otevřená data (open-data) uspějí, tak tento XML jazyk bude nebo nebude v budoucnu obsolete. Vzhledem k přístupu úřadů v otevírání dat, kdy úředník nahraje pdf na web a tím má hotovo, tak pochybuji o budoucnosti.

Bližší informace o zmíněných službách naleznete: [ZDE](https://www.w3schools.com/xml/xml_services.asp)

#### Prezentace SMIL

SMIL (Synchronized Multimedia Integration Language) je jazyk, který je využíván podle názvu pro synchronizaci (zobrazování v čase) multimediálních objektů, které propojuje svým jazykem do jednoho celku. Tuto technologii znáte možná z MMS zpráv, což jsou SMS zprávy obohacené o multimediální prvky.


**Úkol 3.1 - Vytvoření SMIL prezentace**

#### Vektorová grafika SVG

SVG (Scalable Vector Graphics) je formát vektorové grafiky, jejíž data jsou zapsána ve formátu XML. Tento datový formát využívá například vektorový grafický editor Inkscape. Kromě toho některé webové portály si tím urychlují načítání svých stránek (např.: Tinder), jelikož mohou grafické prvky nahradit procedurálně generovanou vektorovou grafikou namísto obrázku. Formát má několik výhod oproti standardním postupům, které se dozvíte na následující stránce: [ZDE](https://www.w3schools.com/graphics/svg_intro.asp).

SVG obrázek se uvozuje do speciálních html značek SVG. Následují značky pro tvorbu grafických elementů [ZDE](https://www.w3schools.com/graphics/svg_inhtml.asp).

SVG umožňuje tvořit následující geometrické útvary:
* obdélníky: [ZDE](https://www.w3schools.com/graphics/svg_rect.asp)
* kružnice: [ZDE](https://www.w3schools.com/graphics/svg_circle.asp)
* elipsy: [ZDE](https://www.w3schools.com/graphics/svg_ellipse.asp)
* přímky: [ZDE](https://www.w3schools.com/graphics/svg_line.asp)
* mnohostěny (polygon): [ZDE] (https://www.w3schools.com/graphics/svg_polygon.asp)
* vícenásobné přímky: [ZDE](https://www.w3schools.com/graphics/svg_polyline.asp)
* cesty: [ZDE](https://www.w3schools.com/graphics/svg_path.asp)
* text: [ZDE](https://www.w3schools.com/graphics/svg_text.asp)

SVG prvkům lze nastavit šířku tahu: [ZDE](https://www.w3schools.com/graphics/svg_stroking.asp) a také na ně můžete aplikovat filtry: [ZDE](https://www.w3schools.com/graphics/svg_filters_intro.asp). Tde je ukázka aplikace filtru pro rozmazání: [ZDE](https://www.w3schools.com/graphics/svg_fegaussianblur.asp).

Dále můžete prvkům přidat stíny: [ZDE](https://www.w3schools.com/graphics/svg_feoffset.asp) nebo vytvářet barevné přechody (gradient) pomocí lineárního přechodu barev: [ZDE](https://www.w3schools.com/graphics/svg_grad_linear.asp) nebo radiálního přechodu barev: [ZDE](https://www.w3schools.com/graphics/svg_grad_radial.asp).

SVG natolik mocné, že můžete vytvářet i grafy: [ZDE](https://css-tricks.com/how-to-make-charts-with-svg/).

Prvky můžete snadno animovat: [ZDE](https://jenkov.com/tutorials/svg/svg-animation.html) a dokonce je můžete i stylovat pomocí kaskádových stylů: [ZDE](https://jenkov.com/tutorials/svg/svg-and-css.html).

**Úkol 3.2 - Vytvoření animovaných SVG diagramů**

Vaším Úkolem je vytvořit diagram navigace na vašem webovém portálu pomocí animovaného SVG diagramu. Tzn. vizualizujte pomocí jednoduchých tvarů, jaký je postup používání vaší stránky a co nalezne v jednotlivých záložkách uživatel vašeho webového portálu.

Pomocníkem vám může být tato stránka, kde vidíte SVG kód "komplexních" obrázků: [ZDE](https://www.freecodecamp.org/news/svg-tutorial-learn-to-code-images/).

#### Notifikace RSS

Používá se pro zaslání upozornění o vydání nového příspěvku do RSS čteček. Díky tomu, že lidé již nejsou příliš zvyklí používat RSS čtečky (víceméně jen IT komunita je dnes používá), tak bude za pár let obsolete. 

**Úkol 3.3 - Vytvoření RSS feedu**

https://www.w3schools.com/xml/xml_rss.asp

#### Webové služby

RDS (Resource Description Framework) je jazyk pro popis prostředků (stránky, multimediální soubory jako podcasty) na webovém portálu. 


https://www.w3schools.com/xml/xml_rdf.asp

https://www.w3schools.com/xml/xml_wsdl.asp

https://www.w3schools.com/xml/xml_soap.asp

https://roytuts.com/consume-soap-web-service-in-php/