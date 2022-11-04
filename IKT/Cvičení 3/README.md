# Informační a komunikační technologie

## Cvičení 3 - Operační systémy

### Samostudium

#### C3S1. Operační systém (OS)

#### C3S2. Historie operačních systémů

Úplně první počítače neměly operační systém. Programy v nich nahrané (nebo přímo v nich hardwarově zkonstruované) přímo komunikovaly s hardwarem. Tím bohužel vznikl problém propietárnosti programů vůči hardwaru - programy nebyly přenositelné. Program musel být dělán na míru konkrétnímu počítači. Řešením byl program s názvem operační systém. Tento program neměl sloužit jako aplikace pro konání služeb, kterých si uživatel žádá, ale jako systémový program, tedy program, který zprostředkovává služby.

Jelikož o historii OS se dozvíte všude možně na webu, tak uvedu jen nejdůležitější milníky v historii OS:
1. General Motors, 1956 - první operační systém pro IBM počítač
2. IBM, 1960 - distribuce počítačů s operačním systémem
3. Lorem, lorem - vznik Unixu, oblíbeného operačního systému, jehož rozhraní se stalo POSIX standardem
4. Microsoft, 1985 - vznik GUI rozhraní Windows pro svůj operační systém MS DOS
5. 


#### C3S3. Shell

Shell je program, který odkrývá uživateli a aplikacím služby a spuštěné procesy operačního systému. Jedná se tedy o rozhraní pro využívání OS. Shelly operačních systémů se rozdělují do dvou kategorií:
1. CLI (Command-Line Interaface) - operační systém je ovládán uživatelem pomocí textové příkazové řádky
2. GUI (Graphical User Interface) - operační systém je ovládán uživatelem pomocí grafického rozhraní ikonek a výběrových položek

Mezi nejznámější shell typu GUI patří Windows, který původně nebyl operační systém, ale byl GUI programem, který se spustil v operačním systému MS DOS, aby uživatel nemusel ovládat počítač pomocí CLI jak bylo v té době zvykem.

#### C3S4. POSIX

POSIX (Portable Operating System Interface) je standard pro tvorbu rozhraní operačních systémů. Tyto příkazy dané POSIX standardem budeme volat přes uživatelské rozhraní, tzv. shell. Konkrétně přes shell typu CLI.

Podle POSIX standardu má každý příkaz následující anatomii:
1. název příkazu: název programu, který chceme spustit
2. příznaky: modifikují chování programu, vyvolávají se pomocí pomlčky nebo dvojité pomlčky
3. argumenty: hodnoty příznaků nebo programu

