# Algoritmizace a programování

## Cvičení 6 - Funkce

### On-site cvičení

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

Napište kód, který se skládá z následujících podprogramů.
1. Funkce pro načtení loginu a hesla z klávesnice. Pokud uživatel vynechá údaj, tak ho aplikace nepustí dál.
2. Funkce pro ověření, zda se dvojice login, heslo nachází mezi registrovanými uživateli
3. Procedura pro registraci neregistrovaného uživatele
4. Funkce pro detekci 3x za sebou nesprávného hesla
5. Procedura pro výpis informace o úspěšném přihlášení.

Opět můžete si kód rozdělit na více užitečných funkcí a procedur podle libosti. Zadání není nutné striktně dodržet, jde pouze o to cvičit informatické myšlení.

```
def nacti_udaje():
    login = over_prazdny_udaj(hlaska="Zadej login: ")
    heslo = over_prazdny_udaj(hlaska="Zadej heslo: ")
    return login, heslo


def over_prazdny_udaj(hlaska):
    vstup = input(hlaska)
    while not vstup:
        print("Nezadal jsi zadny vstup! Zkus to znovu")
        vstup = input(hlaska)
    return vstup
    

def uzivatel_se_spravne_prihlasil(uzivatele, login, heslo):
    return (login, heslo) in uzivatele


def uzivatel_je_registrovan(uzivatele, login, heslo):
    for registrovany_login, heslo in uzivatele:
        if login == registrovany_login:
            return True
    else:
        return False


def ziskej_spravne_heslo_k_loginu(uzivatele, hledany_login):
    for login, heslo in uzivatele:
        if login == hledany_login:
            return heslo


def ziskej_spravne_heslo(uzivatele, login, max_pocet_pokusu):
    spravne_heslo = ziskej_spravne_heslo_k_loginu(uzivatele, login)
    pokusy = max_pocet_pokusu
    print(f"Heslo není správné. Zbývá {pokusy} pokusů.")
    while pokusy > 0:
        zadane_heslo = over_prazdny_udaj(hlaska="Zadej heslo: ")
        if zadane_heslo != spravne_heslo:
            pokusy -= 1
            print(f"Heslo není správné. Zbývá {pokusy} pokusů.")
        else:
            return zadane_heslo
    else:
        return None


def zadost_o_registraci():
    return input("Chcete se registrovat?: ").lower()[0] in ["a", "y"]


def registruj_uzivatele(uzivatele, udaje_registranta):
    uzivatele.append(udaje_registranta)


def privitani_uzivatele(hlaska, login):
    print(hlaska + " " + login)


def odmitnuti_uzivatele(hlaska):
    print(hlaska)


def main():
    uzivatele = [("Pepa", "123"), ("Milan", "heslo"), ("Jana", "janicka")]
    login, heslo = nacti_udaje()

    if uzivatel_se_spravne_prihlasil(uzivatele, login, heslo):
        privitani_uzivatele(login=login, hlaska="Vitej v systému uživateli")
    elif uzivatel_je_registrovan(uzivatele, login, heslo):
        heslo = ziskej_spravne_heslo(uzivatele, login, 2)
        if not heslo:
            odmitnuti_uzivatele(hlaska="Došly vám pokusy. Je nám líto, ale nejste přihlášen. Přeji hezký zbytek dne.")
    else:
        if zadost_o_registraci():
            registruj_uzivatele(uzivatele, (login, heslo))


if __name__ == "__main__":
    main()
```

**Cvičení 4: Výpočet obsahu metodou Monte Carlo**

