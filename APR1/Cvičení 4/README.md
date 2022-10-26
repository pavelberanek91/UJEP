# Algoritmizace a programování

## Cvičení 4 - kolekce

### On-site cvičení

V tomto cvičení se seznámíme s kolekcemi a jejich rozhraním (způsob, jak je používat). Je nutné si uvědomit, že Python je dynamicky typovaný jazyk. Prpoto ve všech kolekcích se mohou nacházet objekty různých datových typů. To ve staticky typovaných jazycích jako je C# nebo Java nelze bez použití generik. Mezi základní kolekce řadíme:
1. seznam = [] = list()
2. ntici = () = tuple()
3. množinu = {} = set()

Seznam je nejpoužívanější kolekcí ze zmíněných. Jedná se o mutabilní kolekci, tedy prvky uvnitř seznamu lze nejen číst, ale i měnit (mutovat). Mezi metody (funkce/chování) seznamu patří:
1. append(obj) = přidá objekt do kolekce na jeho konec
2. insert(obj, idx) = přidá objekt do kolekce na zadaný index
3. extend(list) = přidá prvky z jiného seznamu mezi prvky seznamu, který metodu extend volá
4. pop(idx) = vyjme prvek z kolekce na zadaném indexu a vrátí vám ho do proměnné, bez indexu se vyjme poslední prvek
5. remove(obj) = odstraní objekt z kolekce, pokud se tam objekt nachází
6. clear() = vyprázdní seznam (není smazán, jen je prázdný)
7. copy() = zkopíruje prvky seznamu do jiného seznamu (mělká kopie, kopírují se i reference)
8. count(obj) = spočítá, kolikrát se zadaný prvek v kolekci nachází
9. sort() = seřadí seznam, lze vybrat klíč k řazení a i vzestupnost/sestupnost

Vidíme, že seznam obsahuje spousty užitečných funkcí, které byste si museli v jiných jazycích programovat sami a řešit problém realokace paměti a posouvání hodnot na nově vzniklá prázdná místa.

Další kolekcí je ntice, která je nemutabilní kolekce, tedy prvky uvnitř kolekce nelze měnit, lze je pouze číst. Tato kolekce má pouze dvě metody a to:
1. index(obj) = vrátí index, na kterém se objekt nachází
2. count(obj) = vrátí počet nálezů zadaného objektu v ntici

Tato kolekce je velice minimalistická ve svém chování. Její využití je spíše významové. Ntici používáme pro neměnné hodnoty, u kterých i pevně dané pořadí má určitý význam. Například souřadnice (x, y) nebo přihlašovací údaje (login, heslo). Nejčastěji se nachází jako prvky seznamu nebo jako klíče slovníku (příští lekce).

