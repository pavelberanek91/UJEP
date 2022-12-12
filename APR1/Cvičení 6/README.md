# Algoritmizace a programování

## Cvičení 6 - Uživatelské funkce

### On-site cvičení

Během programování se vám stane, že občas potřebujete nějaký váš algoritmus (logická sekvence příkazů) opakovat ve více částech kódu než jen v jednom cyklu. Takové algoritmy dáváme do struktury, která se nazývá funkce. Funkce je struktura, do které obdobně jako v matice vložíte nějaké vstupní argumenty a ona vám vrátí nějakou návratovou hodnotu. Zavolání funkce pro získání její návratové hodnoty vidíte v následujícím kódu:

```
def secti_cisla(seznam):    #definice funkce
    soucet = 0
    for cislo in seznam:
        soucet += cislo
    return soucet           #návratová hodnota

vysledek_souctu = secti_cisla([1, 2, 3]) #volání funkce s argumentem [1, 2, 3]
print(vysledek_souctu)
```

Funkce je tzv. podprogram, tedy část programu, která je samostatně existovatelná. Její závislost na vnějším světě by byla být co nejmenší, ideálně žádná. To zaručují parametry funkce. Parametry funkce nalezneme v definici funkce. Název parametrů je zcela na nás. Za parametry se dosazují konkrétní argumenty.

```
#                          parametry
def secti_dve_cisla(cislo_prvni, cislo_druhe):
    vysledek_souctu = cislo_prvni + cislo_druhe
    return vysledek_souctu

a = 5
b = 3
#                      argumenty
soucet = secti_dve_cisla(a, b)
print(soucet)
```

Jak vám asi došlo, pro správnou funkčnost funkcí je nutné dodržovat přesné pořadí argumentů (tzv. args). Ještě je možnost nedodržet pořadí, pak můžeme zadat argumenty pomocí předpisu parametrů, za které je chceme dosadit (takzvané argumenty klíčovým slovem - keyword arguments, kwargs). Dokonce lze i míchat argumenty typu args a kwargs, ale musí být dodrženo pravidlo, že args předchází kwargs.

```
def secti_dve_cisla(cislo_prvni, cislo_druhe):
    vysledek_souctu = cislo_prvni + cislo_druhe
    return vysledek_souctu

a = 5
b = 3
#                       arg,     kwarg
soucet = secti_dve_cisla(a, cislo_druhe=b)
print(soucet)
```

Python je jazyk, která je dynamicky typovaný, tzn. narozdíl od staticky typovaných jazyků nemusíme předem psát, že do proměnné budeme ukládat pouze data typu celé číslo, řetězec, aj. Občas mohou některé funkce vykonat chybný kód, pokud do nich vložíme argumenty, které nejsou pro ně vhodné. Proto existuje v Pythonu možnost napovídání typů, tzv. type-hinting. Napovídáním typů píšeme pro nás v budoucnu a další programátory v týmu, jaké datové typy argumentů mají vložit, pokud chtějí, aby funkce neskončila chybovým voláním (tzv. výjimkou). Lze psát typy jak pro argumenty (píšou se k parametrům funkce), tak jakého typu bude návratová hodnota. Python neobsahuje příliš typů (chybí volatelná funkce tzv. Callable typ) nebo jsou příliš obecné (například seznam jako list, ale nelze zvolit jaké typy mají být v seznamu). Pokud byste potřebovali složitější typy, pak se nachází v modulu typing. Kromě napovídání typů mohou paramety mít i svou implicitní (default) hodnotu, pokud za ně nevložíme žádný argument.

```
def secti_dve_cisla(cislo_prvni: float, cislo_druhe: float = 0.0) -> float:
    vysledek_souctu = cislo_prvni + cislo_druhe
    return vysledek_souctu

soucet = secti_dve_cisla(cislo_prvni = 3.2)
print(soucet)
```

