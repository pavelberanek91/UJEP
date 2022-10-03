# Algoritmizace a programování 1

**Obsah přednášky 1**:
* Základní terminologie objektově orientovaného programování, objekty (hodnoty) základních tříd (čísla, logické hodnoty) a operace resp. metody nad nimi

**Obsah cvičení 1**:
* Standardní vstup a výstup
* Objekty základních tříd (řetězce, čísla, logické hodnoty)
* Základní funkce v pythonu
* Základní metody nad objektama základních tříd

## On-site cvičení 1

**Úkol OS1.1: (De)motivační aplikace**

*Vypište na standardní výstup pomocí interpolačního řetězce pro uživatele přídavné jméno podle výběru*

```
# tohle je ulozeni hodnoty (literalu) do promenne
uzivatelske_jmeno = 'Pavle'
pridavne_jmeno = 'osklivy'

# tohle je tisk interpolacniho retezce na standardni vystup
print(f'{uzivatelske_jmeno} ty jsi ale {pridavne_jmeno} jinoch :)')
```

**Úkol OS1.2: Nastavení mysli**

*Vypište na obrazovku přídavné jméno podle zadaného nastavení mysli. Přídavné jméno bude nastavené v proměnné pomocí ternárního přiřazování.*

```
uzivatelske_jmeno = 'Pavle'
nastaveni_mysli = input('Jsi pozitivni nebo negativni?: ')
pridavne_jmeno = 'krasny' if nastaveni_mysli == 'pozitivni' else 'osklivy'
print(f'{uzivatelske_jmeno} ty jsi ale {pridavne_jmeno} jinoch :)')
```

**Úkol OS1.3: Barman**

*Vypište na obrazovku drink, který obdrží uživatel z automatu při zadání věku. Vstup bude nutné přetypovat na celé číslo.*

```
vek_uzivatele = int( input('Kolik ti je let?: ') )
vekova_restrikce = 18
napoj = 'branik' if vek_uzivatele >= vekova_restrikce else 'kofola'
print(f'Na tady mas: {napoj}')
```

**Úkol OS1.4: Detekce pravoúhlého trojúhelníku**

*Vypište na obrazovku pravdivostní hodnotu, zda je zadaný trojúhelník pravoúhlý. Délky stran trojúhelníka budou zadány naráz a odděleny mezerou v libovolném pořadí.*

```
strany = input("Zadej strany trojuhelnika oddelene mezerou: ").split()
strany = list(map(float, strany))
prepona = max(strany)
strany.remove(prepona)
odvesna1, odvesna2 = strany
je_pravouhly = True if prepona**2 == odvesna1**2 + odvesna2**2 else False
je_pravouhly
```

## Domácí cvičení 1

**Úkol HW1.1: Dotazník**

*Napište program, který se zeptá uživatele na jméno, příjmení a věk. Program na obrazovku vypíše větu se jménem uživatele a oznámí mu, kolik let mu bude příští rok. Př.: ```jmeno=Pavel, prijmeni=Beranek, vek=31```, pak na standardním výstupu bude řetězec ```"Jmenuješ se Pavel Beránek a za rok ti bude 32 let.```*

**Úkol HW1.2: Kalkulačka**

*Napište program, který se zeptá na dvě desetinná čísla ze standardního vstupu a na obrazovce se objeví jejich součet, rozdíl, součin a podíl. Tyto operace proveďte při výpisu v interpolačním řetězci (je možná zadat do složených závorek i např.: a+b).*

**Úkol HW1.3: Objem kvádru**

*Napište program, který se zeptá uživatele na 3 hodnoty oddělené čárkou ze standardního vstupu. Program tyto hodnoty separuje do proměnných, provede jejich přetypování a spočítá objem kvádru. Velikost objemu vypíše na obrazovku.*

**Úkol HW1.4: Výsledek relací**

*Relace je vztah mezi hodnotami. Tyto relace jsou <, <=, >, >=, !=, ==. Výsledky relací lze ukládat do proměnných. Zkuste si porovnat věk dvou osob a ulož výsledek do proměnných. Tento výsledek si vytiskněte na obrazovku*

Př.:
```
kontrolni_cislo = 5
zadane_cislo = int(input("Zadej cislo: "))

# Zkuste vsechny relace >, >=, <, <=, !=, ==
je_vetsi_rovno = cislo >= kontrolni_cislo

print(f"Je zadane cislo {zadane_cislo} vetsi nebo rovno jako kontrolni cislo {kontrolni_cislo}? {je_vetsi_rovno}")
```

**Úkol HW1.5: Logické spojky**

*Logické výrazy se vyhodnocují stejně jako relace na Boolovské hodnoty True nebo False. Tyto logické operace jsou v Pythonu AND (logický součin), OR (logický součet), NOT (logická negace). Logický součin se vyhodnotí jako pravda, pokud jsou oba výrazy pravdivé. Logický součet se vyhodnotí jako pravdivý,  pokud je alespoň jeden výraz pravdivý. Logický negace obrací logickou hodnotu výrazu. Z True udělá False a obráceně. Tyto logické výrazy můžete kombinovat s pořadím předností NOT, AND, OR. Také jejich kombinací můžete vytvářet jiné Boolovské funkce (různoznačnost XOR, totožnost XNOR, implikaci, inhibici, aj.). Výrazy můžete i různě závorkovat. Vyzkoušejte si do proměnných ```xlog1, xlog2, xlog3, xlog4``` uložit pravdivostní hodnoty True nebo False a provést vámi vybrané logické operace. Minimálně si vyzkoušet předepsané.*

Př.:
```
xlog1 = True
xlog2 = False
xlog3 = True
xlog4 = True

# logický součin dvou hodnot
log_soucin = xlog1 and xlog2
print(f"{xlog1} and {xlog2} = {log_soucin}")

# logický součin ctyr promennych
log_soucin = xlog1 and xlog2 and xlog3 and xlog4
print(f"{xlog1} and {xlog2} and {xlog3} and {xlog4} = {log_soucin}")

# negovaný logický součet NOR dvou proměnných
# ... doplnte

# různoznačnost XOR dvou proměnných
# ... doplnte

# implikace - budete si muset odvodit :)
# Nápověda pravdivostní tabulkou:
# xlog1  xlog2  vysledek
#   F      F       T
#   F      T       T
#   T      F       F
#   T      T       T
# ... doplnte
```

**Úkol HW1.6: DeMorganovy zákony**

*De Morganovy zákony jsou pravidla, která říkají*
1. Negace výsledku logického součtu proměnných = logickému součinu znegovaných proměnných
2. Negace výsledku logického součinu proměnných = logickému součtu znegovaných proměnných
*Prověřte pomocí kódu v jazyce Python, že opravdu platí a strany si jsou rovny.*

