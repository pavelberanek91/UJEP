# Algoritmizace a programování

## Cvičení 10 - Práce se soubory

### On-site cvičení

Práce s pythonem v příkazové řádce nám stačí pro náš trénink algoritmizace, nikoliv však pro skutečné projekty. V realitě budete nejčastěji programovat nějakou formu automatizace podnikových procesů, kde bude nutné pracovat se soubory (textové soubory, fotografie, aj.). Pojďme se v tomto cvičení podívat na to, jak číst data ze souborů.

První akce se souborem, na kterou se podíváme, bude čtení. Pro umožnění čtení ze souboru je nutné vytvořit tzv. stream, neboli proud dat. Proud dat si můžeme představit jako pomyslnou trubku, kterou zapíchneme do souboru, aby z něj při naší žádosti tekly data do našeho programu. Žádost o operace (čtení, zápis, aj.) se provádí přes tzv. ukazal na soubor (file handler). Je nutné upozornit, že soubor musí existovat, jinak program skončí výjimkou (chybovým hlášením) s názvem FileNotFoundError.

V následujícím programu se otevře soubor "znamky.txt", který se nachází v aktuálním pracovním adresáři (argument je jakákoliv absolutní nebo relativní cesta k souboru od aktuálního pracovního adresáře), a uvede se mód přístupu, v tomto případě je to čtení, což je vyjádřeno příznakem "r" jako read. Proměnná soubor představuje ukazatel na soubor, skrze který lze zadávat příkazy jako například read(). Metoda read() přečte všechny data ze souboru a uloží je do proměnné na levé straně příkazu. Proud je vždy nutné uzavírat, jinak dojde k vámi určitě známé situaci, kdy se snažíte např.: smazat soubor, ale operační systém píše, že ho jiný proces používá.

```
soubor = open("znamky.txt", "r")
data = soubor.read()
soubor.close()
```

Nesmíme tedy zapomínat uzavírat soubory, což se často stává i mně. Proto je lepší používat tzv. kontextový spráce, který se stará o ukončení za nás. Kontextový spráce se vytváří příkazem with. Následující program funguje úplně stejně jako předešlý.

```
with open("znamky.txt", "r") as soubor:
    data = soubor.read()
```

Kromě metody read() lze použít i metodu readlines(), která rovnou rozseká řádky na základě separátoru "\n" do seznamu řádků, avšak tento separátor ponechává u každého prvku vzniklého seznamu (což pro mě osobně je značně nepohodlné).

Pokud bychom chtělí do souboru zapisovat, tak musíme uvést příznak "w" jako write. Pozor tato operace je destruktivní a přemaže obsah souboru (zápis začíná od první pozice pro znak v souboru). Přijdete tedy o všechna data v souboru. Pokud soubor neexistuje, tak ho metoda vytvoří. Důležité je také zmínit, že zapisovaná data musí být typu řetězec. Metoda write zapisuje data od posledního znaku, takže je píše všechny na jeden řádek. Pokud byste chtěli zapsat zvlášť na řádky, pak je nutné dodávat do datového řetězce oddělovač "\n". Také lze použít metody writelines(), která přijme seznam řetězců a každý řetězec zapíše zvlášť na řádek (tedy doplní za vás oddělovač pro nový řádek).

```
data = "Dnes se mi nechce programovat."
with open("znamky.txt", "w") as soubor:
    soubor.write(data)
```

Pokud byste potřebovali jen připisat data do souboru (na pozici posledního znaku a dál), tak se používá příznak "a" jako append. Metody jsou stejné jako v případě příznaku "w".

```
data = "Dnes se mi už vůbec nechce programovat."
with open("znamky.txt", "a") as soubor:
    soubor.write(data)
```

Kromě těchto módu r, w, a existují ještě další řežimy. Základními řezimy jsou:

* r = čte ze souboru od začátku
* w = zapisuje do souboru od začátku, maže původní obsah
* a = připisuje do souboru od konce
* x = pouze vytváří soubor, pokud existuje, vyhodí výjimku

Vidíme, že důležité je, že módy se liší povolenými operacemi a pozicí, od které čtou nebo zapisují. Této pozici se říká hlava a lze jí i přesouvat na jiné pozice. Aktuální pozici hlavy zjistíme metodou tell() a přesunutí hlavy se vyvolá metodou seek().

```
data = "Bla ble bli blo blu bly"
soubor = open("znamky.txt", "w")
print(soubor.tell())
soubor.write(data)
print(soubor.tell())
soubor.seek(0)
print(soubor.tell())
soubor.close()
```

