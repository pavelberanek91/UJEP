# Softwarové inženýrství

## Seminář 2 - Inženýrství požadavků

Obsah semináře:
* [Proces inženýrství požadavků](#s21---proces-inženýrství-požadavků)
* [Sběr požadavků](#s22---sběr-požadavků)
* [Analýza požadavků](#s23---analýza-požadavků)
* [Specifikace požadavků](#s24---specifikace-požadavků)
* [Správa požadavků](#s25---správa-požadavků)
* [On-site cvičení](#on-site-cvičení)

### Samostudium před seminářem

V minulém semináři jste se poučili (snad) o procesu softwarového inženýrství, tedy sady aktivit, které zahrnuje vývoj softwaru. Vývoj softwaru není jen o implementaci (návrhu architektury a programování funkčních požadavků), ale jsou kolem něj i další činnosti. Důležitou aktivitou je analýza požadavků, jelikož bez kvalitní analýzy požadavků nebude tým vývojářů řádně tušit, co má vlastně naprogramovat. V této kapitole se dozvíte o jedne z metodik, jak provádět analýzu požadavků. Tato metodika se nazývá inženýrství požadavků a je procesem sama o sobě.

#### S2.1 - Proces inženýrství požadavků

Inženýrství požadavků zahrnuje následující aktivity (v chronologickém pořadí). Za šipkou jsou uvedeny artefakty, které jsou výstupem aktivity:
1. studie proveditelnosti -> report o proveditelnosti
2. sběr požadavků -> hrubý seznam požadavků
3. analýza požadavků -> dokumentace požadavků
4. specifikace požadavků -> dokumentace specifikace požadavků (software requirements specification, SRS)
5. validace požadavků -> odsouhlasená dokumentace specifikace požadavků

Zde může snadno dojít ke zmatení termínů. Analýza požadavků je jedna z velkých souhrnných aktivit v procesu vývoje softwaru. Touto aktivitou se myslí vše, co provádí IT analytik. Proces inženýrství požadavků je metodika, jak IT analytik provádí tuto velkou aktivitu. Jedna z aktivit procesu inženýrství požadavků se také nazývá analýza požadavků. Tím se však myslí zkoumání samotných funkčních a mimofunkčních požadavků, vyhledávání rozporů požadavků zainteresovaných osob a analýza vágnosti požadavku.

<img src="./soubory/re.png" alt="proces inženýrství požadavků" style="width: 600px;"/>

#### S2.2 - Studie proveditelnosti

První fází procesu inženýrství požadavků je provést studii proveditelnosti. IT analytik dorazí za klientem a získává informace o vizích projektu, jeho cílu, problémech které řeší, atd. Na základě těchto informací musí analytik zjistit, zda je možné takový software vytvořit a přijmout zakázku nebo nikoliv. Mezi základní proměnné, které rozhodují o přijmutí projektu, patří:
* Je pro nás projekt zajímavý? (finančně, pověst)
* Máme k dispozici všechny potřebné zdroje? (čas, vývojáři, technologie)
* Máme know-how pro řešení klientova problému?
* Chceme takový projekt vývíjet? (třeba pro nás není zajímavý)

#### S2.3 - Sběr požadavků

Sběr požadavků lze rozdělit dvou menších fází:
1. počátek (inception)
2. vyjednávání (elicitation)

Mezi těmito dvěmi fázemi nebudu rozlišovat, jelikož počátek představuje prvotní sběr požadavků, zatímco elicitace je kontinuální sběr požadavků. Některá literatura může o těchto aktivitách hovořit jinak, ale hlavní myšlenka je taková, že pokud IT analytik nezná prostředí klienta (problémy které řeší), tak nemůže řádně sbírat požadavky (s čímž musím souhlasit). Často se však seznamuje IT analytik s novými oblastmi problémové domény i během elicitace. Pokud sbírám požadavky pro bankovní společnost, měl bych se seznámit s oborem bankovnictví a prostředím a specifiky banky samotné. 

Vyjednávání požadavků bývá tou nejkomplikovanější aktivitou z procesu inženýrství požadavků. Analytik se seznamuje se všemi zainteresovanými osobami, pomocí vhodných technik z nich získává požadavky na software. To může být značně náročné, jelikož některé zainteresované osoby nejsou příliš mluvné nebo je ani vyvíjený software nezajímá i když ho budou používat. Pokud podnět na nový software vychází z uživatelů, tak budou velice sdílní. Pokud podnět vyznikl ve vedoucím pracovníkovi, pak samotní uživatelé budou vnímat nový software jako problém, díky kterému se budou muset po určitou dobu učit nový proces interakce a budou méně efektivní. Lidé jsou velice rigidní, takže očekávejte občas negativní vyjednávání o požadavcích. Navíc musíte získat požadavky od všech zainteresovaných osob, jelikož vedoucí mohou mít i znalosti o legislativních a standardizačních požadavcích (například softwaru musí splňovat určitou ISO normu nebo musí splňovat požadavky kladené GDPR).

Pokud shrneme, co musí IT analytik provést v této fázi, tak jsou to následující úkony:
* seznámit se s problémovou doménou
* seznámit se s problémy, které má software uživatelům vyřešit
* seznámit se s omezeními, které jsou na software kladeny

Požadavky nemusí získávat jen od lidí samotných. Zdroje pro získávání požadavků mohou být:
* uživatelé softwaru - ten, kdo software bude při práci používat
* zainteresované osoby - všichni ostatní, kdo mají na vývoji softwaru zájem (typicky vedení)
* doménový experti - najatí experti, kteří vědí o kontextu a softwaru daného typu nejvíce
* existující systémy - analytik může analyzovat aktuálně používány SW nebo konkurenční řešení
* dokumenty - dokumenty podniku mohou říci analytikovi hodně o požadavcích jak funkčních (dokumentace podnikovových procesů), tak legislativních/standardizačních.

Analytik může pro sběr použít velké množství technik, které vycházejí z technik sociologického výzkumu. Tyto techniky je vhodné kombinovat. Mezi techniky pro sběr požadavků patří:
* rozhovor (interview) - popovídám si s osobou z očí do očí a oba mi vypráví své představy, já se doptávám na nejasnosti
* strukturovaný rozhovor - to stejné jako interview, ale mám přesně zadané otázky, na které se ptám a které pomohou architektovi software navrhnout
* dotazník - zašlu strukturovaný dotazník všem zainteresovaným osobám a ty mi jej vrátí s odpovědmi, ze kterých získám požadavky (asi nejhorší metoda)
* bouře mozků (brainstorming) - pozveme více osob na schůzku, kde si hromadně vyměnujeme nápady
* pozorování uživatelů (task observation) - sleduju uživatele používat aktuální software nebo pracovat a zapisuju si, jaký je postup a vymýšlím případně jak práci zefektivnit
* modelování případů užití - pomocná technika, kde již získané požadavky vymodeluju diagramem a následně se bavíme s osobou o tom, co lze dopřidat
* prototypování - pomocná technika, ve které vytvořím statický nebo interaktivní prototyp (třeba ve Figma), díky kterému s klientem přijdeme na další požadavky nebo upravíme stávající.

Otázky, které byste měli klást zdrojům požadavků (i sami sobě):
* jaký je účel systému, který chcete vyvinout?
* jaké problémy, které aktuálně máte, bude systém řešit?
* jak systém vyřeší tyto problémy?
* jak bude systém využíván na denní bázi?
* jak problémy s výkonem systému ovlivní vaše používání systému na denní bázi?

Požadavky existují ve dvou formách:
* uživatelské požadavky = sepsáno slovy klienta
* systémové požadavky = sepsáno na základě slov klient pro vývojáře

Úkolem analytika získat natolik kvalitní uživatelské požadavky, aby bylo možné je přepsat do jasné algoritmizovatelné a implementovatelné podoby pro vývojáře.

<img src="./soubory/spirala.png" alt="spirálový model získávání požadavků" style="width: 600px;"/>

Požadavky se dále dělí na dva základní typy
* funkční požadavky: jaké funkcionality musí software vykazovat při interakci s ním
* mimofunkční požadavky: požadavky, které jsou kladené na software a nesouvisí s funkcionalitou

Funkční požadavky jsou požadavky na to, co má software dělat. Například při přihlášení do systému se má objevit určitá stránka. Na této stránce lze vybrat to a to.

Mimofunkčních požadavků existuje velká řada typů. Rozdělujeme je na tři velké kategorie:
* Produktové požadavky: požadavky na chování produktu z dependabilního hlediska. Například systém nesmí za nepřetržitého chodu spadnout po dobu jednoho roku více jak 2 krát. Po pádu se musí sám zotavit do 30 minut.
* Organizační požadavky: požadavky vycházející z vnitřního prostředí podniku, tedy politiky, standardy a procesy podniku
* Vnější požadavky: požadavky vycházející z legislativy nebo propojitelnosti s jinými produkty (tedy z vnějšího okolí podniku)

Na tyto požadavky se často zapomíná a mohou být součástí velkých sporů při předávání softwaru.

<img src="./soubory/mimofun.png" alt="typy mimofunkčních požadavků" style="width: 600px;"/>

#### S2.4 - Analýza požadavků

Po získání požadavků z aktivity sběr požadavků je nutné si požadavky pečlivě projít a provést jejich analýzu. Na tuto analýzu neexistuje žádný exaktní postup. Cílem je pomocí logického přemýšlení, vizualizace výsledného softwaru (v hlavě, na prototypu) a dodatečné diskuze se zainteresovanými osobami dojít k takovým požadavků, které mají následující vlastnosti. Požadavky musí být:
* jasné - je z popisu zcela jasné, co se požadavkem myslí? (z pohledu podnikového hlediska)
* pochopitelné - bude z popisu jasné i programátorům, co se požadavkem myslí?
* kompletní - je popis požadavku úplný, tedy nechybí v něm něco? Tzn. máme potřebné informace od počátku do konce? (opět z pohledu podnikového hlediska)
* specifické - je popis dostatečně detailní pro implementaci? (opět z pohledu programátorského hlediska)
* ověřitelné - můžeme validovat požadavek a zjistit, zda jsme ho implementovali správně?
* kvantifikovatelné - je možné změřit splnění v číselné podobě? (nemusí být u všech, především důležité pro mimofunkční požadavky)
* proveditelné - je vůbec možné takový požadavek naprogramovat?
* nekonfliktní - není požadavek v konfliktu s jiným? Nevylučuje jeho doslovné splnění funkcionalitu jiného požadavku?

Techniky pro analýzu požadavků:
* formální hodnocení - Přečtu si požadavek a zkoumám, zda zmiňuje výše zmíněné vlastnosti
* logická analýza - Představím si realizaci požadavků v hlavě (nebo si pomůžu grafickým prototypem) a pomocí logického uvažování přemýšlim, zda dává smysl (spíše pomůcka pro formální hodnocení), pokud však nepoužívám formální hodnocení, tak tohle je minimum toho, co bych měl udělat
* analýza případů užití a rolí - Slouží zejména jako pomůcka pro analýzu nekonfliktnosti. V systému bude několik rolí (uživatel, administrátor, aj.). Jejich používání softwaru může být v konfliktu s jinou rolí. Představím si, že jsem vždycky daná role a zkoumám, jak se bude z pohledu mé role systém používat.
* prototypování - Pomůcka pro logickou analýzu, kdy zkoumám uvažováním problémy s požadavky na grafickém prototypu, který mi může dost pomoct si uvědomit problémy s požadavkem. Existují i softwary, kde lze vytvářet interaktivní grafické prototypy bez kódu.

Zde uvedu ukázku některých zápisů požadavků a rozeberu je z pohledu vlastností, které nesplňují.

Požadavek č. 1: Přihlášení do systému

```
Po přihlášení do e-shopu pomocí formuláře bych chtěl mít možnost měnit ceny produktů.
```

1. jasnost - Požadavek je jasný z pohledu podnikové logiky. Dokážeme si ho s klientem představit a chápeme se.
2. pochopitelné - Programátoři by také neměli mít problém požadavek pochopit z programátorského hlediska, jelikož se jedná o často řešený algoritmus.
3. kompletní - Požadavek není kompletní. Co se děje, pokud se nepovede přihlásit? Kolik pokusů na přihlášení mám? Máme nabízet reset hesla?
4. specifikcé - Určitě chybí dost programátorských detailů. Jakými všemi způsoby se může uživatel přihlašovat? Budeme potřebovat nějakýho poskytovatele pro ověření? Má se uživatel přihlašovat uživatelským jménem nebo emailem? Lze ho přihlásit pomocí informací z operačního systému (uživatelský účet)? Bude nějaký jednotný administrátorský účet?
5. ověřitelné - Požadavek je ověřitelný. Po implementaci mohou testeři snadno validovat, že se lze přihlásit do eshopu a měnit ceny produktů.
6. kvantifikovatelné - Požadavek není kvantifikovatelný ze své podstaty. To co by na něm bylo kvantifikovatelné by například mohlo být - pokud se 3x nepovede přihlásit, tak program provede nějakou činnost. Tyto číselné informace jsou důležité pro validaci.
7. proveditelné - Tento požadavek je proveditelný. Měl by to být schopen naprogramovat i junior programátor. Pozor však na různé typy útoků typu SQL Injection.
8. nekonfliktnost - Jelikož zde analyzuji jeden požadavek bez kontextu ostatních, tak nelze vlastnost ověřit.

U tohoto požadavku by bylo nutné si promluvit s programátory o všech detailech, které potřebují vědět a následně tyto detaily zjistit od zadavatele požadavku.

Požadavek č. 2: Dependabilní systém

```
E-shop nesmí padat a musí běžet 24 hodin 7 dní v týdnu.
```

1. jasnost - Je zcela jasné, co tím zadavatel myslí. Program prostě musí být dokonale spolehlivý.
2. pochopitelné - Programátoři asi nebudou mít problém požadavek pochopit z programátorského hlediska. Budou mít problém tento požadavek provést.
3. kompletní - Požadavku nechybí žádné detaily. Jelikož nesmí nikdy spadnout, tak není nutné ani zmiňovat, co v případě pádu dělat (například do jaké doby se má zotavit, jak se má zotavit).
4. specifikcé - Požadavku nechybí programátorské detaily, jelikož tohle není ani proveditelné. Zde nelze o specificitě rozhodnoput.
5. ověřitelné - Požadavek je ověřitelný pouze v případě, že budeme žít nekonečně dlouho :) takže není.
6. kvantifikovatelné - Požadavek můžeme sice kvantifikovat jako spadl/nespadl a tím ověřit požadavek, avšak vzhledem k nemožnosti takový požadavek realizovat bych tvrdil, že není z realistického pohledu kvantifikovatelný.
7. proveditelné - Zde je kámen úrazu. Požadavek není proveditelný. Je zcela nesmyslný.
8. nekonfliktnost - Jelikož zde analyzuji jeden požadavek bez kontextu ostatních, tak nelze vlastnost ověřit.

Požadavky byste si měly dále zatřídit podle typu do skupin a připadně jim přidat určité priority, jak moc jsou důležité. Minimálně lze využít schématu:
* musí být implementováno
* mělo by být implementováno
* může být implementováno

Výsledkem této aktivity procesu inženýrství požadavků je zcela jasný seznam požadavků, který nemá žádné konflikty a nevznikne problém s jeho realizací.

#### S2.5 - Specifikace požadavků

Specifikace požadavků je proces, při kterém se zapisují požadavky získané od zainteresovaných osob ve formální podobě do formálního dokumentu. Tomuto dokumentu se říká dokumentace specifikace požadavků (software requirements specification, SRS). Specifikace probíhá pomocí tří typů zápisu (lze využít více typů pro lepší pochopení):
1. přirozeným jazykem - může být chaotické a vágní, ale klient to dokáže přečíst a posoudit
2. přirozeným jazykem s formální strukturou - co se zhruba chce, co jsou vstupy, výstupy, podmínky, co to má dělat
3. pseudokódem
4. grafickým zápisem
5. matematický zápis

Formální struktura je nejpoužívanější forma zápisu. Požadavek lze chápat pomocí uspořádané ntice (systém, vstup, očekávaný výstup, rozhraní, omezení). Do systému vstupují vstupní hodnoty. Klienta nezajímá obsah systému (komponenty a jejich kód) a tak můžeme systém považovat za černou skříňku. Černá skříňka nám vrací výstupní hodnoty, avšak vliv na tyto výstupní hodnoty mají omezení, které jsou dané technickými možnostmi systému, legislativním prostředím, pravidly podniku, aj. Vstupy vstupují do systému přes rozhraní a přes rozhraní i vystupují výstupy.

<img src="./soubory/bb.png" alt="požadavek jako uspořádaná pětice" style="width: 600px;"/>

Zmíněná pětice informací vytváří formální strukturu jak zapisovat požadavky.

Šablonu pro dokumentaci specifikace požadavků naleznete v přílohách v tomto semináři nebo kliknutím na: <a href="#">ŠABLONA</a>.

Specifikované požadavky je možné dále dělit na detailnější požadavky, až dojdeme ke komponentám verifikovatelných automatizovanými testy. Proces inženýrství požadavků se zabývá částí, která přetváří požadavky zainteresovaných osob systémové požadavky. Systémové požadavky pak softwarový architekt rozdělí na subsystémové požadavky, tedy z jakých komplexních komponent = subsystémů se bude výsledný systém skládat a jak přispívají k plnění systémových požadavků, které odpovídají z podnikového hlediska požadavkům zainteresovaných osob. Samotní programátoři pak navrhují jednotlivé komponenty, které tvoří subsystémy.

<img src="./soubory/vmodel.png" alt="hierarchie validace a verifikace požadavků" style="width: 600px;"/>

Na schématu dále vidíme, jak se jednotlivé dílčí požadavky schvalují. Klient (případně další zainteresované osoby) validuje funkční a mimofunkční požadavky při akceptačním testování. Toto testování není automatizovatelné a probíhá manuálně (i když věřím, že šikovná firma si připraví zátěžové automatizované testy, jen to není zvykem). Pokud jdeme do hlubšího dělení, tam je již možné testovat subsystémy pomocí automatizovaných testů. Tyto testy subsystémů bývají složité integrační testy, kde zkoumáte emergentní chování integrovaných komponent. Tyto testy jsou na pomezí validace a verifikace. Při rozdělení subsystémů na samotné komponenty (třídy, funkce) lze již snadno automatizovanými testy verifikovat správné chování komponenty, aby přispívala k plnění funkcionálních požadavků. 

Důležitou otázkou je, jakým způsobem se mají požadavky zapisovat? Má jejich zápis více odpovídat narativu zainteresovaných osob (tedy mají být psány lidskou řečí) nebo mají být napsány v nějakém pseudokódu? Vhodné je najít nějaký průnik obou světů, tedy světu problémové domény (logistika, účetnictví, školství, ... ) a světu vývoje softwaru. Potřebujete přeci jen najít společné místo, kterému porozumí pro případné další vyjednávání a validaci požadavků jak zainteresovaná osoba, tak váš tým vývojářů.

<img src="./soubory/domena.png" alt="průnik problémové domény a softwarového vývoje" style="width: 600px;"/>


#### S2.6 - Správa požadavků

Proces inženýrství požadavků nekončí po získání schvalovacího podpisu k dokumentaci specifikace požadavků pověřenou zainteresovanou osobou. Tým již může začít vyvíjet, avšak požadavky je dále nutné řídit, jelikož mají svůj vlastni životní cyklus. Některé požadavky se mohou v průběhu vývoje softwaru měnit, v agilním vývoji je to dokonce vítané. Navíc v agilním vývoje se dává přednost funkčnímu kódu, se kterým bude zákazník spokojen, před dokumentací. V agilním vývoji se málokdy setkáte s detailní dokumentací požadavků. Kromě toho se mění i technologie i strategie podniku. Pokud podnik přesune své IT operace na dedikovanou firmu, nemůžete již počítat s vlastní databází na serveru podniku. Mohou vzniknout určitá omezení změnou operační platformy. Častým případem může být i původní nepochopení požadavků klienta, které se vyjasní až při vývoji (mohu potvrdit z mé osobní IT kariéry).

Existují dva způsoby, jak řídit životní cyklus požadavků:
* psát změny (nový požadavek, úprava požadavku, hotový požadavek) do dokumentace specifikace požadavků
* využít dedikovaný software pro správu požadavků

Pokud je využita dokumentace specifikace požadavků pro řízení životního cyklu požadavků, pak je nutné, aby tato dokumentace představovala jediný zdroj pravdy (single source of truth). Je nutné zajistit konzistenci verzí mezi vývojáři. Vhodné je centralizované řešení - dokument na cloudovém úložišti, wiki, github repozitář.

Osobně neznám řádný dedikovaný softwaru pro řízení života požadavků. Většinou se využívají obecné nástroje pro projektový management a zadávání požadavků k vývoji (Jira, Confluence). Mnoho týmů využívá obyčejný textový a tabulkový procesor. Na google jsem nalezl vždy pouze vágní software, ze kterého nebylo příliš jasné, k čemu slouží. Proto nabízím vývoj softwaru pro správu životního cyklu požadavků jako bakalářskou nebo diplomovou práci :).

Systém pro správu požadavků by měl minimálně umět:
* prohlížet požadavky
* vytvářet nové požadavky
* upravovat stávající požadavky
* mazat existující požadavky
* prioritizovat požadavky
* zadávat požadavky týmu k vývoji
* zohlednit různé role zadavatelů požadavků
* propojení s dokumentací požadavků
* propojení s dokumentací specifikace požadavků
* vypisovat statistické a historické informace o životním cyklu požadavků

Právě poslední tři body mnohé softwary nesplňují. Vzhledem k tomu, že se na složitějším řešení pravděpodobně nepracuje, tak nejsou tyto informace o životním cyklu požadavků a propojení požadavků nutné pro úspěšné projekty (moje domněnka).

#### S2.7 - Vývoj řízený chováním

Na základě vývoje řízeného testy (Test-driven development, TDD) vznikla technika vývoje zvaná jako vývoj řízený chováním (Behavior-driven development, BDD). Její myšlenka je následující:
1. Klient sepíše požadavky v semi-formálním jazyce (rozumí mu jak klient, tak vývojář) pomocí vyprávění a validačních podmínek (takže specifikace funkčního požadavku).
2. Na základě sepsaného požadavku se vygeneruje automatizované testy, které musí vývojář splnit.

Tím se propojí specifikace požadavků s vývojem samotným. Tato metodika roste na oblibě i v ČR.

Požadavky se píšou ve vybraném semi-strukturovaném jazyce. Například knihovna Behave pro Python používá asi nejpoužívanější semi-formální jazyk Gherkin:

```
Feature: The dealer for the game of 21
    Scenario: Deal initial cards
        Given a dealer
        When the round starts
        Then the dealer gives itself two cards
```

Vidíme, že v jazyce Gherkin se popisuje nějaká vlastnost (feature), která se do systému programuje, tedy nějaký funkcionální požadavek. Pro danou vlastnost může nastat několik scénářů, což jsou nějaké předběžné podmínky nebo kontext. Základní schéma se skládá ze tří klíčových slov: 
* Given: známy stav systému 
* When: akce uživatele
* Then: následek akce na stav systému

Tyto scénáře pro jednotlivé požadavky píše klient. Programátoři následně musí implementovat automatizované validační! (nikoliv verifikační) testy k tomuto požadavku.

```
@given('a dealer')
def step_impl(context):
    context.dealer = Dealer()

@when('the round starts')
def step_impl(context):
    context.dealer.new_round()

@then('the dealer gives itself two cards')
def step_impl(context):
    assert (len(context.dealer.hand) == 2)
```

Více o BDD v Pythonu naleznete:
* [TUTORIAL](https://semaphoreci.com/community/tutorials/getting-started-with-behavior-testing-in-python-with-behave)
* [MANUAL](https://behave.readthedocs.io/en/stable/tutorial.html).

### On-site cvičení

#### C2.1 - Strukturovaný rozhovor (interview)

Vytvořte dvojice. Jeden z dvojice si zahraje na zákazníka a druhý na analytika. Zákazník si přeje nějaký software (neprozrazujte konkrétní detaily analytikovi, jen si je myslete v hlavě). Analytik si připraví krátkou šablonu v textovém dokumentu pro strukturované interview a ptá se zákazníka na předpřipravené otázky. Cílem analytika je získat seznam požadavků na software takový, aby byl zákazník s výsledkem spokojen. Výstupem této fáze je textový dokument, který mi na konci semináře ukážete. 

#### C2.2 - Analýza konfliktních požadavků z uživatelských příběhů

Sepište si z odpovědí ze strukturovaného interview požadavky do prvotních specifikací v textové podobě. Společně rozeberte, zda požadavky splňují vlastnosti kvalitních požadavků (jasnost, úplnost, aj.), dojasněte si je a případně se domluvte, jak vyřešit konflikty v požadavcích. Příběhy vhodně kategorizujte a ujasněte si, jestli nechybí nějaké produktové nebo externí požadavky.

#### C2.3 - Vytvoření UI/UX prototypu

Vyzkoušejte si nástroj Figma (nebo jiný grafický nástroj) a navrhněte na základě požadavků UI/UX prototyp aplikace. Ujasněte si na prototypu, zda jsou všechny požadavky v pořádku nebo případně na základě interakce s prototypem je ve spolupráci s klientem pozměňte.

#### C2.4 - Mapování uživatelských příběhů

Požadavky zapište do schématu pro uživatelské příběhy a zakreslete je do tabule pro uživatelské příběhy. Můžete použít jakýkoliv nástroj, například Miro nebo [Figma](https://www.figma.com/templates/user-story-mapping/). Příběhy rozdělte do epik: [Vysvětlení](https://www.plutora.com/blog/epic-vs-story-whats-the-difference-and-how-to-use-each). Tyto příběhy lze pak použít pro zadávání do kanban tabule z minulé hodiny.

#### C2.5 - Vývoj řízený chováním

Nainstalujte si modul Behave do Pythonu a přepište do jazyka Gherkin alespoň 2 požadavky [TUTORIAL](https://semaphoreci.com/community/tutorials/getting-started-with-behavior-testing-in-python-with-behave)

Implementujte kód a proveďte validační testování pomocí modulu Behave, že jsou požadavky splněny.