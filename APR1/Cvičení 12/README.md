# Algoritmizace a programování

## Cvičení 12 - Výjimky

### On-site cvičení

Ne vždy dokážete pomocí podmínek napsat takový kód, který se vypořádá se všemi možnostmi které mohou nastat tak, aby kód nikdy nespadl. Takovým pádům se říká výjimky a jejich vykázání na obrazovku je vždy nepříjemná záležitost pro uživatele. Python obsahuje mechanismus obsloužení výjimek.

Základní strukturou je dvojice příkazů try-except. Následující kód se pokusí spustit podezřelý kód v bloku try, který může skončit výjimečným stavem:

```
try:
    delenec = int(input("Zadej delenec: "))
    delitel = int(input("Zadej delitel: "))
    print(f"Výsledek výpočtu {delenec}/{delitel} je {float(delenec)/delitel}")
except:
    print("Něco se pokazilo.")
```

Tento příklad mohl skončit do výjimečného stavu dvěma způsoby. Prvním je situace, při které je za dělitel zadána hodnota 0. Této výjimce se říká ZeroDivisionError. Další výjimečnou situací je zadání vstupu, který nelze přetypovat na celé číslo. Této chybě se říká ValueError, jelikož se snažíme dosadit do funkce argument s hodnotou, pro kterou nelze funkci použít. Pokud chceme mezi těmito situacemi rozlišovat a podle toho náležitě reagovat, můžeme explicitně výjimky odchytit. Except je nejobecnější výjimka a zachytí všechny konkrétnější nezachycené. Musí se vždy nacházet na konci mechanismu obsloužení výjimek.

```
try:
    delenec = int(input("Zadej delenec: "))
    delitel = int(input("Zadej delitel: "))
    print(f"Výsledek výpočtu {delenec}/{delitel} je {float(delenec)/delitel}")
except ZeroDivisionError:
    print("Pokusil jsi se dělit nulou!") 
except ValueError:
    print("Nezadal jsi čísla.")
except:
    print("Neznámá chyba.")
```

Všechny tyto příkazy zachytí chybový stav. Python obsahuje i možnost, jak zachytit stav, při kterém k žádné výjimce nedošlo. K tomu slouží klíčové slovo else.

```
try:
    delenec = int(input("Zadej delenec: "))
    delitel = int(input("Zadej delitel: "))
    print(f"Výsledek výpočtu {delenec}/{delitel} je {float(delenec)/delitel}")
except ZeroDivisionError:
    print("Pokusil jsi se dělit nulou!") 
except ValueError:
    print("Nezadal jsi čísla.")
except:
    print("Neznámá chyba.")
else:
    print("Program se vykonal bez chyb")
```

Existují situace, kdy potřebujeme spustit určitý příkaz vždy, ať už dojde k výjimce nebo ne (například uvolnit alokované výpočetní prostředky, uzavřít streamy do souborů, zapsat do logovacího souboru, aj.). K tomu slouží klíčové slovo finally.

```
try:
    delenec = int(input("Zadej delenec: "))
    delitel = int(input("Zadej delitel: "))
    print(f"Výsledek výpočtu {delenec}/{delitel} je {float(delenec)/delitel}")
except ZeroDivisionError:
    print("Pokusil jsi se dělit nulou!") 
except ValueError:
    print("Nezadal jsi čísla.")
except:
    print("Neznámá chyba.")
else:
    print("Program se vykonal bez chyb")
finally:
    print("Konec programu.")
```

Důležité je i pochopit to, že výjimky mají svou hierarchii. Existují nadřazené výjimky a k nim podražené výjimky. Tato hierarchie může mít několik úrovní. Na technické úrovni se jedná o mechanismus dědičnosti z objektově-orientovaného programování, které pochopíte příští semestr. V tomto kódu je například výjimka OSError v pořadí dříve, než výjimka FileNotFoundError. FileNotFoundError je potomek OSError, tedy OSError je obecnější výjimka. Pokud nastane FileNotFoundError, tak tato výjimka bude v následujícím kódu vždy zachycena výjimkou typu OSError. To si můžete snadno zkusit tím, že soubor bla.txt nebude existovat ve vašem pracovním adresáři.

