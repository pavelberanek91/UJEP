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

Toto implicitní chování souvisí s procházením kolekcí. Kolekce je vícero hodnot, na které odkazujeme jednou proměnnou. Zde vidíme kolekci řetězců, na které se odkazujeme proměnnou kamaradi. Pomocí hranaté závorky a čísla pořadí se můžete odkazovat na konkrétní prvek z kolekce. Číslo pořadí říkáme index a v pythonu má první položka index 0. Poslední položka by se vypočítala jako délka kolekce - 1 (jelikož číslujeme od 0). Rychlá zkratka pro vypsání poslední položky je zvolit index -1, jelikož příkaz pro výpočet délky kolekce se tam automaticky doplní za vás. Kromě doslovných hodnot (literálů) můžeme do hranatých závorek za index volit i proměnnou, jejíž obsah se tam nahraje. To umožňuje procházet postupně prvky v kolekci pomocí cyklu. Následující program postupně navyšuje index for cyklem od 0 do délky kolekce nevčetně a inkrementuje po 1. Tím projdeme všechny prvky kolekce. Tento způsob procházení je tzv. mutabilní, tudíž mohu prvek na který se aktuálně odkazuji v původní kolekci změnit na jinou hodnotu.

```
kamaradi = ['Pavel Beranek', 'Jiri Skvor', 'Jiri Fiser', 'Pavel Kuba']
for idx in range(len(kamaradi)):
    kamaradi[idx] = "Maxipes Fik"
print(kamaradi)
```

V jiných programovacích jazycích existuje ještě tzv. FOREACH cyklus. V pythonu je ve skutečnosti jen jeden typ FOR cyklus a to FOREACH. FOREACH cyklus funguje tak, že do řídící proměnné nahraje kopii hodnot z kolekce popořadě. Nelze u něj volit krok ani start. Stop je automaticky zvolen jako délka kolekce. Předchozí cyklus byl také FOREACH cyklus, jelikož příkaz range se při kompilace změní na kolekci hodnot od - do s krokem. Kopii těchto hodnot nahráváme do proměnné index. Při použití této FOREACH verze cyklu bez indexu si zablokujeme mutabilitu, jelikož místo přistupování indexem do původní kolekce používáme jen kopie hodnot z kolekce v řídící proměnné. Jedná se tedy o nemutabilní přístup ke kolekci.

```
kamaradi = ['Pavel Beranek', 'Jiri Skvor', 'Jiri Fiser', 'Pavel Kuba']
for kamarad in kamaradi:
    kamarad = "Maxipes Fik"
print(kamaradi)
```

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

**OS3.1 - SIM karta**

Realizujte algoritmus přihlašování do SIM karty. Program vás požadá o zadání správného PINu SIM karty. Na zadání máte 3 pokusy. Pokud se trefíte do správného PINu, pak vám aplikace vypíše informaci o úspěšném přihlášení do SIM karty. Pokud se netrefíte, pak vás požadá o korektní zadaní. Pokud se netrefíte 3x, tak aplikace vypíše informaci o zablokování SIM karty.

**OS3.2 - Kámen nůžky papír na dvě vítězná kola**

Upravte váš kód na kámen-nůžky-papír z předchozího cvičení na verzi hry, ve které vyhrává hráč nebo počítač až po dvou vítězných kolech.

**OS3.3 - Manipulace s pixely**

Vytvořte si váš vlastní filtr na úpravu vzhledu fotografie. Zkuste například vytvořit nějaký retro filtr.

### Domácí cvičení

**HW3.1 - Zadání čísla**

Napište program, který neskončí dokavaď nezadáá uživatel ze standardního vstupu číslo, které po přetypování nevyhodí chybu.

**HW3.2 - Průměr ze zadaných dat**

Napište program, který bude žádat uživatele o zadávání číselných dat z klávesnice do té doby, dokavaď nenapíše řetězec STOP. Poté vypíše na obrazovku aritmetický průměr z hodnot. Přidávání do kolekce se provádí příkazem append. Na začátku si budete muset vytvořit prázdnou kolekci.

```
kolekce = []
kolekce.append("Pavel")
print(kolekce)
```

**HW3.3 - Modul statistics**

Vemte předchozí program a naimportujte si do něj knihovnu statistics. Tato knihovna obsahuje různé užitečné statistické vzorce. Po nasbírání dat v předchozím cvičení vypište pomocí této knihovny statistické hodnoty jako střední hodnota, modus, medián, směrodatná odchylka, rozptyl, atd.

**HW3.4 - Losovač otázek k maturitě**

