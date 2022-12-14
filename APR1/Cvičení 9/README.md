# Algoritmizace a programování

## Cvičení 9 - Složitost algoritmů

V tomto cvičení ...

### On-site cvičení

Asymptotická analýza je proces výpočtu náročnosti algoritmu na prostředky. Existují tři způsoby, jak měřit náročnost:
* Omega = dolní hranice náročnosti
* Omicron = horní hranice náročnosti (nejčastější způsob měření)
* Theta = obě hranice (Omega i O)

Měření náročnosti se provádí v závislosti na počtu dat, které do algoritmu vstupují. Měří se dvě charakteristiky náročnosti:
1. časová = kolik času provedení algoritmu zabere
2. prostorová = kolik paměti provedení algoritmu zabere

Pokud například s každou další položkou v seznamu roste časová náročnost úměrně jedna ku jedné, pak se jedná o linerání náročnost. Pokud za každou datovou položku v seznamu náročnost neroste, pak se jedná o konstantní náročnost. Tyto řády náročnosti zapisujeme pomocí velkého písmena O a v závorkách závislost růstu. Časová náročnost se dá vyjádřit pomocí počtu potřebných operací pro zpracování, které označujeme písmenem N.

Řády náročnosti:
* O(1) = konstantní (skvělé)
* O(log n) = logaritmická (skvělé)
* O(sqrt n) = odmocninová (skvělé)
* O(n) = lineární (v pořádku)
* O(n*log n) = linearitmetická/kvazilineární (špatné)
* O(n**2) = kvadratická (příšerné)
* O(2**n) = exponenciální (příšerné)
* O(n!) = faktoriální (příšerné)

