<?php

#definice jmenného prostoru
namespace recept;

#vyzadovani jmenného prostoru pro praci (dependencies)
require "interfaces.php";
require "zabezpeceni.php";

#nahrani jmenneho prostoru s aliasem (import komponenty)
use interfaces as I;
use SimpleXMLElement;
use zabezpeceni\Zabezpeceni;


#abstraktni trida, jejiz instance nelze vytvorit a 
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


}

?>