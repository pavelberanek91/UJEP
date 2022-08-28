# Algoritmizace a programování 1

## 1. Informace o předmětu

Úvodní kurz algoritmizace a programování (první část) se zaměřuje na základy procedurálního a objektově orientovaného paradigmatu. Pozornost je soustředěna především na objektovou representaci základních kolekcí (řetězců, seznamů, slovníků) a na elementární algoritmy nad nimi. Kurz je určen pro začátečníky (nepředpokládají se předchozí znalosti programování). Výuka (přednášky a cvičení) bude probíhat v jazyce Python.

Přednáší: [Mgr. Jiří Fišer, Ph.D.](https://ki.ujep.cz/cs/personalni-slozeni/jiri-fiser/)

## 2. Informace o cvičení

Cvičení jsou vedeny samostatnou prací studentů na úkolech ze zadání na tomto repozitáři. Cvičící slouží jako mentor během hodin: pomáhá s vysvětlováním problematiky, hledá chyby v případě "záseku" studenta a radí, jak nejlépe cvičení vyřešit. Odpovědnost za učení je převážně na studentovi. Teorii potřebnou na cvičení získá z přednášek a z materiálů, které jsou ke každé lekci uvedené v tabulce sylabus cvičení. Student si musí tyto materiály před samotným cvičením projít, aby cvičením rozuměl.

Cvičí:
1. [Ing. Mgr. Pavel Beránek, MBA, LL.M.](https://ki.ujep.cz/cs/personalni-slozeni/pavel-beranek/)
2. [RNDr. Jiří Škvára, Ph.D.](https://ki.ujep.cz/cs/personalni-slozeni/jiri-skvara/)
3. [Ricardo Rodríguez Jorge, Ph.D.](https://ki.ujep.cz/cs/personalni-slozeni/ricardo-rodriguez-jorge/)

## 3. Sylabus přednášek

1. Základní terminologie objektově orientovaného programování, objekty (hodnoty) základních tříd (čísla, logické hodnoty) a operace resp. metody nad nimi
2. Proměnné, standardní vstup a výstup, větvení programu (konstrukce if-then)
3. Cykly (while a for), předčasné ukončení cyklů
4. Řetězce a metody nad řetězci, indexace, modifikovatelné odkazované hodnoty (referenční sémantika)
5. Seznamy (rozhraní), asymptotická (časová) složitost
6. Uživatelské funkce (vstupní parametry, návratové hodnoty, oblast viditelnosti proměnných), n tice
7. Klíčové algoritmy nad seznamy (např. duplikace, filtrace, redukce)
8. Slovníky (rozhraní, využití pro representaci asociativních polí, řídkých polí a mezipamětí [cache])
9. Hashovací tabulky (interní implementace, hashovací funkce)
10. Vstup a výstup do souborů (textový)
11. Vstup a výstup do souborů (binární), bytová pole
12. Výjimky a základní ošetření výjimek, kontextový manager (with) použitý ve správě prostředků
13. Závěrečné shrnutí

## 4. Sylabus cvičení

|  Týden |  Název |  Obsah | Materiály | Zadání |
| :----: | :----: | :----: |  :----:   | :----: |
|    1   |  Google Colab | seznámení s prostředím, markup jazyk, proměnná, artimetické a logické operace    | [Materiály]() | [Zadání]() |
|    2   |  Vstup a výstup | výstup, vstup, podmínky, větvení a vnoření podmínek, logické spojky v podmínce | [Materiály]() | [Zadání]() |
|    3   |  Cykly | cyklus while, řídící proměnná, cyklus for (foreach), předčasné ukončení cyklu a iterace | [Materiály]() | [Zadání]() |
|    4   |  Řetězce | indexace, vyhledávání, mutabilita, reference a kopie, metody řetězců                  | [Materiály]() | [Zadání]() |
|    5   |  Seznamy | metody seznamů, procházení seznamu, spojování seznamů, množiny, asymptotická složitost| [Materiály]() | [Zadání]() |
|    6   |  Vlastní funkce | parametry, návratové hodnoty, návrat a rozbalení n-tice, algoritmy, návrh SW   | [Materiály]() | [Zadání]() |
|    7   |  Algoritmy nad seznamem | duplikace, generování, mapování, filtrace, zipování, redukce           | [Materiály]() | [Zadání]() |
|    8   |  Slovníky a jejich využití | metody slovníku, asociativní pole, řídké pole, mezipaměti           | [Materiály]() | [Zadání]() |
|    9   |  Hashovací tabulky | implementace, hashovací funkce, využití v bezpečnosti, princip blockchain   | [Materiály]() | [Zadání]() |
|   10   |  Práce se soubory | čtení, zápis a připisování do textových souborů, binární soubory, bytová pole| [Materiály]() | [Zadání]() |
|   11   |  Práce s adresáři | tvorba a kopírování adresářů a souborů, procházení souborovým systémem       | [Materiály]() | [Zadání]() |
|   12   |  Ošetření výjimek | kontextový manažer, strom výjimek, hierarchie výjimek, testování assercí     | [Materiály]() | [Zadání]() |
|   13   |  Opakování na zápočtový test |  práce s kolekcí, vlastní algoritmy, práce se souborovým systémem | [Materiály]() | [Zadání]() |


## 5. Podmínky získání zápočtu

Podmínkou získání zápočtu je zpracování seminární práce nebo úspěšné napsání zápočtového písemného testu. Zápočet je možné i získat, pokud cvičící usoudí programátorské nadání jedince na cvičeních na základě plnění všech úkolů ze cvičení. 

Zápočtový test proběhne ve zkouškovém období. Kód bude psán na papír pomocí psacích potřeb a jsou povolené libovolné vytištěné materiály. Zakázány jsou jakékoliv elektronické prostředky (chytré hodinky, telefon, tablet, laptop, aj.). Cílem bude napsat sadu menších programů, které řeší zadané problémy. Příklad zápočtového testu naleznete [ZDE]().

Seminární práci si vymýšlí student sám a schvaluje ji cvičící, nebo v případě zájmu bude nějaké zadání vymyšleno přednášejícím/cvičícím. Kontrola toho, zda student své práci dostatečně rozumí (dokáže vysvětlit jednotlivé řádky a mentální postup za nimi) proběhne na konzultacích příslušného cvičícího (pokud garant předmětu neurčí jinak). Příklad seminární práce naleznete [ZDE]().
