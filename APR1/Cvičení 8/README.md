# Algoritmizace a programování

## Cvičení 8 - Funkcionální programování

### On-site cvičení

V cvičení 6 jsem se zmínil o procedurách jako něčem, co je potenciálně nebezpečné, pokud je používáme neuváženě. Funkcionální programování je paradigmat (způsob uvažování), ve kterém se software skládá ze vzájemně volajících se funkcí. Pro procedury zde není místo a dokonce ani pro proměnné. Tím se zcela vyloučí možnost existence stavu. Pro takový způsob programování musí existovat speciální příkazy, které dokáží generovat data za parametry funkcí (generátorová notace, tzv. komprehenze), dokáží data z kolekcí upravovat algoritmem (tzv. map), dokáží z kolekcí vyhazovat data (filter), dokáží kolekce spojovat (zip), dokáží z kolekcí získat agregovanou hodnotu (reduce) a dokáží i vkládat funkce za běhu do programu (lambda).

Python není čistě funkcionální jazyk, tudíž si pouze vypůjčíme tyto funkcionální příkazy z funkcionálních jazyků, jelikož se nám dramaticky zkrátí kód. Nemusí se však zpřehlednit, proto pracuje s příkazy velice opatrně a dodržujte zásadu toho, že kód musí být hlavně čitelný.

Pojďme se podívat na schopnosti generátorové notace, tzv. komprehenze. Následující imperativní kód vytvoří prázdný seznam (to je prvotní stav) a následně v cyklu doplní 10 číslic od 0 do 9. Při každém připisování čísla metodou append dochází ke změnu stavu softwaru.

```
cisla = []
for cislo in range(10):
    cisla.append(cislo)
print(cisla)
```

Pojďme se podívat na funkcionální verzi tohoto příkladu:

```
cisla = [cislo for cislo in range(10)]
print(cisla)
```

Komprehenzi lze využít i při vkládání dat (argumentů) za parametry funkcí (to je její hlavní důvod existence ve funkcionálním programování):

```
def secti_cisla(seznam):
    return sum(seznam)

print(secti_cisla([cislo for cislo in range(10)]))
```

Komprehenze je však daleko mocnější nástroj. Zaprvé ji lze použít pro jakékoliv kolekce, takže lze pomocí ní naplnit například seřazenou ntici (tuple) nebo slovník. Dále její síla spočívá v tom, že kolekce je plněna vyhodnoceným výrazem. Tedy může se nacházet na místě prvku i velice komplexní výraz obalený funkcemi a klidně může být i ternární:

```
cisla = [str(cislo) if cislo % 2 == 0 else cislo for cislo in range(10)]
print(cisla)
```

Tento program naplní kolekci cislama, které jsou buď datového typu řetězec a to jen tehdy, pokud jsou sudá, jinak je naplní číslama typu celé číslo.

Kromě toho se může v komprehenzi i nacházet podmínka, při které se vůbec do kolekce výraz vyhodnotí. Tato podmínka se píše za cyklus. V následujícím kódu se komprehenze u každého čísla ptá, zda ho tam chceme. Pokud bude podmínka vyhodnocena jako pravdivá, tak se výraz teprve vyhodnotí. Pro přehlednost jsem rozdělil výraz, cyklus a podmínku zvlášť na řádky:

```
cisla = [str(cislo) if cislo % 2 == 0 else cislo 
         for cislo in range(10) 
         if input("Chces: ") == "jo"]
print(cisla)
```

Kromě toho lze komprehenzí generovat komprehenzi, což je velice užitečné při tvorbě více dimenzionálních struktur jako jsou matice nebo obecné tenzory. Následující příklad vytvoří seznam seznamů:

```
matice = [["X" for sloupec in range(3)] for radek in range(5)]
```

Dalším užitečným příkazem z funkcionálního programování je příkaz map. Map požaduje dva argumenty a to mapovací funkcí (ta může být zabudovaná do jazyka python, z nějakého načteného modulu nebo i uživatelem definovaná) a kolekci, na jejíž prvky postupně aplikuje mapovací funkci. Následující kód namapuje uživatelem definovanou funkci na komprehenzí generovaný seznam čísel:

```
def pricti_dva_vynasob_tremi(cislo):
    return (cislo + 2)*3

cisla = list(map(pricti_dva_vynasob_tremi, [cislo for cislo in range(20)]))
print(cisla)
```

Tento kód by šlo vytvořit také komprehenzí, ale kód by měl být pomalejší podle mého laického měření:

```
cisla = [pricti_dva_vynasob_tremi(cislo) for cislo in range(20)]
print(cisla)
```