Napište program, který pomocí metody Monte Carlo spočítá obsah kružnice. Dekompozici programu nebudu již napovídat a nechám to na vašem uvážení. Program funguje následovně:
1. Kružnice o vybraném poloměru se nachází uvnitř jiné tělesa, například čtverce (ten použiju já)
2. Program náhodně střílí do čtverce a počítá, kolikrát se trefil do kružnice nebo mimo ní (do čtverce se trefíte vždy)
3. Tento děj opakujte po zvolený počet iterací v cyklu
4. Po dokončení procesu střílení se spočítá obsah obklopujícího tělesa a vynásobí se podílem počtu zásahů ku výstřelů. Výsledná hodnota je aproximace obsahu vnitřního tělesa.

```
import random

def generuj_nahodne_desetinne_cislo(cislo_min, cislo_max):
    return cislo_min + random.random()*(cislo_max - cislo_min)

def vygeneruj_nahodne_souradnice(cislo_min, cislo_max):
    random_x = generuj_nahodne_desetinne_cislo(cislo_min, cislo_max)
    random_y = generuj_nahodne_desetinne_cislo(cislo_min, cislo_max)
    return (random_x, random_y)

def trefeni_se(souradnice, souradnice_stredu, polomer):
    rozdil_x = souradnice[0] - souradnice_stredu[0]
    rozdil_y = souradnice[1] - souradnice_stredu[1]
    return rozdil_x**2 + rozdil_y**2 <= polomer**2

def spocitej_obsah_metodou_mc(polomer, pocet_vystrelu):
    pocet_zasahu = 0
    for ivystrel in range(pocet_vystrelu):
        souradnice = vygeneruj_nahodne_souradnice(cislo_min=-1, cislo_max=1)
        if trefeni_se(souradnice, (0, 0), polomer):
            pocet_zasahu += 1
    obsah_ctverce = (polomer*2)**2
    return pocet_zasahu/pocet_vystrelu * obsah_ctverce

def main():
    obsah_kruznice = spocitej_obsah_metodou_mc(polomer=1, pocet_vystrelu=10000000)
    print(f"Obsah zadane kruznice je: {obsah_kruznice}")

if __name__ == "__main__":
    main()
```

### Domácí úkoly:

**Úkol 1: Pretty printer matic**

Napište proceduru, která přijme 2D matici (seznam seznamů) a ve vhodné grafické textové podobě ji vypíše na obrazovku.

**Úkol 2: Vykreslovací procedura**

Napište proceduru, která přijme seznam hodnot na ose y (řady) a k tomu popisky osy x. Následně vykreslí do jednoho grafu v knihovně matplotlib data na obrazovku. Tím budete mít připravenou proceduru jako náhražku Excelu.

**Úkol 3: Která písmena jsou velká?**
Napište funkci, do které vložíte řetězec a vrátí se vám seznam velkých písmen.

**Úkol 4: Vyhledání pozice slova**

Napište funkci, která vrátí index prvku, který vyhledáváte. Nepoužívejte předpřipravenou funkci index nad seznamem.
```
př.: get_index([g,f,a,f,h], a) -> 2
```

**Úkol 5 - Řada lichých čísel**
Napište funkci, do které vložíte počáteční a konečný prvek z číselné řady a program vám vrátí všechna lichá čísla z této řady.

```
př.: get_licha(min=5,max=15) -> [5,7,9,11,13,15] 
```

**Úkol 6 - Registrace uživatele**

Napište proceduru, která vloží do seznamu tuple s loginem a heslem, pokud se login již nenacházi v seznamu uživatelů a heslo se liší od loginu.

```
př.: registruj((jana, 896), [(jana, 123)(petr, heslo)] -> neregistruje

př.: registruj((milan, milan), [(jana, 123)(petr, heslo)] -> neregistruje

př.: registruj((milan, 896), [(jana, 123)(petr, heslo)] -> registruje
```

**Úkol 7: Validace hesla**

Napište funkci, která požádá uživatele o heslo a vrátí ho, pouze pokud heslo obsahuje alespoň 1 velké písmeno, 4 malé písmeno a alespoň 1 číslo. Pokud heslo neobsahuje tyto znaky, pak žádá o zadání hesla ještě 2x, jinak vypíše chybu printem a vrátí None.


