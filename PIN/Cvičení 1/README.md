# Programování pro internet

**Obsah přednášky 1**:
* Značkovací jazyk XML (syntaxe, elementy, atributy, jmenné prostory) 

**Obsah cvičení 1**:
* Jazyk XML

## Cvičení 1 - Jazyk XML

V tomto cvičení si vyzkoušíte vytvořit XML datový soubor, který budete validovat na Apache serveru pomocí jazyka PHP. Validaci korektní struktury datového souboru budete provádět pomocí přiloženého DTD souboru. Server Apache spustíte pomocí programu Docker pro který máte připraven Docker soubor a Docker-compose YAML soubor. 

### On-site

#### Spuštění docker kontejneru s Apache serverem a PHP překladačem**

Docker je aplikace, která umožňuje spouštět tzv. docker obrazy do docker kontajnerů. Obraz si můžete představit jako miniaturní virtualizovaný počítač, na kterém jsou nainstalovány programy pro vaše potřeby. Jen místo plné verze operačního systému je tam nejmenší možná verze, která je nutné pro spuštění všeho potřebného. Tomu se říká základ obrazu. Jako základ obrazu budeme používat nějaký Linux, do kterého doinstalujeme vše potřebné. Prověďte následující úkon:

1. Vytvořte si složku, která bude sloužit jako váš pracovní adresář
2. V pracovním adresáři vytvořte soubor "docker-compose.yaml" (nebo si nahrajte přiložený soubor)
3. V pracovním adresáři si vytvořte adresář "php"
4. V adresáři php si vytvořte soubor s názvem "Dockerfile" (nebo si nahrajte přiložený soubor)
5. V adresáři php vytvořte adresář "src"
6. V adresáři src si vytvořte soubor s názvem "index.php"
7. V adresáři src si vytvořte soubor s názvem "fakulta.dtd"
8. V adresáři src si vytvořte složky s názvem "fakulty"

Následně zkopírujte obsah z této stránky do příslušných souborů.

**Dockerfile**
```
#zakladni docker image, ze ktereho vychazime
FROM php:8.0-apache

#instalace rozsireni pro XSL procesor
RUN apt-get update && \
    apt-get install -y libxslt1-dev && \
    docker-php-ext-install xsl && \
    apt-get remove -y libxslt1-dev icu-devtools libicu-dev libxml2-dev && \
    rm -rf /var/lib/apt/lists/*

#instalace rozsireni mysqli pro komunikace s mysql databazi
RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli

#instalace novych verzi zavislosti
RUN apt-get update && apt-get upgrade -y
```
Dockerfile je soubor, který slouží dockeru pro vytvoření obrazu, který chceme následně spustit v kontajneru. Zde předložený Dockerfile provede následující:
1. Stáhne linuxový OS s nainstalovaným apache serverem a php verze 8.0
2. Nainstaluje rozšíření PHP o XSL procesor (již není součástí jazyka PHP)
3. Nainstaluje driver pro připojení PHP k mysql databázi s názvem mysqli
4. Stáhne nejnovější verze všech závislostí

Věřím, že existuje možná lepší linuxový přístup, ale lépe jsem ho asi nedokázal napsat :). Kdyby měl nějaký linuxový král lepší verzi, tak jí mile rád přijmu.

**docker-compose.yaml**

```
version: '3.8'
services:
  
  #instalace php 8 na apachi z Docker souboru
  php-apache-environment:
    container_name: php-apache
    build:
      context: ./php
      dockerfile: Dockerfile
    depends_on:
      - db
    volumes:
      - ./php/src:/var/www/html/
    ports:
      - 8000:80

  #instalace databaze MySQL
  db:
    container_name: db
    image: mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: db
      MYSQL_USER: administrator
      MYSQL_PASSWORD: heslo
    ports:
      - 9906:3306

  #instalace phpmyadmin pro spravu databazi
  phpmyadmin:
    image: phpmyadmin/phpmyadmin
    ports:
      - 8080:80
    restart: always
    environment:
      PMA_HOST: db
    depends_on:
      - db
```

