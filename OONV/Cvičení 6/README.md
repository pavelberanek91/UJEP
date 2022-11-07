# Objektově-orientované návrhové vzory

## Cvičení 6 - Tvořící vzory

### Singleton

Návrhový vzor singleton se používá v případech, kdy chcete zaručit, aby šlo vytvořit pouze jednu instanci dané třídy. Pokud někdo požádá o vytvoření nové instance této třídy, tak se mu vrátí již existující instance.

Více se dozvíte o návrhovém vzoru singleton [ZDE](https://refactoring.guru/design-patterns/singleton)

**Úkol**

1. Vytvořte třídu CSVDatabáze.
2. Třída bude obsahovat jeden atribut: cesta_k_csv_souboru.
3. Třída bude obsahovat vše potřebné pro to, aby byla technicky singletonem.
4. Vytvořte třídu Analytik, která umí zapsat a číst z CSV souboru (metody). 
5. V konstruktoru přiřaďte instancím třídy Analytik CSV soubor, do kterého bude zapisovat nebo z něj bude číst.
6. Vytvořte dvě instance Analytika a přiřaďte jim singleton CSV soubor.
7. Ověřte, že obě instance čtou a zapisují do stejného CSV souboru. Pokud byla cesta k CSV souboru změněna, bude změněna pro oba analytiky.

### Prototype

Návrhový vzor prototype se používá v případech, kdy potřebujete vytvořit kopii instance třídy. Problém spočívá v tom, že instance třídy mají některé atributy a metody privátní. Svět kolem je zná jen díky jejich veřejnému rozhraní (veřejné metody, metody z rozhraní interface, veřejné proměnné a gettery a settery). Mnoho atributů vám může být skryto při vytváření kopie instance. Řešením je vytvořit rozhraní s metodou clone, kterou si musí klonovatelné třídy implementovat. Jelikož klonování probíhá uvnitř třídy, pak jsou jim známé i privátní atributy.

Více se dozvíte o návrhovém vzoru prototype [ZDE](https://refactoring.guru/design-patterns/prototype)

**Úkol**

1. Vytvořte třídu Nepřítel.
2. Třída bude obsahovat následující privátní atributy: druh, HP, MP, Attack, Defense, poziceX, poziceY.
3. Třída bude obsahovat metodu PohniSe (pokud chcete další, tak můžete podle libosti)
4. Privátní atributy budou odkryty veřejnosti pomocí getterů a setterů
5. Vytvořte rozhraní ICLoneable s metodou clone. 
6. Třída Nepřítel bude toto rozhraní implementovat.
7. Napište implementaci metody clone.
8. Vytvořte instanci třídy Nepřítel s nějakými atributy pro parametry konstruktoru.
9. Vytvořte kopii této třídy.
10. Pohněte se s oběmi instancemi a zkontrolujte, že mají tytéž informace a rozdílné poziceX a Y.


### Builder

Návrhový vzor Builder řeší problém s třídami, které obsahují velké množství nastavení, které při vytváření specifikujete pomocí atributů parametrů v konstruktoru. Tento problém je snadno identifikovatelný konstruktorem s velkým počtem parametrů. Typickým řešením těchto situací je vytvořit velké množství potomků, které rodiče rozšiřují o daný parametr. Tím bohužel vytvoříte obří množství tříd, kterých může být tolik, kolik je možných kombinací parametrů. Tím bychom problém velkého rozhraní konstruktoru vyřešili za cenu velkého množství potomků. 

Řešením je využít návrhový vzor builder, který extrahuje kroky tvorby do třídy zvané builder. Třída, která má velký konstruktor je osekána na potřebné minimum. Builder poté vytvoří tento objekt a klient pouze zvolí, jaké metody se mají zavolat pro rozšíření vytvářeného objektu.

Vylepšním návrhového vzoru je využití tzv. Directors. Proces tvorby je delegován na direktory. Ty volají konkrétní buildery, kteří mají vlastní implementaci build metod.

Více se dozvíte o návrhovém vzoru singleton [ZDE](https://refactoring.guru/design-patterns/builder)

**Úkol**

1. Vytvořte třídu Voják s následujícími parametry v konstruktoru: brnění, meč, luk, kopí, přilba, chrániče, štít, magická kniha.
2. Všechny tyto atributy jsou typu boolean a určují, zda bude příslušná položka v inventáři Vojáka.
3. Vytvořte rozhraní IBuilder, do kterého abstrahujete tvořící kroky na metody.
4. Vytvořte 4 konkrétní buildery: builder lidského vojáka, builder orčího vojáka, builder elfího vojáka a builder nemrtvého vojáka.
5. Vytvořte directory s názvem PěšákDirectory, LučistníkDirector, MágDirector.
6. Implementuje kód pro tvorbu jednotek do diredcorů.
7. Zvolte rasu a nechte a directora vytvořit několik instancí každého typu jednotky
8. Poté zvolte jinou rasu a vytvořte opět armádu.
