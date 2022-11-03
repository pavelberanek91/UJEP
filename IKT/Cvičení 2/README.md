# Informační a komunikační technologie

## Cvičení 2 - Počítačové sítě

### 2.1 Počítačová síť

#### Dělení počítačových sítí
Počítačové sítě lze dělit podle mnoha kategorií. Jedna z nejznámějších kategorií je dělení na základě velikosti počítačové sítě.
* Nanoškálové sítě - uvnitř biologických systémů, typicky slouží jako sensory, součást nanotechnologického výzkumu
* BAN (Body) - sítě s dosahem kolem lidského těla, typicky pro nositelou elektroniku nebo medicínské sensory/zařízení (inzulínová pumpa)
* PAN (Personal) - sítě pro jednu osobu a její blízké technologie, např.: notebook a k němu připojená klávesnice, myš, telefon, tablet
* NAN (Near-me) - sítě s dosahem desítek až stovek metrů kolem mé osoby, např.: aplikace pro setkávání/seznamování lidí, roste o tyto aplikace zájem, proto se tento termín začal používat a pravděpodobně se bude ještě více využívat s rozvojem IoT zařízení
* LAN (Local) - síť s dosahem jedné několika místností až celé budovy, v dnešní době realizováno nejčastěji v kombinaci s WLAN (bezdrátovou LAN)
* CAN (Campus) - síť, která původně označovala univerzitní internet, avšak dnes za CAN sítě považujeme propojené LAN sítě do jedné rychlé sítě a pokrývající velké množství budov.
* MAN (Metropolitan) - síť, která svou velikostí pokrývá velké území (od kampusu univerzity až po celé město)
* WAN (Wide) - síť, která pokrývá geografické regiony (města, státy, velké kontinentální vzdálenosti)
* GAN (Global) - síť, která pokrývá neomezeně velké geografické území (internet jako takový)

Pro každou ze sítí existuje sada technologií, protokolů a konceptů využití. Z praktického hlediska to až tak důležité není, ale pomáhá to lidem rozumět si zejména při technické výzkumné činnosti.

Další dělení počítačových sítí je podle jejich topologie. V dnešní době nejsou osobní počítače již fyzicky propojeny do těchto topologií. Logicky však být mohou. S rozvojem IoT se o to více ještě uplatňují jiné topologie než hvězda, tudíž toto dělení bude podle mě znova důležité pro komunikaci myšlenek v oblastí počítačových sítí.
* Sběrnice (Bus)
* Kruh (Ring)
* Hvězda (Star)
* Strom (Tree)
* Síť (Mesh)
* Plná síť (Full-mesh)

#### Protokolové zásobníky
Protokolový zásobník je soustava protokolů, které se používají pro komunikaci v počítačové síti. Protokol je sada dohodnutých pravidel, které využívají zařízení a programy, aby si vzájemně rozuměli. Funkčně mohou provádět podobné nebo rozdílné věci a proto se protokoly dělí na vrstvy v protokolovém zásobníku. Vrstvy spolu komunikují. Nejznámější model protokolového zásobníku je OSI/ISO sedmi-vrstevnatý model. Používaná realiace protokolového zásobníku je čtyř-vrstevnatý TCP/IP model. Pokud pochopíte nejdůležitější protokoly a jak na sebe navazují v protokolovém zásobníku, tak pochopíte počítačové sítě. Minimálně byste měli alespoň znát některé nejvyužívanější protokoly, jelikož s jejich názvy se často ve světě IT a při používání OS/programování setkáte.

