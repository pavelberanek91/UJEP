# Algoritmizace a programování

## Cvičení 10 - Práce se soubory

### On-site cvičení

**OS10.1: Lorem**

Lorem ipsum ...

```
#r = read, w = write, a = append; rb, wb, ab; r+, w+, a+
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
studenti
```

lorem ipsum ...

```
import random

studenti = ["Beranek", "Fiser", "Sykorova", "Kubera"]

with open("znamky.txt", "a") as soubor:
    for student in studenti:
        soubor.write(f"{student}: {random.randint(1, 5)}\n")
```

Naprogramujte nějakou jednoduchou hru typu šibenice nebo kámen nůžky papír. Vypočítejte na konci skóre, které hráč nahrál. Skóre uložíte do soubor top3_hraci.txt, kde se zaradi na prislusne misto mezi top3 hráče.

```
top3_hraci.txt:
    pepa 8
    jana 6
    milan 3
hráč obdržel 7 bodů, pak nová verze souboru:
    pepa 8
    pavel 7
    jana 6
```

lorem ipsum

```
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

lorem ipsum

```
with open("top3.txt", "w") as soubor:
    soubor.write("pepa 8\n")
    soubor.write("jana 5\n")
    soubor.write("milan 3\n")
```

lorem ipsum

```
top3_hraci = []
with open("top3.txt", "r") as soubor:
    radky = soubor.readlines()
    for radek in radky:
        data = radek.split()
        jmeno_hrace = data[0]
        skore_hrace = int(data[1])
        top3_hraci.append((jmeno_hrace, skore_hrace))
top3_hraci
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