Kromě funkcí existují i speciální podprogramy, které se nazývají procedury. Procedury jsou funkce, které nemají návratovou hodnotu. Provedou pouze algoritmus. Pokud nebudeme používat příkazy jako global, tak nemají schopnost příliš měnit svůj svět a pak jsou neškodné. Někteří lidé je však používají pro změnu hodnot proměnných mimo svůj blok podprogramu, tedy mění stav systému (hodnoty proměnných). To je velice nebezpečná technika, proto vznikl paradigmat funkcionální programování, které procedury absolutně vylučuje. My budeme procedury používat zejména pro výpis na obrazovku nebo provádění nějakých úkonů od databáze (ulož data do databáze, smaž data z databáze, atd.). K proceduře můžeme dát nápovědu typu jako None, jelikož nic nevrací.

```
def pozdrav(koho: str) -> None:
    print(f"Ahoj {koho}")

pozdrav(koho="Jarmila")
```

**OS6.1: Která písmena jsou velká?**

Napište funkci, do které vložíte řetězec a vrátí se vám seznam velkých písmen.
```
def vrat_velka_pismena(retezec: str) -> list:
    velka_pismena = []
    for pismeno in retezec:
        if pismeno.isupper():
            velka_pismena.append(pismeno)
    return velka_pismena

print(vrat_velka_pismena("Ahoj Jak Se Mas Terezo?"))
```

**OS6.2: Vyhledání pozice slova**

Napište funkci, která vrátí index prvku, který vyhledáváte. Nepoužívejte předpřipravenou funkci index nad seznamem.

```
př.: get_index([g,f,a,f,h], a) -> 2
```

```
def vrat_index_prvku(prvky: list, hledany_prvek: any) -> int:
    for idx in range(len(prvky)):
        if prvky[idx] == hledany_prvek:
            return idx

print(vrat_index_prvku([1,2,3,4,5,6], 4))
```

**OS6.3 - Řada lichých čísel**

Napište funkci, do které vložíte počáteční a konečný prvek z číselné řady a program vám vrátí všechna lichá čísla z této řady.

```
př.: get_licha(min=5,max=15) -> [5,7,9,11,13,15] 
```

```
def vrat_licha_cisla_rady(min_cislo: int, max_cislo: int) -> list:
    licha_cisla = []
    for cislo in range(min_cislo, max_cislo+1):
        if cislo % 2 == 1:
            licha_cisla.append(cislo)
    return licha_cisla

print(vrat_licha_cisla_rady(5, 50))
```

**OS6.4: Pretty printer matic**

Napište proceduru, která přijme 2D matici (seznam seznamů) a ve vhodné grafické textové podobě ji vypíše na obrazovku.

```
def vytiskni_matici(matice: list) -> None:
    for radek in matice:
        print(" ".join(radek))

matice = [
    ["X", "O", "O"],
    ["X", "_", "_"],
    ["_", "X", "_"] 
]

vytiskni_matici(matice)
```

**OS6.5: Vykreslovací procedura**

Napište proceduru, která přijme seznam hodnot na ose y (řady) a k tomu popisky osy x. Následně vykreslí do jednoho grafu v knihovně matplotlib data na obrazovku. Tím budete mít připravenou proceduru jako náhražku Excelu.

```
import matplotlib.pyplot as plt

def vykresli_graf(kategorie: list, rady: list, nazev: str, 
                  nazev_osy_x: str, nazev_osy_y: str, styl_rad: list) -> None:
    plt.title(nazev)
    plt.xlabel(nazev_osy_x)
    plt.ylabel(nazev_osy_y)
    for irada, rada in enumerate(rady):
        plt.plot(kategorie, rada, styl_rad[irada])
    plt.show

rady = [
    [5, 6, 3, 1, 0],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
]    
kategorie = ["Po", "Ut", "St", "Ct", "Pa"]
styly = ["ro", "b-", "g.-"]
vykresli_graf(
    kategorie = kategorie, 
    rady = rady,
    nazev = "Graficek",
    nazev_osy_x = "dny", 
    nazev_osy_y = "nejaka cisla",
    styl_rad = styly
)
```

### Domácí úkoly:

**HW6.1 - Registrace uživatele**

Napište proceduru, která vloží do seznamu tuple s loginem a heslem, pokud se login již nenacházi v seznamu uživatelů a heslo se liší od loginu.

```
př.: registruj((jana, 896), [(jana, 123)(petr, heslo)] -> neregistruje

př.: registruj((milan, milan), [(jana, 123)(petr, heslo)] -> neregistruje

př.: registruj((milan, 896), [(jana, 123)(petr, heslo)] -> registruje
```