#### Vybrané protokoly
Mezi nejznámější protokoly (a hlavně nejpochopitelnější) řadíme například:
* DHCP (Aplikační vrstva) - slouží pro dynamické připojení do počítačové sítě (nemusíte volat adminovi, ať vás připojí na wifi, důležitá technologie pro veřejné WLAN)
* DNS (Aplikační vrstva) - slouží pro překlad názvů webových stránek na IP adresa (resp. slouží pro předávání síťových informací, viz kurz počítačových sítí)
* HTTP (Aplikační vrstva) - slouží pro komunikaci s webovými servery (stahování webových stránek, zasílání dat do formulářů, přenos XML souborů, ...)
* FTP (Aplikační vrstva) - slouží pro přenos dat po počítačové síti (nahrávání dat na server, stahování dat ze serveru)
* IMAP/POP3 (Aplikační vrstva) - slouží pro stahování elektronické pošty (emailu), POP3 pracuje s lokální kopií emailů, IMAP pracuje s emaily na poštovním serveru
* SMTP (Aplikační vrstva) - slouží pro přenos elektronické pošty mezi poštovními servery
* SSH (Aplikační vrstva) - slouží pro bezpečné (zašifrované) komunikaci po síti (ovládání serveru klientem přes ssh příkazy)
* TCP (Transportní vrstva) - slouží pro vytvoření spojení mezi počítači pro obousměrné přenášení dat, oproti UDP je garantován spolehlivý přenos a ve správném pořadí
* UDP (Transportní vrstva) - to samé jako TCP, akorát přenos je bez záruky doručení, tzn. data nemusí dorazit, avšak pokud je cílem rychlost (online hry, streaming, youtube/netflix), pak není jiná možnost
* IP (Internetová vrstva) - základní protokol pro přenos dat po síti a bez něj by nefungoval internet, slouží pro přenos dat na základě IP adres od zdroje k cíli 
* IGMP (Internetová vrstva) - používajího routery a umožňuje zasílat data jen vybrané skupině uzlů (multicast) namísto původní jednomu/všem (unicast/broadcast), což umožňuje efektivní streaming videoher/videa/videokonferencí do sítě
* ICMP (Internetová vrstva) - slouží pro zasílání chybových zpráv klientům (např.: server není dostupný), používajího diagnostické síťové nástroje 
* ARP (Vrstva fyzického rozhraní) - slouží v rámci lokální sitě pro získání linkové adresy síťového rozhraní (v Ethernetu je to MAC adresa) pomocí známé IP adresy, bez toho by nebyl switch schopný zjistit, zda data z routeru/jiného uzlu má zaslat vašemu notebooku, vašemu telefonu, telefonu vaší sestry, vaší televizi atd.
* MAC (Vrstva fyzického rozhraní) - řídí komunikace samotného zařízení s přenosovým médiem (používají ho i celulární sítě jako LTE), řídí přístup na sdílené médium vhodným algoritmem (u Ethernetu CSMA/CD)


### 2.2 Síťové prvky

#### Modem
Vás poskytovatel internetu vám zasílá data skrze nějaký typ signálu. Signál je realizován změnou fyzikálních veličin, takže může být na principu optického přenosu, elektrického proudu, elektromagnetických vln či jiných experimentálních principů. Aby počítačová síť byla schopná s daty z internetu pracovat (a obdobně je do internetu zasílat) musí dojít k transformaci signálu na data. To je úkolem modem. Modem je zkratka za Modulátor-Demodulátor, kde modulace je proces vložení dat do signálu a demodulace je proces získání dat ze signálu. Modem tedy bude představovat první síťový prvek u vás doma, do kterého je připojen signál od poskytovatele. Modem vám typicky pronajímá váš poskytovatel internetového připojení (ISP, internet service provider).

#### Směrovač (Router)
Síťový prvek, který přeposílá data mezi počítačovými sítěmi. Data se posílají mezi sítěmi ve formě tzv. paketů (balíčků dat), které si routery různých sítí posílají, než dorazí internetem (internet je vlastně sada propojených routerů) od zdroje k cíli. Tuto cestu můžeme vysledovat příkazem tracert (poslední kapitola tohoto cvičení).