Dalším příkazem je zip. Zip vyžaduje jako argumenty čárkou oddělené kolekce. Tyto kolekce poté spojí do seznamu seřazených ntic, kde v ntici jsou vždy prvky z kolekcí, které se vyskytují na stejných indexech. V novém Pythonu je chystaná změna, že pokud kolekce nejsou stejně dlouhé, pak program zahlásí výjimku. V aktuální verzi Pythonu na Google Colabu takové chování ještě není, takže filter je "blbuvzdorný".

```
prijmeni = ["Novak", "Skocdopolova", "Stekanatek", "Gyros", "Kebabova"]
pohlavi = ["M", "F", "NB", "F"]

data = list(zip(prijmeni, pohlavi))
print(data)
```

Dalším příkazem je filter. Filter vyžaduje obdobně jako map dva argumenty a to filtrační funkci (opět může být uživatelem definovaná) a kolekci, na kterou se filtrační funkce vykoná. Podstatné je to, že filtrační funkce musí vrátit pravdivostní hodnotu True nebo False, tedy datový typ bool. Pro prvky, pro které vrátí filtrační funkce hodnotu True, tak ty v kolekci zůstanou. Prvky pro které se vrací hodnota False z kolekce zmizí. Následující kód odstraní ze seznamu známek všechny, které nejsou známkou, tedy nejsou v rozmezí hodnot 1 až 5 včetně krajních hodnot.

```
def je_znamkou(znamka):
    return 1 <= znamka <= 5
    
znamky = list(filter(je_znamkou, [1,2,6,5,7,8,9,0,4,5]))
print(znamky)
```

Lambda funkce jsou funkce, které nemají jméno, proto se jim také říká anonymní funkce. Název lambda vznikl z matematické teorie zvané lambda calculus, který se jimi nazývá. Tyto funkce mají místo jména písmeno lambda. Nezajímá nás jejich název, jen tělo, tedy chování funkce. V programování představují funkce, které mohou vytvořit bez definování klíčovým slovem def. Slouží převážně jako jednoduché jednorázové funkce, které již opakovaně nevyužiji. Zadefinované funkce používáme opakovaně nebo jsou komplexnějšího charakteru.

Následující dva fragmenty kódu ukazují, jak lze přepsat zadefinovanou filtrační funkci, která je využívaná jako filtrační, do anonymní funkce.

```
def zacina_na_a(jmeno):
    return jmeno[0].lower() == "a"

print(list(filter(zacina_na_a, ["Alena", "Jiri", "Zbysek", "Adam"])))
```

```
print(list(filter(lambda jmeno: jmeno[0].lower() == "a", ["Alena", "Jiri", "Zbysek", "Adam"])))
```

Hlavní využití lambda funkcí u začátečníků je v případech nutnosti nastavení zabudovaných funkcí pythonu. Zabudované funkce jako min, max, sort pracují nad kolekcí. Pokud do nich vložíte kolekci kolekcí (například seznam seřazených ntic), tak pak neví, podle jakých hodnot mají vlastně provádět svůj algoritmus, neznají tedy svůj klíč. Ten lze nastavit lambda funkcí, která vrátí prvek z vložené kolekce, podle kterého se má algoritmus provádět.

```
hraci = [("Tomas", 20), ("Jana", 10), ("Karel", 15), ("Rostistlav", 30), ("Premysl", 25)]
hraci.sort(key=lambda hrac: hrac[1])
print(min(hraci, key=lambda hrac: hrac[1]))
print(max(hraci, key=lambda hrac: hrac[1]))
```

Výhodou lambda funkcí v pythonu je to, že můžete s nimi pracovat jako s proměnnou. Můžete je vkládat do za parametry funkcí, můžete ukládat odkaz na jejich algoritmus do proměnných (tím je vlastně zpětně pojmenujete), lze je vkládat do kolekcí a jiné zajímavé techniky.

```
uprava_pixelu = {
    "zesvetli": lambda px: px + 5,
    "ztmav": lambda px: px - 5
}

operace = input(f"Zadej co chces delat {uprava_pixelu.keys()}: ")
print(uprava_pixelu[operace](100))
```

Posledním příkazem je příkaz reduce. Příkaz reduce vyžaduje redukoční funkce a kolekci čísel. Redukční funkce je nějaká agregační (shrnující) funkce, která nahradí dimenzi hodnotou. Nejjednodušším příkladem je součtová funkce, která vezme seznam a nahradí ho jedním číslem, součtem hodnot v seznamu. Tím dochází k redukci seznamu na číslo (vektor na skalár). Obdobně lze redukovat matici na seznam, 3D tenzor na matici, atd. Tato technika je užitečná při práce s veledaty, kdy se znatelně urychlí zpracování dat v situacích, kdy se smíříme jen s agregovanou hodnotou, která v sobě nějakým způsobem informace z dimenze udržuje svým výsledkem.

