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

... lorem ...

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

Kontextové diagramy jsou diagramy, které používají systémový inženýr pro návrh systému holistickým způsobem. Jejich cílem je, aby vývojáři pochopili, jak vyvíjený software přispívá do celkového obrázku k řešení cílu. 

<img src="./soubory/kontext.png" alt="kontextový diagram pro systém" style="width: 600px;"/>



#### S3.2 - Návrh architektury


#### S3.3 - Návrh komponent

Poté, co máme architekturu, tedy rozdělení softwarového systému na subsystémy a jejich komponenty, tak můžeme začít navrhovat samotné komponenty. Struktura komponenty závisí na použitém paradigmatu programování:

1. Procedurální programování: komponentou jsou moduly, atributy jsou globální proměnné a operacemi jsou funkce a procedury
2. Objektově-orientované programování: komponentou je třída, atributy jsou členské proměnné (datové členy) a operacemi jsou metody.
3. Funkcionální programování: komponentou jsou moduly, operacemi jsou funkce, atributy neexistují (resp. v čistě funkcionálním přístupu neexistuje stav, takže funkce vrací data, která se ihned konzumují jinými funkcemi).

**UML**

... UML jako takové ...

**UML diagramy pro procedurální programování**

... UML ... pro moduly a funkce

**UML diagramy pro objektově-orientovaní programování**

... UML ... pro třídy

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

Dekorátor je návrhový vzor, který umožňuje vložit do komponenty nové chování. Mějme třídu NotifikátorEmailu. Tato třída je odpovědná za to, že ve stavové liště počítače se objeví notifikační zpráva o příjmu nového emailu. Řekněme, že v budoucnu přišel požadavek na to, aby třída uměla přijímat notifikaci i ze Slacku, Discordu, WhatsAppu, aj. Jelikož v této fázi je třída již uzavřena k přepsání, ale otevřena z rozšíření (open-closed princip), tak ji určitě nebudeme přepisovat. Můžeme tedy jen rozšířovat, jenže to vznikne velké množství potomků, jelikož podle nainstalovaných aplikací bude aplikace notifikovat jen příslušné aplikace. Pokud bychom všechen nový kód narvali do jednoho potomka, dojde k vytvoření božské komponenty, která umí všechno a nemá tedy jednu odpovědnost - porušení single-responsibility principu.

Muší váha je návrhový vzor, který umožňuje ...

Most je návrhový vzor, který umožňuje ...

Kompozit je návrhový vzor, který umožňuje ...

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



#### S3.5 - Návrh uživatelského rozhraní

### On-site cvičení


#### C3.1 - Tvorba kontextového diagramu

#### C3.2 - Výběr vhodného architektornického vzoru

#### C3.3 - Třídní diagramy pro architektonický vzor

#### C3.4 - Docker-compose soubor pro architekturu z mikro-služeb

#### C3.5 - Návrh uživatelského rozhraní ve Figma