Routery spolu komunikují pomocí routovací protokoly, čímž si sdílí informace sloužící pro výběr cest pro zasílání paketů (například protop Routing Information Protocol, RIP). Tuto cestu vybírá routovací algoritmus (např.: distance vector algoritmy nebo link-state algoritmy, které typicky využívají klasické algoritmy z teorie grafů jako je např.: Dijsktrův algoritmus). Skrze routovací protokol získává router informaci o topologii počítačové sítě (jaké uzly jsou k dispozici, přes jaké uzly je dosáhnout a jaké nejsou dostupné). Tyto informace jsou zaneseny do routovacích tabulek, kde se k nim přidává typicky i informace o ceně za cestu, vypočtenou z routovacích algoritmů.

#### Přepínač (Switch)
Síťový prvek, který přeposílá data uvnitř počítačové sítě. Uzly počítačové sítě jsou spolu přes switch propojené, jinak by musely být spojené přes svá síťová rozhraní do jiné topologie, jako je např. sběrnice nebo kruh). Přepínač se nazývá přepínačem z toho důvodu, že přepíná cesty mezi zdrojem a cílem, resp. zasílá data pouze uzlu, kterému data náleží (to je rozdíl oproti hloupějšímu Hubu - rozbočovači, který zasílá data všem uzlům). Uzly jsou switchem identifikovány na základě jejich fyzické adresy (MAC). Lze také koupit různě drahé switche, od nejlevnějších, které jsou okamžitě připravené na připojení k počítačům doma, po firemní konfigurovatelné, na kterých lze nastavit i QoS (Quality of Service - preference propustnosti dat, malé latence, malé chybovosti, atd.).   

#### Přístupový bod (Access Point)
Síťový prvek, který umožňuje bezdrátovým zařízením připojit se do sítě a stát se uzly. V domácnostech bývá součástí routeru. Dočasně je možné ho nahradit i bezdrátovou ad-hoc sítí (smartphone sloužící jako hot-spot), avšak to není doporučené jako permanentní řešení.

