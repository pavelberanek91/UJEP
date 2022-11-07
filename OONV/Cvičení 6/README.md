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
5. Vytvořte directora s postupy pro tvorbu pěšáků, lučistníků, kopiníků a mágů.
6. Zvolte rasu a nechte a directora vytvořit několik instancí každého typu jednotky.
7. Poté zvolte jinou rasu a vytvořte opět armádu.

Pokud si se cvičením nevíte rady, zkuste následující vysvětlení: [ZDE](https://betterprogramming.pub/understanding-the-builder-design-pattern-f4f56fa18c9)

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
            Kasarna kasarna = new Kasarna();
            
            ElfiVojakBuilder elfiBuilder = new ElfiVojakBuilder();
            NemrtvyVojakBuilder nemrtvyBuilder = new NemrtvyVojakBuilder();

            List<Vojak> elfiVojaci = new List<Vojak>(){};
            elfiVojaci.Add(kasarna.VytvorPesaka(elfiBuilder));
            elfiVojaci.Add(kasarna.VytvorKopinika(elfiBuilder));
            elfiVojaci.Add(kasarna.VytvorMaga(elfiBuilder));
            elfiVojaci.Add(kasarna.VytvorKopinika(elfiBuilder));

            List<Vojak> nemrtviVojaci = new List<Vojak>(){};
            nemrtviVojaci.Add(kasarna.VytvorPesaka(nemrtvyBuilder));
            nemrtviVojaci.Add(kasarna.VytvorPesaka(nemrtvyBuilder));
            nemrtviVojaci.Add(kasarna.VytvorLucistnika(nemrtvyBuilder));
            nemrtviVojaci.Add(kasarna.VytvorMaga(nemrtvyBuilder));
        }
    }

    class Vojak{

        public int Hp {get; set;}
        public int Mp {get; set;}
        public int Attack {get; set;}
        public int Defense {get; set;}
        public List<string> Inventar {get; set;}

        public Vojak(int hp, int mp, int attack, int defense){
            this.Hp = hp;
            this.Mp = mp;
            this.Attack = attack;
            this.Defense = defense;
            this.Inventar = new List<string>();
        }
    }

    interface IBuilder{
        void Reset();
        void PridejBrneni();
        void PridejMec();
        void PridejLuk();
        void PridejKopi();
        void PridejPrilbu();
        void PridejChranice();
        void PridejStit();
        void PridejMagickouKnihu();
        Vojak VytrenujVojaka();
    }
    
    class LidskyVojakBuilder: IBuilder{
        private Vojak _lidskyVojak;

        public LidskyVojakBuilder(){
            this.Reset();
        }

        public void Reset(){
            this._lidskyVojak = new Vojak(50, 10, 5, 5);
        }

        public Vojak VytrenujVojaka(){
            Vojak vytvoreny_vojak = this._lidskyVojak;
            this.Reset();
            return vytvoreny_vojak;
        }

        public void PridejMec(){
            this._lidskyVojak.Inventar.Add("lidsky mec");
            this._lidskyVojak.Attack += 5;
        }

        public void PridejKopi(){
            this._lidskyVojak.Inventar.Add("lidske kopi");
            this._lidskyVojak.Attack += 7;
        }

        public void PridejLuk(){
            this._lidskyVojak.Inventar.Add("lidsky luk");
            this._lidskyVojak.Attack += 5;
        }

        public void PridejStit(){
            this._lidskyVojak.Inventar.Add("lidsky stit");
            this._lidskyVojak.Defense += 5;
        }

        public void PridejBrneni(){
            this._lidskyVojak.Inventar.Add("lidske brneni");
            this._lidskyVojak.Defense += 5;
        }
        
        public void PridejPrilbu(){
            this._lidskyVojak.Inventar.Add("lidska prilba");
            this._lidskyVojak.Defense += 3;
        }

        public void PridejChranice(){
            this._lidskyVojak.Inventar.Add("lidske chranice");
            this._lidskyVojak.Defense += 2;
        }

        public void PridejMagickouKnihu(){
            this._lidskyVojak.Inventar.Add("lidska magicka kniha");
            this._lidskyVojak.Mp += 10;
        }
    }

    class OrciVojakBuilder: IBuilder{
        private Vojak _orciVojak;

        public OrciVojakBuilder(){
            this.Reset();
        }

        public void Reset(){
            this._orciVojak = new Vojak(50, 10, 5, 5);
        }

        public Vojak VytrenujVojaka(){
            Vojak vytvoreny_vojak = this._orciVojak;
            this.Reset();
            return vytvoreny_vojak;
        }

        public void PridejMec(){
            this._orciVojak.Inventar.Add("orci mec");
            this._orciVojak.Attack += 5;
        }

        public void PridejKopi(){
            this._orciVojak.Inventar.Add("orci kopi");
            this._orciVojak.Attack += 7;
        }

        public void PridejLuk(){
            this._orciVojak.Inventar.Add("orci luk");
            this._orciVojak.Attack += 5;
        }

        public void PridejStit(){
            this._orciVojak.Inventar.Add("orci stit");
            this._orciVojak.Defense += 5;
        }

        public void PridejBrneni(){
            this._orciVojak.Inventar.Add("orci brneni");
            this._orciVojak.Defense += 5;
        }
        
        public void PridejPrilbu(){
            this._orciVojak.Inventar.Add("orci prilba");
            this._orciVojak.Defense += 3;
        }

        public void PridejChranice(){
            this._orciVojak.Inventar.Add("orci chranice");
            this._orciVojak.Defense += 2;
        }

        public void PridejMagickouKnihu(){
            this._orciVojak.Inventar.Add("orci magicka kniha");
            this._orciVojak.Mp += 10;
        }
    }

    class ElfiVojakBuilder: IBuilder{
        private Vojak _elfiVojak;

        public ElfiVojakBuilder(){
            this.Reset();
        }

        public void Reset(){
            this._elfiVojak = new Vojak(50, 10, 5, 5);
        }

        public Vojak VytrenujVojaka(){
            Vojak vytvoreny_vojak = this._elfiVojak;
            this.Reset();
            return vytvoreny_vojak;
        }

        public void PridejMec(){
            this._elfiVojak.Inventar.Add("elfi mec");
            this._elfiVojak.Attack += 5;
        }

        public void PridejKopi(){
            this._elfiVojak.Inventar.Add("elfi kopi");
            this._elfiVojak.Attack += 7;
        }

        public void PridejLuk(){
            this._elfiVojak.Inventar.Add("elfi luk");
            this._elfiVojak.Attack += 5;
        }

        public void PridejStit(){
            this._elfiVojak.Inventar.Add("elfi stit");
            this._elfiVojak.Defense += 5;
        }

        public void PridejBrneni(){
            this._elfiVojak.Inventar.Add("elfi brneni");
            this._elfiVojak.Defense += 5;
        }
        
        public void PridejPrilbu(){
            this._elfiVojak.Inventar.Add("elfi prilba");
            this._elfiVojak.Defense += 3;
        }

        public void PridejChranice(){
            this._elfiVojak.Inventar.Add("elfi chranice");
            this._elfiVojak.Defense += 2;
        }

        public void PridejMagickouKnihu(){
            this._elfiVojak.Inventar.Add("elfi magicka kniha");
            this._elfiVojak.Mp += 10;
        }
    }

    class NemrtvyVojakBuilder: IBuilder{
        private Vojak _nemrtvyVojak;

        public NemrtvyVojakBuilder(){
            this.Reset();
        }

        public void Reset(){
            this._nemrtvyVojak = new Vojak(50, 10, 5, 5);
        }

        public Vojak VytrenujVojaka(){
            Vojak vytvoreny_vojak = this._nemrtvyVojak;
            this.Reset();
            return vytvoreny_vojak;
        }

        public void PridejMec(){
            this._nemrtvyVojak.Inventar.Add("nemrtvy mec");
            this._nemrtvyVojak.Attack += 5;
        }

        public void PridejKopi(){
            this._nemrtvyVojak.Inventar.Add("nemrtve kopi");
            this._nemrtvyVojak.Attack += 7;
        }

        public void PridejLuk(){
            this._nemrtvyVojak.Inventar.Add("nemrtvy luk");
            this._nemrtvyVojak.Attack += 5;
        }

        public void PridejStit(){
            this._nemrtvyVojak.Inventar.Add("nemrtvy stit");
            this._nemrtvyVojak.Defense += 5;
        }

        public void PridejBrneni(){
            this._nemrtvyVojak.Inventar.Add("nemrtve brneni");
            this._nemrtvyVojak.Defense += 5;
        }
        
        public void PridejPrilbu(){
            this._nemrtvyVojak.Inventar.Add("nemrtva prilba");
            this._nemrtvyVojak.Defense += 3;
        }

        public void PridejChranice(){
            this._nemrtvyVojak.Inventar.Add("nemrtve chranice");
            this._nemrtvyVojak.Defense += 2;
        }

        public void PridejMagickouKnihu(){
            this._nemrtvyVojak.Inventar.Add("nemrtva magicka kniha");
            this._nemrtvyVojak.Mp += 10;
        }
    }

    class Kasarna{
        public Vojak VytvorPesaka(IBuilder builderRasy){
            builderRasy.Reset();
            builderRasy.PridejMec();
            builderRasy.PridejStit();
            builderRasy.PridejBrneni();
            builderRasy.PridejPrilbu();
            return builderRasy.VytrenujVojaka();
        }

        public Vojak VytvorLucistnika(IBuilder builderRasy){
            builderRasy.Reset();
            builderRasy.PridejLuk();
            builderRasy.PridejPrilbu();
            return builderRasy.VytrenujVojaka();
        }

        public Vojak VytvorKopinika(IBuilder builderRasy){
            builderRasy.Reset();
            builderRasy.PridejKopi();
            builderRasy.PridejPrilbu();
            builderRasy.PridejChranice();
            return builderRasy.VytrenujVojaka();
        }

        public Vojak VytvorMaga(IBuilder builderRasy){
            builderRasy.Reset();
            builderRasy.PridejChranice();
            builderRasy.PridejMagickouKnihu();
            return builderRasy.VytrenujVojaka();
        }
    }
}
```