**Úkol 8: Nalezení písmen s háčky a čárkami**

Napište funkci, který nalezne všechna písmena ve větě, která obsahují háčky a čárky a vrátí seznam těchto písmen. Věta bude vstupem funkce.

```
př.: nalezni_hacky_carky("čau jak se máš") -> [č,á,š]
```

**Úkol 9 - Objem tělesa**

Napište funkci, která spočíta objem vloženého tělesa. Vstupem budou délky hran a typ tělesa. Výstupem bude objem. Typy těles jsou - krychle, kvádr, koule.

```
př.: get_objem([2,3,4], "kvádr") -> 24
př.: get_objem([2], "koule") -> 33.5
```

**Úkol 10: Všechna velká**

Napište funkci, do které vložíte řetězec a vrátí se vám řetězec, který bude obsahovat všechna písmena velká.

```
př.: get_velka("Ahoj") -> "AHOJ"
```

**Úkol 11: Čísla bezezbytku**

Napište funkce, do které vložíte počátek číselné řady, konec číselné řady a modulo a vrátí se vám počet čísel dělitelných v řadě modulem bezezbytku.

```
př.: delitelna_bez(a=5, b=20, mod=5) -> [5,10,15,20]
```

**Úkol 12: Počet výskytů**

Napište funkci, do které vložíte řetězec a znak a vrátí se vám počet výskytů tohoto znaku v řetězci.

```
př.: pocet_vyskytu("aha hmm", "h") -> 2
```

**Úkol 13: Každé druhé**

Napište funkci, do které vložíte řetězec a funkce vám vrátí každé druhé písmeno. Můžete použít list slicing.

```
př.: kazde_druhe("ahojpepo") -> [h,j,e,o] nebo "hjeo"
```

**Úkol 14: Smazání písmenka**

Napište funkci, do které vložíte řetězec a znak a funkce vám vrátí seznam písmen bez vloženého znaku. Můžete použít remove.

```
př.: smazani("ahoj", "o") -> [a,h,j]
```

**Úkol 15: Spojení seznamů**

Napište funkci, do které vložíte dva seznamy a funkce vám vrátí seznam složený ze dvou řetězců na přeskáčku.

```
př.: spoj([1,2,3],["a","b","c"]) -> [1,"a",2,"b",3,"c"]
```

**Úkol 16: Skalární součin**

Napište funkci, která přijme dva seznamy čísel o stejné velikosti a vrátí jejich skalární součin.

př.: sksoucin([1,2,3],[2,3,4]) -> 1x2 + 2x3 + 3x4 = 20


**Úkol 17: Náhodný seznam**

Napište funkci, která vrátí seznam náhodných desetinných čísel v rozmezí od a do b, kde a,b jsou parametry funkce.


**Úkol 18: Promíchání písmenek**

Napište funkci, do které vložíte seznam písmenek a funkce vrátí nový seznam, kde budou tato písmenka náhodně rozmíchaná.

**Úkol 19 - Brownovský pohyb**

Napište program strukturovaným paradigmatem, který bude představovat brownovský pohyb jedné částice v prostoru. Realizace ja zcela na vás.


**Úkol 20: Výpočet kořenů kvadratické rovnice**

Napište program pro výpočet kořenů kvadratické rovnice procedurálním paradigmatem.

**Úkol 21: Porovnání frekvence slov dvou textů**

Napište proceduru, která přijme text od uživatele a vrátí seznam slov s počtem výskytů slov v procentech. Tato procedura bude volána z jiné procedury, která přijme 2 texty a vypíše na obrazovku v hezké podobě informace o shodnosti těchto dvou textů (jaké informace to budou je na vás).

**Úkol 22: Zašifrování a dešifrování textu**

Napište funkci, do které vložíte text a substituční slovník. Funkce provede substituční šifru, kde nalezená písmena ve slovníku (klíče) přemění na příslušné hodnoty. Př.: text="ahoj", substituční slovník = {a = j, o = k} pak funkce vrátí "jhkj". Obdobně napište i dešifrovač textu.