#### Opakovač (Repeater, Wi-Fi repeater/extender)
Síťový prvek, který přijme signál, zesílí ho a přepošle ho dál. Může být jako pro kabelová média (koaxiální vodič, kroucená dvojlinka), tak pro bezdrátové médium. Některé routery mají dnes možnost chovat se jako AP. Někteří IT specialisté tvrdí, že Wi-Fi repeater zanáší do počítačové sítě jen chaos a zpomaluje síť. Daleko lepší je podle nich využít router nastaven jako AP. Autor tohoto textu nemá zkušenost s repeatery, jen s routery nastaveny jako AP, takže nemůže porovnat :( ...



### 2.3 Diagnostika počítačové sítě
Pokud se vaše sociální okolí (pokud nějaké máte ...) dozví, že máte IT vzdělání, tak vám zaručuji, že se stanete levným IT servisem. Jedny z nejčastějších problémů jsou problémy s počítačovou sítí (nejde internet). Pro tyto případy se vyplatí umět alespoň nejzákladnější příkazy pro diagnostiku počítačové sítě, čímž rozhodně uděláte radost i případně technické podpoře, který se vás přestane ptát na to, jestli jste zkusili router restartovat.

#### ping
Příkaz pro testování dosáhnutelnosti nějakého uzlu v počítačové síti. Lze pomocí něj vystopovat, kde se narušila síťová cesta.
```
ping www.google.com
ping 192.168.0.1
```

#### ipconfig
Nejdůležitější příkaz na ovládnutí. Ukazuje potřebné základní informace pro následnou diagnostiku a dokumentací vaší sítě.
```
ipconfig
ipconfig /all
ipconfig /release
ipconfig /renew
```

Na Linoxovém OS Debian byl nahrazen příkazem ip nebo si nainstalujte net-tools
```
sudo apt-get install net-tools
/sbin/ifconfig
```

#### hostname
Vrátí uživatelské jméno v počítačové síti. Hodí se, pokud si nejste jisti, jak se v počítačové síti nazývá váš počítač.
```
hostname
```

#### getmac
Vrátí mac adresu zařízení. Tím značně usnadníte život všem síťovým administrátorům, které žádáte o připojení do sítě.
```
getmac
```

#### nslookup
Zobrazí data pro diagnostiku DNS (Domain Name System) infrastruktury. Bez příznaků zobrazuje adresu DNS serveru, který počítač používá pro překlad URL na IP adresy.
```
nslookup
```

#### tracert
Příkaz vypíše trasu, kterou paket cestuje než dorazí do cíle. Vrátí tedy seznam navštívených uzlů s latencí při přeskoku mezi uzly.
```
tracert www.google.com
```

#### netstat
Zobrazí všechny aktivní TCP připojení a porty, na kterých počítač naslouchá.
```
netstat
```

#### arp
Zobrazí záznamy v ARP (Address Resolution Protocol) cache paměti, které obsahují tabulky se záznamy o IP adresách a příslušných fyzických adresách. Příznak /a zobrazí ARP cache tabulky pro všechny síťová rozhraní.
```
arp /a
```

#### pathping
Jedná se o kombinace příkazů ping a tracert. Komplexní analýza pohybu dat s latencí od zdroje k cíli.
```
pathping www.google.com
```

#### systeminfo
Detaily o konfiguraci počítače, což se může hodit často i když to vyloženě nesouvisí s diagnostikou sítě jako spíš počítače samotného.
```
systeminfo
```

### 2.4 Nastavení domácího routeru
Ať z vás budou IT specialisti či nebudou, minimálně každý z nás by měl ovládat základy technologií, na kterých jsme denně závislí. V běžném životě z oblastí počítačových sítí je to domácí router. Domácí router je takové all-inclusive síťové zařízení, které předsatvuje router, switch i access-point v jednom. Jeho základní nastavení by měl ovládat každý z nás.

#### Zapojení domácího routeru
Router se umisťuje do prostoru, kde chcete mít nejlepší pokrytí signálem. Z vašeho modelu připojíte přívodní datový vodič do portu WAN na zadní straně routeru. WAN port je odlišně označen od ostatních LAN portů (typicky je WAN port modrý a LAN porty žluté). Stolní PC se zapojuje typicky do LAN portů switche v routeru přes UTP vodiče.

#### Přihlášení se do routeru
Pro přihlášení do routeru budete potřebovat znát jeho IP adresu. Připojte se nějakým zařízením do lokální sítě routeru přes LAN portu UTP vodičem (zpočátku buď nemáte nastavenou WLAN, takže nic jiného nezbyde, nebo router má implicitní WLAN s heslem na zadní spodní straně routeru/v manuálu). Následně zjistěte IP adresu routeru, což můžete zjistit příkazem ipconfig /all a vyhledáním IP adresy výchozí brány (gateway). Tuto adresu zadáte do prohlížeče do lišty pro URL adresy a dostanete se do přihlašovacího rozhraní routeru. Login a heslo je typicky admin/admin nebo je napsáno na spodní straně routeru/manuálu. Po zadání byste se měli dostat do nastavení routeru.

#### Rychlé nastavení
Routery obsahuji čarodejě :) ... (průvodce, setup wizard) pro rychlé nastavení. Avšak mnoho důležitých nastavení se naléza mimo čaroděje :D ... ano mám rád ten termím. Mezi základní oblasti nastavení routeru patří: 
* SSID - název lokální WLAN sítě, tento název vidíme, když vyhledáváme síť, můžeme viditelnost i zakázat
* 2.4 GHz vs. 5 GHz - nové routery umí vysílat na dvou frekvenčních pásmech, 5 GHz je rychlejší na krátké vzdálenosti, ale vlny neprojdou překážkami
* QoS - prioritizace určitých služeb, jako například online videoher nebo video stremování, případně prioritizace určitých zařízení (můžete si urychlit rychlost na úkor rychlosti rodiny)
* Guest sítě - síť pro návštěvníky, můžete dát open, ale hrozí pak připojení někoho, kdo projde kolem domu, doporučuje se alespoň WPA2 heslo, můžete omezit i například, v jaké časy je síť otevřena, stejně tak o jaké pásmo se jedná (typicky 2.4 GHz)
* Traffic monitoring - v routeru byste měli být schopni vidět základní diagnostické údaje o přenosu ve vaší síti a můžete i přenos omezit, například omezíte, jaké zařízení může stáhnout maximálně tolik dat a navíc můžete podle vytíženosti jednotlivých zařízení i lépe prioritizovat
* FTP server - pokud má váš routeru USB vstup, pak je možné využít router jako FTP server; připojíte-li do něj nějaké médium jako externí disk nebo FLASH disk a povolíte FTP, pak tento disk bude na síti viditelný pro všechny ve vaší LAN síti (lze dokonce nastavit i přístup jen do určitých složek)
* Filtrování MAC adres - lze nastavit white-list a black-list (nevím, jak to teď lépe nazvat po BLM, jelikož tyto termíny vadili společnosti) na jednotlivé MAC adresy zařízení (tzn. nastavíte, jaká konkrétní zařízení se mohou připojit nebo jaká zařízení se nemohou připojit)
* Rodičovská kontrola - nastavení časových limitů pro jednotlivá zařízení (používejte ve spojení s MAC filtrováním)