Poslední kolekcí je množina, která je mutabilní kolekce. Její využití souvisí s její vlastností, že objekty uvnitř množiny musí mít unikátní hodnotu. Pokud do množiny vložíme více objektů se stejnou hodnotou, zůstane tam pouze jeden z nich. Kromě využití pro mazání duplicit ze seznamu má spousty užitečných operací z množinové matematiky:
1. union(set) = sjednocení volající množiny (ta která metodu volá pomocí tečky) a argumentové množiny (ta, která je v závorce jako tzv. argumentú
2. intersection(set) = průnik volající množiny s argumentovou množinou
3. difference(set) = smaže prvky z volající množiny, které jsou v argumentové množině
5. symetric_difference(set) = sjednocení prvků množin, od kterého se odečte průnik množin
6. issubset(set) = zjistí, zda je volaná množina podmnožinou argumentové
7. issuperset(set) = zjistí, zda je volaná množina nadmnouzinou argumentové
8. isdisjoint(set) = zjistí, zda množiny neobsahují stejné položky

Využití množiny jako kolekce tedy souvisí s aplikacemi, kde je zapotřebí využívat množinovou matematiky. Jedná se o různé problémy plánování směn nebo zjišťování zákazníků, kterým je vhodné zaslat zprávu.

**OS4.1 - Počet samohlášek v ntici**

Vytvořte seznam ntic, který naplňte dvojicemi (jméno, počet samohlásek ve jméně). Jména jsou zadaná v předpřipraveném seznamu. Použijte k tomu metodu count.

```
jména = ["Pavel", "Milan", "Alena", "Rostislavomir"]
#doplnte kod
...

#vysledek = [("Pavel", 2), ("Milan", 2), ("Alena", 3), ("Rostislavomir", 5)]
```

**OS4.2 - Přihlašovací systém**

Napište kód, který požádá uživatele o login a heslo. Program následně zkontroluje, zda se zadaná dvojice (login, heslo) nachází v seznamu registrovaných uživatelů. Pokud ne, tak program zjistí, zda se nachází alespoň login v seznamu registrovaných. Pokud tam login nalezne, tak vypíše hlášku o nesprávném hesle. Pokud se tam nenachází ani login, tak program dovolít uživateli se registrovat - přidá se zadaný login a heslo mezi registrované uživatele.

```
registrovani = [('Pavel', '1234'), ('Zbysek', 'heslo')]
#dopište kód
...
```

**OS4.3 - Šibenice**

Naprogramujte konzolovou verzi hry šibenice. Hra má skryté slovo, které uživatel nevidí. Místo něj vidí na obrazovku na počátku pouze podtržítka. Hra ho požádá o zápis písmenka. Pokud dané písmenko už v minulosti hádal, tak ho hra požádá o hádání znova. Pokud ho nehádal, tak hra program zjistí, zda se někde zadané písmenko nachází v odkryté tajence. Pokud ne, tak se hráčovi ubere život. Pokud ano, tak bude místo podtržítka písmenko odkryto. Hra končí v případě uhádnutí celého slova nebo když hráčovi dojdou životy.

### Domácí cvičení

**HW4.1 - Nákupní košík**

Mějme následující seznam produktů s cenou:
```
produkty = [
  ("banán", 10),
  ("rohlík", 3),
  ("paštika", 30),
  ("hermelín", 50),
  ("chleba", 30),
  ("salám", 60),
  ("kečup", 70),
  ("eidam", 40),
  ("mandarinka", 8),
  ("okurka", 10),
]
```
Napište program, do kterého uživatel napíše název produktu a množství, které chce zakoupit daného produktu. Až uživatel napíše ZAPLATIT, tak program ukončí zadávání zboží do košíku a vypíše na obrazovku celkovou cenu za nákup.


**HW4.2 - Nejlepší a nejhorší hráč**

Mějme seznam hráčů a jejich nahrané skóre ve hře:
```
hraci = [("Pavel", 5), ("Honza", 3), ("Jana", 7), ("Milan", 4), ("Michaela", 9)]
```
Vypište na obrazovku jméno nejlepšího a nejhoršího hráče podle skóre.

**HW4.3 - Nejlepší hráči**

Mějme seznam hráčů a jejich nahrané skóre ve hře:
```
hraci = [("Pavel", 5), ("Honza", 3), ("Jana", 7), ("Milan", 4), ("Michaela", 9)]
```
Vypište na obrazovku hráče v pořadí od nejlepšího po nejhoršího a jen ty nejlepší 3 (top-3).

**HW4.4 - Skupiny**

Napište program, do kterého uživatel zadá seznam studentů ze standardního vstupu a počet skupin, na které chce studenty rozdělit. Program ze seznamu studentů následně vytvoří seznam ntic, kde ntice bude tak velká, jako je vypočítaná velikost skupiny podle požadovaného počtu skupin. Počet lidí ve skupině nemusí vycházet (některé skupiny mohou být podle zadaného počtu studentů menší). S takovou variantou také počítejte.

**HW4.5 - Šum**

Napište program, který vytvoří obrázek složený z náhodných hodnot v odstinech šedi (šum). Tento šum následně vizualizujte knihovnou PIL.

**HW4.6 - Studenti a zapsané kurzy**

Mějme následující seznamy studentů, které chodí na příslušný předmět:

```
studenti = ["Pavel Beránek", "Jana Novotná", "Jan Hřib", "Víteslav Nezval", "Petr Slavný", "Milan Balog", "Alena Jakubská"]
apr1 = ["Pavel Beránek", "Jana Novotná", "Petr Slavný", "Milan Balog", "Alena Jakubská"]
ikt = ["Pavel Beránek", "Petr Slavný", "Alena Jakubská"]
```
Použijte množinové operace a zjistěte následující:
1. Kolik studentů celkem studuje APR1 nebo IKT (dohromady)
2. Kolik studentů studuje APR1, ale nestuduje IKT
3. Kolik studentů studuje APR1 a zároveň studuje IKT
4. Kolik studentů nestuduje ani jeden z předmětů
5. Zjistěte pomocí množinové operace, zda APR1 obsahuje všechny studenty z IKT

**HW4.7 - Zadaná písmenka**

Napište program, který přijme ze standardního vstupu různá slova. Program přestane přijímat slova, jakmile uživatel napíše slovo STOP. Poté se na obrazovku vypíše seznam písmenek bez duplicit, která všechny slova obsahovala. K smazaní duplicit využijte množinu. Příklad:

```
zadano = ["pavel", "hromada", "traktor"]
vysledek = ["p", "a", "v", "e", "l", "h", "r", "o", "m", "d", "t", "k"]
```

**HW4.8 - Piškvorky**

Naprogramujte konzolovou verzi hry piškovkry s polem 3x3 (tic-tac-toe). Zde máte ode mne naprogramovaný začátek. Stačí dodělat AI a kontrolu vítězství na řádcích, sloupcích a diagonálách.

```
herni_pole = [['_', '_', '_'],['_', '_', '_'],['_', '_', '_']]
vitezstvi = False
seznam_hracu = ['x', 'o']
while not vitezstvi:
    for hrac in seznam_hracu:
        for radek in herni_pole:
            print(' '.join(radek))
        spravna_pozice = False
        while not spravna_pozice:
            pozice = int(input('Zadej umisteni symbolu 1-9?: '))
            radek, sloupec = pozice//3, pozice%3-1
            if herni_pole[radek][sloupec] == '_':
                herni_pole[radek][sloupec] = hrac
                spravna_pozice = True
            else:
                print(f'pozice {pozice} je jiz obsazena!')
            
```

**HW4.9 - Člověče nezlob se**

Naprogramujte konzolovou verzi hry Človeče nezlob se. Hraji ji proti sobě 4 protihráči, z nichž jeden je lidský hráč. Figurky musí projít od startovního domečku přes políčka až do cílového domečku. Hráč má na výběr se kterou figurkou ze svých 4 táhne. Pokud se náhodou na stejné pozici setkají dvě figury, pak je stojící figura vyhozena do čekacího domečku. Hráč vyhrává, jakmile má všechny figury ve svém cílovém domečku. Pro start ze startovního domečku je nutné hodit na hrací kostce číslo 6. Hraje se s 6 stěnnou kostkou. Hrací pole si můžete představit jako přímku (stačí políčka natáhnout a vidíte to).

**HW4.10 - Pexeso**

Naprogramujte konzolovou verzi hry Pexeso. Hraji ji proti sobě dva lidští hráči. Na začátku hry se náhodně rozmíchají dvojice písmen v herním poli. Hráči se pak střídají a vybírají mezi zakrytými políčky ty, které odkryjí. Pokud se jim povede odkrýt za sebou obě písmenka ze stejné dvojice, tak dvojice zůstavá odkrytá a hráč si přičítá bod. Hra končí, když jsou všechna písmenka odkrytá.

**HW4.11 - Nejkratší cesta**

Mějme následující seznam trojic, kterýho obsahuje jména města a vzdálenost mezi nimi:

```
start_mesto = "Chabařovice"
cilove_mesto = "Litoměřice"
vzdálenosti = [
  ("Chabařovice", "Ústí nad Labem", 8),
  ("Chabařovice", "Krupka", 1),
  ("Krupka", "Teplice", 1),
  ("Teplice", "Ústí nad Labem", 3),
  ("Teplice", "Litoměřice", 5),
  ("Ústí nad Labem", "Litoměřice", 10),
]
```

Vzdálenosti neodpovídají realitě. Napište algoritmus, který nalezne nejkratší cestu od startovního do cílového města.