Kromě těchto módu můžeme přidat k módům znaménko +, kterým umožníme, že slouží jak pro čtení, tak i pro zápis:

* r+ = čtení i zápis, hlava je na pozici 0, nemaže původní soubor
* w+ = čtení i zápis, hlava je na pozici 0, maže původní soubor
* a+ = čtení i zápis, hlava je na konci souboru, nemaže původní soubor

Dále ještě můžeme číst tzv. binárně. Pokud se jedná o soubor typu zip nebo jiny netextový formát, můžeme číst alespoň jeho binární data a následně s nimi něco provádět (typicky je dekódujeme).

* rb = čtení binárních dat, hlava je na pozici 0, nemaže původní soubor
* wb = zápis binárních dat, hlava je na pozici 0, maže původní soubor
* ab = připisování binárních dat, hlava je na konci souboru, nemaže původní soubor

Tyto módy lze také spouštět s plusovým příznakem a lze tak použít jak zápisové metody, tak metody pro čtění:

* rb+ = čtení a zápis binárních dat, hlava je na pozici 0, nemaže původní soubor
* wb+ = čtení a zápis binárních dat, hlava je na pozici 0, maže původní soubor
* ab+ = čtení a zápis binárních dat, hlava je na konci souboru, nemaže původní soubor

Jedná se o pokročilou práci, která je závislá na typu dat a formátu, proto zde uvedu použe jeden příklad pro (snad) pochopení myšlenky. Více se dozvíte v nějakém kurzu multimédií. Představme si, že chceme číst data ze souboru, který je archivem typu zip.

```
with open("pisnicky.zip", "r") as zip_file:
    data = zip_file.read()
```

Tento naivní kód skončí výjimkou, protože soubor je ve formátu zip a nejedná se o textový soubor (tedy soubor s libovolnou příponou, obsahující textová data). Pokud bychom chtěli číst zazipovaný soubor, musíme ho číst binárním způsobem.

```
with open("pisnicky.zip", mode="rb") as zip_file:
    data = zip_file.read()
print(data[:20])
```

Pokud si vytiskneme prvních 20 znaků souboru, tak nám to nic neřekne, jelikož se jedná bytové řetězce. Pokud bychom chtěli převést tato data na informace pro člověka čitelné, tak bude nutné si napsat velice komplexní program, který zohledňuje bytovou strukturu formátu, nebo použít předpřipravenou knihovnu.

```
from zipfile import ZipFile

with ZipFile("pisnicky.zip") as zip_file:
    data = zip_file.read("pisnicky/eva_a_vasek.txt").decode("utf-8")
print(data[:20])
```

**OS10.1: Zápis nahodných známek do CSV souboru**

Zapište do souboru "znamky.txt" náhodné známky pro studenty ze seznamu studenti = ["Jirásek", "Kaštánek", "Kubíková", "Lípová"]. Formát zápisu bude jméno: známka a co řádek, to jeden student.

```
import random

studenti = ["Jirásek", "Kaštánek", "Kubíková", "Lípová"]

with open("znamky.txt", "w") as soubor:
    for student in studenti:
        soubor.write(f"{student}: {random.randint(1, 5)}\n")
```

**OS10.2: Čtení známek z CSV souboru**

Vytvořte si csv soubor "znamky.csv" v nějakém tabulkovém kalkulátoru nebo ručně v textovém editoru. Struktura csv souboru bude následující složena v tomto pořadí z řádků, obsahujících zmíněná data ve sloupcích:
1. Student,Matematika,Fyzika,Informatika
2. Novák,1,2,1
3. Jozífková,3,1,1
4. Knajpl,5,4,5

První řádek je nadpisový, zbylé tři jsou datové. Následně otevřete soubor pro čtení (budete muset pravděpodobně použít nějaké dekódování jako "utf-8-sig" pokud to vytváříte tabulkovým kalkulátorem) a načtěte si data ze souboru. Data načtěte do slovníku, kde klíčem je jméno studenta a hodnotou je seznam jeho známek.

```
with open("znamky.csv", "r", encoding="utf-8-sig") as soubor:
    text = soubor.read()
radky = text.split("\n")[:-1]

studenti = dict()
for iradek, radek in enumerate(radky):
    if iradek == 0:
        continue
    data = radek.split(";")
    jmeno = data[0]
    znamky = list(map(int, data[1:]))
    studenti[jmeno] = znamky
print(studenti)
```

**OS10.3: Žebříček nejlepších hráčů**