```
try:
    with open("bla.txt", "r") as soubor:
        text = soubor.read()
except OSError:
    print("Chyba operačního systému")
except FileNotFoundError:
    print("Chyba souboru")
except:
    print("Neznámá chyba")
```

Následující kód je již správně. Konkrétnější chyba FileNotFoundError se nachází před obecnější chybou OSError. Pořadí výjimek tedy vždy píšeme od těch nejkonkrétnějších k těm nejobecnějším, zakončeno nejobecnější možnou výjimkou Except.

```
try:
    with open("bla.txt", "r") as soubor:
        text = soubor.read()
except FileNotFoundError:
    print("Chyba souboru")
except OSError:
    print("Chyba operačního systému")
except:
    print("Neznámá chyba")
```

V určitých situacích chcete vyvolat i výjimku sami v místech, kde by python výjimku nevyvolal. Jedná se o situace, kdy je lepší program shodit než aby běžel dál. K tomu slouží příkaz raise, za kterým následuje název výjimky, kterou chceme vyvolat.

```
raise ZeroDivisonError
```

Jeden speciální typ výjimky s názvem AssertionError má speciální význam. Při vývoji softwaru by každý programátor měl psát verifikační testy. Verifikace je aktivita, při kterém si programátor ověřuje, zda programuje správně, tedy bez bugů. V praxi programujete nějaký požadavek od klienta. Řekněme, že klient chce napsat funkci, které sečte dvě čísla a vrátí jejich výsledek. Aniž byste napsali kus kódu, tak víte, co má funkce dělat, neboli pro jaké vstupy má vrátit jaké výstupy. Lze tedy připravit i testy předem. Pokud vaše implementace funkce pro součet bude fungovat správně, pak i projdou tyto testy. Nejjednodušším testům se říká jednotkové testy a AssertionError (chyba ověření) je mechanismus, kterým můžeme testy vytvořit. V praxi se však používají testovací pracovní rámce jako UnitTest, Pytest, Hypothesis, Selenium, Roboto framework, které umožní komplexnější verifikaci softwaru.

```
def secti(a, b):
    return a + b

def main():
    assert secti(2, 3) == 5

if __name__ == "__main__":
    main()
```

Osobně doporučuji rozdělit si kód na hlavní kód (main) a spouštěč testů (testrunner). Hlavní kód se spustí pouze tehdy, když žádný z testů ve spouštěči testů neskončí výjimkou. Samotné testy můžeme napsat jako procedury, které spouští testují asserci.

```
def secti(a, b):
    return a + b

def test_secti_dve_cela_cisla():
    ...

def test_secti_dve_jina_cela_cisla():
    ...

def test_secti_dve_jina_desetinna_cisla():
    ...

def testrunner():
    test_secti_dve_cela_cisla()
    test_secti_dve_jina_cela_cisla()
    test_secti_dve_jina_desetinna_cisla()

def main():
    ...

if __name__ == "__main__":
    testrunner()
    main()
```

Oblíbeným pracovním rámcem pro psaní testů ja AAA pracovní rámec. AAA je zkratka za arrange (připrav), act (spusť/konej) a assert (ověř). Podle tohoto rámce každý test vypadá tak, že si nejprve připravíme potřebná data, spustíme funkce a ověříme návratovou hodnotu z funkce s tím, co od funkce očekáváme.

```
def secti(a, b):
    return a + b

def test_secti_dve_cela_cisla():
    #AAA framework (arrange, act, assert)
    #arrange
    a = 5
    b = 3
    #act
    vysledek = secti(a, b)
    #assert
    assert vysledek == 8

def test_secti_dve_jina_cela_cisla():
    #AAA framework (arrange, act, assert)
    #arrange
    a = 5
    b = 0
    #act
    vysledek = secti(a, b)
    #assert
    assert vysledek == 5

def test_secti_dve_jina_desetinna_cisla():
    #AAA framework (arrange, act, assert)
    #arrange
    a = 5.0
    b = 2.0
    #act
    vysledek = secti(a, b)
    #assert
    assert vysledek == 7.0

def testrunner():
    test_secti_dve_cela_cisla()
    test_secti_dve_jina_cela_cisla()
    test_secti_dve_jina_desetinna_cisla()

def main():
    ...

if __name__ == "__main__":
    testrunner()
    main()
```