Analýza složitosti nebo alespoň znalost složitosti základních funkcí je užitečná pro optimalizaci kódu. Zejména pokud se jedná o náročné programy na časové a prostorové prostředky jako jsou počítačové simulace nebo videohry. Pokud chápete, které operace ve vašich algoritmech jsou nejvíce asymptoticky náročné, tak vyhledáte úzká hrdla vaší aplikace, na jejichž optimalizaci se můžete zaměřit. Přehled složitostí základních operací nad kolekcemi pythonu naleznete [ZDE](https://wiki.python.org/moin/TimeComplexity).

V tomto cvičení si vyzkoušíte předpřipravené algoritmy, jejichž asymptotickou složitost máte určit z grafického průběhu prodlužování doby nutné pro výpočet se zvětšováním množství dat a také pomocí speciální knihovny big_O.

**OS9.1: Měření času v Pythonu**

Pro měření času lze použít v jazyce python standardní knihovnu time.

```
import time
start = time.time()
pocet_dat = 1000000
for _ in range(1000000):
    pass
konec = time.time()
ubehnuty_cas = konec - start
print(f"Pro vstup o velikosti {pocet_dat} trvalo vykonání algoritmu {ubehnuty_cas} sekund)
```

Pro vykreslení závislosti jedné veličiny na druhé můžeme použít knihovnu matplotlib, která však není součástí standardní knihovny pythonu. Pokud někdo z vás pracuje na svém lokálním počítači v nějakém prostředí jako je VS Code, bude nutné si tuto knihovnu nainstalovat. Knihovnu nainstalujeme do svého počítače pomocí příkazu do terminálu/příkazové řádky: ```pip install matplotlib```. Kdo pracuje v Google Colab, tak tam je knihovna již nainstalována.

Následující program vykreslí časovou náročnost For cyklu (procedura iteracni_cyklus) v závislosti na počtu dat, které musí proiterovat (pocet_cisel). Počet dat je v tomto programu 10E0, 10E1, 10E2, 10E3, 10E4, 10E5, 10E6 (vědecká notace zápisu 10 na ...). Program si ukládá do seznamu doba_trvani a pocet_cisel jaká byla velikost dat a jak dlouho program trval. Tyto data poté vykreslí pomocí modulu matplotlib na obrazovku. Jako první argument procedury plot je osa x (tedy počet čísel pro zpracování) a na ose y je doba trvání. Příznak "ro-" je grafický formát vykreslované řady, tedy červené barva, data puntíkama, které budou propojené čárou.

```
import time
import matplotlib.pyplot as plt

def iteracni_cyklus(pocet_cisel):
    for cislo in range(pocet_cisel):
        pass

zaklad = 10
maximalni_exponent = 6
doba_trvani = []
pocet_cisel = []
for exponent in range(maximalni_exponent + 1):
    start = time.time()
    iteracni_cyklus(zaklad**exponent)
    konec = time.time()
    pocet_cisel.append(zaklad**exponent)
    doba_trvani.append(konec-start)

plt.plot(pocet_cisel, doba_trvani, "ro-")
plt.show()
```

**OS9.2: Modul big_O**

Pro Python existuje modul, který nám změří, do které ze složitostí daný algoritmus nejpravděpodobněji spadá. Tento modul není základním modulem jazyka Python (naprogramoval ho dobrovolník). Modul vyžaduje tři věci pro spočítání nejpravděpodobnější složitosti a to:
1. funkci, ve které je měřený algoritmus (může být uživatelem definovaná i zabudovaná)
2. generátor dat, které se budou do algoritmu vkládat
3. počet opakování, po které bude měřit

Modul vrátí po zavolání své hlavní funkce big_o(funkce, generátor, počet_měření) nejpravděpodobnější složitost a slovník všech složitostí k nim reziduál (jak moc daná složitost sedí na daný algoritmus). Nás nebude tento slovník zajímat, takže ho ukládám v kódu do proměnné _, kterou typicky v pythonu značíme, že nás hodnota nezajímá a nezaslouží si pojmenovat. Generátory dat se tvoří pomocí lambda funkcí a počet opakování se zde nachází z toho důvodu, že časy trvání jsou různé (možná jste si všimli z minulého kódu při opakovaném spouštění). Proto je nutné měření opakovat a následně z výsledků usoudit na nejlepší složitost.

```
def najdi_nejvetsi_cislo(cisla):
    nejvetsi_nalezene_cislo = 0
    for cislo in cisla:
        if cislo > nejvetsi_nalezene_cislo:
            nejvets_nalezene_cislo = cislo
    return nejvetsi_nalezene_cislo

generator_celych_kladnych_cisel = lambda cislo: big_o.datagen.integers(cislo, 0, 10000)
nejlepsi_komplexita, _ = big_o.big_o(najdi_nejvetsi_cislo, generator_celych_kladnych_cisel, n_repeats=100)
print(nejlepsi_komplexita)
```

Generátor je anonymní funkce, která vytváří seznam náhodných čísel od specifikované hodnoty do specifikované hodnoty:

```
f = lambda cislo: big_o.datagen.integers(cislo, 0, 10)
print(f(10))
```

Měření zabudovaných funkcí pythonu je jednoduché, stačí místo uživatelské funkce uvést název zabudované funkce. 

```
slozitost, _ = big_o.big_o(sorted, lambda cislo: big_o.datagen.integers(cislo, 10000, 50000))
print(slozitost)
```

Tato knihovna má jednu nevýhodu a to, že funkce musí mít pouze jeden parametr. Tím je pro složitější algoritmy nepoužitelná, nebo se musí dělat různé způsoby obcházení, které trošku znejisťují výsledné měření.


**OS9.3: Konstantní náročnost**

Algoritmus má konstantní náročnost pokud počet nutných operací se nemění s velikostí vstupu. Příkladem může být přidání dat na konec seznamu. Nezáleží na tom, kolik prvků se nachází v seznamu, zda žádný nebo 1000. Přidat prvek na konec seznamu trvá vždy stejnou dobu.

```
l = []
l.append(1)

l = list(range(1000))
l.append(1)
```

Bonus: vykonejte více běhů a zprůměrujte výsledek.

**OS9.4: Logaritmická náročnost**

Algoritmus má logaritmickou náročnost pokud se počet nutných operací snižuje o určitou hodnotu s každým dalším krokem. Příkladem může být algoritmus binárního prohledávání. Tento algoritmus vrací pravdivostní hodnotu, zda se hledaný prvek nachází uvnitř seřazené kolekce. Algoritmus nalezne prostředek kolekce a zjistí, zda je hledaný prvek větší nebo menší prostřední prvek. Podle toho zkrátí napůl seznam a algoritmus se opakuje. Vzhledem ke zkracování prohledávaného intervalu na polovinu vždy se přidávání další datové položky příliš neprojeví na časové náročnosti.

```
def binarni_vyhledavani(data, hledana_hodnota):
    levy_okraj = 0
    pravy_okraj = len(data)-1
    nalezeno = False

    while levy_okraj <= pravy_okraj and not nalezeno:
        prostredek = round((levy_okraj + pravy_okraj)/2)
        if data[prostredek] == hledana_hodnota:
            nalezeno = True
        else:
            if hledana_hodnota < data[prostredek]:
                pravy_okraj = prostredek-1
            else:
                levy_okraj = prostredek+1

    return nalezeno

data = [0, 1, 2, 8, 13, 17, 19, 32, 42,]

print(binarni_vyhledavani(data, hledana_hodnota=3))
```

Bonus: vykonejte více běhů a zprůměrujte výsledek.

**OS9.5: Odmocninová náročnost***

Algoritmus má odmocninovou náročnost pokud počet potřebných operací je závislý na počtu prvočísel pod odmocninou. Příkladem je program, který zjišťuje, zda je zadané číslo prvočíslem. Využívá k tomu jednoduchý algoritmus, při kterém se vezmou všechna čísla od 2 do zkoumaného čísla nevčetně a pokud je zkoumané číslo dělitelné nějakým z předchozích čísel beze zbytku, pak číslo není prvočíslem.

```
def je_prvocislem(cislo):
    if cislo >= 2:
        for predchozi_cislo in range(2, cislo):
            if cislo % predchozi_cislo == 0:
                return False
    else:
        return False
    return True
```

Bonus: vykonejte více běhů a zprůměrujte výsledek.

**OS9.6: Lineární náročnost***

Algoritmus má linární závislost v případě, kdy počet potřebných operací se lineárné zvedá s velikostí vstupních dat. To se děje v následujícím příkladě, který zjišťuje, zda se v kolekci nachází vyhledávány prvek. Přidáním dalšího prvku se úměrně tomu zvedne i doba vyhledávání. Složitosti O(n), O(2*n), atd. považujeme všechny za lineární.

```
def vyhledej_prvek(hledany_prvek, data):
    for prvek in data:
        if prvek == hledane_prvek:
            return True
    else:
        return False

vyhledej_prvek(hledany_prvek=5, data=range(10))
```

Bonus: vykonejte více běhů a zprůměrujte výsledek.

**OS9.7: Linearitmetická náročnost***

Algoritmus má linearitmetickou závislost v případě, že počet operací se s velikostí vstupu zvětšuje jako velikost dat vynásobeno logaritmem z velikosti dat. Typickým příkladem jsou rekurzivní řadící algoritmy jako quick sort. Quick sort funguje tak, že v každém kroku vybere náhodně prvek (pivot) a získá prvky menší a větší jak pivot. Následně se pro tyto dva vzniklé nové seznamy zavolá opět quick sort, kde seznamy jsou argumentem. Tímto dělením na menší seznamy vzniká logaritmická složitost. Funkce je takto rekurzivně volaná a následně se vynořuje a řádně se poskládá zpět, což zanáší komplexitu N navíc. Tím dostáváme N*log N.

```
from random import randrange

def quicksort(data):
    if len(data) < 2:
        return data
    else:
        nahodne_cislo = randrange(0, len(data))
        pivot = data.pop(nahodne_cislo)
        mensi_nez_pivot = [cislo for cislo in data if cislo <= pivot]
        vetsi_nez_pivot = [cislo for cislo in data if cislo > pivot]
        return quicksort(mensi_nez_pivot) + [pivot] + quicksort(vetsi_nez_pivot)

print(quicksort([10, 5, 2, 3, 7, 0, 9, 12]))
```

Bonus: vykonejte více běhů a zprůměrujte výsledek.

**OS9.8: Kvadratická náročnost***

Algoritmus má kvadratickou složitost, když počet operací představuje čtverec (druhá mocnina) z velikosti datového vstupu. Příkladem může být dvojný cyklus. Pro každou iteraci vnějšího cyklu se provádí iteratování skrze celý vnitřní cyklus. Pokud bychom měli 3 cykly, tak se jedná o O(n**3). Těmto typům komplexností říkáme souhrnně polynomiální.

```
def vytiskni_pozice(input):
    for i in input:
        for j in input:
            print(f'i: {i}, j: {j}')

vytiskni_pozice(range(10))
```

Bonus: vykonejte více běhů a zprůměrujte výsledek.

**OS9.9: Exponenciální náročnost***

Algoritmus má exponenciální složitost v případě, že vyžadovaný počet operací pro zpracování dat roste s množstvím dat exponenciálně. Příkladem je Fibonacciho posloupnost. Pro výpočet například 6. čísla posloupnosti je zapotřebí rekurzivní vyvolávání nad všema předešlýma číslama.

```
def fibonacci(generace):
    if (generace <= 1):
       return generace
    return fibonacci(generace - 2) + fibonacci(generace - 1)
```

Bonus: vykonejte více běhů a zprůměrujte výsledek.

**OS9.10: Faktoriální náročnost***

Algoritmus má faktoriální složitost, pokud počet operací roste s počtem permutací vstupních dat, které jsou možné vytvořit. Takových problémů existuje bohužel spousty. Jedním z nejznámějších je problém obchodního cestujícího. Obchodní cestující si má vybrat nejkratší cestu mezi 10 městy. Pokud přidáme 11 město, tak se musí zohlednit při výpočtu jak toto přidané město ovlivní cestu z každého jiného města (napojíme ho na všechna města). Problém obchodního cestujícího se řeší v kurzu evolučního modelování. Proto zde uvedu jednodušší příklad a to je výpočet řady faktoriálů až do zvoleného maximálního faktoriálu.


```
def faktorial(cislo):
    for i in range(cislo):
        print(f'Iterace {i}: {cislo}')
        factorial(cislo-1)

print(faktorial(10))
```

Bonus: vykonejte více běhů a zprůměrujte výsledek.

### Domácí úkoly:

**HW9.1: Matematické definice náročnosti**

V následujícím článku si pročtětě definice náročností typu Omega, Omicron a Theta. Zkuste je pochopit na základě vašich znalostí z teoretických základů informatiky.

https://algoritmy.net/article/102/Asymptoticka-slozitost

**HW9.2: Amortizovaná složinost**

Pročtěte si následující článek, který vám vysvětlí, jaký je rozdíl mezi asymptotickou složitostí a tzv. amortizovanou složitostí.

https://algoritmy.net/article/3024/Amortizovana-slozitost

**HW9.3: P a NP**

Řády náročnosti lze dělit ještě do tříd náročnosti. Nejznámější dělení ja na P (problémy řešitelné v polynomiálním čase) a NP (problémy řešitelné v polynomiálním čase jen nederministickým strojem). 

https://algoritmy.net/article/1240/Algoritmus

**HW9.4: P = NP?**

Velkou otázkou vědy zůstává, zda P = NP nebo se tyto dvě třídy nerovnají. Pokud tento pravděpodobně nejsložitější problém teoretické informatiky vyřešíte, sláva vás nemine.

https://cs.wikipedia.org/wiki/Probl%C3%A9m_P_versus_NP

