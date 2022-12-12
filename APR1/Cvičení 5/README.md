# Algoritmizace a programování

## Cvičení 5 - Slovníky

### On-site cvičení

V minulém cvičení jste si vyzkoušeli kolekce, tedy datové struktury, do kterých lze ukládat větší množství informací. Při programování píšete programy, které ukládají data o objektech z naší každodennosti. Pokud bychom chtěli uložit informace o své kočce například pomocí seznamu, pak by vypadal kód následně:

```
kocka = [
    "Karel", 
    14, 
    ["Alfons", "Brunhilda"],
    (10, 10),
]

kocka2 = [
    14,
    "Karel", 
    ["Alfons", "Brunhilda"],
    (10, 10),
]
```

Bez dodatečného vysvětlení by asi nikdo z vašich programátorských kolegů nepochopil, že první položka v kolekci kocka představuje jméno, druhá věk, třetí seznam majitelů a čtvrtá GPS souřadnice, kde se vaše kočka nachází. U seznamů je klíčem k získání nějaké hodnoty celé číslo, které představuje pořadí hodnoty, tzv. index.

Daleko lepší řešení je využít datové struktury slovník, která mapuje množinu klíčů na množinu hodnot, kde klíčem může být libovolný nemutabilní typ (řetězec, seřazená ntice, celé číslo, desetinné číslo, aj.). Hodnotou může být jakýkoliv datový typ. Slovník je tedy kolekce skládající se z párů klíč:hodnota, tzv. key-values pairs.

```
kocka = {
    "jmeno": "Karel", 
    "vek": 14, 
    "majitele": ["Alfons", "Brunhilda"],
    "gps": (10, 10),
    1: "easter egg",
    2.3: "také easter egg",
    ("Chabarovice", "Chlumec"): 2,
    ("Pavel", "Alzbeta"): "rodiče",
    ("Míca", "Levhart", "Pomněnka"): "koťata",
}
```

Vyvolání hodnoty ze slovníku zadáním klíče se provádí následovně (klíč musí existovat):

```
kocka["vek"]
kocka[("Pavel", "Alzbeta")]
kocka[1]
```

Přidání nové dvojice do slovníku je v jazyce Python snadné:

```
kocka["bydliste"] = "Pasteurova UJEP"
```

Slovník má několik užitečných metod, které vám odkryjí, co je v něm uloženo:
* slovnik.values(): vrací seznam hodnot, které se ve slovníku nachází
* slovnik.keys(): vrací seznam klíčů, které se ve slovníku nachází a které můžeme využívat pro vyvolání hodnot
* slovnik.items(): vrací seznam párů klíč-hodnota, které jsou ve slovníku uložené

Na závěr je důležité upozornit, že ve slovníku nesmí být duplicitní klíče, avšak hodnoty mohou být duplicitní. Slovník by v případě duplicity netušil, jakou hodnotu vrátit. Python si s tím poradí tím, že vrátí hodnotu k poslednímu nálezu uvedeného klíče, ale této "featurce" se pojďme raději vyhnout.

**OS5.1 - Předkladový slovník**

Napište program, který obsahuje slovník, kde klíčem je české slovo a hodnotou je jeho anglický předklad. Následně využijte slovník pro překlad následující věty: "Pes na kole jel a stekal na postaka.".

```
slovnik_z_cj_do_aj = {"pes": "dog","na": "on","stekal": "barked","postaka": "postman",}
veta_cz = "Pes na kole jel a stekal na postaka."
veta_cz = veta_cz.lower().replace(".", "")
veta_en = ""
for slovo in veta_cz.split():
    if slovo in slovnik_z_cj_do_aj: #.keys()
        veta_en += slovnik_z_cj_do_aj[slovo] + " "
    else:
        veta_en += slovo + " "
veta_en
```

**OS5.2 - Hromadný předkladač**

Napište program, který přeloží větu do třech různých jazyků pomocí tří překladových slovníků. Neopakujte kód a zapřemýšlejte se nad tím, jak lze situaci vyřešit pomocí FOR cyklu.

```
slovnik_z_cj_do_aj = {"pes": "dog","na": "on","stekal": "barked","postaka": "postman",}
slovnik_z_cj_do_nj = {"pes": "Hund","na": "an","stekal": "geflossen","postaka": "genügend",}
slovnik_z_cj_do_fj = {"pes": "koira","na": "päällä","stekal": "hän haukkui","postaka": "tarpeeksi",}

slovniky = [slovnik_z_cj_do_aj, slovnik_z_cj_do_nj, slovnik_z_cj_do_fj, ]

veta_cz = input("zadej vetu: ")
veta_cz = veta_cz.lower().replace(".", "")

for slovnik in slovniky:
    prelozena_veta = ""
    for slovo in veta_cz.split():
        if slovo in slovnik: #.keys()
            prelozena_veta += slovnik[slovo] + " "
        else:
            prelozena_veta += slovo + " "
    print(prelozena_veta)
```