Na následující stránce si můžete přečíst návod k použití všech základních příkazů: [ZDE](https://www.hostinger.com/tutorials/linux-commands). Pro případ, že by se s webovou stránkou něco stalo, tak uvedu zmíněné příkazy i sem (bez návodu na použití, to už je snadno vygooglitelné).

Mezi základní příkazy patří:
1. sudo (Super User DO) - provede příkazy, které potřebují administrátorské (root) oprávnění
2. pwd (Path of current Working Directory) - zjistí plnou cestu k aktuálnímu adresáři, ve kterém se nacházíte (pracujete v něm)
3. cd (Change Directory) - přesune vás do jiného zvoleného adresáře (dvojklik na složku v GUI shellu), speciální znaky jsou - (předchozí adresář), .. (o adresář výše), . (aktuální adresář) a ~ (domovský adresář)
4. ls (List fileS) - vypíše v aktuální adresáři všechny soubory a adresáře (pro výpis skrytých je nutný přínazk -a)
5. cat (ConcatenATe) - vypisuje a připojuje výpis souboru nebo souborů na standardní výstup (CLI)
6. cp (CoPy) - kopíruje soubor nebo adresář
7. mv (MoVe) - přesouvá soubory nebo adresáře
8. mkdir (MaKe DIRectory) - vytváří adresáře
9. rmdir (ReMove Directory) - odstraní prázdný adresář
10. rm (ReMove) - odstraní soubor, avšak umí s příznakem -r odstranit i adresář s celým jeho obsahem (rekurzivní odstranění)
11. touch - vytváří prázdný soubor
12. locate - vyhledá soubor s daným názvem nebo řetězcovým vzorem v předem sestavené databázi souborů (offline vyhledávání)
13. find - vyhledá soubor s daným názvem nebo řetězcovým vzorem v souborovém systému počítače (real-time vyhledávání), je pomalejší jak locate
14. grep (Global Regular Expression Print) - vyhledá regulární výraz v souboru a vytiskně nález
15. df (Disk Filesystem) - vypíše využití prostoru disku v procentech a kB
16. du (Disk Usage) - vypíše kolik prostoru na disku daný soubor nebo adresář zabírá
17. head - vypíše ze souboru prvních N řádků
18. tail - vypíše ze souboru posledních N řádků
19. diff (DIFFerence) - vypíše rozdílné řádky mezi dvěma soubory
20. tar (Tape ARchive) - zabalí více souborů nebo adresářů do jednoho archivu
21. chmod (Change MODe) - změní práva na přístup do souborů (čtení, zápis, spuštění) pro vlastníka, člena skupiny a ostatní
22. chown (Change OWNership) - změní vlastníka souboru nebo adresáře na vybraného uživatele
23. jobs - vypíše všechny běžící procesy a jejich stav, důležité pro zjištění PID procesu pro zabití
24. kill - zabije proces podle vybraného PID
25. ping - zjistí, zda je uzel v síti k dispozici pro komunikaci
26. wget (Web GEt) - stáhne z webu soubor nebo rekurzivně obsah adresářů
27. uname (Unix NAME) - vypíše informace o operačním systému a hardwaru počítače
28. top, htop (Table Of Processes) - vypíše informace o běžících procesech včetně výpočetních prostředků, které zabírají
29. history - vypíše historii použitých příkazů v shellu
30. man (MANual) - vypíše uživatelský manuál ke zvolenému POSIX příkazu
31. echo - vypíše na standardní výstup specifikovaný řetězec, lze využít pro výpis výstupu programů, které normálně netisknout data na obrazovku 
32. zip, unzip - provede kompresi nebo dekompresi archivu
33. hostname - vypíše síťový název uzlu v síti nebo IP adresu
34. useradd, userdel - přidá nový uživatelský účet do počítače nebo ho smaže
35. apt-get (Advancet Package Tool) - software pro stahování, odinstalaci a modifikace programů 
36. nano, vi, emacs, jed - zapne textový editor v CLI shellu
37. alias, unalias - vytvoří textového zástupce (alias) pro soubor nebo program
38. su (Switch User) - přepne účet na jiný uživatelský účet 
39. ps (Process Status) - vypíše snímek (snapshot) všech běžících procesů v systému
40. clear - smaže text na obrazovce CLI shellu

### Zadání cvičení

#### C3Z1. Základní POSIXové příkazy

V tomto cvičení si vyzkoušíte základní POSIXové příkazy pro ovládání počítače pomocí rozhraní v příkazové řádce.

#### C3Z2. Přesměrování a roury

#### C3Z3. Skripty

**Video týdne1: Linuxové operační systémy**

V následujícím videu se dozvíte něco o historii linuxových operačních systémů a proč jich existuje takové množství. [ZDE](https://www.youtube.com/watch?v=ShcR4Zfc6Dw)

**Video týdne 2: Základy informačních technologií**

V tomto cvičení jste se seznámili se základami operačních systémů. Kromě toho byste měli mít všeobecný přehled i v celém oboru informačních technologií. Následující video je rychlý průlet termínů a konceptů z oblasti počítačové vědy, které byste měli znát. [ZDE](https://www.youtube.com/watch?v=-uleG_Vecis)