Pro docker existuje rozšíření jménem docker compose, které přijímá YAML soubory, ve kterých se propojí jednotlivé docker obrazy do jednoho spolupracujícího celku. Tento soubor provede následující:
1. Spustí náš předpřipravený obraz z Dockerfilu, propojí ho s databází (tu za chvilku vytvoříme), a nastaví port na 8000. Důležité je také propojení souborových systémů, kde na Apache serveru adresář /var/www/html nastavíme na náš adresář v počítači jako ./php/src
2. Stáhne docker obraz mysql z docker hub repositáře, nastaví jeho port na 9906, nastaví root heslo, vytvoří admina a nastaví mu heslo
3. Stáhne docker obraz phpmyadmin z docker hub repositáře, nastaví jeho port na 8080 a propojí ho s obrazem s názvem db (naše MySQL databáze)

**index.php**

```
<!DOCTYPE html>
<html>
<head>
    <title>Fakultonahrávač</title>
</head>
<body>
    <h1>Fakultonahrávač</h1>
    <form enctype="multipart/form-data" action="index.php" method="POST">
        <label for="fakulta">Kliknutím nahrajte recept ve validním XML souboru.</label>
        <br>
        <input type="file" name="fakulta" data-max-file-size="2M"/>
        <br>
        <button type="submit">Odeslat</button>
    </form>
<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $adresar_fakulty = 'fakulty/';
    $nahrana_fakulta = $adresar_fakulty . basename($_FILES['fakulta']['name']);

    if (file_exists($nahrana_fakulta)){
        echo '<p class="text-danger">Soubor se stejným názvem již existuje v databázi. Prosím přejmenujte soubor.!</p>';
    } 
    else if (move_uploaded_file($_FILES['fakulta']['tmp_name'], $nahrana_fakulta)) {
        $puvodni_xml = new DOMDocument();
        $puvodni_xml->load($nahrana_fakulta);
        $koren = 'fakulta';
        $generator_dokumentu = new DOMImplementation;
        $doctype = $generator_dokumentu->createDocumentType($koren, "", 'fakulta.dtd');
        $novy_xml = $generator_dokumentu->createDocument(null, "", $doctype);
        $novy_xml->encoding = "utf-8";

        $puvodni_uzel = $puvodni_xml->getElementsByTagName($koren)->item(0);
        $novy_uzel = $novy_xml->importNode($puvodni_uzel, true);
        $novy_xml->appendChild($novy_uzel);

        if ($novy_xml->validate()) {
            echo '<p>Nahraný soubor je validní a byl úspěšně nahrán do databáze.</p>';
        } else {
            echo '<p>Nahraný soubor není validní! Prosím zkontrolujte správnou strukturu.</p>';
            unlink($nahrana_fakulta);
        }
    } else {
         echo '<p>Došlo k chybě při nahrávání souboru!</p>';
    }
}
?>
</body>
</html>
```

Tento soubor obsahuje značně komplikovaný program, který validuje XML soubor vůči validačnímu souboru DTD. Problém vězí v tom, že PHP umí validovat pomocí DTD souborů pouze pokud jsou součástí XML souboru. Pravděpodobně asi nechcete nutit uživatele, ať to jeho XML souboru vkládá ručně DTD soubor z našeho serveru a pak nám ho zasílá (občas ani nemůže, protože XML soubor generuje a zasílá na náš server nějaká aplikace). Z toho důvodu tento skript vytvoří nový XML soubor, kam vloží text DTD souboru z našeho serveru a pak vloží text nahraného XML souboru a vytvoří tak nový XML soubor s vloženým DTD souborem. Asi vidíte, jak je to pitomé. Proto v praxi budete používat XSD soubory, které se naučíte používat příští cvičení. DTD soubory jsou starý formát se specifickým jazykem a omezenými možnostmi, přes to se dobře čtou a je to snadné k zapamatování na jednoduchou validaci. Proto doporučuji jejich strukturu se naučit ke státnicím. Úspěšně nahrané soubory se nám budou ukládat do adresáře fakulty.

Následně spustíme docker compose pomocí příkazu v terminálu: ```docker compose up --build -d```. Naše webová aplikace by měla běžet na localhostovi na portu 8000.

#### Jazyk XML

Pravděpodobně jste se již někdy setkali s XML kódem a pokud ne, tak jste si ještě pravděpodobněji setkali s HTML kódem, který představuje podmnožinu XML. Jazyk XML představuje standard pro počítačová data, které je možné vyměňovat mezi různými platformami. Mohu například stáhnout data z databáze a zobrazit je na mobilní aplikaci, webové stránce, textovém dokumentu nebo si je ponechat v raw podobě.

