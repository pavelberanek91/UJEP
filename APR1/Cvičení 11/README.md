# Algoritmizace a programování

## Cvičení 11 - Práce s adresáři

### On-site cvičení

**OS11.1: Lorem**

Lorem ipsum ...

```
import os
os.mkdir("poznamky")
```

Lorem ipsum ...

```
os.chdir("poznamky")
os.chdir("..")
```

Lorem ipsum ...

```
with open("poznamky/apr1.txt", "w") as soubor:
    soubor.write("slintam jako pes")
```

Lorem ipsum ...

```
!rm -r C
```

Prepsat tak, aby byl multiplatformni. Tzn. ani jednou tam nebude os.system().

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

Napiste vlastni proceduru pro kopirovani souboru.

```
zkopiruj("original.txt", "kopie.txt")
```

lorem ipsum

```
!echo tohle se ma zkopirovat > mujtexticek.txt
```

```
shutil.copy()
shutil.copy2()
shutil.copytree("B", "C/B_kopie")
```

Lorem ipsum

```
os.rmdir("slozkaA") #nelze pokud neni slozka prazdna
```

Lorem ipsum

```
import shutil
shutil.rmtree("A")
```

* os.chdir() - presun se do slozky
* os.getcwd() - v jake slozce jste
* os.mkdir() - vytvor slozku
* os.mkdirs() - vytvor slozky
* os.listdir() - vypis slozky v aktualni slozce
* os.rmdir() - odstran slozku
* os.remove() - odstrani soubor
* shutil.rmtree() - odstran slozku s podslozkami
* shutil.copytree() - zkopiruj slozku s obsahem
* shutil.copyfile() - zkopiruje soubor bez metadata
* shutil.copy2() - zkopiruje soubor s metadaty

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