**Úkol 23: SIR model procedurálně**

Přepište program, realizující simulaci SIR modelu šíření viru tak, aby byl napsán strukturovaným paradigmatem namísto imperativního paradigmatu.
[TEORIE](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology)

```
import matplotlib.pyplot as plt

#tady zacina program
def main():
    t = list(range(76))  #časové stopy (týdny)
    N = 7768662420       #světová populace
    I = 1                #počet nakažených
    R = 0                #počet vyléčených
    S = N - I            #počet nakazitelných
  
    nakazitelni = [S]
    nakazeni = [I]
    vyleceni = [R]

    rychlostSireni = 1.5     #nejaktuálnější basic reproduction rate: https://en.wikipedia.org/wiki/Basic_reproduction_number
    rychlostZotaveni = 0.5  #recovery rate kterej sem si přibližně spočítal (průměrnej denní přirůstek nakažených/průměrnej denní přirůstek vyléčených)

    for i in range(75):
        dS = - rychlostSireni * I * S / N
        dI = rychlostSireni * I * S / N - rychlostZotaveni * I
        dR = rychlostZotaveni * I
        S += dS
        I += dI
        R += dR

        nakazitelni.append(S)
        nakazeni.append(I)
        vyleceni.append(R)

    plt.title("SIR Model of Coronavirus")
    plt.ylabel("World Population")
    plt.xlabel("Time")
    plt.plot(t,nakazitelni,"b-",label = "Susceptible")
    plt.plot(t,nakazeni,"r-",label = "Infected")
    plt.plot(t,vyleceni,"m-",label = "Recovered")
    plt.legend()
    plt.show()


if __name__== "__main__":
    main()
```


**Úkol 24: Strukturovaný upravovač fotografií**

Přepište kód na úpravu fotografie pomocí filtrů do procedurálního paradigmatu. Pro případ zde přikládám impertivní kód:

```
from PIL import Image
obrazek = Image.open("prase.jpg")
sirka, vyska = obrazek.size
x = 0
while x < sirka:
    y = 0
    while y < vyska:
        r, g, b = obrazek.getpixel((x,y))
        prumer = int((r+g+b)/3)
        if prumer > 127:
            obrazek.putpixel((x,y), (r+30, g+30, b+30))
        else:
            obrazek.putpixel((x,y), (r-30, g-30, b-30))
        y += 1
    x += 1
display(obrazek)
```

**Úkol 25: Procedurálně napsaná hra**

Napište nějakou jednoduchou textovou hru pomocí procedurálního paradigmatu. Ideální kandidáti jsou uhádni číslo, šibenice, karetní hra prší, člověče nezlob se nebo piškvorky.

**Video týdne 1: idiom Main**

Většina programovacích jazyků má vstupní bod s názvem Main. Python takový bod nemá. Další problém je dán tím, že soubory v pythonu mohou být jak moduly, tak skripty. Pokud má kód s logikou v prvním bloku - globálním (plně neodsazeno), tak se kód spustí při importu. Proto použití idiomu Main je možné oddělit chování programu při importování a při používání ve formě programu. Více o tom v následujícím videu: [ZDE](https://www.youtube.com/watch?v=g_wlZ9IhbTs)

**Video týdne 2: zacyklené importování**

Ze cvičení jste se dozvěděli, že funkce lze rozdělit do více souborů a vytvářet tak moduly jazyka Python. Při importování můžete narazit na to, že program A vyžaduje balíček B, balíček B vyžaduje funkce balíčku C a balíček C vyžaduje program jako balíček A. Tím jste v cyklu podobnému slepice a vejce. V následujícím videu se dozvíte, jak se vypořádat s tímto problémem. [ZDE](https://www.youtube.com/watch?v=UnKa_t-M_kM)
