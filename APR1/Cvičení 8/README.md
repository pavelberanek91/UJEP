# Algoritmizace a programování

## Cvičení 8 - Funkcionální programování

### On-site cvičení

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

### Domácí úkoly:

**HW8.1: Lorem**

**HW8.2: Lorem**

**HW8.3: Lorem**

**HW8.4: Lorem**

**HW8.5: Lorem**

**HW8.6: Lorem**

**HW8.7: Lorem**

**HW8.8: Lorem**

**HW8.9: Lorem**

**HW8.10: Lorem**

**HW8.11: Lorem**

**HW8.12: Lorem**

**Video týdne 1: Chyby začátečníků**

V této lekci jste se naučili využívat i funkcionální příkazy, jako je filter, map, zip, comprehension, reduce, lambda a další užitečné příkazy. Pojďme se tedy podívat na některé chyby, které možná jste doposud dělali a jak je napravit. [ZDE](https://www.youtube.com/watch?v=qUeud6DvOWI)

**Video týdne 2: Cachování výsledků dekorátorem**

Dekorátory jsou funkce, které obalují jiné funkce. V Pythonu existuje spousty předpřipravených dekorátorů, u kterých ani nemusíte chápat vnitřní implementaci a stačí, když jen víte, k čemu a jak je použít. Na tomto videu uvidíte jeden velice užitečný dekorátor, který se hodí k cyklům, které využívají rekurzi. [ZDE](https://www.youtube.com/watch?v=DnKxKFXB4NQ)