V následujícím programu vidíte ukázku dvou redukčních funkcí, vytvořených lambda funkcí. První provádí součet čísel v kolekci a druhá součin čísel v kolekci. Parametr A představuje výsledek předchozí operace. Parametr B představuje aktuální prvek z kolekce. Příkaz reduce je inteligentní a v případě součtu pochopí, že prvotní číslo za A musí být 0, zatímco v případě součinu to musí být 1.

```
import functools

cisla = [cislo for cislo in range(1, 6)]
print(functools.reduce(lambda a, b: a+b, cisla))
print(functools.reduce(lambda a, b: a*b, cisla))
```

Jelikož je značně otravné psát za jednoduché lambda funkce do reduce příkazu celé tělo, existuje modul operator, kde se nachází redukční funkce. 

```
import functools
import operator

cisla = [cislo for cislo in range(1, 6)]
print(functools.reduce(operator.add, cisla))
print(functools.reduce(operator.mul, cisla))
```

**OS8.1: Řada čísel komprehenzí**

Vytvořte seznam naplnění číslama od 50 do 500 po 10 pomocí komprehenze.

```
cisla = [cislo for cislo in range(50, 501, 10)]
```

**OS8.2: Sudá čísla komprehenzí**

Vytvořte seznam sudých desetinných čísel od 0 do 20 pomocí komprehenze.

```
suda_cisla = [float(cislo) for cislo in range(21) if cislo % 2 == 0]
```

**OS8.3: Písmeno od indexu do indexu**

Vytvořte seznam naplněn písmenama od nějakého index do nějakého indexu, který si zvolí uživatel (0 = a, 1 = b).

```
import string
start = int(input("Zadej pocatecni index: "))
konec = int(input("Zadej konecny index: "))
pismena = [string.ascii_lowercase[idx] for idx in range(start, konec+1)]
pismena = list(string.ascii_lowercase[start:konec+1])
```

**OS8.4: Opakované nahrávání celého čísla**

Načtěte pomocí komprehenze opakovaně 5x vstup a přetypujte ho na int.

```
cisla = [int(input("Zadej cislo:")) for _ in range(5)]
```

**OS8.5: Mocniny dvojky**

Načtěte pomocí komprehenze mocnicny dvojky od 2 na nultou až 2 na desátou.

```
mocniny_dvojky = [2**mocnina for mocnina in range(11)]
```

**OS8.6: Náhodný šum**

Přepište následující program pro generování šumu do funkcionální podoby pomocí komprehenze. Matice je v Pythonu seznam seznamů, takže finta spočívá v generování seznamu seznamů.

```
import random
import matplotlib.pyplot as plt

matice = []
nradku = 50
nsloupcu = 100
for iradek in range(nradku):
    radek = []
    for jsloupec in range(nsloupcu):
        radek.append(random.randint(0, 255))
    matice.append(radek)

plt.imshow(matice, cmap="gray")
```

```
import random
import matplotlib.pyplot as plt

matice = [ [random.randint(0, 255) for j in range(nsloupcu)] for i in range(nradku)]

plt.imshow(matice, cmap="gray")
```

**OS8.7: Nezačínají na A**

Mějme seznam jmen = ["Alena", "Jiri", "Zbysek", "Adam"]. Odstraňte filterem včechna jména, která nezačínají na písmenko "a".

```
def zacina_na_pismeno_a(jmeno): 
    return jmeno[0].lower() == "a"

print(list(filter(zacina_na_pismeno_a, ["Alena", "Jiri", "Zbysek", "Adam"])))
```

**OS8.8: Nejsou číslem**

Mějme seznam ["1", "2", "Auto", "Kocka", "3"]. Odstraňte filterem všechny prvky, ktere nejsou číslo.

```
def je_cislem(retezec): 
    return retezec.isnumeric()

print(list(filter(je_cislem, ["1", "2", "Auto", "Kocka", "3"])))
```

**OS8.9: Prošli**

Mějme dva seznamy: ["Alena", "Milan", "Jakub"] a [5, 2, 1] (známky na vysvědčení). Proveďte filtr tak, aby v seznamu zůstali jen ti, kteří nepropadli. Vraťte je ve výsledné kolekci seznam dvojic (jméno, známka). Známku nahraďte řetězcem "prošel".

```
def nepropadl(student): 
    return 1 <= student[1] < 5

print(list([(student[0], "prošel") for student in filter(nepropadl, 
            zip(["Alena", "Milan", "Jakub"], [5, 2, 1]))]))
```

**OS8.10: Je číslem pomocí lambdy**

Přepište následující funkci do anonymní funkce a aplikujte ji ve filtru nad zadaným seznamem.

```
def je_cislem(retezec):
    return retezec.isnumeric()

print(list(filter(je_cislem, ["1", "2", "Auto", "Kocka", "3"])))
```

```
print(list(filter(lambda retezec: retezec.isnumeric(), ["1", "2", "Auto", "Kocka", "3"])))
```

