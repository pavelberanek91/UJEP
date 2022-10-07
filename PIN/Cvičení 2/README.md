# Programování pro internet

**Obsah cvičení 2**:
* Psaní schémat jazykem DTD
* Psaní schémat jazykem XSD
* Fragmentace XSD schémat na logické celky
* Validace pomocí XSD v php

## Cvičení 2 - Popisování jazykem XSD

V této lekci se seznamíte s psaním velice komplexních XML Schémat pomocí jazyka XML, který vám umožní psát velice komplexní webové aplikace, využívající XML soubory od klientů.

### On-site

#### Úkol 2.1 - Jazyk XSD

XSD Schema je alternativa k šabloně v DTD formátu. Tento způsob psaní schémat je daleko složitější, ale silnější, než DTD. XSD je název jazyku, který se používá pro popis XML schémat a znamená XML Schema Definiton (je zde trošku terminologický zmatek - někdo používá termín XML Schema, někdo XSD Schema).
- Ukázku XSD Schema naleznete na stránce: [W3Schools XML Schema](https://w3schools.com/xml/xml_schema.asp)
- Porovnání XSD a DTD schémat můžete nalézt na této stránce: [W3Schools XSD How To](https://w3schools.com/xml/schema_howto.asp)

#### XSD Simple elements

Základní stavební bloky XSD dokumenty jsou:
1. kořen [W3Schools XSD <schema>](https://w3schools.com/xml/schema_schema.asp) - každý XSD potřebuje kořenový element, v něm se mohou nacházet definice jmenných prostorů
2. elementy [W3Schools XSD Elements](https://w3schools.com/xml/schema_simple.asp) - jsou dvou typů a to simple a complex; simple obsahují data v primitivních datových typech jako string, decimal, integer, boolean, date a time; complex obsahují další elementy nebo atributy
3. atributy [W3Schools XSD Attributes](https://w3schools.com/xml/schema_simple_attributes.asp) - obsahují data o stejných typech jako simple elementy a mohou být implicitní (default), pevně dané (fixed) a vyžadované (required) a dělají z elementu komplexní typ
4. restrikce [W3Schools XSD Restrictions](https://w3schools.com/xml/schema_facets.asp) - určují rozsah nebo výčet hodnot, kterých musí data elementů a atributů nabývat
5. data - jsou typu [string](https://w3schools.com/xml/schema_dtypes_string.asp), [date](https://w3schools.com/xml/schema_dtypes_date.asp), [numeric](https://w3schools.com/xml/schema_dtypes_numeric.asp), [misc](https://w3schools.com/xml/schema_dtypes_misc.asp) (boolean, binary, anyURI, double, float, atd.)

#### XSD Complex elements

Komplexní element v XSD představuje element, který obsahuje další elementy, atribut a/nebo restrikce [W3Schools XSD Complex](https://w3schools.com/xml/schema_complex.asp) a dělíme je na:
1. Prázdné elementy [W3Schools XSD Empty](https://w3schools.com/xml/schema_complex_empty.asp) - element bez obsahu, ale může mít atributy (takže může obsahovat data)
2. Pouze s elementy [W3Schools XSD Elementy Only](https://w3schools.com/xml/schema_complex_elements.asp) - element nebo sekvence elementů, která může být pojmenovaná 
3. Pouze s textem [W3Schools XSD Text Only](https://w3schools.com/xml/schema_complex_text.asp) - jednoduchý element s rozšířením nebo restrikcí  
4. Smíšené [W3Schools XSD Mixed](https://w3schools.com/xml/schema_complex_mixed.asp) - kombinace předchozích 

#### XSD Indikátory

Jazyk XSD obsahuje mechanismus indikátorů, které jsou určené k tomu, aby řídily způsob používání XML elementů [W3Schools XSD Indicators](https://w3schools.com/xml/schema_complex_indicators.asp). Dělíme je na indikátory:
1. Řádu - řídí pořadá elementů (all = libovolné pořadí, choice = exkluzivní výběr, sequence = přesně dané pořadí)
2. Výskytu - řídí počet elementů (maxOccurs = maximální počet elementů, minOccurs = minimální počet elementů)
3. Skupiny - řídí uspořádání prvků do pojmenovaných skupin

#### Substituční skupiny

Další užitečným mechanismem je substituční mechanismus, který lze využít např.: pro vícejazyčné XML dokumenty. XSD umožňuje definovat skupinu zaměnitelných elementů (tzv. substituční skupina), ve které jsou elementy vzájemně zaměnitelné [W3Schools XSD Substitution](https://w3schools.com/xml/schema_complex_subst.asp).

#### XSD Libovolné elementy

Pokud chceme ještě větší volnost a umožnit vložit uživateli v XML v nějaké části libovolné elementy, pak můžeme využít v XSD element <any> [W3Schools XSD Any](https://w3schools.com/xml/schema_complex_any.asp). Obdobný mechanismus existuje i pro atributy elementů pomocí <anyAttribute> [W3Schools XSD anyAttribute](https://w3schools.com/xml/schema_complex_anyattribute.asp).


**Úkol 2.1 - DTD soubor student**

Napište DTD validační soubory k entitě student z minulé hodině. Pokud se vám nelíbí moje DTD k fakultě, tak si také vytvořte vlastní DTD pro fakultu.

Zde vidíte příklad mého DTD souboru, který slouží pro validaci barmanských receptů:

```
<!ELEMENT menu (recept+)>
<!ATTLIST menu xmlns:xsi CDATA #FIXED "http://www.w3.org/2001/XMLSchema-instance">
<!ATTLIST menu xsi:noNamespaceSchemaLocation CDATA #FIXED "menu.xsd">

<!ELEMENT recept (informace, ingredience, postup)>
<!ATTLIST recept 
autor_článku CDATA #REQUIRED
hodnocení CDATA #FIXED "1"
počet_hodnotících CDATA #FIXED "0">

<!ELEMENT informace (název, země_původu?, doba_přípravy, obtížnost)>

<!ELEMENT název (#PCDATA)>

<!ELEMENT země_původu (#PCDATA)>

<!ELEMENT doba_přípravy (#PCDATA)>

<!ELEMENT obtížnost (začátečník|pokročilý|mistr)?>
<!ELEMENT začátečník EMPTY>
<!ELEMENT pokročilý EMPTY>
<!ELEMENT mistr EMPTY>

<!ELEMENT ingredience (položka+)>
<!ATTLIST ingredience počet_porcí CDATA "1">

<!ELEMENT položka (#PCDATA)>
<!ATTLIST položka 
odkaz_koupě CDATA #IMPLIED
typ (základ|dochucovadlo|dekorace|nezařazené) "nezařazené">

<!ELEMENT postup (#PCDATA)>
```

**Úkol 2.2 - Přepsání DTD souboru na XSD soubor**

K DTD souborům vytvořte XSD soubory, které budou validovat stejné XML soubory. Jelikož XSD umí více než DTD, můžete rozšířit validační možnosti. Zaměřte se na to, ať máte XSD soubory přehledně strukturované. 

Zde vidíte příklad mého XSD souboru, který slouží pro validace barmanských receptů:

```
<?xml version="1.0" encoding="UTF-8" ?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">

<!-- definition of simple elements -->
<xs:element name="název" type="xs:string"/>
<xs:element name="doba_přípravy" type="xs:positiveInteger"/>
<xs:element name="obtížnost" type="xs:string"/>
<xs:element name="země_původu" type="xs:string"/>
<xs:element name="postup" type="xs:string"/>
<xs:element name="obtížnost">
    <xs:complexType />
</xs:element>

<!-- definition of simple types -->
<xs:simpleType name="položka_typ">
    <xs:restriction base="xs:string">
        <xs:enumeration value="základ"/>
        <xs:enumeration value="dochucovadlo"/>
        <xs:enumeration value="dekorace"/>
        <xs:enumeration value="nezařazené"/>
    </xs:restriction>
</xs:simpleType>

<!-- definition of attributes -->
<xs:attribute name="autor_článku" type="xs:string"/>
<xs:attribute name="hodnocení" type="xs:positiveInteger" fixed="1"/>
<xs:attribute name="počet_hodnotících" type="xs:decimal" fixed="0"/>
<xs:attribute name="počet_porcí" type="xs:positiveInteger" default="1"/>
<xs:attribute name="odkaz_koupě" type="xs:string"/>
<xs:attribute name="typ" type="položka_typ" default="nezařazené"/>

<!-- definition of complex types -->
<xs:element name="menu">
    <xs:complexType>
        <xs:sequence>
            <xs:element ref="recept" minOccurs="1" maxOccurs="unbounded"/>
        </xs:sequence>
    </xs:complexType>
</xs:element>

<xs:element name="recept">
  <xs:complexType>
    <xs:sequence>
      <xs:element ref="informace"/>
      <xs:element ref="ingredience"/>
      <xs:element ref="postup"/>
    </xs:sequence>
    <xs:attribute ref="autor_článku" use="required"/>
    <xs:attribute ref="hodnocení"/>
    <xs:attribute ref="počet_hodnotících"/>
    </xs:complexType>
</xs:element>

<xs:element name="informace">
  <xs:complexType>
    <xs:sequence>
      <xs:element ref="název"/>
      <xs:element ref="země_původu" minOccurs="0" maxOccurs="1"/>
      <xs:element ref="doba_přípravy" />
      <xs:element ref="obtížnost" minOccurs="0" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>

<xs:element name="ingredience">
  <xs:complexType>
    <xs:sequence>
      <xs:element ref="položka" minOccurs="1" maxOccurs="unbounded"/>
    </xs:sequence>
    <xs:attribute ref="počet_porcí" default="1"/>
  </xs:complexType>
</xs:element>

<xs:element name="položka">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension base="xs:string">
                <xs:attribute ref="odkaz_koupě"/>
                <xs:attribute ref="typ"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>

</xs:schema>
```

**Úkol 2.3 - Validace validního XML souboru XSD souborem**

Přepište soubor index.php tak, aby validoval ne pomocí DTD schématu, ale pomocí XSD schématu. Tento úkol vyřešíte po chvilce googlení :).