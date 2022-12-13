# Algoritmizace a programování

## Cvičení 11 - Práce s adresáři

### On-site cvičení

V tomto cvičení se podíváme na to, jak volat příkazy shellu operačního systému, na kterém program spouštíme. Shell operačního systému je uživatelské rozhraní, skrze které může uživatel vyvolávat systémová volání operačního systému, který zadávají příkazy řadičům hardwaru počítače. To nám umožní například vytvářet adresáře, kopírovat soubory, vytvářet procesy programů a další zajímavé operace s operačním systémem.

Základním příkazem v knihovně os je příkaz system, který je schopen spustit libovolný shellový příkaz. Příkaz mkdir vytvoří uvedený adresář. 

```
import os
os.system("mkdir hudba")
```

Pro vytvoření prázdného souboru existuje příkaz touch. Pro přesun do adresáře slouží příkzaz cd. Tento program se přesune do adresáře hudba a vytvoří v něm soubor "eva_a_vasek.txt".

```
os.system("cd hudba")
os.system("touch eva_a_vasek.txt")
```

Když kód spustíte, tak zjistíte, že program vytvořil soubor ve vašem původním pracovním adresáři a nikoliv v adresáři hudba, kam jste se přesunuli. Důvodem je fakt, že os.system() vždy vytvoří novou instanci shellu, která začíná v adresáři projektu. Nepamatuje si tedy přesuny. Řešením je řetězení pomocí dvou ampersandů.

```
os.system("cd hudba && touch eva_a_vasek.txt")
```

Pokud bychom se chtěli v nějakém složitém řetězení i vynořit z adresáře do jeho nadřazeného, tak to provedeme příkazem:

```
os.system("cd ..")
```

Pokud bychom chtěli do souboru zapsat, tak nejjednodušší možností je použít přesměrování výstupu programu do souboru. Máme dvě možnosti a to přepiš (jedna šipka) a připiš (dvě šipky). Jelikož přepiš vytváří i soubor v případě jeho neexistence, tak touch je zbytečné v takovém případě používat.

```
os.system("echo bílá orchidej > eva_a_vasek.txt")
```

Základní příkazy Linuxu, které se vám budou hodit tedy jsou:
* cd = change directory, změní adresář na uvedený
* mkdir = make directory, vytvoří uvedený adresář
* touch = vytvoří prázdný soubor
* echo = vypíše zmíněný text na obrazovku
* > = přesměrování výstupu programu do souboru, který bude přepsán
* >> = přesměrování výstupu programu do souboru, kam bude text připsán 

**OS11.1: Tvorba adresářů v cyklu**

Na základě zmíněných příkazů linuxu vykonejte pomocí os.system() následující algoritmus:
1. Vytvořte adresáře A, B, C.
2. Do každého adresáře vytvořte 10 souborů s názvy 1.txt, 2.txt, ..., 10.txt.
3. Do každého ze souboru zapište text "01110000 01111001 01110100 01101000 01101111 01101110".

```
adresare = ["A", "B", "C"]
for adresar in adresare:
    os.system(f"mkdir {adresar}")
    for soubor in range(1, 11):
        os.system(f"echo 01110000 01111001 01110100 01101000 01101111 01101110 > {adresar}/{soubor}.txt")
```

Vytvořený kód není multiplatformní a závisí na shellu operačního systému. Ne všechny shelly mají stejné příkazy. Proto existují multiplatformní verze základních příkazů, které jsme volali přes os.system. Dalším problémem tohoto přístupu práce s operačním systémem je ten, že příkazy vrací celé číslo jako návratovou hodnotu. Ta říká, zda se program vykonal bez chyby (navrátí se hodnota 0) nebo s chybou (navrátí se nenulová hodnota). To je nepřijemné u příkazů, které v shellech vypisují informace na obrazovku, jako například ```ls```. Tento příkaz vypíše na obrazovku adresáře a soubory, které se nachází v aktuální složce. Představuje tak základní program pro procházení adresářové struktury na vašem počítači pomocí shellu.

V následujícím výčtu skriptů ukazuji os.system verze příkazů a ekvivalentní verzi multiplatformní verzi.

Vytvoření adresáře test.
```
os.system("mkdir test")
os.mkdir("test")
```

Přesun do adresáře test.
```
os.system("cd test")
os.chdir("test")
```

Výpis aktuálního pracovního adresáře.
```
os.system("pwd")
print(os.getcwd())
```

Výpis souborů a adresářů v aktuálním adresáři.
```
os.system("ls")
print(os.listdir())
```

Pokud byste potřebovali naráz vytvořit více adresářů, tak je možné použít mkdirs.
```
os.mkdirs("hudba/punk/punkhardcore")
```

Mazání souborů se provádí příkazem os.remove() a mazání adresářů příkazem os.rmdir(). Je tu však podmínka a to, že adresář musí být zcela prázdný.
```
os.remove("hudba/eva_a_vasek.txt")
os.rmdir("hudba")
```