Prohlédněte si ukázku XML kódu pro popis dat na následujícím odkazu: [W3Schools XML Introduction](https://w3schools.com/xml/xml_whatis.asp)

Každý xml kód se zkládá z elementů, které představují dvojici data a značka (tag): [W3Schools XML Elements](https://w3schools.com/xml/xml_elements.asp)

K datům je dále možné přidat atributy, které přidávají dodatečnou informaci: [W3Schools XML Attributes](https://w3schools.com/xml/xml_attributes.asp)

Místo atributů je možné využít další element a neexistuje žádný standard k tomu, jaká informace by měla být dodána jako element a jaká jako atribut. Já osobně doporučuji, aby elementy byly informace pro čtenáře a atributy informy pro aplikaci, kterou XML soubor zpracováváte. To ovšem může způsobat problém s tzv. validací. Více o problematice elementy vs. atributy naleznete na [W3Schools Elements vs. Attr](http://w3schools.com/xml/xml_dtd_el_vs_attr.asp)

Jelikož mohou mít XML elementy stejné názvy, ale zcela jiný význam, mohly by se elementy při zpracování aplikací plést. Z toho důvodu je možné k elementům přidat prefix, který elementy dále kategorizuje do jmenných prostorů. Příklad může být problém table jako stolu a table jako tabulky: [W3Schools XML Namespaces](https://w3schools.com/xml/xml_namespaces.asp)

**Úkol 1.1: Student**

Vytvořte jednoduchý xml dokument, ve kterém budou informace o entitě student naší univerzity. Měl by tedy mít informace jako jméno, příjmení, studentské číslo, fakulta, aj. Některé informace můžete uložit do vnořených elementů, jiné do atributů. 

#### Well Formed XML

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

**Úkol 1.2: Well-formed XML**

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

### XML služby

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


**Úkol 1.3: RSS**
Stáhněte si do mobilního zařízení nebo počítače nějakou RSS čtečku (pro Android např.: Feedly) a přidejte si RSS feed na nějakou stránku. Pokud vydá nový příspěvek, přijde vám upozornění. Prozkoumejte jeho strukturu pokud jste na počítači. Pro zájemce si můžete vytvořit vlastní RSS k webové stránce a zasílat tak upozornění. Například pro Wordpress existují hotové pluginy.

### Návrh XML stromu

XML nemá žádný model pro grafickou reprezentaci, jako například třídy v OOP jako diagramy tříd z jazyka UML. Přesto by se nám nějaký alespoň primitivní grafický model
pro přemýšlení nad návrhem, komunikaci o datovém modelu v týmu nebo dokumentaci hodil. Jelikož XML představuje datovou strukturu, kde nalezneme prvotní značku (kořen), 
značky, obsahující další značky, (větve) a značky, neobsahující žádné další značky, (listy), tak se nabízí možnost zakreslit XML jako stromovou strukturu.

Na stránce [W3 Schools XML Tree](https://w3schools.com/xml/xml_tree.asp) vidíte grafickou reprezentaci xml kódu pomocí stromové struktury. Pod obrázkem naleznete kód k příslušnému stromu. 

**Úkol 1.4: Struktura XML dokumentu**

Vaším úkolem je vytvořit návrh struktury xml dokumentu podle následující klientské specifikace:
> Chtěl bych vytvořit webovou aplikaci pro záznam studentů naší univerzity. O studentovi zaznamenávejte informace: jméno, příjmení, studentské číslo, email, studijní rok, rozvrh, předměty, splněné předměty a další zajímavé informace.
> Chtěl bych vytvořit webovou aplikaci pro záznam fakult univerzity. O každé fakultě zaznamenávejte informace jako: děkan, katedry, vedoucí kateder, zaměstnanci, kontakt na zaměstnance, pozice zaměstnanců, tituly a další zajímavé informace

### Validní XML

Ve cvičení úkol 1.2 jste zkoušeli upravit XML soubor tak, aby byl "Well formed". Kromě "Well formed" by měl být XML soubor ještě validní. Aby byl XML dokument validní, pak se musí jeho struktura řídit šablonou ve formátu DTD (Document Type Definition) nebo XML Schema (novější typ šablony, která je sama o sobě XML). Představit si to lze obdobně jako v objektově orientovaném programování, kde v našem případě šablona odpovídá třídě a XML dokument odpovídá objektu (instanci třídy).

Ukázku DTD naleznete na stránce: [W3Schools XML DTD](https://w3schools.com/xml/xml_dtd.asp)

Každý DTD dokument se skládá ze stavebních bloků: [W3Schools XML DTD Building Blocks](https://w3schools.com/xml/xml_dtd_building.asp) a DTD představuje strukturu
na sebe navazujících bloků - co každý blok obsahuje za potomky a jaké má příbuzné.

1. Elementy [W3Schools XML DTD Elements](https://www.w3schools.com/xml/xml_dtd_elements.asp) - mohou být prázdné, s daty, s potomky, libovolnými bloky (element, data) a o různém počtu bloků (právě 1, alespoň 1, nula a více, nula nebo jeden) nebo s výčtem konkrétních bloků pomojí spojky OR.
2. Atributy [W3Schools XML DTD Attributes](https://www.w3schools.com/xml/xml_dtd_attributes.asp) - atributy mají typy (data, výčet, ID, odkaz na ID, entita, atd.) a hodnoty (pevně dané, povinné a volitelné)
3. Entity [W3Schools XML DTD Entities](https://www.w3schools.com/xml/xml_dtd_entities.asp) - zkratky za konstantní hodnoty, které často využíváte
4. Parsovaná data - data mezi elementy, která budou zpracována parserem a entity budou rozvinuty
5. Znaková data - data mezi elementy, která se berou doslovně a nejsou nijak zpracována (entity nebudou rozvinuty a v obsahu zůstane jejich alias)

**Úkol 1.5: Validace XML pomocí DTD**

Vaším prvním úkolem bude napsat XML soubor s názvem "prf.xml", která bude obsahovat informace o Přírodovědecké fakultě UJEP, a soubor s názvem "pf.xml", která bude obsahovat informace o Pedagogické fakultě UJEP. Tyto soubory musí být dobře formované (well-formed), tzn. nesmí mít žádné chyby v zápisu XML elementů jako například křízení značek a podobně. Dále musí být soubor validní, což znamená, že splňuje požadavky schématu (tím je soubor fakulta.dtd). Ověřte, zda jsou well formed a validní pomocí validátorů. DTD soubor, který máte k dispozici pro validaci bude automaticky použit při nahrání souboru na formulář v index.php.

```
<!ELEMENT fakulta (katedra+)>
<!ATTLIST fakulta 
děkan CDATA #REQUIRED>

<!ELEMENT katedra (vedoucí, zaměstnanci, předměty)>
<!ATTLIST katedra 
zkratka_katedry CDATA #REQUIRED
webové_stránky CDATA "https://www.ujep.cz/cs/"
>

<!ELEMENT vedoucí (jméno, (telefon|email)+)>

<!ELEMENT jméno (#PCDATA)>

<!ELEMENT telefon (#PCDATA)>

<!ELEMENT email (#PCDATA)>

<!ELEMENT zaměstnanci (zaměstnanec+)>

<!ELEMENT zaměstnanec (jméno, (telefon|email)+, pozice?)>

<!ELEMENT pozice (lektor|asistent|odborný_asistent|docent|profesor)?>
<!ELEMENT lektor EMPTY>
<!ELEMENT asistent EMPTY>
<!ELEMENT odborný_asistent EMPTY>
<!ELEMENT docent EMPTY>
<!ELEMENT profesor EMPTY>

<!ELEMENT předměty (předmět*)>

<!ELEMENT předmět (název, popis?)>
<!ATTLIST předmět 
zkratka CDATA #REQUIRED
typ (přednáška|seminář|cvičení|kombinované) "kombinované"
>

<!ELEMENT název (#PCDATA)>
<!ELEMENT popis (#PCDATA)>
```


**Video týdne 1: Základy internetových technologií**

Jelikož jste na kurzu programování pro internet, tak bude nutné znát, jak fungují některé internetové (komunikace) a webové (obsah) technologie. Následující video představuje souhrn všech důležitých termínů se kterými budete pracovat. [ZDE](https://www.youtube.com/watch?v=erEgovG9WBs)
