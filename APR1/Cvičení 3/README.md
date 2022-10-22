# Algoritmizace a programování

## Cvičení 3 - Opakování pomocí cyklů

### On-site

V minulém cvičení jsme se naučili rozhodovat o tom, zda některé příkazy jazyka Python vykonáme nebo ne pomocí konstrukce IF. Také jsme se naučili volit mezi alternativními možnostmi mezi provedenými bloky kódu pomocí sekvence IF-ELIF-...-ELIF-ELSE. Která větev se vykoná závisí na tom, která z podmínek bude splněna (výlučně vůči ostatním). Podmínky mohou být velice komplikované pomocí propojení logickými operátory (and, or, not) s různorodými relacemi (<, <=, >, >=, ==, !=). Dále můžeme měnit precedenci vyhodnocování výrazů ve složené podmínce pomocí závorek.

V tomto cvičení se naučíme opakovat blok kódu do té doby, dokavaď je podmínka opakování splněna. Opakování budeme říkat odborně cyklus a v pythonu máme na výběr cyklus typu WHILE a FOR.

Následující program představuje typické využití WHILE cyklu. WHILE cyklus opakuje svůj blok kódu (odsazené příkazy) do té doby, dokavad je jeho podmínka vyhodnocena jako pravdivá (True). V podmínce se vyskytuje (až na vyjímku nekonečného cyklu) tzv. řídící proměnná. Na hodnotě této proměnné závisí ukončení cyklu. Zde je řídící proměnná jméno a program se bude opakovat do té doby, dokavaď v této proměnné bude prázdný řetězec. Konkrétně se opakuje příkaz, který požádá uživatele o zadání jména ze standardního vstupu a uloží ho do řídící proměnné. Jelikož řetězec o bílém znaku (například mezera) již není prázdný řetězec, tak dochází k odstranění bílých znaků z obou konců získaného řetězce pomocí příkazu strip().

```
jmeno = ""
while jmeno == "": 
    jmeno = input("Zadej sve jmeno: ").strip()
print("Dekuji za zadani")
```

While cyklus je možné i využít pro inkrementaci proměnné od nějaké hodnoty do nějaké hodnoty. Inkrementace představuje neustále přičítání nějaké diference (realizace aritmetické řady ze středoškolské matematiky). Toho lze využít například pro určitý počet opakování. Následující program nastaví řídící proměnnou na 0, spustí cyklus, který se ukončí při dosažení čísla 10 včetně, a tiskně průběžně hodnotu řídící proměnné na obrazovku. Na konci cyklu inkrementuje řídící proměnnou, což je důležité, jinak by se podmínka neustále vyhodnocovala jako pravdivá a cyklus by nikdy neskončil.

```
cislo = 0
konec = 10
while cislo <= konec:
    print(cislo)
    cislo += 1
```
Pro tento způsob opakování je však lepší použít FOR cyklus, který je kratší o dva řádky (nikoliv instrukce). FOR cyklus vytvoří za svým klíčovým slovem řídící proměnnou a nastaví jí hodnotu podle prvního čísla v příkazu range. Druhé číslo v range představuje maximální hodnotu, při jejímž dosažení se má cyklus ukončit (nevčetně této hodnoty). Poslední číslo v příkazu range představuje krok inkrementace. Tento program je tedy totožný s předchozím programem na WHILE cyklus.

```
for cislo in range(0, 11, 1):
    print(cislo)
```

Jelikož nejčastěji inkrementujeme s krokem = 1, tak v případě zapsání pouze dvou čísel do příkazu range má první číslo význam start hodnoty řídící proměnné, druhé číslo je stop hodnota řídící proměnné a inkrementační krok se implicitně nastaví na 1.

```
for cislo in range(0, 11):
    print(cislo)
```

Nejčastěji začínáme od čísla 0, tudíž pokud napíšeme do příkazu pouze jedno číslo, tak jeho význam je stop číslo řídící proměnné. Start číslo bude nastaveno implicitně na 0 a krok inkrementace bude implicitně nastaven na 1.

```
for cislo in range(11):
    print(cislo)
```

