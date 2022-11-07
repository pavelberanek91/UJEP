# Algoritmizace a programování

Pro úspěšnou programátorskou kariéru je nutné trénovat 3 základní dovednosti informatického myšlení:
1. dekompozice problému na dílčí části
2. abstrakce činností do obecných celků
3. vyhledávání vzorů

Dekompozice vám umožní složitý problém (u nás program) rozdělit na dílčí části, které je možné zvlášť vyřešit (naprogramovat) a poté propojit do jednoho funkčního celku. 

Abstrakce umožní neopakovat zbytečně stejný kód pod sebou a zobecnit ho pro univerzálnější využití. Typickým příkladem je namísto ptaní se na konkrétní hodnoty v kolekci od prvné do poslední je využít index, který navyšujeme iterováním v cyklu. Abstrahovat lze i do vyšších celků, jako jsou podprogramy, třídy, moduly a podsystémy.

Vyhledávání vzorů umožní poznat v programu typický problém, který jsme již řešili nějakým postupem, například známým algoritmem.

Takový logicky uspořádaný kód je pak přehlednější, sémantičtější a zejména upravitelnější a opravitelnější. Z technické hlediska nám k tomu pomůže v jazyce python definice podprogramu. Podprogramy rozdělujeme na funkce a procedury (tento terminus technicus se může zdroj od zdroje lišit, nebudu ho striktně vyžadovat). Funkce vracejí nějaké návratové hodnoty a procedury nevracejí. Podprogramy mají své vstupní parametry, které mohou mít implicitní (defaultní) hodnoty nebo mohou být jejich hodnoty určeny argumenty). Podprogramy volají jiné podprogramy nebo hlavní program (typicky zvaný main). 

Python není staticky typovaný jazyk. Přesto se hodí psát alespoň formou nápovědy, s jakým datovým typem podprogram počítá u svých parametrů nebo jaký datový typ navrací jako návratovou hodnotu. Tomuto mechanismu se říká napovídání typů - type hinting. Python umí type hinting pro mnohé typy, avšak pokud nějaký chybí, pak ho naleznete v knihovně typing. Nový python 3.11 by měl umět i návratovou hodnotu self, tudíž s další verzí pythonu počítejte s novými typy k dispozici bez knihovny Callable. Type hinting pro parametry se píše pomocí dvojtečky v definici funkce u parametrů a type hinting pro návratovou hodnotu se píše za název funkce pomocí šipky.

Proceduru main budeme realizovat tak, že na poslední řádky programu napíšeme podmínku, která rozhoduje o tom, zda náš program je hlavním programem. Nahrávané moduly jsou také programy a jejich kód se při importování spustí. Hlavní program se od importovaného modulu liší tím, že jeho systémová proměnná ```__name__``` je rovna hodnota ```"__main__"```. V této konstrukci se píšou dvě podtržítka (double underscore), což zkracujeme v angličtině jako dunder. Systémovou proměnnou ```__name__``` tedy čteme jako dunder-name-dunder.

**Cvičení 1: Součet čísel**
Napište strukturovaný (procedurální) kód, který:
1. Načte dvě čísla z klávesnice
2. Vstupy z klávesnice se přetypují do zvoleného datového typu (int, float, aj.)
3. Čísla se sečtou
4. Výsledek součtu se vytiskne

Body 1 až 4 realizujte zvlášť jako podprogramy.

```
from typing import Callable

def pretypuj_vstupy(vstupy: tuple, datovy_typ: Callable) -> tuple:
    return tuple(map(datovy_typ, vstupy))


def nacti_data_z_klavesnice(datovy_typ: Callable) -> tuple:
    prvni_vstup = input("Zadej prvni vstup: ")
    druhy_vstup = input("Zadej druhy vstup: ")
    return pretypuj_vstupy( (prvni_vstup, druhy_vstup) , datovy_typ)


def secti_cisla(prvni_cislo: float = 0, druhe_cislo: float = 0) -> float:
    vysledek = prvni_cislo + druhe_cislo
    return vysledek


def vytiskni_vysledek(vysledek: str = "") -> None:
    if not vysledek:
        print("Nebylo zadano, co chces vytisknout!")
    else:
        print(f"Vysledek operace je {vysledek}")


def main():
    cislo_a, cislo_b = nacti_data_z_klavesnice(float)           
    soucet = secti_cisla(prvni_cislo = cislo_a, druhe_cislo = cislo_b)
    vytiskni_vysledek(str(soucet))


if __name__ == "__main__":
    main()
```

**Cvičení 2: Výpočet objemu**

Napište kód, který se skládá z následujících podprogramů:

1. Funkce pro načtení 3 čísel z klávesnice. Čísla musí být validní čísla, jinak se nevrátí z funkce.
2. Funkce pro výpočet objemu kvádru.
3. Výpis v hezké podobě objemu na obrazovku.

Podprogramy podle libosti můžete rozsekat i na dílčí podprogramy.

```
def validni_cislo(vstup: str) -> bool:
    return vstup.isdecimal()


def nacti_vstupy(pocet_vstupu: int) -> list:
    validni_vstupy = []
    for icislo in range(pocet_vstupu):
        vstup = ""
        while not validni_cislo(vstup):
            vstup = input(f"Zadej {icislo+1}. cislo: ")
        validni_vstupy.append(float(vstup))
    return validni_vstupy


def vypocti_objem(sirka: float, vyska: float, delka: float) -> float:
    return sirka * vyska * delka


def vypis_vysledek(sirka: float, vyska: float, delka: float, vysledek: float) -> None:
    print(f"Objem kvadru o rozmerech {sirka}x{vyska}x{delka} je {vysledek}")


def main():
    rozmery_kvadru = nacti_vstupy(pocet_vstupu = 3)
    objem_kvadru = vypocti_objem(*rozmery_kvadru)
    vypis_vysledek(*rozmery_kvadru, vysledek=objem_kvadru)


if __name__ == "__main__":
    main()
    
```

**Cvičení 3: Přihlašovací systém**

```

```

**Video týdne 1: idiom Main**

Většina programovacích jazyků má vstupní bod s názvem Main. Python takový bod nemá. Další problém je dán tím, že soubory v pythonu mohou být jak moduly, tak skripty. Pokud má kód s logikou v prvním bloku - globálním (plně neodsazeno), tak se kód spustí při importu. Proto použití idiomu Main je možné oddělit chování programu při importování a při používání ve formě programu. Více o tom v následujícím videu: [ZDE](https://www.youtube.com/watch?v=g_wlZ9IhbTs)

**Video týdne 2: zacyklené importování**

Ze cvičení jste se dozvěděli, že funkce lze rozdělit do více souborů a vytvářet tak moduly jazyka Python. Při importování můžete narazit na to, že program A vyžaduje balíček B, balíček B vyžaduje funkce balíčku C a balíček C vyžaduje program jako balíček A. Tím jste v cyklu podobnému slepice a vejce. V následujícím videu se dozvíte, jak se vypořádat s tímto problémem. [ZDE](https://www.youtube.com/watch?v=UnKa_t-M_kM)
