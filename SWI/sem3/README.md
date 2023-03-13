# Softwarové inženýrství

## Seminář 3 - Návrh architektury softwaru

Obsah semináře:
* [Návrh systému](#s31---návrh-systému)
* [Návrh architektury](#s32---návrh-architektury)
* [Návrh komponent](#s33---návrh-komponent)
* [Návrhové vzory](#s34---návrhové-vzory)
* [Návrh uživatelského rozhraní](#s35---návrh-uživatelského-rozhraní)
* [On-site cvičení](#on-site-cvičení)

### Samostudium před seminářem

V této lekci se dozvíte spousty spousty opravdu spousty informací o tom, jak modelovat software. A to existuje ještě mnoho dalších informací na internetu a knihách. Přeji příjemné noční počtení :).

Při návrhu softwaru jsou se můžeme setkat s celkem 4 rolemi návrhářů. Často všechny role zastupuje stejný člověk, ale u velkých projektů mohou být v praxi oddělené:

* Systémový inženýr (System inženýr)
* Softwarový architekt (Software architect)
* Návrhář komponent (Component designer)
* Návrhář uživatelského rozhraní (User-interface designer)

Systémový inženýr navrhuje prvky a propojení systémů pomocí holistického přístupu. Holistický přístup k problému je takový přístup, ve kterém se považuje systém za více než součet jeho komponent, propojení komponent pro vzájemnou spolupráci udává výsledné vlastnosti systému. U systémového návrhu se navrhuje, jak vyvíjený softwarový systém, hardware na kterém software poběží a uživatelé softwaru pomáhá k řešení problému klienta. Užitečným nástrojem systémových inženýrů jsou vysoce abstraktní diagramy vyvíjeného systému, které se nazývají kontextové.

Softwarový architekt navrhuje softwarový systém (tedy dílčí komponentu z návrhu systémového inženýra). Konkrétné navrhuje, z jakých dílčích podsystému a komponent podsystémů bude výsledný software sestaven (podsystém je kolekce kontextově propojených komponent - spolupracují za dosažením kritické dílčí funkcionality). Při návrhuje přemýšlí nad systémem jako černou skříňkou, která má veřejné vstupy a výstupy, určené veřejným rozhraním komponent. Užitečným pomocním pro architekty jsou architektonické vzory, což jsou typická schémata propojených podsystémů, která se ve světě vývoje softwaru vyskytují. Architekt doplní vzor o dilčí komponenty a definuje jejich rozhraní.

Návrhář komponent se zabývá vnitřní strukturou a běhovým (run-time, tedy po spuštění) chováním komponent, které softwarový inženýr navrhl. Navrhuje atributy (v pythonu datové členy) a chování (v pythonu metody) a případně implementuje i jejich základní strukturu. Návrháři komponent bývají často mediorní/seniorní programátoři (zejména v agilním vývoji). Junioři pak implementují a upravují dílčí funkcionality metod změnou/doplněním vybraných řádků. Jelikož architekt často neodhadne všechny dílčí nutné komponenty, tak navrhuje jen klíčové komponenty. Návrháři navrhují i nové komponenty. Mohou se však dostat se stávající navrženou architekturou do typických návrhových problémů. Užitečným pomocníkem pro řešení takových problémů jsou návrhové vzory (design patterns). Jedná se o doporučené postupy jak řešit problémy, kterými jsou například exploze potomků (potomek je rozšířením uzavřeného rodiče podle tzv. open-closed principu) nebo exploze parametrů konstruktorů. Dalším pomocníkem jsou UML diagramy (Unified Modelling Language, jednotný modelovací jazyk). Jedná se o rodinu diagramů, kterými lze modelovat jakékoliv systémy, podsystémy a jejich komponenty. Z některých diagramů lze vygenerovat i funkční kód, který si pak junior programátor doplní (xUML, tzv. eXecutable UML, spustitelné UML).

Návrhář uživatelského rozhraní je osoba, která je zodpovědná za návrh toho, jak se bude se systémem interagovat. Jelikož v dnešní době je konkurence vysoká a díky různým knihovnám je snadné rychle vyvíjet software, tak kvalitní užitečné uživatelské rozhraní je způsob, jak spolu konkureční vývojářské skupiny soutěží i pozornost potenciálních klientů. Stejně tak lidi jsou rigidní (neohební, špatně se učí nové věci), tudíž každý nový software ve firmě nepřijímají zrovna kladně, pokud mají své postupy již zaběhnuté ve spolupráci se starým softwarem (manažer si ale nový software přeje, uživatelé ne). Proto se v poslední dekádě rozdělila oblast návrhu uživatelského rozhraní na dílčí specializované oblasti, na které se najímají návrháři:

* UI (User-Interface) návrhář - zabývá se vzhledem uživatelského rozhraní
* UX (User-eXperience) návrhář - zabývá se návazností prvků uživatelských rozhraní tak, aby byl (po kliku sem se objeví tato stránka nebo toto modální okno)
* IX (Interaction-eXperinece) návrhář - zabývá se návrhem interakce s prvky (co uvidí uživatel při kliku na prvek - probliknutí, ohraničení rámečkem, posouvání prvků mezi sebou, atd.)

Hlavním pomocníkem těchto návrhářů jsou softwary pro tvorbu základního strukturního vzhledu (tzv. wire frame), software pro tvorbu vzhledu a interakcí a bitmapové a vektorové grafické editory. V poslední době jsou velice populární 2 aplikace - Figma a Adobe XD.

#### S3.1 - Návrh systému

Kontextové diagramy jsou diagramy, které používají systémový inženýr pro návrh systému holistickým způsobem. Jejich cílem je, aby vývojáři pochopili, jak vyvíjený software přispívá do celkového obrázku k řešení cílu. Z těchto diagramů by měl tým návrhářů být schopen vyčíst jaké entity interagují se systémem, kde jsou hranice systému, vztah systému k externím komponentám (jiné aplikace).

<img src="./soubory/kontext.png" alt="kontextový diagram pro systém" style="width: 600px;"/>

Kontextové diagramy se skládají z následujících prvků:

* Produkt (kružnice) - systém nebo entita, která interaguje se systémem.
* Agent (obdélník) - externí systém nebo externí entita, který není součástí systému, ale interaguje se systémem (ty produkty, které nelze ovlivnit).
* Tok (spojnice) - představují tok dat mezi entitami, tok je popsán komentářem, který vyjadřuje, co se tokem koná.


#### S3.2 - Návrh architektury

Komponenty se navrhují do nějakého diagramu, který vyjadřuje podstatu komponent (například diagram tříd z UML). Topologie (propojení) komponent se typicky řídí nějakým vzorem, kterým říkáme architektonické vzory. Architekt musí tedy zvolit dobrý architektonický vzor a dosadit do něj alespoň podstatné komponenty bez velkých detailů. Takže stačí nazvat obdélníky názvama komponent, které vyjadřují dostatečně jejich účel a vhodně je propojit, kde dobrým způsobem propojení je vybraný architektonický vzor.

Mezi základní architektonické vzory patří:
1. Vrstevnatá architektura (Layered architecture)
2. Klient-server (Client-server)
3. Pán-otrok (nazvěme to nově Hlavní-Vedlejší kvůli BLM hnutí v USA)
4. Roury-filtry (Pipes and filters)
5. Zprostředkovatel (Broker)
6. Peer-to-Peer
7. Událost-sběrnice (Event-bus)
8. Model-View-Controller (MVC)
9. Tabule (Blackboard)
10. Tlumočník (Interpreter)

**Vrstevnatá architektura**

Vrstevnatá architektura je architektura softwaru, kterou znáte například z OSI/ISO modelu protokolového zásobníku z počítačových sítí nebo z jeho praktické realizace TCP/IP protokolového zásobníku. Jedná se o užitečný vzor, který lze použít pro tradiční stolní aplikace i webové e-commerce aplikace. Princip vzoru je dekompozice programu na N vrstev, kde tradičně máme minimálně 4 vrstvy:
* Prezentační vrstva: vrstva grafického rozhraní, tedy komponenty, které uživatel vidí a přes které interaguje s aplikací.
* Aplikační vrstva: jedná se o takové operace, které využívají aplikačně nezávislé služby z vrstvy business logiky a konají aplikačně závislý kód. Tyto operace úzce souvisí s GUI prvky prezentační logiky.
* Vrstva business logiky: jedná se o služby, tedy komponenty, které konají uživatelem žádané činnosti. Tyto služby by mělo jít využít i v jiné aplikaci.
* Vrstva datového přístupu: jedná se o komponenty, které umožňují persistenci (zachování i po vypnutí) dat, takže databáze.

**Klient-server architektura**

V tomto vzoru se nachází jedna hlavní komponenta zvaná server, ke které se připojují ostatní komponenty, které nazýváme klienty. Server poskytuje klientům služby, o které server žádají. Server neustále naslouchá klientům, ale může je i prioritizovat v prioritní frontě. Pro vás se jedná o jeden z nejznámějších vzorů, jelikož na jeho principu fungují veškeré cloudové služby: emailový schránka, stremovací servery jako Netflix, Cloudová úložiště, aj.

**Hlavní-vedlejší architektura**

V tomto vzoru hlavní komponenta rozděluji práci vedlejším komponentám. Vedlejší komponenty provedou výpočetní operaci a navrátí výsledek hlavní komponentě. Ta následně výsledky vedlejších komponent zaprocesuje. Tato architektura může být využita v cloudových databázích s redundancí nebo chytrých domácích úložištích.

**Roury-filtry architektura**

Vzor Roury a filtry je vzor, ve kterém dochází k postupnému zpracování vstupních dat skrze sekvenci aktivity. Těmto aktivitám se říká filtry. Vstup jde první rourou do prvního filtru, který zpracuje data a zašle je upravená druhému filtru druhou rourou. Takto se sekvence opakuje až do posledního filtru. Roury nemusí být jen zcela propustné kanály, ale mohou obsahovat i nějaký synchronizační algoritmus, například buffering. Tento vzor se používá pro psaní aplikací, které zpracovávají data. Příkladem je ETL transformace: Extract-Transform-Load, kde se nejprve data získají z nějakého zdroje (například webscrapping), následně se transformují do vhodné podoby a uloží do databáze. Transform může být sám o sobě sada filtrů, propojených rourama. Další aplikací jsou překladače programovacích jazyků, které se skládají s pustupně navazujících fází, které transformují vždy svůj vstup a předají ho jako pozměněný výstup další fáze: lexiální analýza, syntaktický analýza, sémantická analýza, optimalizace, generování spustitelného souboru.

**Zprostředkovatel architektura**

Vzor zprostředkovatel je architektura, ve které se nachází komponenta zvaná zprostředkovatel. Zprostředkovatel komunikuje se servery, které poskytují služby klientům, a klienty, které žádají služby od serverů. Pokud má klient zájem o službu serveru, tak požádá o službu zprostředkovatele. Zprostředkovatele vybere vhodný server, kterého o službu pro klienta požádá. Zprostředkovatel vybírá vhodný server podle různých parametrů - typ služby, vytíženost serveru, atd. Servery tedy musí hlásit své informace nebo si je musí zprostředkovatel ukládat a vypočítávat. S takovou architekturou se setkáte zejména u aplikací s veledaty. Pokud jste někdy slyšeli o big data technologiích nebo o brokerech e-shopů s velkým vytížením jako jsou technologie Apache Kafka, RabbitMQ, JBoss Messaging, tak to je přesně ono.

**Peer-to-Peer architektura**

V této architektuře jsou komponenty zároveň servery i klienty. Komponenty se vzájemně žádají o služby. Jedná se tedy o způsob polo-duplexní komunikace z počítačových sítí, kde jeden uzel je příjemcem a druhý vysílačem, jen tady se střídají role klient a server. Tuto architekturu znáte z aplikací na sdílení obsahu jako jsou různé torrenty nebo různé aplikace vystavěné na block-chainu.

**Událost-sběrnice architektura**

Tato architektura je typická pro mobilní aplikace (ve smyslu aplikace pro mobilní telefony ... ne že by ta aplikace někam utíkala). V této architektuře se setkáme se 4 typy komponent:

* Zdroje událostí (Event sources)
* Naslouchači událostí (Event listeners)
* Kanály (Channels)
* Událostní sběrnice (Event bus)

Událostní sběrnice je komponenta, která obsahuje kanály. Kanály jsou cesty pro zprávy. Zdroje událostí zasílají na vstup kanálu zprávy a naslouchači z kanálů zprávy přijímají. Naslouchači se registrují pro náslech z vybraných kanálů. 

**MVC architektura**

Jedná se o jednu z nejznámějších architektur pro programátory, kteří nikdy o problematice architektur neslyšeli. Pomocí této architektury se typicky staví webové aplikace, jelikož na tomto principu fungují webové frameworky jako je Ruby on Rails (Ruby), Django (Python), Laravel (PHP), ASP.NET (C#), aj. Aplikace je rozdělena do tří částí:
* model - obsahuje business logiku a data
* view - zobrazuje data uživateli
* controller - zpracovává data uživatele

Existují různé variace a rozšíření této architektury. Typicky se z modelu ještě oddělují služby (business logika) do Services a v modelu zůstávají jen data. Z dat se dále ještě oddělí logika práce s daty od dat samotných a vznikne tak část Repository, která obsahuje operace nad daty (metody nad objektově namapovanými entitami databáze nebo query dotazy - tzv. native queries).

Typický tok dat pak vypadá následovně (rozšířený model, typický třeba pro Spring framework v Javě):
1. Klient vidí data v pohledu View (např.: webová stránka), ve kterém něco zašle formulářem.
2. Controller zpracuje zaslaná data a podle vstupního pole a dat zavolá službu ze Services.
3. Zavolaná služba provede algoritmus a zavolá Repository, které má data persistentně změnit.
4. Repository má sadu metod pro CRUD operace (Create, Read, Update, Delete) nebo nějakou složitější operaci pomocí SQL/CQL/PSSQL, TSQL a Bůh ví jakého dalšího SQL dotazu (tzv. native query).
5. Model je pak sada definovaných relačně namapovaných objektů nebo dokumentů, která provedou pomocí getterů/setterů práci s databází.

**Tabule (Úložiště) architektura**

Tato architektura je velice zajímavá, jelikož se s ní běžně nesetkáte, pokud neděláte datové vědy. Využití je zejména v oblasti umělé inteligence. Architektura se skládá z následujících komponent.

* Tabule - jedná se o globální paměťový prostor, obsahující data (stav tabule). 
* Zdroje znalostí - komponenty, které obsahují algoritmy pro vyhledávání v datech tabule a výpočtu nového stavu tabule.
* Řadič - komponenta, která koordinuje práci zdrojů znalostí nad tabulí. 

Představit si to můžeme na příkladu výuky v učebně. Na tabuli je nějaký problém, např.: příklad na výpočet kořenů kvadratické rovnice. Žáci mají krok za krokem výpočítat na tabuli řešení problému: určení diskriminantu, výpočet prvního kořene, druhého, slovní zápis řešení, atd. Učitel je řadičem, zdroje znalostí jsou žáci. Žáci si čtou aktuální obsah na tabuli a pokud tuší, jak provést změnu obsahu tabule (ví, jak na další krok výpočtu), tak se přihlásí o slovo. Řadič (učitel) vybere konkrétní zdroj znalostí, který zapíše na tabuli nový krok, tedy změní stav tabule. 

Tento vzor se používá v oblasti zpracování přirozeného jazyka, rozpoznání řeči, identifikace a sledování vozidel, interpretace signálů a dalších oblastí umělé inteligence.

Tato architektura je také mimo oblast umělé inteligence známá pod pojmem repozitář/úložiště.

**Tlumočník architektura**

Vzor tlumočník (asi to čtěte jako interpetr, což se ustálilo v české programovací terminologie) je vzor, který se používá pro interpretaci formálního jazyka, tedy jeho pochopení ke spuštění požadovaných operací. Vzor čte datový soubor s jazykem řádek po řádku a interpretuje, co má s řádkem dělat. Používá se u SQL dotazů, programovacích jazyků, komunikačních protokolů. Hlavní myšlenka spočívá v tom, že obdržené jednotky jazyka (symboly, lexémy, tokeny, různé obory to nazývají různě) se rozdělují na terminály a neterminály (o tom se budete učit v kurzu automatů a formálních jazyků). Neterminály se dále dělí na další terminály a neterminály, zatímco terminály se již na nic nedělí (listy stromu). Analýzou terminálů a neterminálů získáte strom, který vyjadřuje operace nad listy. Tyto operace jsou ještě závislé na kontextu. Po analýze lze spouštět operace nad listy v nějakém kontextu (stav aplikace) a provádět něco užitečného (například REPL jazyka Python). S tímto vysoce specializovaným architektonickým vzorem se setkáte v kurzech jako jsou doménově-specifické jazyky.

#### S3.3 - Návrh komponent

Poté, co máme architekturu, tedy rozdělení softwarového systému na subsystémy a jejich komponenty, tak můžeme začít navrhovat samotné komponenty. Struktura komponenty závisí na použitém paradigmatu programování:

1. Procedurální programování: komponentou jsou moduly, atributy jsou globální proměnné a operacemi jsou funkce a procedury
2. Objektově-orientované programování: komponentou je třída, atributy jsou členské proměnné (datové členy) a operacemi jsou metody.
3. Funkcionální programování: komponentou jsou moduly, operacemi jsou funkce, atributy neexistují (resp. v čistě funkcionálním přístupu neexistuje stav, takže funkce vrací data, která se ihned konzumují jinými funkcemi).

**UML**

Jednotný modelovací jazyk je sada diagramů, které lze použít pro modelování jakéhokoliv systému. V praxi se jedná o dominantní způsob jak vyjadřovat strukturu a chování systémů. Ještě se používají BPMN diagramy pro podnikové procesy (Business Process Modeling Notatin). Diagramy se rozdělují do 3 kategorií:

1. Diagramy struktury - používají se pro modelování struktury softwaru, tedy z jakých komponent se software skládá (statický aspekt softwaru).
2. Diagramy chování - používají se pro modelování chování softwaru, tedy co se musí dít uvnitř a vně systému (dynamický aspekt softwaru).
3. Diagramy interakce - používají se pro modelování toku dat a řízení uvnitř systému (podmnožina chování).

Diagramy struktury jsou následující diagramy:
* diagram tříd (class diagram) - nejpoužívanější, používá se pro modelování softwaru s paradigmatem OOP, tedy komponenty jsou třídy.
* diagram objektů (object diagram) - podobný diagramu tříd, jen se zde vyskytují instance tříd. Pomáhá lepšímu pohledu na zhmotněný (rozeběhnutý) software.
* diagram komponent (component diagram) - každá komponenta je podsystém, který se skládá z dílčích komponent. Podsystémy spolu komunikují. Slouží pro lepší přehled u velkých systémů.
* diagram balíčků (package diagram) - podobné jako diagram komponent, ale balíček je něco obecnějšího. Zatímco komponenta je samostatně existující kus softwaru s rozhraním (třeba třída nebo modul funkcí), tak balíček je cokoliv spolu souvisejícího (datové zdroje, software, konfigurační soubory, atd.). 
* diagram nasazení (deployment diagram) - ukazuje vztah mezi softwarem a hardwarem, na kterém bude software nasazen. Užitečné pro modelování distribuovaných aplikací, kde spolu hardwarové uzly komunikují.
* diagram složené struktury (composite structure diagram) - málo používáný diagram, který modeluje vnitřní strukturu tříd. 
* diagram profilů (profile diagram) - jedná se o další velice specifický diagram, který slouží pro rozšíření UML diagramů o další prvky. Je to takový způsob, jak si customizovat UML.

Diagramy chování jsou následující diagramy:
* diagram případů užití (use case diagram) - důležité diagramy, které se v sekvenčních metodikách vývoje softwaru používají pro zakreslení funkčních požadavků na software. Ukazují, jak jednotlivé role interagují se systémem a žádají jeho služby (případy použití).
* diagram aktivit (activity diagram) - také velice důležité diagramy, které modelují podnikové procesy. Jelikož software přispívá k plnění podnikových procesů, tak modelují i tok používání softwaru a jeho výstupů. 
* stavový diagram (state machine diagram) - modelují stavy systému při interakci agentů se systémem. Jedná se o konečný automat.

Diagramy interakce jsou následující diagramy:
* sekvenční diagram (sequence diagram) - ukazuje sekvenci událostí v čase zhora dolu s důrazem na pořadí. Vyjadřuje návaznost spolupráce komponent.
* diagram časování (timing diagram) - ukazuje sekvenci událostí v čase zleva doprava s důrazem na délku událostí (oproti sekvenční diagramu). Důležité pro real-time systémy.
* diagram komunikace (communication diagram) - podobné jako sekvenční diagramy, jen komponenty jsou třídy, které si vyměnují zprávy. Jedná se o lepší diagram pro OOP.
* diagram přehledu interakcí (interaction overview diagram)  - podobné, jako sekvenční diagram, jen prvky mohou být subsystémy, obsahující interakční diagramy (je to tedy takový sekvenční diagram diagramů - sekvenčních, časových, komunikačních).


Nebudeme si nic nalhávat. V praxi jsou lidé líní modelovat software. Proto rozdělujeme využití UML diagramů na dvě kategorie:

* dopředný návrh = návrh pomocí UML modelů je sestaven dříve, než se začne programovat. Cílem je poskytnout programátorům přehled o vyvíjeném softwaru.
* zpětný návrh = návrh pomocí UML modelů je sestaven poté, co se doprogramovalo. Cílem je dokumentace softwaru pro lepší udržitelnost.

**UML diagramy pro procedurální programování**

Pokud budete komponenty vyjadřovat pomocí procedur a funkcí, které jsou v balíčkách, pak bych doporučoval následující diagramy:
* diagram komponent
* sekvenční diagram
* stavový diagram
* diagram případů užití

Diagramy komponent dokáží modelovat procedury a funkce s rozhraním. Sekvenční diagram pak ukazuje návaznosti komunikace komponent. Pro specifický software, který mění stav se vyplatí stavový diagram. Diagram případů užití je dobrý pro propis toho, jak se bude se softwarem interagovat. Minimálně zkuste diagram komponent, ideálně všechny.

**UML diagramy pro objektově-orientované programování**

Pokud budete komponenty vyjadřovat pomocí třídy, pak bych doporučoval následující diagramy:
* diagram tříd
* sekvenční diagram
* diagram případů užití

Diagramy tříd dokáží modelovat třídy z OOP. Sekvenční diagram pak ukazuje návaznosti komunikace komponent. Diagram případů užití je dobrý pro propis toho, jak se bude se softwarem interagovat. Minimálně zkuste diagram tříd, ideálně všechny.

**Návrhové principy komponent**

Při návrhu architektury softwaru pomocí komponent se využívá několika návrhových principů pro správně navržené komponenty:
1. Modularizace (modularization)
2. Abstrakce (abstraction)
3. Zapouzdření (encapsulation)
4. Propojení (coupling)
5. Soudržnost (cohesion)
6. Rozdělení rozhraní od implementace (separation of interface and implementation)
7. Dostatečnost (sufficiency)
8. Celistvost (completeness)

**Modularizace**

Návrhový princip modularizace říká, že návrhář komponenty musí rozdělit komponenty a subsystémy architekta na dílčí komponenty, které mají oddělené úkoly. Jelikož architekt přemýšlí vysokoúrovňově, tak není vhodné pro budoucí udržitelnosti navrhnout architektovo komponenty v instantizovatelné podobě. Došlo by k tomu, že mají příliš atributů a příliš metod. Mohou tak vzniknout tzv. božské komponenty, které umí všechno a zbytek komponent neumí málo. Kód se tak stává prakticky striktně imperativním s hromadou řádků pod sebou. Stejně tak je nutné rozdělit i chování jedné komponenty do řady funkcionálně oddělitelných operací (v OOP to budou metody).

<img src="./soubory/modularizace.png" alt="komponenty s nevhodnou modularizací" style="width: 600px;"/>

Jedná se o nejdůležitější návrhový princip, jelikož kvalita modularizace má dramatický dopad na udržitelnost softwaru. Modularizací komponent dochází k modularizaci uživatelských požadavků, testových případů a lepší dělby práce. Pokud jedna komponenta provádí většinu funkcionálních požadavků, tak se vám bude velice špatně testovat. Stejně tak se vám bude nepřijemně dělit práce mezi programátory. Na kanban tabuli budou všechny papírky při nejlepším metody stejné třídy. Otázkou však je: "Jak moc podrobně musím modularizovat komponenty?", tedy otázkou zůstává míra granularity. Modularizaci si můžeme představit jako strom a vy stále přemýšlíte, jestli máte rozdělit podčást stromu na další větve nebo nikoliv. S volbou vhodné granularity vám pomohou další dva principy: abstrakce a zapouzdření.

**Abstrakce**

Návrhový princip abstrakce říká, že návrhář komponenty má zaměřit pouze na podstatné detaily modelované entity. Zatímco princip modularizace říká co má být uděláno - architekt má dělit komponentu, tak princip abstrakce říká jak má dělit komponentu - na takové dílčí komponenty, které zachycují všechny podstatné charakteristiky. Abstrahují se atributy (data) a operace (chování). Dobrou pomůckou pro mě vždy bylo, že komponentu dělím na to, co stále dokážu pojmenovat podstatným jménem. Zároveň takto vzniklá dílčí komponenta je stále abstrakt a nemusí v jejím návrhu být nic, co určuje technické reálie, tedy již v názvu je zmíňka o nečem, co vyjadřuje implementační detaily.

<img src="./soubory/abstrakce.png" alt="komponenty s nevhodnou abstrakcí" style="width: 600px;"/>

Př.: Mějme komponentu PsíÚtulek. Tato komponenta představuje informační systém pro psí útulek s operacemi jako: přidej_psa(), odeber_psa(), přidej_kotec(), atd. Tuto komponentu můžeme dál dělit, jelikož když si představíme reálný psí útulek, tak v něm nalezneme kotce (a korce jsou v naší komponentě jako atribut). Rozdělíme tedy komponentu PsíÚtulek na agregaci Kotců. Stejně tak některé operace komponenty PsíÚtulek můžeme převést na třídu Kotec. Kotec bychom mohli dál rozdělit na Dvířka, Stěny, Misku, Jídlo v misce, atd. Dostali bychom se však do implementačních detailů toho, jak jsou kotce tvořené. Takové dělení by tedy bylo již přehnané, proto zůstanu u kotců, které abstrahují detaily toho, jak jsou kotce tvořené.

**Zapouzdření**

Návrhový princip zapouzdření říká, že návrhář komponenty má schovat implementační detaily operací. Software tedy obsahuje víc, než okolí vidí. Implementačí detaily se schovávají pomocí dvou technik:
1. veřejné rozhraní operací (interface, protocol)
2. vlastnosti atributů (properties, getters/setters, accessors/mutators)

<img src="./soubory/zapouzdreni.png" alt="systém se zapozdřením" style="width: 600px;"/

U schovávání implementačních detailů pro atributy musí návrhář komponenty dát možnost komponentně rozhodnout o tom, v jaké podobě podává svému okolí informace a v jaké podobě si je nastavuje. Také musí oddělit veřejné informace od soukromých informací, kterých se zapozdření týká. K soukromým informacím má svět přístup jen pomocí speciálních metod, kterým se říká přistupovače (accessors, getters) a měniče (mutators, setters). Veřejné informace je možné číst a měnit přímo. 

V praxi se většinou všechny atributy udělají soukromé a vygenerují se k nim pomocí vývojového prostředí nebo generativní umělé inteligence gettery a settery (vstupem bývá konstruktor). Tyto gettery a settery vždy obsahují alespoň triviální implementaci, která jen přistupuje k soukromému atributu. V případě nutnosti algoritmu je to do budoucna připraveno a není nutné měnit již existující kód, který je na atributech závislý.

Můžeme dokonce vynecháním setterů vytvořit z atributu jen atribut pro čtení, který lze však měnit interně v komponentě. Mechanismus této změny nemusí nikoho zajímat. Komponenta si informaci pro čtení mění soukromými metodami. Stejně tak lze udělat i atribut pouze k nastavení vynecháním setteru, ale to se příliš nepoužívá (v Pythonu to myslím do této doby nelze provést).

<img src="./soubory/zapouzdreni.png" alt="komponenty s nevhodným zapouzdřením" style="width: 600px;"/>

Zapouzdření operací provádíme přes rozhraní (interface v C#, protokol v Pythonu). Rozhraní je sada metod, které představují pro komponentu závazek. Pokud komponenta implementuje rozhraní, pak se zavazuje, že bude mít implementaci těchto operací. Pokud by neměla implementaci, pak porušila závazek a komponenty pracují s těmito operacemi se nemohou spolehnout na to, že komponenta umí operace, které navenek tvrdí, že umí. Komponenta má tedy více operací, než ostatní komponenty mohou volat.

Zapozdření pomáhá výběru vhodné granularity modularizace, jelikož pomáhá určit správnou míru abstrakce komponent. Pokud rozdělíme komponentu na takové dílčí komponenty, které neposkytují navenek žádné rozhraní nebo atributy, jelikož vše je již soukromé a pouze jen interně nastavitelné, tak jsme pravděpodobně modularizovali přespříliš. 

**Propojení**

Návrhový princip propojení říká, že návrhář komponenty musí dělit komponenty tak, aby propojení bylo udržitelné (ideálně nulové propojení, avšak s modularizací propojenost roste). Propojení určuje míru nezávislosti komponent. Existuje několik typu propojení:

1. Propojení obsahem
2. Propojení společným místem
3. Propojení daty

<img src="./soubory/propojení.png" alt="komponenty s nevhodnou propojeností" style="width: 600px;"/>

U propojení obsahem je jedna komponenta závislá na interních informacích a implementačních detailech operací jiné komponenty. Tohle je závažné propojení, které se by se nemělo stát, pokud jste správně použili zapozdření a abstrakci.

U propojení společným místem existuje nějaké společné paměťové místo (např.: globální proměnné, statická třída), ke kterému všechny komponenty přistupují. Změna této globální proměnné ovlivní všechny napojené komponenty. Toto propojení není tak závažné jako propojení obsahem.

U propojení daty vzniká závislost tím, že jedna producentská komponenta vrací ze své operace data, které vyžaduje operace nějaké konzumentské komponenty. Tomuto nelze zabránit.

Problém propojení je v tom, že změna kódu v tomto globálním místě (například při refaktorizaci) má dopad na všechny napojené komponenty. To může vyústit v refaktorizaci i napojených komponent. Snižuje se tedy udržitelnost softwarového systému.

**Soudržnost**

Návrhový princip soudržnosti říká, že návrhář komponenty musí modularizovat systém tak, aby moduly spolu soudržně pracovaly na úkolu. Představme si, že 3 komponenty (K1, K2, K3) mají spolupracovat na jednom konkrétním úkolu. Pokud jejich propojení bude vypadat tak, že K1 vrátí výsledek K2, která ho zpracuje a vrátí K3 a není nutné nic jiného dělat, než využívat návratové hodnoty jejich operací, pak jsou komponenty vysoce soudržné. Pokud bude nutné lepit komponenty nějakým lepidlem (glue code), pak nejsou tolik soudržné, jejich schopnost spolupracovat na řešení úkolů klesá.

Vysoká soudržnost je pozitivní, jelikož nemusíte do systému doprogramovávat mnoho kódu, avšak zvyšuje propojení komponent.

<img src="./soubory/soudržnost.png" alt="komponenty s nevhodnou soudržností" style="width: 600px;"/>

**Rozdělení rozhraní od implementace**

Návrhový princip rozdělení rozhraní od implementace říká, že návrhář komponenty musí 

<img src="./soubory/separace.png" alt="komponenty s nevhodnou separací" style="width: 600px;"/>

**Dostatečnost**

Návrhový princip dostatečnosti říká, že návrhář komponenty musí zachytit do rozhraní komponenty takové minimální množství charakteristik, aby komponenta umožňovala smysluplné interakce. Jedná se o takové charakteristiky, které bude potřebovat většina uživatelů komponenty (což budou další komponenty). 

<img src="./soubory/dostatečnost.png" alt="komponenta s nevhodnou dostatečností" style="width: 600px;"/>

Př.: Nechť existuje komponenta pro vykreslování grafů s názvem Grafátor. Rozhraní této komponenty bude využívat komponenta, která doluje data z internetu s názvem Dolovač. Dolovač získal data, která potřebuje vizualizovat od Grafátoru do jednoho grafu a potřebuje je oddělit barvami (jeden graf, více časových řad). Dolovač volá Grafátor přes jeho veřejné rozhraní. To bohužel sice obsahuje možnost vložit matici hodnot (osa y) a kategorie (osa x), avšak neobsahuje možnost zadat barvy pro každou časovou řadu. Výsledný graf bude složen jen z černobílého grafu. Komponenta Grafátor není dostatečná pro komponentu Dolovač. Jak vidíme, dostatečnost je subjektivní. Architekt musí přemýšlet o univerzálnosti komponent.

**Celistvost**

Návrhový princip celistvosti říká, že návrhář komponenty musí zachytit do rozhraní komponenty všechny podstatné charakteristiky komponenty aby vznikla vhodná míra abstrakce. Jedná se o velice pochopitelný princip. Příkladem může být komponenta s názvem Kalkulačka. Každá kalkulačka musí minimálně umět sčítat, odčítat, násobit a dělit. Pokud nějaká z těchto základních operací chybí v rozhraní, pak rozhraní není celistvou reprezentací abstrakce kalkulačky. Bude o to víc pravděpodobné, že dostatečnost (předchozí princip) bude pro některé komponenty narušena.

<img src="./soubory/celistvost.png" alt="komponenta s nevhodnou celistvostí" style="width: 600px;"/>

#### S3.4 - Návrhové vzory

Z předchozí podkapitoly je asi zřejmé, že během návrhu komponent se můžete dostat do velkého množství problémů, které nejsou už tak abstraktní, aby je šlo identifikovat v době návrhu softwarové architektury a vznikají teprv při samotném návrhu komponent. Řešením těchto problémů jsou návrhové vzory. Jedná se o široké téma, které je vhodné probrat na specializovaném kurzu (např.: v roce 2022 a 2023 to byl kurz KI/OONV - objektově-orientované návrhové vzory pod vedením Dr. Fišera a Pavla Beránka). Minimálně byste ale v této fázi měli vědět, že nějaké vzory existují a jaké problémy řeší. Tak budete vědět, co si alespoň vyhledat na internetu, až budete řešit návrhový problém. 

Návrhové vzory dělíme na 3 velké kategorie:
* Vzory tvorby (creational patterns)
* Vzory struktury (structural patterns)
* Vzory chování (behavioral patterns)

**Vzory tvorby**

Vzory pro tvorbu poskytují různé mechanismy tvorby komponent, které zvyšují flexibilitu a znovupoužitelnost kódu.

1. jedináček (singleton)
2. tovární metoda (factory method)
3. abstraktní továrna (abstract factory)
4. stavitel (builder)
5. prototyp (prototype)

Singleton je návrhový vzor, který zajišťuje, že třída může mít pouze jednu instanci, ke které mají ostatní komponenty globální přístup. Příklad může být nějaký videoherní server. Jakmile se první hráč připojí, tak vytvoříme první instance třídy GameServer. Každý další hráč, jenž se připojí, tak obdrží odkaz na tuto instanci. Kód se však nezmění. Při požádání o tvorbu instance druhým hráčem obdrží odkaz na první instanci, ale neví o tom. Tím je zajištěno, že oba hráči hrají na stejném serveru. Jiný příklad jsou jakákoliv společná datová místa, jako například databáze.

Tovární metoda je návrhový vzor, který poskytuje veřejné rozhraní pro tvorbu objektů v nadtřídě, ale nechá podtřídy implementovat svou instantizaci. Myšlenka je docela jednoduchá. Řekněme, že bychom psali GUI aplikaci (aplikace s grafickýcm uživatelským rozhraním), která je multiplatformní. Měla by fungovat jak na OS Windows, tak Linuxových operačních systémech. Využívaný GUI framework je multiplatformní, avšak existují určitá specifikace tlačítek, formulářů, textových položek pro každý operační systém. Nechť existují třídy pro generování Windows tlačítka, Linux tlačítka, Windows formuláře, Linux formuláře, atd. Vytvoříme dvě továrny a to továrnu pro Windowsové GUI prvky a Linuxové GUI prvky. Továrnám můžeme zadat, ať vytvoří prvky pro svůj operační systém. Při spuštění programu se zjistí nějakou operací z knihovny, o jaký operační systém na klientovo počítači se jedná. Podle operačního systému se nastaví továrna (samozřejmě si továrnu může nastavit klient sám). Poté se klient žádá nastavenou továrnu o tvorbu jednotlivých prvků a ona tvoří správné prvky pro správný operační systém.

Abstraktní továrna je návrhový vzor, který umožňuje tvorbu různých objektů, které mají být spojeny nějakým atributem (rodina objektů). Příklad mohou být zbraně různých typů ve hře Borderlands (revolver, SMG, odstřelovací puška, aj.) od různých značek (Hyperion, Jacobs, aj.). Máme tedy různé typy objektů různých rodin. Vzor je realizován tak, že pro každý typ produktu se vytvoří abstraktní třída (může být použito i rozhraní, pokud produkty nemají společná data). Každá značka tedy může mít různý revolver, ale všechny jsou přeci jen revolverem a mají toho mnohé společného. Liší se pouze implementací závazků (abstraktních metod). Tyto realizace abstraktních produktů jsou tvořeny konkrétními továrnami. Každá konkrétní továrna vytváří produkty své rodiny. Takže továrna Hyperion bude vytvářet své hyperionovské revolvery a SMG, které jsou implementací abstraktního revolveru a abstraktní SMG, stejně tak továrna Jacobs si bude vytvářet instance produktů SMG a revolver, které jsou implementací abstraktního revolveru a SMG. Klient si pak zvolí, kterou továrnu (rodinu produktů) chce využívat a zadá jí příkaz pro tvorbu objektu (revolver, SMG). Typicky to funguje tak, že si klient zvolí do konstruktoru nebo setterem používanou továrnu a provádí nějaký svůj vlastní kód. V určité fázi svého chování vyžaduje inicializovat produkty z nastavené továrny, tak ji využije. 

Stavitel je návrhový vzor, který umožňuje konstrukci složitých objektů krok po kroku z dílčích kroků. Kromě toho je možné provést různé reprezentace těchto dílčích kroků. Tímto způsobem se vyřešít problém obřího konstruktoru, kde je nutné zadat spousty parametrů. Příkladem mohou být videohry, kdy inicializer vojáka obsahuje příznaky, zda má brnění, štít, kopí, meč, luk, aj. Podle argumentů těchto parametrů se pak vytvoří různě vypadají voják s danou výbavou. Kromě toho voják může být i různé rasy (lidé, nemrtví, elfové, orkové, aj.). Stavitel řeší tento problém tím, že obsahuje třídu Vedoucí, která obsahuje kroky, jak vybudovat komplexní objekt (algoritmus konstrukce). Tyto kroky implementují konkrétní stavitelé, což jsou třídy implementující rozhraní Stavitel. Implementací rozhraní se zavazují, že budou umět jednotlivé kroky, se kterými Vedoucí počítá. Každý konkrétní stavitel pak představuje jinou variaci stavebního kroku (například rasy/národy ve strategických videohrách). Ačkoliv je zde podobnost mezi stavitelem a abstraktní továrnou, tak stavitel se více zaměřuje na postup konstrukce krok za krokem. Abstraktní továrny vrací instanci daného typu a dané rodiny okamžitě. Stavitel je více customizovatelný při tvorbě.

Prototyp je návrhový vzor, který umožňuje vytvořit kopii existujícího objektu aniž abychom museli přistupovat k jeho soukromým promenným, které nemají veřejný přístup pomocí getterů. Řešením problému je delegovat klonující proces na klonovaný objekt. Pokud objekt umožňuje klonování, tak si sám naprogramuje implementaci klonovací metody. Ve vzoru pouze vytvoříme jednotné klonovací rozhraní, které si všechny klonovatelné objekty implementují.

**Vzory struktury**

Vzory pro sestavování komponent do větších struktur takovým způsobem, aby struktury flexibilní a výkonné.

1. fasáda (facade)
2. adaptér (adapter)
3. prostředník (proxy)
4. dekorátor (decorator)
5. muší váha (flyweight)
6. most (bridge)
7. kompozit (composite)

Fasáda je návrhový vzor, který poskytuje jednoduché obalující rozhraní pro snadné používání kolekce objektů. Představme si nějakou aplikaci, jejíž cílem je vylepšit fotografii. Fotografie projde sadou zlepšujících operací, které jsou realizovány různými třídami, např.: UpravovačKontrastu, UpravovačBarev, aj. Tyto třídy potřebují různé informace pro svou instantizaci, které lze zjistit algoritmickým způsobem z vložené fotografie. Využití takové sady tříd a jejich nastavení pro instantizaci objektů za účelem spolupráce je značně složité. Proto obalíme instantizaci a algoritmus do nové třídy Fasáda, která skrývá tyto složité detaily. Klient pak použije jen fasádu a ta se postará o zbytek. Například Upravovač(fotografie) bude fasáda. Klient jen vloží do fasády fotografii a vyjde mu vylepšená. Je to forma zapozdření struktury komunikujících komponent.

Adaptér je návrhový vzor, který umožňuje spolupráci komponent se vzájemně nekompatibilním rozhraním. Klient chce zavolat službu nějaké komponenty svým vlastním způsobem jak chce klient. Komponenta však vyžaduje jiný způsob toho, jak zavolat její službu. Vytvoříme adaptér, který v sobě obsahuje metodu na adaptovanou službu. Dále obsahuje implementaci metody pro zavolání služby takovým způsobem, jakým chce klient (může si volání definovat rozhraním). Implementovaná metoda v adaptéru se postará o kompatibilitu volání. Klient tedy volá adaptér, který se postará o převod požadavku klient do takové formy, jakou vyžaduje adaptovaná služba. Jedná se o jeden z nejčastějších problémů v oblasti vývoje softwaru při využívání knihoven třetích stran a legacy kódů. Př.: klient chce zavolat vykresli obdélník a to tak, že zadá souřadnice levého horního rohu a pravého dolního rohu. Tento výstup klienta již nelze měnit. Knihovna pro vykreslení však vyžaduje souřadnice levého horního rohu obdélníka, šírku a výšku. Napíšeme tedy adaptér, který ve své metodě vypočítá ze souřadnic obou bodů šířku a výšku a zavolá následně službu grafické knihovny.

Prostředník je návrhový vzor, který umožňuje snížit využití výpočetních prostředků počítače tím, že vytvoří light-weight náhradu těchto náročných objektů. Představme si aplikaci, kde klientské třídy přistupují k databázi. Databáze je objekt, který obsahuje spousty dat a její instantizace zabírá velké množství operační paměti. Klienti potřebují s databází pracovat relativně často a instantizace databáze je časově náročný proces. Možností je vytvořit prostředníka, kterého budou klientské třídy volat místo databáze. Prostředník nezabírá tolik RAM a on se postará o efektivní komunikaci s databází. Může i cachovat data do určité doby a poté teprv instantizovat databázi a zapsat. Jedná se o podobný princip, jako je NoSQL databáze Redis. Ta funguje tak, že stojí jako prostředník před jinou databází, např.: PostgreSQL. Jakmile klient požádá o data z Postgres, tak to provádí přes Redis. Redis se nejprve podívá do své paměti, jestli s taková data v nedávné době nepotřeboval nějaký jiný klient (tedy jsou nacachovaná). Pokud jsou, tak vrátí nacachovanou kopii. Pokud nejsou, tak instantizuje Postgres, získá data a uloží do své cache. Tím se dramaticky zvětší výkon webové aplikace.

Dekorátor je návrhový vzor, který umožňuje vložit do komponenty nové chování. Mějme třídu NotifikátorEmailu. Tato třída je odpovědná za to, že ve stavové liště počítače se objeví notifikační zpráva o příjmu nového emailu. Řekněme, že v budoucnu přišel požadavek na to, aby třída uměla přijímat notifikaci i ze Slacku, Discordu, WhatsAppu, aj. Jelikož v této fázi je třída již uzavřena k přepsání, ale otevřena z rozšíření (open-closed princip), tak ji určitě nebudeme přepisovat. Můžeme tedy jen rozšířovat, jenže to vznikne velké množství potomků (SlackNotifier, SlackWhatsAppNotifier, atd.), jelikož podle nainstalovaných aplikací bude aplikace notifikovat jen příslušné aplikace. Pokud bychom všechen nový kód narvali do jednoho potomka, dojde k vytvoření božské komponenty, která umí všechno a nemá tedy jednu odpovědnost - porušení single-responsibility principu. Řešením je vytvořit sadu dekorátorů ke každé aplikaci (SlackNotifierDecorator, WhatsAppNotifierDecorator, atd.). Tyto dekorátor jsou třídy, umí stejné metody jako obalovaná třída, avšak dodají si vlastní kód navíc. Díky tomu, že implementují společné rozhraní, tak lze napsat dekorátor obalující dekorátor obalující dekoratáror až do posledního dekorátoru, který obaluje obalovanou třídu, jejíž chování rozšiřujeme. Stačí tedy vytvořit veřejné rozhraní k obalované komponentně a dekorátory implementují tuto metodu tak, aby se volala ze všech dekorátorů stejně. Tato dekorační metoda v dekorátoru spustí nějaký kód, pak spustí kód obalované komponenty a pak spustí svůj vlastní kód na závěr. Samozřejmě můžete spustit kód jen před nebo po volání metody obalované komponenty.

Muší váha je návrhový vzor, který umožňuje snížit paměťovou zátěž aplikace. Je typická pro problematiku videoher, kde se nachází v jednu chvíli v renderovaném prostoru (nebo na celém videoherním serveru) spousty objektů podobného typu. Například kulka z pistole nebo jiné částicové systémy. Komponenty obsahují dva typy atributů - unikátní (extrensic) a sdílené (intrisic). Aby šlo využít muší váhu, tak musí unikátní vlastnosti musí být mutabilní (lze změnit hodnotu) a sdílené vlastnosti nemutabilní (hodnoty lze jen číst). Unikátní vlastnosti jsou například poloha částice a sdílené vlastnosti jsou například textura nebo konstantní rychlost částice. Místo abychom všechny vlastnosti dali do jedné třídy Částice, tak je rozdělíme do dvou tříd: např.: Částice a PohybujícíSeČástice. Do Částice dáme všechny společné vlastnosti všech částic a do PohybujícíSeČástice dáme všechny unikátní vlastnosti. Každá částice je pak instancí PohybujícíSeČástice a obsahuje odkaz na Částici, ze které si v případě potřeby čte sdílená data. Tím se dramaticky sníží množství operační paměti, která je zapotřebí.

Most je návrhový vzor, který řeší problém exploze potomků. Řekněme, že píšete aplikaci, ve které máte několik typů jednotek - voják, lučistník, kopiník, atd. Dále mějme několik ras - lidé, elfové, nemrtví. Každá rasa může mít jakékoliv jednotky a každá jednotka je třída (LidskýVoják, ElfíVoják, LidskýLučistník, ElfíLučistník). Každá rasa má vlastní chování a každá jednotka také své vlastní chování. Tyto složeniny rasy a jednotky jsou holistické kompozity takového chování. Dekorátor nelze využít, jelikož ten se zabývá tvorbou objektů a nikoliv jejich propojením. Řešení je triviálnější, než čekáte. Asi vás napadne, že v takových situacích je možné udělat z jednoho atributu (např.: rasa) nějakou vlastnost jednotek ve formátu string a poté pomocí rozhodování řešit holistické chování. Jelikož jsme v návrhových vzorech, tak problémy budou pravděpodobně složitější, než vlastnost ve formě řetězce. Celá vlastnost musí být objektem samotným, jelikož má nějaká data a nějaké chování. Myšlenka však zůstává. Pokud lze ortogonálně separovat objekt (tzn. nějaká atributy a operace jsou na sebe kolmá, takže spolu nesouvisí a jdou oddělit), tak je oddělíme do dvou tříd. Třída jednotky a třída Rasa. Tyto dvě třídy budou abstrakty a jejich implementace budou právě jednotlivé typy jednotek a jednotlivé rasy. Propojení dosáhneme pomocí agregace, tedy potomek třídy Jednotka (např.: Lučistník) v sobě obsahuje potomka třídy Rasa (např.: Elf). Tím jsme se úspěšně vyhli problému exploze potomků.

Kompozit je návrhový vzor, který umožňuje pracovat s komponentou, jakoby se jednalo o stromovitou datovou strukturu. Jedná se o zajímavý vzor uplatnitelný při prohledávání dat v komplexních objektech. Představme si komponentu Šachy, která v sobě obsahuje seznam instancí třídy Figurka. Každá figurka má své souřadnice (řádek a sloupec šachovnice). Nás zajímá, jestli nějaká z figurek není na konkrétním políčku, protože chceme na to políčko vstoupit vybranou figurkou. Nejjednodušší řešení bude provést FOR cyklus přes všechny figurky v seznamu figurek a získat z tohoto cyklu žádanou informaci. Existuje však situace, kdy objekty v seznamu nejsou tak triviální jako figurky a obsahujou další objekty. Řešením je uvažovat ve dvou typech kategorií se společným rozhraním. Řekněme, že náš kompozit se bude skládat z tříd typu kompozit (uzel stromu) a list. Kompozity lze dále rozložit a listy již ne. Listy provádí operaci, kterou chceme (získání informace, spuštění algoritmu a jiné operace). Oba typy tříd umí metodu spusť_operaci() ze společného rozhraní. Avšak kompozity delegují spuštění na své potomky, zatímco potomci požadovanou operaci spustí. Kompozity obsahují seznam svých uzlů (další kompozity nebo listy) a metody pro přidávání uzlů, odebírání uzlů, vrať_uzel a spusť_operaci. Přidávané uzly také musí splňovat společné rozhraní. Pokud naprogramujeme tímto způsobem naší strukturu, tak ať je libovolného třídy, pak je rozložitelná kompozitem do stromu.

**Vzory chování**

Vzory pro dodávání odpovědnosti ve formě chování komponentám.

1. řetěz odpovědnosti (chain of responsibility)
2. příkaz (command)
3. iterátor (iterator) 
4. prostředník (mediator)
5. memento (memento)
6. pozorovatel (observer)
7. stav (state)
8. strategie (strategy)
9. šablonová metoda (template method)
10. návštěvník (visitor)

Řetěz odpovědnosti je návrhový vzor, který umožňuje zaslat požadavek frontě řešitelů požadavku (pipe-line), kde každý řešitel rozhodne o tom, co s požadavkem udělá a zašle to dalšímu řešiteli v řadě. Představte si, že voláte do nějakého call-centra, např.: vašeho dodavatele elektrické energie. Máte problém s tím, že vám již nefunguje půl roku elektrický proud :D. Nejprve se dovoláte nějakému obecnému operátorovi, která vás přepojí na nějakého odborného operátora. Ten vás následně přepojí na operátora, řešící nefungující elektrický proud. Ten následně vyšle technika na vaše odběrné místo. Každý řešitel vašeho požadavku má možnost s požadavkem něco dělat (např.: zapsat si problém) a přeposlat ho dál, nebo jen přeposlat dál. Hlavní myšlenka spočívá v tom, že řešitelé jsou konkrétní implementace jednotného rozhraní, které je zavazuje umět si přiřadit další řešitele v pořadí. Řešitelé si při konstrukci konstruktorem nastaví svého dalšího řešitele v pořadí a již ho nepřenastavují aby netrhali vytvořený řetěz. Kromě toho mají svou metodu pro řešení požadavku. Ta musí i rozhodnout o tom, zda požadavek vyřeší, částečně vyřeší a pošlou dále nebo ho pošlou dále. Komponenta Řetěz (pokud to neudělá klient sám) pak určuje někde ve své logice, jak budou řešitelé propojeni, tzv. instantizuje komponenty a nastaví jejich následníka. Vzhledem k tomu, že každý řešitel by měl mít část kódu společného (rozhodování o tom, zda mu náleží požadavek a zda ho přepošle dál nebo ho eliminuje) a také má odkaz na následníka, tak se zde hodí skvěle abstraktní třída.

Příkaz je návrhový vzor, který umožňuje přeměnit požadavek na samostatně existující objekt, který drží všechny potřebné informace o požadavku. Tento vzor se používá kdekoliv, kde potřebujete separovat zájmy a tyto zájmy vytváří určitou vrstvu nebo rodinu. Příkladem je naivně tvořená GUI aplikace. Aplikace má nějaké GUI prvky (tlačítko, formulář, navigační lišta, atd.). Při interakci s tímto prvkem můžete vyvolat nějakou logiku rovnou nebo lépe zavolat službu, která to provede. Pokud budou grafické prvky oddělené od logiky, pak můžeme snadno zaměnit grafické prvky za jiné bez značného přepisování aplikace. Aby šlo tyto tzv. zájmy separovat, je zapotřebí, aby GUI prvky dodaly službě všechny potřebné informace pro vykonání služby - ty se právě zabalí do příkazu. Dalším důvodem pro separaci zájmů je služba, která je možná volat z více GUI bodů. Například uložit projekt lze pomocí tlačítka na obrazovce (např. ikonka diskety), z výběrového menu (soubor - uložit) nebo klávesovou zkratkou. Jedna služba má více způsobů, jak ji zavolat. V takovém případě bychom duplikovali kód pokud bychom nevyužili návrhového vzoru Příkaz. Hlavní myšlenka je taková, že KonkrétníPříkazy jsou implementace rozhraní Příkaz. Příkaz obsahuje metodu pro spuštění příkazu. Konkrétní příkazy jsou typicky nemutabilní typy, takže je lze nastavit pouze při konstrukci konstruktorem. Při jejich zavolání se vytvoří nová instance KonkrétníhoPříkazu, do které se nastaví na koho má příkaz působit (Příjemce příkazu) a jaké jsou parametry (vše potřebné pro business logiku). Tyto KonkrétníPříkazy vyvolává nějaký Vyvolávač (Invoker). Invoker sestaví příkaz konstruktorem a spustí ho. Aby věděl jak ho spustit, tak využívá rozhraní Příkazu. KonkrétníPříkazy pak působí na svého Příjemce (Receiver), který se podívá do parametrů zaslaného příkazu a provede logiku. Tento návrhový vzor se často kombinuje s mementem pro Undo/Redo operace v editorech (Word, Excel, Powerpoint, Gimp). Doporučuji se tento návrhový vzor naučit, jelikož pravděpodobně skoro všechny aplikace, které budete dělat a klient je bude používat pro kancelářskou práci, tak vyžadují tuto schopnost. V editorech funguje tak, že Invoker je samotná GUI aplikace, která ve svém konstruktoru naváže na tlačítka, menu položky a klávesové zkratky příslušné příkazy pro open, save, copy, rename, ... konkrétní příkazy. Každý příkaz pracuje s nějakým GUI prvkem, například editorem, což je nějaké pracovní pod okénko. Tento měněný GUI prvek má příkaz v sobě nastaven (Receiver). Jakmile aplikace zaregistruje událost (klik na tlačítko), tak spustí požadovaný příkaz, který zapůsobí na příjemce a uloží se do zasobníku s historií úkonů.

Iterátor je návrhový vzor, který umožňuje procházet (traverzovat) kolekcí bez toho, aniž bychom museli odkrývat její vnitřní reprezentaci (seznam, zásobník, fronta, ntice, strom, graf). To nám umožňuje vytvořit si vlastní unikátní způsoby jak procházet komplexní komponentu z komponent dokonce různými způsoby (do hloubky, do šířky, aj.). Vzor je realizován tak, že se vytvoří rozhraní Iterator. Toto rozhraní má dvě důležité operace - získej další prvek v pořadí a příznak, zda existuje další prvek v pořadí (tzn. zda se má dále traverzovat nebo jsme na konci). Toto rozhraní implementují KonkrétníIterátory, které představují traverzní algoritmy. Například iterátor pro prochází do hloubky, iterátor pro procházení do šířky. Konkrétní iterátory v sobě obsahují algoritmy, o které se zavázeli svým rozhraním Iterátor (získání dalšího prvku a zjištění, zda jsme na konci). KonkrétníIterátory také v sobě obsahují odkaz na KonkrétníKolekci, kterou chceme iterovat, jelikož nad ní pracují. Tyto KonkrétníKolekce implementují stejné rozhraní IterovatelnéKolekce, jelikož iterátory mohou pracovat nad více kolekcema.

Prostředník je návrhový vzor, který slouží pro redukci chaotického chování mezi komponentami pomocí jednotného místa komunikace - prostředníka. Komponenty v sobě obsahují odkaz na objekt, implementující rozhraní pro prostředníky. Toto rozhraní umí jednu operaci a to zasílat zprávu zadanému příjemci. Konkrétní prostředník je pak třída, splňující toto rozhraní. Tato abstrakce pomáhá tomu, že může existovat více prostředníků (takže některé komponenty spolu komunikují skrze různé prostředníky). Konkrétní prostředník má v sobě odkaz na registrované komponenty a operaci, kterou registrované komponenty volají když chtějí poslat jiné komponentě zprávu. Myšlenka je v tom, že komponenty nemají nic vědět o jiných komponentách. Celá identifikační logika je na prostředníkovi. Když komponentaA zavolá prostředníka a zašle informaci, tak mediátor musí rozhodnout o tom, jaké komponenty mají být o zpravě informovány. Mediátor reaguje na zavolání jeho operace a volá reakční metody vybraných komponent. Mediátor v sobě může obsahovat i určitou business logiku.

Memento je návrhový vzor, který umožňuje provádět to, čemu v emulátorech videoher říkáme save-state, load-state, tedy umožňuje uložit aktuální stav objektu a později po změnách ho opět nahrát zpět. Jedná se o ukládací a nahrávací mechanismus videoher. Silnější obdoba problému je zásobník takových stavů, který znáte z kancelářských aplikací, vracející změny (šipka zpět/undo, šipka dopředu/redo). Vzor je realizován pomocí třídy Správce (CareTaker), jehož úkolem je uchovávat v sobě historii aplikace. Tato aplikace bude nazývána Původce (originator) a jeji nemutabilní stav se bude nazývat Memento. Správce v případě požadavku (undo operace) vybere ze zásobníku mement Memento na vrcholu a pošle ho Původcovi metody pro obnovení stavu (restore operace). Memento je jen jednochá třída se všemi informacemi o stavu v době uložení. Původce umí kromě nahrání mementa z minulosti i uložit nové memento na vrchol zásobníku Správce. Pokud jazyk umí zanořené třídy, pak Memento je zanořená třída uvnitř Původce. Původce pak má přístup do jeho atributů (i když jsou privátní). Naopak Správce nemůže do privátních atributů zasahovat a číst je, takže nic nepokazí. Pokud není jazyk vybaven schopností zanořených tříd (např.: PHP), pak je nutné vytvořit k Mementu rozhraní, které bude používat Správce. Toto rozhraní bude definovat jediné operace, které může Správce s mementem provádět. Původce pak provádí jakékoliv operace bez omezení, ale podmínkou jsou veřejné modifikátory přístupu (není to nejšťastnější řešení, tak radši nepoužívejte PHP :) ...).

Pozorovatel je návrhový vzor, který umožňuje vytvořit odběratelský (subscribe) mechanismus, který odběratelským třídám posílá notifikace o událostech, které se provádí na objektu, ke kterému se upsali odběrem. Pozorovaná třída, ke které se komponenty upisují se nazývá Vydavatel (Publisher). Ten v sobě agreguje Odběratele (Subscribery). Vydavatel má schopnosti zapsat nebo odepsat Odběratele (jako v emailech). Vydavatel má schopnost vyslat signál všem Odběratelům o změně jeho interního stavu dedikovanou notifikační operací. Každý, kdo chce být Odběratelem, tak musí implementovat rozhraní pro Odběratele, kde jeho povinností je implementace operace pro update (příjem zprávy). Vydavatel si může registrovat pouze ty odběratele, splňující tuto povinnost.

Stav je návrhový vzor, který umožňuje změnit chování objektu když se změní jeho interní stav (tedy dojde k nějaké změně jeho atributů setterem). Objekt se chová navenek, jakoby změnil třídu (jiné chování). Jedná se o ideální návrhový vzor pro systémy, které se chovají jako stavové automaty, tedy konečné automaty typu Mealy/Moor. Praktická implementace těchto automatů může být soubor, který se nachází v různých stavech, požadavek na Kanban tabuli, pull-request na githubu. Řekněme, že máte soubor, do kterého píšete v nějakém redakčním systému. Tento soubor vám poskytuje všechny potřebny metody pro editaci. Soubor následně publikujete a čeká na schválení od recenzentů. Recenzenti mohou provádět jiné operace se souborem - schválení, zamítnutí, aj. Soubor se může vrátit do předchozího stavu po zamítnutí nebo se může dostat do následného stavu po přijetí, kde je publikován a lidé si ho mohou prohlížet přes URL. Po určité expirační době se opět může publikovaný soubor vrátit do původního stavu a zmizet z veřejného přístupu (nějak takto fungují zpravodajské portály jako novinky.cz). Realizace vzoru je provedena tak, že všechny konkrétní stavy implementují rozhraní stav. Toho rozhraní obsahuje všechny povinné operace pro všechny konkrétní stavy. Operace navíc si implementují potomci v sobě. Dokument je pak třída, která má operaci změň stav a může ho změnit pouze za objekty, implementující rozhraní stav. Dokument má v sobě uložen aktuální stav a může využívat jeho operace. Jedná se tedy o formu rozšíření třídy pomocí agregace.

Strategie je návrhový vzor, který umožňuje vytvořit rodinu vzájemně zaměnitelných algoritmů. Skvělým příkladem je navigace v mapové aplikaci. Na mapách se můžete navigovat autem, pěšky, veřejnou hromadnou dopravou. Při výběru typu navigace vám appka ukáže jinou optimální cestu. Podle kontextu (co si vybere uživatel) se mohou algoritmy vypočítání optimální trasy měnit bez změny v kódu, jelikož jsou ze stejné rodiny a dělají stejnou činnost, jen mají jinou implementaci. Vzájemná zaměnitelnost se řeší tak, že všechny tyto algoritmy (konkrétní strategie) jsou třídy, které splňují jednotné rozhraní pro strategii.

Šablonová metoda je návrhový vzor, ve kterém jsou obecné kroky algoritmu nadefinovány v nadtřídě (struktura algoritmu), ale konkrétní implementaci kroků je na potomcích. Tento vzor se používá, pokud máte nějaký problém, ve kterém lze identifikovat obecné kroky. Konkrétní způsob realizace těchto kroků se ale liší podle kontextu. Například pokud je příliš dat, použiju takový způsob realizace. Pokud málo kroků, použiju takový způsob realizace. Některé kroky mohou být společné pro všechny potomky. Ty které si mají potomci sami doplnit, tak se vytvoří jako abstraktní metody. Příkladem může být dolovač dat z různých datových formátů - csv, pdf, xlsx, docx, html, aj. Každý dolovač bude podle formátu mít svá specifika, avšak dolování dat je proces, který je všude stejný - otevření souboru, parsování souboru, analyzování souboru, vytvoření reportu ze souboru, zavření souboru.

Návštěvník je návrhový vzor, který umožňuje oddělit chování od objektů, na které mají působit. Vypadá to, jakobyste oddělili zpětně třídu na datovou strukturu a funkce, avšak stále v objektovém paradigmatu. Realizuje se pomocí rozhraní Návštěvník, který definuje sadu polymorfních metod. To jsou takové metody, které se jmenují stejně, ale mají jiné paramety (takže v Pythonu máte smůlu). KonkrétníNávštěvníci jsou pak implementace tohoto rozhraní. Každá polymorfní metoda je chování vůči zadanému objektu. Představme si to jako učitele. Učitel může učit fyziku, matematiku, informatiku. Když jde na hodinu matematiky (třída matematiky jsou data), tak učí, ale učí didaktikou matematiky. Pokud jde na hodinu fyziky, tak učí didaktikou fyziky. Podle typu dat (kontextu) se různě chová, což je polymorfismus. Tento kontext je tvořen objektem, který nazýváme Element. Element bude rozhraní, které obsahuje metodu pro přijmutí návštěvníka. KonkrétníElementy jsou pak implementace rozhraní Element, které mají v sobě implementaci metody pro přijetí Návštěvníka. Tím jsme dostali systém, kde Elementy přijímají Návštěvníky, kteří podle toho, který Element je přijal konají různé chování. Objekt se chová různě podle toho, kde je. Za mě osobně velice zajímavý pattern :).

#### S3.5 - Návrh uživatelského rozhraní

... doplnit ...

### On-site cvičení

Cílem tohoto cvičení je navrhnout architekturu aplikace z pohledu všech typů rolí v architektonickém procesu vývoje. Vyzkoušíte si tvorbu obecného kontextového diagramu jako systémový inženýr, výběr a návrh základních komponent z pohledu softwarového architekta až návrháře komponent (záleží jak detailně budete komponenty rozebírat) a návrh uživatelského rozhraní z pohledu návrháře rozhraní. Z návrháře rozhraní si vyzkoušíte částečně všechny tři role - návrhář vzhledu, zážitku i interakce. Pro tvorbu diagramů (úkoly C3.1 až C3.3) si najděte nějaký vhodný editor UML diagramů nebo obecných diagramů. V úkolu C3.4 nejsou žádné praktické úkoly, jen si prohlédněte seznam návrhových vzorů a zamyslete se, zda se vás nějaký týká a neřeší aktuální problém již v době návrhu nebo zda bude pravděpodobně řešit problém, který v budoucnu nastane. V úkolu C3.5 si navrhnete uživatelské rozhraní v nějakém softwaru, ve kterém se vám bude dobře navrhovat. Lze využít velice šikovně i software pro prezentační snímky, protože prvky ve snímku umožňují hypertextové odkazy na jiné snímky a mohou simulovat interakci a průchod softwarem. Každopádně spíše doporučuji použít software Figma nebo Adobe XD pokud máte licenci. 

#### C3.1 - Tvorba kontextového diagramu

Hrajete si na systémového inženýra. Z úkolu z předchozí lekce si vytvořte jednoduchý kontextový diagram, který říká, z jakých hlavních subsystémů a komponent je složena vaše výsledná aplikace, kterou budete odevzdávat k zápočtu.

#### C3.2 - Výběr vhodného architektornického vzoru

Hrajete si na softwarového architekta. Na základě kontextového diagramu vyberte, jaký architektonický vzor by byl nejlepší pro váš program v jeho kontextu. Architektonický vzor doplňte o hlavní komponenty, které vytváří to nejdůležitějších ze struktury kódu. Řešte pomocí UML diagramů a vyznačte šikovně architektonický vzor (například třídy ve vrstvách, třídy zasebou v rouře, atd.). UML třídy nechte zatím jen s názvem (bez operací a atributů).

#### C3.3 - Třídní diagramy pro komponenty

Hrajete si na návrháře komponent. Pokud se vám to vejde (u jednodušší aplikace), tak do předchozího diagramu doplňte do komponent operace a atributy. Pokud se to nevejde, tak je dopňte do nového souboru, kde bude jen třídní diagram. Nezapomeňte vyznačit modifikátory přístupu, statické metody a atributy, abstraktní třídy a rozhraní, agregaci a dědičnost a jiné komponenty třídních diagramů. Vhodné jsou i poznámky pro slovní vysvětlení toho, co třída dělá.

#### C3.4 - Návrhový vzor

Pročtěte si ještě jednou (nebo poprvé, protože vím, že jste to ještě neudělali) návrhové vzory a zamyslete se, jestli ve vaší aplikace nebude jeden z nich vhodné využít (možná i více z nich). Pokud si všimnete podobnosti vašeho propojení komponent s jedním ze vzorů, tak si o vzoru více vyhledejte a ujistěte se. Vhodné použití vzorů může dramaticky zlepšit udržitelnost vaší aplikace.

#### C3.5 - Návrh uživatelského rozhraní

Ve vhodném softwaru pro tvorbu grafických prototypů (třeba Figma) navrhněte grafický prototyp vaší aplikace (ideálně stolní i mobilní verzi), která bude interaktivní.