Toto implicitní chování souvisí s procházením kolekcí. Kolekce je vícero hodnot, na které odkazujeme jednou proměnnou. Zde vidíme kolekci řetězců, na které se odkazujeme proměnnou kamaradi. Pomocí hranaté závorky a čísla pořadí se můžete odkazovat na konkrétní prvek z kolekce. Číslo pořadí říkáme index a v pythonu má první položka index 0. Poslední položka by se vypočítala jako délka kolekce - 1 (jelikož číslujeme od 0). Rychlá zkratka pro vypsání poslední položky je zvolit index -1, jelikož příkaz pro výpočet délky kolekce se tam automaticky doplní za vás. Kromě doslovných hodnot (literálů) můžeme do hranatých závorek za index volit i proměnnou, jejíž obsah se tam nahraje. To umožňuje procházet postupně prvky v kolekci pomocí cyklu.

```
kamaradi = ['Pavel Beranek', 'Jiri Skvor', 'Jiri Fiser', 'Pavel Kuba']
for idx in range(len(kamaradi)):
    kamaradi[idx] = "Maxipes Fik"
print(kamaradi)
```

```
kamaradi = ['Pavel Beranek', 'Jiri Skvor', 'Jiri Fiser', 'Pavel Kuba']
for kamarad in kamaradi:
    kamarad = "Maxipes Fik"
print(kamaradi)
```

**OS3.1 - SIM karta**

lorem

**OS3.2 - Kámen nůžky papír na dvě vítězná kola**

lorem

**OS3.3 - Manipulace s pixely**

For cyklus je ideálním cyklem pro procházení grafických dat. Obrázek je vlastně seznam řádků a každý řádek je seznam hodnot barev. Pro procházení takové struktury je potřeba využít dvojného cyklu. Vnější cyklus se v následujícím případě bude opakovat tolikrát, kolik má obrázek řádků. V řádku projdeme každý pixel, tedy budeme vnitřní cyklus opakovat tolikrát, kolik má obrázek sloupců. Počet řádku a sloupců zjistíme z velikosti obrázku. Abychom však dostali do paměti obrázek v podově schopné procházení bude nutné využít nějakou knihovnu. Takovou knihovnou může být např.: PIL. Následující kód vezme nahraný obrázek s názvem prase.jpeg a provede binarizace jeho pixelů, tedy na základě průměrné hodnoty z intenzit pixelů přebarví pixely na černou nebo bílou. Rozhodnutí o barvě závisí na práhové hodnotě (threshold).

```
import PIL #Python Image Library, Pillow

obrazek = PIL.Image.open("prase.jpeg")
sirka, vyska = obrazek.size

for y in range(vyska):
    for x in range(sirka):
        r, g, b = obrazek.getpixel( (x, y) )
        prumer = (r + g + b)//3 #    R        G       B
        if prumer > 170:
            obrazek.putpixel( (x, y), (255, 255, 255) )
        else:
            obrazek.putpixel( (x, y), (0, 0, 0) )

display(obrazek) #obrazek.show()

```

### Domácí cvičení

#### Cvičení 3.1

**Video týdne 1: Porovnání rychlosti cyklů**

V tomto cvičení jste se naučili provádět opakování příkazů pomocí cyklů. Otázkou tedy zůstává, jaký cyklus použít, pokud chci provést nějakou aritmeticko-logickou operaci nad kolekcí objektů (například sečti všechna čísla v kolekci). Odpovědí je: pokud můžete, nepoužívejte cyklus. Vysvětlení této odpovědi naleznete v tomto videu: [ZDE](https://www.youtube.com/watch?v=Qgevy75co8c)

**Video týdne 2: Příkaz Else na konci cyklu**

Python obsahuje možnost využít příkazu Else i na konci cyklu while a for. Jedná se o vlastnost jazyka, kterou sám tvůrce nemá v oblibě. Pojďte se podívat na detailní video o tom, jaký je mechanismus tohoto příkazu u cyklů. [ZDE](https://www.youtube.com/watch?v=6Im38sF-sjo)