**HW6.2: Validace hesla**

Napište funkci, která požádá uživatele o heslo a vrátí ho, pouze pokud heslo obsahuje alespoň 1 velké písmeno, 4 malé písmeno a alespoň 1 číslo. Pokud heslo neobsahuje tyto znaky, pak žádá o zadání hesla ještě 2x, jinak vypíše chybu printem a vrátí None.


**HW6.3: Nalezení písmen s háčky a čárkami**

Napište funkci, který nalezne všechna písmena ve větě, která obsahují háčky a čárky a vrátí seznam těchto písmen. Věta bude vstupem funkce.

```
př.: nalezni_hacky_carky("čau jak se máš") -> [č,á,š]
```

**HW6.4 - Objem tělesa**

Napište funkci, která spočíta objem vloženého tělesa. Vstupem budou délky hran a typ tělesa. Výstupem bude objem. Typy těles jsou - krychle, kvádr, koule.

```
př.: get_objem([2,3,4], "kvádr") -> 24
př.: get_objem([2], "koule") -> 33.5
```

**HW6.5: Všechna velká**

Napište funkci, do které vložíte řetězec a vrátí se vám řetězec, který bude obsahovat všechna písmena velká.

```
př.: get_velka("Ahoj") -> "AHOJ"
```

**HW6.6: Čísla bezezbytku**

Napište funkce, do které vložíte počátek číselné řady, konec číselné řady a modulo a vrátí se vám počet čísel dělitelných v řadě modulem bezezbytku.

```
př.: delitelna_bez(a=5, b=20, mod=5) -> [5,10,15,20]
```

**HW6.7: Počet výskytů**

Napište funkci, do které vložíte řetězec a znak a vrátí se vám počet výskytů tohoto znaku v řetězci.

```
př.: pocet_vyskytu("aha hmm", "h") -> 2
```

**HW6.8: Každé druhé**

Napište funkci, do které vložíte řetězec a funkce vám vrátí každé druhé písmeno. Můžete použít list slicing.

```
př.: kazde_druhe("ahojpepo") -> [h,j,e,o] nebo "hjeo"
```

**HW6.9: Smazání písmenka**

Napište funkci, do které vložíte řetězec a znak a funkce vám vrátí seznam písmen bez vloženého znaku. Můžete použít remove.

```
př.: smazani("ahoj", "o") -> [a,h,j]
```

**HW6.10: Spojení seznamů**

Napište funkci, do které vložíte dva seznamy a funkce vám vrátí seznam složený ze dvou řetězců na přeskáčku.

```
př.: spoj([1,2,3],["a","b","c"]) -> [1,"a",2,"b",3,"c"]
```

**HW6.11: Skalární součin**

Napište funkci, která přijme dva seznamy čísel o stejné velikosti a vrátí jejich skalární součin.

př.: sksoucin([1,2,3],[2,3,4]) -> 1x2 + 2x3 + 3x4 = 20


**HW6.12: Náhodný seznam**

Napište funkci, která vrátí seznam náhodných desetinných čísel v rozmezí od a do b, kde a,b jsou parametry funkce.


**HW6.13: Promíchání písmenek**

Napište funkci, do které vložíte seznam písmenek a funkce vrátí nový seznam, kde budou tato písmenka náhodně rozmíchaná.

**HW6.14: Zašifrování a dešifrování textu**

Napište funkci, do které vložíte text a substituční slovník. Funkce provede substituční šifru, kde nalezená písmena ve slovníku (klíče) přemění na příslušné hodnoty. Př.: text="ahoj", substituční slovník = {a = j, o = k} pak funkce vrátí "jhkj". Obdobně napište i dešifrovač textu.

**Video týdne 1: idiom Main**

Většina programovacích jazyků má vstupní bod s názvem Main. Python takový bod nemá. Další problém je dán tím, že soubory v pythonu mohou být jak moduly, tak skripty. Pokud má kód s logikou v prvním bloku - globálním (plně neodsazeno), tak se kód spustí při importu. Proto použití idiomu Main je možné oddělit chování programu při importování a při používání ve formě programu. Více o tom v následujícím videu: [ZDE](https://www.youtube.com/watch?v=g_wlZ9IhbTs)