**OS11.2: Multiplatformní tvorba adresářů**

Přepište předchozí kód z cvičení OS11.1, využívající příkazy konkrétního shellu tak, aby kód byl multiplatformní. Kód nebude ani jednou využívat příkaz system().

Pokud budete potřebovat smazat existující adresáře, můžete do buňky v jupyter notebooku vložit následující příkaz: ``````!rm -r A```. Vykřičník spouští shell a vykoná příkaz (je to tedy stejné, jako funkce system). Příkaz slouží pro rekurzivní mazání adresářů a smaže adresář A s celým jeho obsahem. Pokud vyměníte jméno za B, tak smaže i obsah adresáře B.

```
adresare = ["A", "B", "C"]
for adresar in adresare:
    os.mkdir(adresar)
    os.chdir(adresar)
    for soubor in range(1, 11):
        with open(f"{soubor}.txt", "w") as textacek:
            textacek.write("slintam jako pes")
    os.chdir("..")
```

**OS11.3: Vlastní kopírovací procedura**

Napište vlastní proceduru pro kopírování souboru, která bude multiplatformní. Procedura se bude volat následujícím způsobem: ```zkopiruj("original.txt", "kopie.txt")```

```
def zkopiruj(zdroj, kopie):
    with open(zdroj, "r") as soubor:
        obsah = soubor.read()
    with open(kopie, "w") as soubor:
        soubor.write(obsah)

zkopiruj("original.txt", "kopie.txt")
```

Modul shutil obsahuje příkazy pro kopírování souborů pro nás. Příkaz copy() provede kopírování obsahu souboru stejně jako ve cvičení, které jste zkoušeli. Copy2() kopíruje i metadata, což jsou informace o souboru (autor, datum poslední revize, informace o fotoaparátu, aj.). Pokud bychom chtěli kopírovat celý adresář s jeho obsahem, pak knihovna shutil obsahuje příkaz copytree, který provede rekurzivní kopírování adresáře s jeho obsahem a obsahu obsahu adresáře.

```
shutil.copy()
shutil.copy2()
shutil.copytree("B", "C/B_kopie")
```

Pokud bychom chtěli smazat adresář, tak v modulu os existuje příkaz rmdir, který to provede. Bohužel je zde problém v tom, že adresář musí být prázdný. Před smazáním adresáře je nutné smazat veškerý jeho obsah a obsah obsahu. Jedná se tedy o rekurzivní procházení stromu a mazání uzlů.

```
os.rmdir("slozkaA")
```

Knihovna shutil má pro nás rekurzivní mazání souborového stromu předpřipraveno ve funkci rmtree.

```
shutil.rmtree("A")
```

Zde je seznam všech funkcí z knihovny os a shutil, které se vám budou určitě hodit při běžné práci v jazyce Python.

* os.chdir() - přesun se do adresáře
* os.getcwd() - v jaké složce se aktuálně nacházíte
* os.mkdir() - vytvoř adresář
* os.mkdirs() - vytvoř adresáře
* os.listdir() - vypiš adresáře a soubory v aktualním adresáři
* os.rmdir() - odstraň adresář
* os.remove() - odstraň soubor
* shutil.rmtree() - odstraň adresář s jeho podadresáři a všema soubory
* shutil.copy() - zkopíruj soubor bez metadat
* shutil.copy2() - zkopíruj soubor s metadaty
* shutil.copytree() - zkopíruj adresář s jeho obsahem

### Domácí úkoly:

**HW11.1: Vytvoř prázdný soubor**

Napište kód, který vytvoří prázdný soubor s názvem test.txt.

**HW11.2: Překopíruj data**

Vytvořte adresář texty_pisnicek. Vložte do tohoto adresáře nějaké stažené lyrics s internetu ve formátu txt. Následně vytvořte soubor zaloha_textu_pisnicek pomocí příkazů pythonu a překopíruje obsah složky A do slozky B pomocí příkazů pythonu.

**HW11.3: Musí být smazány**

Napište kód, který smaže všechny složky, jejichž název je v seznamu pro_smazani.

**HW11.4: Budou vytvořeny**

Napište kód, který vytvoří všechny složky, jejichž název je v seznamu seznam_pro_vytvoreni. Kód napište tak, aby neskončil žádnou výjimkou.

**HW11.5: Připiš data**

Napište kód, který vyhledá ve složce všechny soubory s příponou ".txt" a připíše na jejich konec hlášku "baf :)".

**HW11.6: Prázdnota**

Napište kód, který zjistí, zda je aktuální pracovní adresář prázdný. Pokud není, tak vypíše na obrazovku hlášku "jsou tu data!".

**HW11.7: Zálohuj pracovní adresář**

Napište kód, který zkopíruje obsah aktuálního pracovního adresáře do adresáře záloha.

**HW11.8: Smaž vše na A**

Napište kód, který smaže všechny soubory z aktuálního adresáře začínající na pismeno "a".