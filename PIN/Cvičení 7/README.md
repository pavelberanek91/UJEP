# Programování pro internet

## Cvičení 7 - PHP

### Samostudium

#### C7S1. Jazyk PHP

Věřím, že programování v novém jazyce vám již nedělá problémy. Všechny konstrukce již máte ze svých studijních let dostatečně osahané. Uvádím zde seznam toho, kde naleznete PHP programové konstrukce až narazíte na to, že je ve vašem kódu budete potřebovat:

1. [Hello world](https://www.w3schools.com/php/php_syntax.asp)
2. [Komentáře](https://www.w3schools.com/php/php_comments.asp)
3. [Proměnné](https://www.w3schools.com/php/php_variables.asp)
4. [Výpis obsahu proměnných](https://www.w3schools.com/php/php_echo_print.asp)
5. [Datové typy](https://www.w3schools.com/php/php_datatypes.asp)
6. [Podmínky](https://www.w3schools.com/php/php_if_else.asp)
7. [Přepínač](https://www.w3schools.com/php/php_switch.asp)
8. [While cyklus](https://www.w3schools.com/php/php_looping_while.asp)
9. [For cyklus](https://www.w3schools.com/php/php_looping_for.asp)
10. [Foreach cyklus](https://www.w3schools.com/php/php_looping_foreach.asp)
11. [Předčasné ukončení cyklu](https://www.w3schools.com/php/php_looping_break.asp)
12. [Do while cyklus](https://www.w3schools.com/php/php_looping_do_while.asp)
13. [Funkce](https://www.w3schools.com/php/php_functions.asp)
14. [Kolekce - pole](https://www.w3schools.com/php/php_arrays_indexed.asp)
15. [Kolekce - asociativní pole](https://www.w3schools.com/php/php_arrays_associative.asp)
16. [Kolekce - vícedimenzionální pole](https://www.w3schools.com/php/php_arrays_multidimensional.asp)
17. [Řazení kolekcí](https://www.w3schools.com/php/php_arrays_sort.asp)
18. [Práce s číslem](https://www.w3schools.com/php/php_numbers.asp)
19. [Práce s řetězcem](https://www.w3schools.com/php/php_string.asp)
20. [Matematický modul](https://www.w3schools.com/php/php_math.asp)
21. [Regulární výrazy](https://www.w3schools.com/php/php_regex.asp)
22. [Superglobální proměnné](https://www.w3schools.com/php/php_superglobals.asp)
23. [Callbacky](https://www.w3schools.com/php/php_callback_functions.asp)
24. [Výjimky](https://www.w3schools.com/php/php_exceptions.asp)

#### C7S2. Formuláře

V tomto cvičení budete potřebovat pracovat s formulářem v HTML a zpracovávat zaslaná data pomocí jazyk PHP.

1. [Získání dat z formuláře](https://www.w3schools.com/php/php_forms.asp)
2. [Validace zadaných dat do formuláře 1](https://www.w3schools.com/php/php_form_validation.asp)
3. [Validace zadaných dat do formuláře 2](https://www.w3schools.com/php/php_form_required.asp)
4. [Validace zadaných dat do formuláře 3](https://www.w3schools.com/php/php_form_url_email.asp)
5. [Zpětná vazba z formuláře](https://www.w3schools.com/php/php_form_complete.asp)

#### C7S3. Práce se soubory

V tomto cvičení budete potřebovat pracovat s adresářem a XML soubory. Zde naleznete základní operace nad souborovým systémem serveru v jazyce PHP:

1. [Čtení ze souboru](https://www.w3schools.com/php/php_file_open.asp)
2. [Zápis do souboru](https://www.w3schools.com/php/php_file_create.asp)
3. [Nahrávání souboru formulářem](https://www.w3schools.com/php/php_file_upload.asp)
4. [Filtrování dat z formuláře](https://www.w3schools.com/php/php_filter.asp)
5. [Pokročilé filtrování dat z formuláře](https://www.w3schools.com/php/php_filter_advanced.asp)
6. [Práce s XML pomocí SimpleXML 1](https://www.w3schools.com/php/php_xml_simplexml_read.asp)
7. [Práce s XML pomocí SimpleXML 2](https://www.w3schools.com/php/php_xml_simplexml_get.asp)
8. [API SimpleXML](https://www.w3schools.com/php/php_ref_simplexml.asp)
9. [Práce s XML pomocí Expatu parseru](https://www.w3schools.com/php/php_xml_parser_expat.asp)
10. [Práce s XML pomocí XMLDOM parseru](https://www.w3schools.com/php/php_xml_dom.asp)
11. [API XMLDOM](https://www.w3schools.com/php/php_ref_xml.asp)


#### C7S4. Adresářová struktura PHP projektu

Projekty v PHP nemají pevně danou strukturu. Existují ovšem doporučení pravidla. 

**Pravidlo číslo 1: Oddělení sémantiky**

* kód dělíme do modulů (různé funkce a třídy se souvisejícím kódem)
* moduly dělíme do jmenných prostorů (různé moduly se souvisejícím kódem)

**Pravidlo číslo 2: Oddělení HTML a PHP**

* PHP je kód pro předzpracování webového kódu na straně serveru (backend)
* HTML je kód pro tvorbu struktury webového kódu na straně klienta (frontend)
* Nedává smysl tyto dva světy míchat 

**Pravidlo číslo 3: Oddělení souborů**

1. Projekt by měl mít v dedikované složce všechny soubory veřejně přístupné přes HTTP/S protokol: složka public (CSS, JS, IMGS)
2. Projekt by měl mít v dedikované složce všechny kódy na straně serveru (PHP soubory): složka modules (PHP bez html kódu)
3. Projekt by měl mít v dedikované složce všechny kódy na straně klienta (šablonové PHP soubory): složka templates (HTML využívající PHP moduly - kód však píseme do souboru s příponou .php!)
4. Všechny tyto složky se dělí na sémanticky (významově) oddělené podsložky

**Pravidlo číslo 4: Jmenné konvence**

PHP nemá pevně dané jmenné konvence, takže je zcela na vás, zda budete využívat PascalCase, camelCase, snake_case. Měli byste však vámi zvolený styl dodržet. 

#### C7S5. OOP v PHP

PHP má široké možnosti v modelování entit pomocí objektově-orientovaného paradigmatu. V tomto cvičení budou vysvětleny následující partie OOP v PHP:
1. Rozhraní (interface)
2. Abstraktní třída 
3. Zapouzdření (encapsulation)
4. Dědičnost (inheritance)
5. Komunikace na úrovni tříd (klíčové slovo static)
6. Polymorfismus
7. Rys (trait)
```

V následujícím kódu vidíme definici rozhraní v jmeném prostoru interfaces. Rozhraní můžete dát do vašeho hlavního souboru s PHP kódem, do jiného souboru ve stejném jmenném prostoru nebo i do jiného souboru v jiném jmenném prostoru. Zde jsou nadefinované dvě rozhraní XMLZapisovatelné a SessionZapisovatelné. Obě rozhraní mají jednu metodu s parametry a bez implementace. Rozhraní představuje závazek pro třídy. Pokud nějaká třída implementuje rozhraní, tak se zavazuje, že si vytvoří implementaci (vlastní kód) k těmto metodám. Uživatel instancí třídy implementujících rozhraní se může spolehnout, že instance budou metodu umět (proto závazek). Mohu například nad všemi instancemi třídy, které implementují rozhraní XMLZapisovatelné (ať už to jsou instance libovolných tříd) ve foreach cyklu tuto metodu zavolat a nenastane chyba.

<?php

#definice jmenneho prostoru
namespace interfaces;

#rozhrani - vsechny tridy, ktere ho implementuji se zavazuji k implementaci metod
interface XMLZapisovatelne {
    public function zapisDoXML($cesta);
}

interface SessionZapisovatelne {
    public function zapisDoSession($klic, $hodnota);
}

?>
```

V následujícím kódu vidíme rys. Rysy jsou kolekce metod, které řeší problém vícenásobné dědičnosti v jazyce PHP. Jedná se o metody, které si může více tříd nahrát a jejich instance je následně mohou volat. Metody v definici rysu mají narozdíl od rozhraní vlastní implementaci. Třída může implementovat kolik rysů chce. Oproti rozhraním a dědičnosti tříd nemá rys sémantická pravidla použití. Metody v rysu by měly spolu souviset, avšak využívající třídy nemusí být v žádném vztahu. U rozhraní se třídy zavazují, u dědičnosti třídy rozšiřují předka u rysů je jen využívají.

```
<?php
namespace zabezpeceni;

trait Zabezpeceni {

    //XSS utoky typu: <script>location.href('http://www.hacked.com/%27)</script>
    public function predzpracuj_vstup($data){  //ochrani pred XSS utoky
        $data = trim($data);                   //stripnuti bilych znaku
        $data = stripslashes($data);           //odstran lomitka
        $data = htmlspecialchars($data);       //preved html znaky na jejich entitni podobu
        return $data;
    }
}
?>
```

V následujícím kódu vidíme abstraktní třídu. Abstraktní třídy využívá rys Zabezpeceni z jmenného prostoru zabezpeceni. Pomocí příkazu use využívá metody tohoto rysu, takže všichni potomci je zdědí. Dále obsahuje několik atributů se zvoleným modifikátorem přístupnosti. Dále vidíme konstruktor, který volá pro vstupní argumenty metody z rysu (predzpravuj_vstup) a poté si je uloží mezi své instanční atributy. Dále zde vidíme jednu abstraktní metodu vypis_informace, kterou si musí potomci této třídy implementovat.

```
use zabezpeceni\Zabezpeceni;

abstract class Clanek {

    #nahrani rysu (trait)
    use Zabezpeceni;

    #vlastnosti abstraktni tridy, ktere zdedi potomci
    protected $_autor;
    protected $_nazev;

    #rodicovsky konstruktor pro Recept (Recept ho vola, at nemusi v kodu konstruovat vse)
    public function __construct($autor, $nazev)
    {
        #pouziti metody z rysu (trait) pro validace dat - tento algoritmus muze mit vice trid
        $this->_autor = $this->predzpracuj_vstup($autor);
        $this->_nazev = $this->predzpracuj_vstup($nazev);
    }

    #abstraktni metoda, kterou musi potomek implementovat
    abstract public function vypis_informace();
}
```

Následující kód pro třídu rozdělím do více fragmentů kódu. Celý kód naleznete v přiložené složce v tomto cvičení. Kód začíná předpisem třídy, kde vidíme, že třída ja poslední třídou (nelze již tvořit potomky), rozšiřuje (je potomkem) třídy Clanek (abstraktní třída) a implementuje dvě rozhraní. Tyto rozhraní z jmenného prostoru interfaces používám přes alias I. Abychom mohli využívat rozhraní a rysy z jiných souborů, musíme si je nahrát příkazem require (zde používám relativní cestu).

Třída Recept má privátní atributy, které náleží potomkům, třídní konstantu (obsahuje cestu do xml databáze) a statickou metodu pro komunikaci na úrovni třídy. Tato proměnná se využívá jako čítač nahraných receptů do systému přes formulář.

```
#definice jmenného prostoru
namespace recept;

#vyzadovani jmenného prostoru pro praci (dependencies)
require "interfaces.php";
require "zabezpeceni.php";

#nahrani jmenneho prostoru s aliasem (import komponenty)
use interfaces as I;
use SimpleXMLElement;
use zabezpeceni\Zabezpeceni;

#vytvoreni nededitelne (final) tridy implementujici 2 rozhrani z jmenneho prostoru
final class Recept extends Clanek implements I\SessionZapisovatelne, I\XMLZapisovatelne{

    //unikatni vlastnosti potomka oproti rodici
    private $_puvod;
    private $_cas;
    private $_obtiznost;
    private $_ingredience;
    private $_postup;

    #tridni konstanta - nemuze byt zmenena, patri tride
    const XML_DATABAZE_RECEPTU = "menu.xml";

    #staticka promenna - muze byt zmenena, patri tride
    public static $pocet_vytvorenych_receptu = 0;
```

V následujícím kódu vidíme konstruktor a destruktor. Konstruktor přijímá sadu atributů skrze své parametry, volá si svůj rodičovský konstruktor pro nastavení atributů zděděných od svého rodiče a nastavuje si vlastní unikátní atributy. Pro zvyšování statické proměnné se využívá statická metoda, která se volá přes dvě dvojtečky. Stejně tak práce se statickou proměnnou se odehrává přes dvě dvojtečky. Po konstruktoru následuje destruktor, který při zničení objektu zapíše veškeré své informace do XML souboru. 

PS: Nejsem si jistý svou pamětí, ale mám dojem, že v destruktoru nastal velký problém s cestami. Při volání destruktoru jsem se objevil na nějaké jiné dočasné cestě v operačním systému, takže zápis do souboru musel probíhat absolutní cestou. Obecně tento způsob využívání destruktoru jako v mém kodu nedoporučuji. Mám ho zde uveden jen pro kompletnost OOP možností v jazyce PHP.

```
//konstruktor (ceckovsky typ commentu)
    public function __construct($autor, $nazev, $puvod, $cas, $obtiznost, $ingredience, $postup) {
        
        #volani rodicovske metody - konstruktor rodice
        parent::__construct($autor, $nazev);

        #nastaveni vlastnosti odlisnych od rodice
        $this->_puvod = $this->predzpracuj_vstup($puvod);
        $this->_cas = $this->predzpracuj_vstup($cas);
        $this->_obtiznost = $this->predzpracuj_vstup($obtiznost);
        $this->_ingredience = $this->predzpracuj_vstup($ingredience);
        $this->_postup = $this->predzpracuj_vstup($postup);
        
        #volani staticke metody tridy
        $this->_id = Recept::pocet_receptu() + 1;

        #inkrementace staticke promenne tridy
        Recept::$pocet_vytvorenych_receptu += 1;
    }

    /* 
    destructor (multiline comment) 
        pri destrukci objektu zapis jeho informace do xml pro zobrazeni a do sessionu informaci o tom,
        jaky clanek byl uzivatelem pridan (clanek bude pak specialne vyznacen)
    */
    function __destruct() {

        #zapise do hlavniho datoveho xml souboru novy clanek
        $this->zapisDoXML("menu.xml");

        #TODO: zapis do session (bude se pouzivat pro oznaceni receptu zadaneho aktualnim uzivatelem)
        $this->zapisDoSession("recepty", $this->get_nazev());
      }
```

V následujícím fragmentu vidíme sadu getterů a setterů, které nemají žádnou hlubší programovou logiku.

```
#gettery (Pythonovsky typ commentu)
    function get_autor(){return $this->_autor;}
    function get_nazev(){return $this->_nazev;}
    function get_puvod(){return $this->_puvod;}
    function get_cas(){return $this->_cas;}
    function get_obtiznost(){return $this->_obtiznost;}
    function get_ingredience(){return $this->_ingredience;}
    function get_postup(){return $this->_postup;}

    #settery
    function set_autor($value){$this->_autor = $value;}
    function set_nazev($value){$this->_nazev = $value;}
    function set_puvod($value){$this->_puvod = $value;}
    function set_cas($value){$this->_cas = $value;}
    function set_obtiznost($value){$this->_obtiznost = $value;}
    function set_ingredience($value){$this->_ingredience = $value;}
    function set_postup($value){$this->_postup = $value;}
```

V následujícím fragmentu vidíte metody. Nejprve vidíme metody vypis_informace a zapisDoSession, které se třída zavázala, že implementuje díky rozhraní. Všimněte si, že jsem úplně blbej a název metody vypis_informace jsem napsal snake_casem z jazyka Python :). Metoda zapisDoSession obsahuje kód, který v této lekci pro vás ještě není důležitý. Úplně na spod fragmentu vidíme statickou třídu, která vrací počet receptů v mé XML databázi (u mě je to jeden XML soubor, vy budete muset možná spočítat počet XML souborů ve vašem vybraném adresáři, tedy pokud vůbec budete chtít ve svém kódu podobný přístup využít).

```
    #metody, ktere jsou prislibem rozsirovani rodice
    public function vypis_informace(){
        echo $this->get_autor();
        echo $this->get_puvod();
        echo $this->get_cas();
        echo $this->get_obtiznost();
        echo $this->get_ingredience();
        echo $this->get_postup();
    }


    #metody, ktere jsou příslibem implementace rozhraní
    public function zapisDoSession($klic, $hodnota){
        echo "klic:".$klic." hodnota:".$hodnota." sess:".var_dump($_SESSION[$klic]);
        if (empty($_SESSION[$klic])) {
            $_SESSION[$klic] = array($hodnota);
            echo "EMPTY! klic:".$klic." hodnota:".$hodnota." sess:".var_dump($_SESSION[$klic]);
        } else {
            array_push($_SESSION[$klic], $hodnota);
            echo $_SESSION[$klic];
            echo "EXISTS! klic:".$klic." hodnota:".$hodnota." sess:".var_dump($_SESSION[$klic]);
        }
    }

    public function zapisDoXML($cesta){
    
        #zapis pomoci simpleXML do xml souboru
        $xml = simplexml_load_file(Recept::XML_DATABAZE_RECEPTU) or die("Chyba: nelze nacist xml soubor ".Recept::XML_DATABAZE_RECEPTU);        
        
        /* 
        bohuzel mi neslo vyresit pomoci xpath, jelikoz pak simplexml pise, ze pridavam do docasneho 
        stromu (nove vytvoreny uzel k nove vytvorenemu uzlu). Jina knihovna by to pravdepodobne zvladla 
        (nebo bych musel furt ukladat po kazde zmene) a mohl by se pouzit elegantnejsi XPath
        */
        $novy_recept = $xml->addChild("recept");
        
        $nova_informace = $novy_recept->addChild("informace");
        $nova_informace->addChild("název", $this->get_nazev());
        $nova_informace->addChild("země_původu", $this->get_puvod());
        $nova_informace->addChild("doba_přípravy", $this->get_cas());
        $obtiznost = $nova_informace->addChild("obtížnost");
        $obtiznost->addChild($this->get_obtiznost());

        $nove_ingredience = $novy_recept->addChild("ingredience");
        $nove_ingredience->addChild("položka", $this->get_ingredience());
        #TODO: rozsekat foreachem na jednotlive polozky

        $novy_postup = $novy_recept->addChild("postup", $this->get_postup());
        
        $xml->saveXML("menu2.xml");
    }
    

    #staticka metoda - zjisti pocet existujicich receptu v XML souboru, nevyzaduje instanci
    public static function pocet_receptu(){
        
        #simpleXml - nacte xml dokument
        $xml=simplexml_load_file(Recept::XML_DATABAZE_RECEPTU) or die("Chyba: nelze nacist xml soubor menu.xml");

        #vrat pocet potomku rootu
        return $xml->count();
    }  
```

Shrnutí:

* Abstraktní třídy obsahují předpisy (signatury) metod a implementované metody, ale nemůžete vytvářet její instance. Tato struktura je vhodná pro tvorbu společného předka, který reprezentuje základní chování rodiny tříd.
* Rozhraní (protokol) je množina předpisů metod, které nutí implementující třídu vytvořit vlastní konkrétní implementaci metody. Rozhraní jsou vhodné pro dodávání struktury a standardizace do kódové báze.
* Rys je skupina znovupoužitelných vlastností a metod. Třída může využívat více rysů. Rysy jsou vhodné pro organizaci kódu a snížení míry opakování se v kódu.

### Zadání cvičení

#### C7Z1. Formulář

Vytvořte formuláře, který slouží pro ruční zadávání dat o studentovi/fakultě (podle toho, k čemu jste psali validátor a xsl transformaci). Data z formuláře validujte tak, aby uživatel nenapsal nějakou chybu a neopomenul povinné informace na základě XSD šablony.

#### C7Z2. Data z formuláře do instancí tříd

Nahraná data z formuláře uložte do instance třídy, kterou pomocí XML souboru modelujete (student, fakulta). Vyzkoušejte si vhodným způsobem modelovací schopnosti jazyka PHP (rozhraní, gettery/settery, metody, statické proměnné, atd.).

#### C7Z3. Uložení dat z instance to XML souboru

Jedna z metod vaší třídy bude sloužit pro uložení dat do XML souboru. Vyberte si vhodný parser a uložte data. Nezapomeňte zvalidovat data vaší XSD šablonou a vyzkoušet, zda funguje XSL transformace.

#### C7Z4. Struktura projektu

Předělejte strukturu projektu tak, aby kód byl udržitelný. Oddělete html od php do šablon a modulů, zkontrolujte si dodržení jednotnosti jmenné konvence, atd.

**Video týdne 1: Webové technologie**

Dnes jste začali pracovat v jazyce PHP pro tvorbu zadního konce? (= backendu :) ...) webových stránek. Podívejte se na následující video, které vám ukáže další možné technologické ekosystémy, které můžete použít. [ZDE](https://www.youtube.com/watch?v=FQPlEnKav48)