Otázkou zůstavá, kolik takových testových případů (test cases) napsat. Asi nemá smysl napsat 10 testů pro různá celá čísla. Správný způsob přemýšlení je takový, že byste měli napsat takový počet testových případů, abyste otestovali různé domény ekvivalence. Doména ekvivalence je taková sada hodnot, pro kterou se test bude chovat stejně (tedy test 2 + 3 a 3 + 5). Stejná doména ekvivalence již není například 2 + "3" nebo 2.0 + 3 nebo dokonce i 2 + 1000000000 (tedy extrémní/krajní hodnota).

Užitečnou metodikou vývoje softwaru s využíváním testů je takzvaný vývoj řízený testy (TDD - test driven development). Metodika nám předepisuje následující postup:
1. Napíšeme předpis funkce, avšak tělo nevyplňujeme.
2. Napíšeme prvotní test, který musí po spuštění selhat (funkce není stále implementována).
3. Napišeme rychlou implementaci funkce tak, aby všechny testy prošly (může i napevno vracet toužený výsledek).
4. Napišeme další test.
5. Pokud aplikace pro další test selže, tak předěláme implementaci tak, aby neselhala.
6. Pokud se při psaní implementace opakujeme (například další elif), pak refaktorujeme kód (typicky abstrahujeme).
7. Postup opakujeme

Při dodržování této metodiky byste měli mít vždy kód, který pro dané testy funguje a můžete si být jistý jeho správností za daných podmínek daných testy. Sice budete trošku déle vyvíjet kód, ale čas by se vám měl vrátit na testování funkčnosti kód a ladění chyb.

**OS12.1: Test, který projde**

Napište alespoň jeden test k této funkci, který projde a skončí úspěchem při asserci.

```
def vrat_jmena(pocet):
    jmena = []
    for ijmeno in range(pocet):
        jmena.append(input("Zadej jmeno: "))
    return jmena
```

```
def vrat_jmena(pocet):
    jmena = []
    for ijmeno in range(pocet):
        jmena.append(input("Zadej jmeno: "))
    return jmena

def test_tri_jmen():
    pocet = 3
    jmena = vrat_jmena(pocet)
    assert len(jmena) == 3

def test_nuloveho_poctu():
    pocet = 0
    jmena = vrat_jmena(pocet)
    assert jmena == []

test_nuloveho_poctu()
test_tri_jmen()
```

**OS12.2: Test, který selže**

Napište alespoň jeden test k této funkci, který selže a skončí neúspěchem při asserci.

```
def vrat_jmena(pocet):
    jmena = []
    for ijmeno in range(pocet):
        jmena.append(input("Zadej jmeno: "))
    return jmena
```

```
def vrat_jmena(pocet):
    jmena = []
    for ijmeno in range(pocet):
        jmena.append(input("Zadej jmeno: "))
    return jmena

def test_retezcoveho_argumentu():
    pocet = "2"
    jmena = vrat_jmena(pocet)
    assert len(jmena) == 2

test_retezcoveho_argumentu()
```

**OS12.3: Závěrečné cvičení**

Následující cvičení je váš závěr z APR1 kurzu. Pokud zvládnete následující cvičení sami, pak jste se řádně naučili programovat a jste na dobré cestě stát se junior programátorem v jazyce Python. Budete psát kód, který načte známky z textového souboru v následujícím formátu:

```
Jana,1,3,5,4,2
Milan,1,5,6,0,2
Pavel,3,2,1,0,3
```

Program má za úkol přešíst soubor se známkama, spočítat průměrnou známku pro každého studenta a vytisknout je v hezké podobě na obrazovku. Kód by měl být ošetřen mechanismem výjimek, rozdělen do podprogramů a verifikován jednotkovými testy. Pro inspiraci uvádím své řešení:

```
def get_students_marks(filename):
    students_marks = {}
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print(f"Specified file with filename {filename} not found")
    else:
        for row in file:
            data = [cell.strip() for cell in row.split(",")]
            name = data[0]
            try:
                marks = list(map(int, data[1:]))
            except ValueError:
                print("Not all marks were integer numbers.")
            except Exception as err:
                print("Unknow error. Please contact IT support.")
                print(f"ERROR DETAIL: {err}")
            for mark in marks:
                if not 1 <= mark <= 5:
                    raise AssertionError("Not all marks in file are not between 1 to 5")
            students_marks[name] = marks
        file.close()
    finally:
        print("Reading done!")
    return students_marks

def get_average_marks(students_marks):
    average_marks = {}
    for student_name in students_marks:
        try:
            average_marks[student_name] = sum(students_marks[student_name])/len(students_marks[student_name])
        except ZeroDivisionError:
            average_marks[student_name] = "N"
        except:
            print(f"Unknow exception at student: {student_name}. Student will be ignored.")
    return average_marks

def print_marks(students_marks):
    for istudent, student in enumerate(students_marks):
        print(f"id: {istudent+1} name:{student} average mark:{students_marks[student]}")

def run_tests(testing=True):
    if testing:
        #AAA framework (arrange, act, assert)
        test_file = "test1.txt"
        nrows = len(get_students_marks(test_file))
        assert nrows == 3

        test_file = "test1.txt"
        return_type = type(get_students_marks(test_file))
        assert str(return_type) == "<class 'dict'>"

        test_file= "test1.txt"
        first_tuple = list(get_students_marks(test_file).items())[0]
        assert first_tuple == ("david",[1, 2, 1, 3, 4])

        test_file= "test1.txt"
        last_tuple = list(get_students_marks(test_file).items())[-1]
        assert last_tuple == ("martina",[1, 5, 2, 4, 3])

        test_file = "non_existing.txt"
        empty_marks = get_students_marks(test_file)
        assert empty_marks == {}

        test_file= "test2.txt"
        #last_tuple = get_students_marks(test_file)
        #assert empty_marks == {}

def main():
    run_tests()
    students_marks = get_students_marks("test1.txt")
    average_marks = get_average_marks(students_marks)
    print_marks(average_marks)
    
if __name__ == "__main__":
    main()
```

### Domácí úkoly:

**HW12.1: Ošetřené čtení souboru**

Napište vhodně ošetřený kód, který otevře soubor pro čtení.

**HW12.2: Ošetřené dělení**

Napište vhodně ošetřený kód, který načte 2 vstupy z klávesnice a podělí je.

**HW12.3: Úspěch při otevření souboru**

Napište kód, který v případě bezchybného otevření souboru vypíše na obrazovku řetězec "v pořádku".

**HW12.4: Zákaz většího jak 10**

Napište kód, který v případě vstupu většího jak 10 vyvolá výjimku na obrazovku s hláškou "číslo nesmí být větší jak 10!"

**Video týdne 1: Editory kódu**

Od dalšího semestru budemme vyvíjet v nějakém vhodném editoru kódu. Může to být obyčejný textový editor nebo i složité integrované vývojové prostředí (IDE). IDE se od obyčejného editoru liší tím, že má specializované funkce pro analýzu a úpravu programového kódu. Tyto IDE mohou být také zaměřeny striktně na jeden jazyk jako je například IDE Pycharm pro jazyk Python. Některé textové editory je možné pomocí pluginů přeměnit na skutečné IDE. Příkladem takového editoru je Visual Studio Code, které budu používat po celý druhý semestr. Výběr prostředí pro vývoj bude na vás. Zde naleznete video, které porovnává různé editory kódy a IDE. [ZDE](https://www.youtube.com/watch?v=8PhdfcX9tG0)

**Video týdne 2: VSCode finty**

Pokud budete vyvíjet ve VS Code jako já, tak v následujícím videu se naučíte pár fint, které vám mohou zvýšit vaší pracovní efektivitu (ergnonomii). [ZDE](https://www.youtube.com/watch?v=ifTF3ags0XI)