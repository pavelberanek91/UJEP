# Programování pro internet

**Obsah cvičení 4**:
* CSS
* XSLT
* XPath
* Bootstrap/W3.CSS

## Cvičení 4 - Zobrazení pomocí XSLT

V této lekci se seznamíte s navigací v XML dokumentu pomocí navigačního jazyka XPath a transformaci vyhledaných elementů do jiných jazyků pomocí jazyka XSLT. Tím si ušetříte velké množství práce, kterou byste museli jinak věnovat učením se knihoven pro práci s XML a GUI knihoven pro vizualizaci ve vybraném programovacím jazyce.

### On-site

#### XML technologie

Pokud XML představují jen holá data s významem, splňující schéma XSD, pak otázkou zůstává, jak tato holá validní data předat uživateli. Možností je napsat si aplikaci, která XML parsuje pomocí nějaké knihovny (případně si napsat vlastní parser) a vizualizovat je pomocí nějaké GUI knihovny. Chytřejší možností transformovat data na jiná, které rozumíme běžně používané aplikace (PDF čtečky, webové prohlížeče). K takové transformaci slouží jazyk XSLT (eXtensible Stylesheet Language Transformations), který představuje obdobu kaskádových stylů, ale XSLT je daleko mocnější stylový jazyk. Příklad XSLT naleznete na [W3Schools XML XSLT](https://w3schools.com/xml/xml_xslt.asp). 

S pracovními rámci pro kaskádové styly jako je W3.CSS nebo Bootstrap5 můžete díky předpřipraveným třídám i vytvořit transformaci XML do HTML, kde jsou prvkám rovnou přiřazeny třídy. XSLT může být při spojení s Bootstrap mocný nástroj, avšak představuje bezpečností díru a proto se již nevyužívá v praxi.

Pro potřeby transformace je nutné procházet řízeným způsobem XML dokumentem. K tomu nám slouží jazyk XPath, který přebírá navigační výrazy a nalezá příslušné prvky, splňující cestu definovanou navigačním výrazem. Tato technologie je důležitá nejen pro XSLT, ale i pro XQuery, umožňující dotazovat se nad XML dokumenty. Příklad XPath naleznete na [W3Schools XML XPath](http://w3schools.com/xml/xml_xpath.asp).

Tyto XML technologie obecně označujeme jako XSL jazyk (eXtensible Stylesheet Language - obdoba css ale silnější)[W3Schools XSL Language](https://w3schools.com/xml/xsl_languages.asp):
1. XSLT - jazyk pro transformaci
2. XPath - jazyk pro navigaci
3. XSL-FO - jazyk pro vizualizaci (již se nepoužívá, nahrazen CSS3)
4. XQuery - jazyk pro dotazování

#### Převod XML do HTML pomocí XSLT

Ukázku transformace z XML na HTML (konkrétně xhtml) naleznete na stránce [W3Schools XSLT Transform](https://w3schools.com/xml/xsl_transformation.asp). Transformace se provádí pomocí XSLT elementů:
1. <template> [W3Schools XSLT Template](https://w3schools.com/xml/xsl_templates.asp) - sada transformačních pravidel, aplikujících se na vyhledané uzly výrazem jazyka XPath v atributu match
2. <apply-templates> [W3Schools XSLT Apply](https://w3schools.com/xml/xsl_apply_templates.asp) - aplikace XSLT pravidel (templates) na element nebo jeho děti

#### Podmínky a cykly v XSLT

V jazyce XSLT lze využívat podmínky a cykly, kterými dále řídíme, na které uzly a jak aplikovat pravidla v templates. Tyto příkazy provádíme pomocí následujících elementů:
1. <value-of> [W3Schools XSLT ValueOf](https://w3schools.com/xml/xsl_value_of.asp) - získá data z jednoho uzlu a může je využít při transformaci
2. <for-each> [W3Schools XSLT ForEach](https://w3schools.com/xml/xsl_for_each.asp) - realizace cyklu v XSLT z vyfiltrovaného výběru XML uzlů
3. <sort> [W3Schools XSLT Sort](https://w3schools.com/xml/xsl_sort.asp) - slouží pro seřazení uzlů
4. <if> [W3Schools XSLT If](https://w3schools.com/xml/xsl_if.asp) - slouží jako realizace podmínky v XSLT
5. <choose> [W3Schools XSLT Choose](https://w3schools.com/xml/xsl_choose.asp) - realizace přepínače v XSLT (switch=<choose>, case=<when>, default=<otherwise>)

#### Využití XPath v XSLT

Jazyk XPath [W3Schools XPath Introduction](https://w3schools.com/xml/xpath_intro.asp) používá výrazy pro cesty ve tvaru osa::uzel[predikát] [W3Schools XPath Nodes](https://w3schools.com/xml/xpath_nodes.asp):
1. Uzel - XML je brán jako strom uzlů, kde uzel může být větev (element, atribut, data, atd.) nebo list (atomická hodnota - samotná data)
2. Osa [W3Schools XPath Axes](https://w3schools.com/xml/xpath_axes.asp) - relativní vztah k vybranému uzlu pro nalezení jeho příbuzných (rodič, dítě, sourozenec, předek, potomek, následný uzel, atd.)
3. Predikát - dodatečné nepovinné filtrování, viz cvičení Cv.3.4

#### Predikáty a operátory v XPath

Nad nalezenými uzly z XPath výrazu lze provádět dodatečnou filtraci predikáty nebo agregaci operátory. Díky predikátům a operátorům může být výsledek cesty množina uzlů, řetězec, boolean nebo číslo. Pokud budeme aplikovat XSLT, tak potřebujeme získat množinu uzlů. Bližší popis mechanismů predikátů a operátorů:
1. Predikát [W3Schools XPath Syntax](https://w3schools.com/xml/xpath_syntax.asp) - filtrují nalezený výsledek (první element, poslední, s atributem větším než, s atributem rovno, atd.), ale je možnost využít v nich i divokých karet (wildcards)
2. Operátor [W3Schools XPath Operators](https://w3schools.com/xml/xpath_operators.asp)- aritmetické (+,-,*,/,div,mod) a logické operace (=,!=,<,<=,>,>=,and,or), které je možné využít pro zpracování výsledku cesty

#### Kaskádové styly

Jelikož jazyk XSL-FO je již obsolete (ten je bohužel zapotřebí pro konverzi XML do PDF), tak se využívá pro vizualizaci dat CSS3. Kaskádové styly nejsou součástí našeho kurzu, avšak měli byste mít alespoň základní ponětí o nich. V tomto cvičení si vyzkoušíte naformátovat přetransformovaný XML dokument pomocí kaskádových stylů.

#### XSLT ve webových aplikacích

Nejčastější využití XML je u webových aplikací, takže otázkou zůstává, kde se vlastně transformace provádí u vztahu klient-server. K transformaci může docházet na straně klienta, kterému je do aplikace zaslán XML dokument, nejčastěji jazykem Javascript [W3Schools XSLT on the Client](https://w3schools.com/xml/xsl_client.asp), nebo na straně serveru, který XML transformuje pro klienta a zašle mu již transformovaný dokument [W3Schools XSLT on the Server](https://w3schools.com/xml/xsl_server.asp), např.: jazykem PHP.

**Úkol 4.1: Vytvoření XSLT souboru**

Vaším úkolem je k souborům fakulta a student vytvořit transformační soubory XSLT, které převedou XML do HTML stránky. Zde je ukázka transformačního souboru mého jiného projektu:

```
<?xml version="1.0" encoding="UTF-8"?>
<xsl:transform version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html"/>
    <xsl:template match="/">
        <html>
            <head>
                <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css" />
                <meta name="viewport" content="width=device-width,initial-scale=1"></meta>
                <title>Drinky</title>
            </head>
            <body>

                <header class="w3-container w3-teal w3-center">
                    <h1>Receptář drinků</h1>
                </header>

                <nav class="w3-bar w3-large w3-border-bottom w3-border-teal">
                    <a class="w3-bar-item w3-button w3-hover-none w3-text-grey w3-hover-text-teal w3-right w3-border-left" href="menu.xml">Zobraz recepty</a>
                    <a class="w3-bar-item w3-button w3-hover-none w3-text-grey w3-hover-text-teal w3-right w3-border-left" href="#">Zašli recept</a>
                </nav>

                <aside class="w3-sidebar w3-bar-block w3-border-right w3-border-teal" style="width:20%">
                    <ul> 
                        <xsl:for-each select="menu/recept">
                            <xsl:sort select="informace/název"/>
                            <li class="w3-bar-item w3-button w3-hover-none w3-text-grey w3-hover-text-teal">
                                <a style="text-decoration: none">
                                    <xsl:attribute name="href">
                                        <xsl:value-of select="concat('#article',position())"/>
                                    </xsl:attribute>
                                    <xsl:value-of select="informace/název" />
                                </a>
                            </li>
                        </xsl:for-each>
                    </ul>
                </aside>

                <main style="margin-left:25%">
                    <section>
                        <ul>
                            <xsl:for-each select="menu/recept">
                                <xsl:sort select="informace/název"/>
                                <li class="w3-ul w3-border w3-margin-bottom">

                                    <article class="w3-card-4 w3-bottombar w3-border-teal w3-padding-16">                                        
                                        <xsl:attribute name="id">
                                                <xsl:value-of select="concat('article',position())"/>
                                        </xsl:attribute>
                                        <header class="w3-container">
                                            <h2 class="w3-container w3-serif w3-text-teal">
                                                <xsl:value-of select="informace/název"/>
                                            </h2>
                                            <xsl:apply-templates select="informace"/>
                                        </header>
                                        <section class="w3-container">
                                            <xsl:apply-templates select="ingredience"/>
                                            <xsl:apply-templates select="postup"/>
                                        </section>
                                        <footer class="w3-container w3-text-grey">Autor: <xsl:value-of select="@autor_článku"/></footer>
                                    </article>

                                </li>
                            </xsl:for-each>
                        </ul>
                    </section>
                </main>

            </body>
        </html>
    </xsl:template>

    <xsl:template match = "informace">
        <table class="w3-table w3-tiny w3-bordered">
            <tr>
                <td>Název:</td>
                <td><xsl:value-of select="název" /></td>
            </tr>
            <tr>
                <td>Doba přípravy:</td>
                <td><xsl:value-of select="doba_přípravy" /> minut</td>
            </tr>
            <tr>
                <xsl:choose>
                    <xsl:when test="země_původu">
                        <td>Země původu:</td><td><xsl:value-of select="země_původu" /></td>
                    </xsl:when>
                    <xsl:otherwise>
                        <td>Země původu:</td><td>Neznámá</td>
                    </xsl:otherwise>
                </xsl:choose>
            </tr>
            <tr>
                <xsl:if test="node()">
                    <td>Obtížnost:</td><td><xsl:value-of select ="name(obtížnost/*[1])"/></td>
                </xsl:if>
            </tr>
        </table>
    </xsl:template>

    <xsl:template match = "ingredience">
        <h3 class="w3-opacity w3-large w3-margin-top">Ingredience:</h3>
        <ul class="w3-ul w3-card-4" style="width:50%">
            <xsl:for-each select="položka">
                <xsl:choose>
                    <xsl:when test="@typ='základ'">
                        <li class="w3-pale-red">
                            <xsl:value-of select="." />
                            <span class="w3-cursive w3-margin">(<xsl:value-of select="@typ"/>)</span>          
                        </li>
                    </xsl:when>
                    <xsl:when test="@typ='dochucovadlo'">
                        <li class="w3-sand">
                            <xsl:value-of select="." />
                            <span class="w3-cursive w3-margin">(<xsl:value-of select="@typ"/>)</span>          
                        </li>
                    </xsl:when>
                    <xsl:when test="@typ='dekorace'">
                        <li class="w3-pale-blue">
                            <xsl:value-of select="." />
                            <span class="w3-cursive w3-margin">(<xsl:value-of select="@typ"/>)</span>          
                        </li>
                    </xsl:when>
                    <xsl:otherwise>
                        <li>
                            <xsl:value-of select="." />
                        </li>
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:for-each>
        </ul>
    </xsl:template>

    <xsl:template match = "postup">
        <h3 class="w3-opacity w3-large w3-margin-top">Postup:</h3>
        <p>
            <xsl:value-of select="." />
        </p>
    </xsl:template>

</xsl:transform>
```

**Úkol 4.2: Transformace souboru v PHP**

Proveďte XSLT transformaci na serveru pomocí jazyka PHP. Skript zde uvedu. Na vás zbývá dotvořit záložku na webovém portále, kde si člověk vybere fakultu nebo studenta a při kliku se provede transformace příslušného xml souboru do html souboru, který se zobrazí návštěvníkovi.

```
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $adresar_recepty = '../recepty/';
        $nahrany_recept = $adresar_recepty . basename($_FILES['recept']['name']);

        if (file_exists($nahrany_recept)){
          echo '<p class="text-danger">Soubor se stejným názvem již existuje v databázi. Prosím přejmenujte soubor.!</p>';
        } else if (move_uploaded_file($_FILES['recept']['tmp_name'], $nahrany_recept)) {

          // XSD validace
          $xml = new DOMDocument;
          $xml->load($nahrany_recept);
          if ($xml->schemaValidate('../šablony/recept.xsd')){
          
            echo '<p class="text-success">Nahraný soubor je validní a byl úspěšně nahrán do databáze.</p>';
            
            // XML
            $xml_dokument = new DOMDocument();
            $xml_dokument->load($nahrany_recept);

            // XSL
            $xsl_dokument = new DOMDocument();
            $xsl_dokument->load("../styly/recept.xsl");

            // XSLTtransformation
            $xsl_procesor = new XSLTProcessor();
            $xsl_procesor->importStylesheet($xsl_dokument);
            $transformovany_xml = $xsl_procesor->transformToDoc($xml_dokument);
              
            // ulozeni transformovaneho dokumentu
            $nazev_dokumentu = basename($_FILES['recept']['name']) . ".html";
            $transformovany_xml->save("../dokumenty/" . $nazev_dokumentu );

          } else {
            echo '<p class="text-warning">Nahraný soubor není validní! Prosím zkontrolujte správnou strukturu.</p>';
            unlink($nahrany_recept);
          }
        } else {
            echo '<p class="text-danger">Došlo k chybě při nahrávání souboru!</p>';
        }
      }
```

Upravte si kód v PHP tak, aby fungoval pro váš webový portál.

**Úkol 4.3: Využití Bootstrap v XSLT**

Dodejte do XSLT souboru soubor s kaskádovými styly a používejte třídy frameworku bootstrap5 pro responzivní zobrazení webových stránek. V uvedeném transformačním souboru na míchané drinky z úkolu 4.1 můžete vidět, jak využívám konkurenční framework W3.CSS uvnitř transformace pro stylování vytvářeného HTML souboru responzivními třídami.

**Video týdne 1: CSS užitečné rady**

V této lekci jste si vyzkoušeli transformovat XML soubor na jiný XML soubor a dodat do něj kaskádové styly pro vytvoření (snad) pohledné grafiky. Pokud se ponoříte do CSS tak zjistíte, že to není příliš příjemná zkušenost. V následujícím videu naleznete rady, která vám mohou pomoct řešit určité problémy při stylování stránek. [ZDE](https://www.youtube.com/watch?v=Qhaz36TZG5Y)


**Video týdne 2: CSS moderně**

Patlání stylů ručně se již v dnešním ekosystému webových technologií nedělá. Podívejte se na následující video, které je zaměřené na CSS a JS, které vám ukáže, jaké technologie postaveně nad CSS se dnes používají pro stylování stránky pomocí CSS.[ZDE](https://www.youtube.com/watch?v=ouncVBiye_M)

