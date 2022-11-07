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

**Řešení**

```
using System;
using System.Collections.Generic;
using System.IO;

namespace ws
{
    class Program
    {
        static void Main(string[] args)
        {
            Analytik pepa = new Analytik(CSVDatabaze.ziskejDatabazi("db.csv"));
            Analytik franta = new Analytik(CSVDatabaze.ziskejDatabazi("db_alternativni.csv"));

            pepa.ZapisDoDB("Ahoj ja jsem Pepa\n");
            franta.ZapisDoDB("Ahoj ja jsem Franta\n");
            Console.WriteLine(pepa.PrectiDataZDB());
            Console.WriteLine(franta.PrectiDataZDB());
        }
    }

    class Analytik{

        public CSVDatabaze db {get; set;}
        public Analytik(CSVDatabaze db){
            this.db = db;
        }

        public void ZapisDoDB(string data){
            using (StreamWriter sw = File.AppendText(this.db.Cesta)){
                sw.Write(data);
            }
        }

        public string PrectiDataZDB(){
            string text = "";
            using (StreamReader sr = File.OpenText(this.db.Cesta)){
                text = sr.ReadToEnd();
            }
            return text;
        }
    }

    class CSVDatabaze{

        private static CSVDatabaze _db;
        public string Cesta {get; private set;}
        private CSVDatabaze(string cesta){
            this.Cesta = cesta;
        }

        public static CSVDatabaze ziskejDatabazi(string cesta){
            if(CSVDatabaze._db == null){
                CSVDatabaze._db = new CSVDatabaze(cesta);
            } 
            return CSVDatabaze._db;
        }
    }
}
```

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

**Řešení**

```
using System;
using System.Collections.Generic;
using System.IO;

namespace ws
{
    class Program
    {
        static void Main(string[] args)
        {
            Nepritel jozinZBazin = new Nepritel("Jozin", 50, 10, 5, 3, 3.5f, 2.3f);
            Nepritel klonJozina = jozinZBazin.VytvorKlon();
            jozinZBazin.PohniSe(5.0f, 5.0f);
            System.Console.WriteLine(jozinZBazin.Xpos);
            System.Console.WriteLine(klonJozina.Xpos);
        }
    }

    interface IKlonovatelne<T>{
        public T VytvorKlon();
    }

    class Nepritel: IKlonovatelne<Nepritel>{
        
        public string Typ {get; private set;}
        public int Hp {get; private set;}
        public int Mp {get; private set;}
        public int Attack {get; private set;}
        public int Defense {get; private set;}
        public float Xpos {get; private set;}
        public float Ypos {get; private set;}


        public Nepritel(string typ, int hp, int mp, int attack, int defense, float xpos, float ypos){
            this.Typ = typ;
            this.Hp = hp;
            this.Mp = mp;
            this.Attack = attack;
            this.Defense = defense;
            this.Xpos = xpos;
            this.Ypos = ypos;
        }

        public void PohniSe(float dx, float dy){
            this.Xpos += dx;
            this.Ypos += dy;
        }

        public Nepritel VytvorKlon(){
            return new Nepritel(this.Typ, this.Hp, this.Mp, this.Attack, this.Defense, this.Xpos, this.Ypos);
        }
    }
}
```

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

Pokud si se cvičením nevíte rady, zkuste následující vysvětlení: [ZDE](https://betterprogramming.pub/understanding-the-builder-design-pattern-f4f56fa18c9)