### Domácí úkoly:

**HW8.1: Funkce Map svépomocí**

Napište algoritmus, který realizuje funkci Map(funkce, kolekce) jen za pomocí podmínky, cyklu a definované vlastní funkce.

**HW8.2: Funkce Zip svépomocí**

Napište algoritmus, který realizuje funkci ```Zip([1,...,n-kolekcí])``` jen za pomocí podmínky, cyklu a definované vlastní funkce.

**HW8.3: Náhodná čísla komprehenzí**

Napište algoritmus s využitím komprehenze, který vytvoří seznam naplněný náhodnými hodnotami od 5 do 10.

**HW8.4: Náhodná písmena komprehenzí**

Napište algoritmus s využitím komprehenze, který vytvoří seznam naplněný náhodnými hodnotami od "a" do "z" podle abecedy.

**HW8.5: Komprehenze se vstupem uživatele**

Napište algoritmus s využitím komprehenze, který vytvoří seznam naplněný řetězci, které budou v průběhu tvorby seznamu komprehenzí žádány ze vstupu příkazem input().

**HW8.6: Lichá čísla komprehenzí**

Napište algoritmus s využitím komprehenze, který vytvoří seznam lichých čísel.

**HW8.7: Velká abeceda bez samohlásek**

Napište algoritmus s využitím komprehenze, do kterého vložíte větu a komprehenze vám vrátí seznam slov z věty, které budou napsány velkou abecedou a budou odstraněny všechny samohlásky [a,e,i,o,u,y]

**HW8.8: Mapování kladných**

Napište algoritmus s využitím map, který převezme matici a vrátí seznam pravdivostních hodnot, kde pravdivostní hodnota představuje, zda v daném řádku jsou všechny prvky kladné.

**HW8.9: Mapování na délku řetězců**

Napište algoritmus s využitím map, který převezme řetězec zadaný uživatelem a vrátí seznam délek slov v řetězci.

**HW8.10: Mapování s filtrací**

Napište algoritmus s využitím map, který převezme seznam čísel, odstraní všechny kladné a vrátí seznam absolutních hodnot ponechaných čísel. Pro filtraci můžete použít funkci filter.

**HW8.11: Pořadí písmen**

Napište algoritmus s využitím zip, který převezme seznam čísel a seznam písmen a vrátí seznam dvojic (číslo, písmeno), kde číslo představuje pořadí písmena v abecedě. Pro zadání seznamu písmen využijte string.ascii_lowercase a seznam čísel vhodným způsobem vygenerujte na základě velikosti seznamu string.ascii_lowercase.

**HW8.12: Rozdělení seznamu**

Napište algoritmus, který pomocí funkce zip rozdělí seznam trojic na tři seznamy. Budete si muset tento jev vygooglit (zkuste hledat termín python unzipping).

**HW8.13: Součin trojic**

Napište algoritmus, který přijme seznam trojic a vrátí seznam, obsahující součiny prvků ve trojicích.

**HW8.14: Kvadrát lambdou**

Napište anonymní funkci, která provádí kvadrát z absolutní hodnoty z vloženého čísla.

**HW8.15: Skalární součin lambdou**

Napište anonymní funkci, která vrátí skalární součin dvou vektorů, které jsou argumentem.

**HW8.16: Odstranění malých písmen lambdou**

Napište anonymní funkci, která bude sloužit jako filtrační funkce pro příkaz filtr. Tato anonymní funkce odstraní všechny prvky, které nejsou velkým písmenem.

**HW8.17: Obrácení pořadí lambdou**

Napište anonymní funkci, která bude sloužit jako mapovací funkce pro příkaz map. Tato funkce obrací pořadí seznamů. Do funkce map tedy přije matice, kde řádky jsou seznamy, které budou anonymní funkcí obráceny.

**HW8.18: Fibonacciho posloupnost**

Vytvořte pomocí anonymní funkce Fibonacciho posloupnost.

**Video týdne 1: Chyby začátečníků**

V této lekci jste se naučili využívat i funkcionální příkazy, jako je filter, map, zip, comprehension, reduce, lambda a další užitečné příkazy. Pojďme se tedy podívat na některé chyby, které možná jste doposud dělali a jak je napravit. [ZDE](https://www.youtube.com/watch?v=qUeud6DvOWI)

**Video týdne 2: Cachování výsledků dekorátorem**

Dekorátory jsou funkce, které obalují jiné funkce. V Pythonu existuje spousty předpřipravených dekorátorů, u kterých ani nemusíte chápat vnitřní implementaci a stačí, když jen víte, k čemu a jak je použít. Na tomto videu uvidíte jeden velice užitečný dekorátor, který se hodí k cyklům, které využívají rekurzi. [ZDE](https://www.youtube.com/watch?v=DnKxKFXB4NQ)