**OS5.3 - Čítač slov**

Napište program, který spočítá počet slov ve věte "Ahoj Jano. Jak se mas Jano. Mas se taky tak dobre jako ja Jano? Tak cau Jano!". Program tedy spočítá, kolikrát se ve věte nachází slovo ahoj, jano, jak, atd. Vytvořte následně pomocí modulu matplotlib histogram zastoupení slov, kde na ose X bude slovo a na ose Y jeho absolutní počet.

```
import matplotlib.pyplot as plt

veta = 'Ahoj Jano. Jak se mas Jano. Mas se taky tak dobre jako ja Jano? Tak cau Jano!'
nechtene_symboly = ["?", "!", ",", "."]
veta = veta.lower()
for symbol in nechtene_symboly:
    veta = veta.replace(symbol, "")

citac_slov = {}

for slovo in veta.split():
    if slovo in citac_slov:
        citac_slov[slovo] += 1
    else:
        citac_slov[slovo] = 1

plt.bar(x=citac_slov.keys(), height=citac_slov.values())
```

**OS5.4 - Čítač písmen**

Napište program, který spočítá počet písmen ve věte "Ahoj Jano. Jak se mas Jano. Mas se taky tak dobre jako ja Jano? Tak cau Jano!". Program tedy spočítá, kolikrát se ve věte nachází písmeno a, b, c, d, atd. Vytvořte následně pomocí modulu matplotlib histogram zastoupení písmen, kde na ose X bude písmeno a na ose Y jeho absolutní počet. V histogramu se musí nacházet všechna písmena abecedy bez háčků a čárek, tedy i ty, které se nenachází ve větě. Můžete využít modul string, ve kterém se nachází řetězec všech písmeno abecedy.

```
import matplotlib.pyplot as plt
import string

veta = 'Ahoj Jano. Jak se mas Jano. Mas se taky tak dobre jako ja Jano? Tak cau Jano'
nechtene_symboly = ["?", "!", ",", ".", " "]
veta = veta.lower()
for symbol in nechtene_symboly:
    veta = veta.replace(symbol, "")

citac_pismen = {} #to se muze hodit, priradim = 0
for pismeno in string.ascii_lowercase:
    citac_pismen[pismeno] = 0

for pismeno in veta:
    if pismeno in citac_pismen:
        citac_pismen[pismeno] += 1

plt.bar(x=citac_pismen.keys(), height=citac_pismen.values())
```

**OS5.5 - Modelování entit pomocí slovníků**

Napište program, který obsahuje seznam klientů a jejich akciové portfolio. Každý klient v seznamu klientů bude reprezentován slovníkem s následujícími atributy: jméno, emailový kontakt a držené akcie. O klientech víte následující informace:

1. Jiří Guláš má email gulas@gmail.cz a vlastní 50 akcií Applu, 100 akcií IBM a 70 akcií Microsoftu.
2. Richard Polívka má email polivka@gmail.cz a vlastní 30 akcií Tesly, 50 akcií IBM a 20 akcií Microsoftu.

Napište následně malý skript, který vypíše jména těch uživatelů ze seznamu klientů, které drží alespoň nějaké akcie firmy Apple.

```
klienti = [
    {
        'jmeno': 'Jiri Guláš',
        'kontakt': 'gulas@gmail.cz',
        'akcie': {
            'APL': 50,
            'IBM': 100,
            'MSC': 70,
        },
    },
    {
        'jmeno': 'Richard Polívka',
        'kontakt': 'polivka@gmail.cz',
        'akcie': {
            'TSL': 30,
            'IBM': 50,
            'MSC': 20,
        },    
    },
]

for klient in klienti:
    if "APL" in klient["akcie"]:
        print(klient['jmeno'])
```

### Domácí cvičení

**HW5.1 - Lorem**

lorem

**HW5.2 - Lorem**

lorem

**HW5.3 - Lorem**

lorem

**HW5.4 - Lorem**

lorem

**HW5.5 - Lorem**

lorem

**Video týdne 1: Code interview**

Až se budete ucházet o práci jako softwaroví vývojáři, tak váš pravděpodobně čeká tzv. code interview. Mnoho úkolů, které vám dávám za domácí úkol nebo probíráme při lekcích jsou ve skutečnosti úkoly, které já sám jsem buď osobně řešil na code interview nebo je sám zadávám zájemcům při prácí ve firmách nebo pro moje potřeby (občas jsem pozván na nějaké interview jako hodnotitel). To, co se cíleně sleduje, je schopnost algoritmizaci, rozpoznání vzorů, abstrahování a jasné vysvětlení myšlenky. Podívejte se na toto video s typickým příklad, který se objevuje v mnoha code interview. Jak uvidíte na konci, asymptotická složitost je dobré téma z počítačové vědy, které byste měli znát. [ZDE](https://www.youtube.com/watch?v=1t1_a1BZ04o)