Naprogramujte nějakou jednoduchou hru typu šibenice nebo kámen nůžky papír. Vypočítejte na konci skóre, které hráč nahrál. Skóre uložíte do soubor top3_hraci.txt, kde se zaradi na prislusne misto mezi top3 hráče.

```
top3_hraci.txt:
    milan 3
    jana 5
    pepa 8
hráč pavel obdržel 7 bodů, pak nová verze souboru:
    jana 5
    pavel 7
    pepa 8
```

Pokud nemáte naprogramovanou nějakou hru z minulých cvičení nebo domácích úkolů, pak můžete použít ode mě naprogramovanou hru šibenice. Jedná se o velice jednoduchou verzi, která byla sestavena během 10 minut. Nezaručuji absenci chyb. Vymyslete si k ní lepší systém bodování, než je uveden a proveďte zápis do souboru nejlepších hráčů po dohrání hry hráčem.

```
jmeno = input("Jak se jmenujes? ")
tajenka = "ujep"
obrazovka = ["_" for pismeno in range(len(tajenka))]
nzivotu = 3
while "_" in obrazovka and nzivotu > 0:
    zadane_pismeno = input(f"Tajenka: {' '.join(obrazovka)}. Zbyva zivotu: {nzivotu}. Zadej pismeno: ").lower()[0]
    if zadane_pismeno in tajenka and zadane_pismeno not in obrazovka:
        for ipismeno, pismeno in enumerate(tajenka):
            if pismeno == zadane_pismeno:
                obrazovka[ipismeno] = zadane_pismeno
    else:
        print("Spatne pismeno!")
        nzivotu -= 1

if nzivotu > 0:
    skore = nzivotu * len(tajenka)
    print(f"Uhadl jsi tajenku. Skore: {skore}")
else:
    print("Umrel jsi!")
```

Nezapomeňte si také vytvořit počáteční verzi souboru s nějakými daty pro testování.

```
with open("top3.txt", "w") as soubor:
    soubor.write("milan 3\n")
    soubor.write("jana 5\n")
    soubor.write("pepa 8\n")
```

Kód pro zápis doporučuji rozdělit na tři fáze:
1. Získání aktulních hráčů a jejich skóre ze souboru do seznamu
2. 

```
top3_hraci = []
with open("top3.txt", "r") as soubor:
    radky = soubor.readlines()
    for radek in radky:
        data = radek.split()
        jmeno_hrace = data[0]
        skore_hrace = int(data[1])
        top3_hraci.append((jmeno_hrace, skore_hrace))
print(top3_hraci)
```

lorem ipsum

```
jmeno = "pavel"
print(top3_hraci)
top3_hraci.append((jmeno, skore))
print(top3_hraci)
top3_hraci.sort(key=lambda x:x[1])
print(top3_hraci)
top3_hraci = top3_hraci[1:]
print(top3_hraci)

with open("top3.txt", "w") as soubor:
    for hrac_skore in top3_hraci:
        hrac, skore = hrac_skore
        soubor.write(f"{hrac} {skore}\n")
```

### Domácí úkoly:

**HW10.1: Prvních deset řádků**

Napište kód, který otevře soubor test.txt a vypíše na obrazovku obsah prvních 10 řádků.

**HW10.2: Čísla zvlášť na řádek**

Napište kód, který otevře soubor test.txt a zapíše do něj čísla od 0 do 20, každé číslo zvlášť na nový řádek.

**HW10.3: Zapsat a připsat**

Napište kód, který do souboru test.txt napíše větu "Ahoj Jirko". Následně soubor zavře. Poté se znovu otevře a připíše se na jeho konec hláška "Cau Jirko" bez toho, aniž by byla předchozí věta smazána.

**HW10.4: Čtení CSV souboru**

Vytvořte pomocí nějakého tabulkového kalkulátoru tabulku a zapište do 3 sloupců alespoň 10 čísel (vždy číslo na jednom řádku), tedy v každé buňce bude jedno číslo. Vyexportujte soubor do csv formátu a přečtěte v pythonu. Pomocí pythonu spočítejte součet čísel v každém sloupci.

**HW10.5: Tvorba CSV souboru**

Nechte uživatele zadávat pomocí příkazu input čísla do kolekce. Čísla bude moct zadávat do té doby, dokavaď nenapíše STOP. Následně zjistěte počet zadaných čísel a rozdělte je rovnoměrně do tří seznamů. Tyto seznamy uložte do csv souboru, kde každý seznam představuje jeden sloupec. Zkuste si tento csv soubor otevřít ve vámi vybraném tabulkovém kalkulátoru.