## Domácí cvičení

### DÚ 2.1 Kvantový internet
Jedna ze žhavých novinek na poli počítačových sítí jsou kvantové počítačové sítě a kvantový internet. Zjistěte si, jak takový kvantový internet funguje (fyzikální princip) a jaké má výhody oproti stávajícím nekvantovým řešením. Kde jsou oblasti jeho uplatnění?

### DÚ 2.2 Ovládání počítače přes SSH
Vyzkoušejte si instalaci SSH serveru na váš počítač (např.: OpenSSH Server pro Windows 10) a zkuste se připojit na tento server pomocí jiného zařízení a ovládat ho (např.: vypsat všechny soubory v adresáři, vytvořit nový adresář, smazat data). Zkontrolujte na vašem SSH serveru, že ke změnám opravdu došlo. Najděte si nějaký tutorial, kterého se držte pokud jste začátečníci v IT.

### DÚ 2.3 Mapování domácí sítě
Podívejte se na síťové diagramy lokálních sítí (zadejte na google LAN schematic diagram nebo network diagram). Pomocí vhodných diagnostických příkazů/vyhledání dat v routeru zjistěte, jak je vaše domácí síť sestavena. Nakreslete si jednotlivé uzly a připište k nim důležité informace (minimálně IP adresa a role prvku v síti, více ideálně i hostname, mac adresa, atd.). Diagramy doporučuji kreslit nějakým vhodným softwarem (jsou i online free).

### DÚ 2.4 Trasování cesty
Vypusťte nejaká data do světa a sledujte jejich cestu skrze internet. Zkuste alespoň 3 různé cesty. Proč je někdy cesta krátka a někdy dlouhá?

### DÚ 2.5 Nastavení vašeho routeru
Přihlašte se doma do vašeho domácího routeru a podívejte se, jaké možnosti máte. Zejména zjistěte, zda můžete vysílat jen 2.4 GHz nebo i 5 GHz, zda máte nastavené priority v QoS, zda máte možnost nastavit síť pro hosty, zda máte možnost využít FTP server na routeru, atd. 

Veškeré změny jsou na vás vlastní krk :) nechoďte pak za mnou, ale v případě průseru vám mohu na discordu pomoct. Minimálně si zkuste nastavit síť pro hosty, jelikož tím byste neměli být schopni nic pokazit. Piju whisky btw. :), ideálně Jack Daniels.