Napište program, který v kolekci obsahuje seznam maturitních otázek. Poté se spustí cyklus, který se opakuje do té doby, dokavaď v seznamu nějaká otázka zbývá. Kdykoliv uživatel zmáčkně klávesu ENTER, tak program jednu z otázek náhodně vylosuje a vypíše na obrazovku. Otázky budou voleny náhodně. Podívejte se do modulu random, jaké by funkce by se vám mohly hodit pro tento účel.

**HW3.5 - Sudá a lichá řada**

Napište program, který pomocí for cyklu proiteruje řídící proměnnou od hodnoty 0 do hodnoty 100. Pokud číslo v řídící proměnné bude liché, pak bude číslo uloženo do kolekce lichá_čisla. Pokud bude sudé, tak do kolekce sudá_čísla. Sudost nebo lichost můžete zjistit pomocí operace modulo (značí se procentem v jazyce python).

**HW3.6 - Fibonacciho posloupnost**

Napište program, který vypíše na obrazovku Fibonacciho posloupnost od hodnoty 0 do hodnoty zadané uživatelem (generace králíků).

**HW3.7 - Samohlásky**

Napište program, který projde slovo a spočítá v něm počet samohlášek.

**HW3.8 - Vyhledání extrémů**

Napište program, který projde kolekci čísel a nalezne mezi nimi největší a nejmenší číslo. Nepoužívejte funkce min a max!

**HW3.9 - Analýza sentimentu**

Napište program, který přijme zadanou větu a zjistí, zda má zadavatel spíše negativní nebo spíše pozitivní náladu. Definujte si k tomu kolekci pozitivních slov a kolekci negativních slov.

**HW3.10 - Hádání čísla**

Napište program, kde uživatel hádá náhodné číslo v rozmezí od 1 do nějaké maximální meze. Na začátku je maximální mez nastavena na hodnotu 2. S každým uhádnutým číslem se mez zvětšuje o jedna, takže pokud uživatel v prvním kole číslo uhádne, tak v příštím kole již hádá mezi 1 a 3. Pokud uživatel číslo neuhádně, tak hádáná hodnota musí zůstat stejná a uživatel jen dostane nápovědu, jestli musí hádat číslo nižší nebo vyšší. Uživatel má 3 životy, které pokud dojdou, tak hra končí. Po ukončení hry se na obrazovku vypíše nějakým vhodným způsobem vypočítané skóre.

**HW3.11 - Rovnice lovec-kořist**

Následující program představuje simulaci šíření viru v populaci. Parametry šíření jsou síla viru Beta a rychlost uzdravování Gama. Poměr těchto čísel se nazývá reprodukční číslo, o kterém jste asi slyšeli v souvislosti s Covidem.

```
import matplotlib.pyplot as plt

#SIR model wiki (compartmental models in epidemiology)

t = list(range(76))  #časové stopy (týdny)
N = 7768662420       #světová populace
I = 1                #počet nakažených
R = 0                #počet vyléčených
S = N - I            #počet nakazitelných
  
nakazitelni = [S]
nakazeni = [I]
vyleceni = [R]

rychlostSireni = 1.0     #nejaktuálnější basic reproduction rate: https://en.wikipedia.org/wiki/Basic_reproduction_number
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
plt.legend() #matplotlib pyplot legend
plt.show()
```

Upravte program SIR modelu šíření viru do Lotka-Volterrova modelu pro lovce a kořist. Diferenciální rovnice naleznete [ZDE](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations)

**HW3.12 - Piškvorky**

Naprogramujte hru piškvorky, kde proti sobě hrají dva hráči.

**Video týdne 1: Porovnání rychlosti cyklů**

V tomto cvičení jste se naučili provádět opakování příkazů pomocí cyklů. Otázkou tedy zůstává, jaký cyklus použít, pokud chci provést nějakou aritmeticko-logickou operaci nad kolekcí objektů (například sečti všechna čísla v kolekci). Odpovědí je: pokud můžete, nepoužívejte cyklus. Vysvětlení této odpovědi naleznete v tomto videu: [ZDE](https://www.youtube.com/watch?v=Qgevy75co8c)

**Video týdne 2: Příkaz Else na konci cyklu**

Python obsahuje možnost využít příkazu Else i na konci cyklu while a for. Jedná se o vlastnost jazyka, kterou sám tvůrce nemá v oblibě. Pojďte se podívat na detailní video o tom, jaký je mechanismus tohoto příkazu u cyklů. [ZDE](https://www.youtube.com/watch?v=6Im38sF-sjo)
