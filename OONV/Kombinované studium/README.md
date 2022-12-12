# Objektově-orientované návrhové vzory

## Kombinované studium

### 1. O předmětu

Kurz objektově-orientované návrhové vzory se zabývá řešením typických problémů architektury kódu, který využívá paradigmat s názvem objektově-orientované programování. Vědci v oblasti softwarového inženýrství sesbírali typické problémy a vymyslely jejich řešení, které zlepšuje kód z pohledu zejména udržitelnosti. Těmto technikám se říká návrhové vzory.

V tomto kurzu se budete seznamovat s jednotlivými návrhovými vzory v jazyce se statickým typováním. Vybraným jazykem je jazyk C#. Důvodů je několik:
1. přeje si to garant (Dr. Fišer)
2. návrhové vzory jsou často používané ve videohrách a C# se využívá v Unity enginu
3. C# je jednoduchý staticky typovaný jazyk a měli byste se s takovými jazyky seznámit (C++ bych vám nepřál)

### 2. Podmínky zápočtu

Zápočet bude udělen za to, že vhodně aplikujete libovolný návrhový vzor nebo vzory do vaší aplikace v jazyce C#. Některé návrhové vzory jsou realativně primitivní (například fasáda). Pokud využijete nějaký jednodušší návrhový vzor, tak doporučuji vytvořit komplexnější aplikaci nebo využít k ní alespoň jeden další návrhový vzor. Pro případ nedostatku kreativity jsou v kapitole 6 uvedeny náměty na seminární práci.

Na zápočet se přihlašujete ve vypsaném termínu. Termíny budou vyhlášeny pro vás kombinované studenty zvlášť o víkendu, kde se můžete přihlásit jen vy. Nic vám nebrání se zapsat i na termín s prezenčními studenty. Pokud vám okolnosti nedovolí se dostavit, tak je možné domluvit se online zápočtu, kde si popovídáme na webkameře o vaší práci.

Práce musí být vaší originální prací. Plagiátorství se trestá okamžitým uzavřením zápočtu jako nezapočteno.

### 3. Harmonogram předmětu

Cvičení z předmětu je rozděleno do dvou schůzek:
1. Úvod do jazyka C# (4.12. od 11:00 do 12:50)
2. Vybrané návrhové vzory (18.12. od 14:00 do 17:50)

Ke každému cvičení je zde uvedena sada domácích úkolů. které doporučuji si zkusit. V případě nutností konzultace napište email a můžeme úkoly prodiskutovat.

### 4. On-site cvičení 1 - Úvod do jazyka C#

**Úkol OS1.1 Založení .NET projektu:**

Nejjednodušší způsob jak začít vyvíjet v jazyce C# je stáhnout si prostředí Visual Studio, které představuje IDE (integrované vývojové prostředí) pro .NET aplikace. Jelikož Visual Studio je značně náročné na systémové prostředky, tak budu používat na cvičeních Visual Studio Code.

Pro založení .NET projektu budete potřebovat stáhnutý samotný .NET. Jedná se o ekosystém modulů (middleware), které umožní vytvářet, kompilovat a spouštět aplikace pro Windows a další operační systémy od firmy Microsoft. Buď si stáhněte a nainstalujte .NET ručně z oficiálních stránek nebo pomocí balíčkového instalátoru ho v terminálu nainstalujte. Na MacOS se jedná například o balíčkovací systém brew.

```
#instalace dotnet na macos
brew install dotnet
```

Poté si otevřete váš oblíbený editor kódu (např.: Visual Studio Code), založte adresář s projektem a otevřete ho. Poté si otevřete terminál a napište následující příkaz, kterým založíte consolový projekt s .NET dané verze (zde verze 6.0). 

```
#zalozeni projektu v aktualnim pracovnim adresari
dotnet new console --framework net6.0
```

Pokud vám terminál zahlásí chybu v argument ```--framework```, pak spusťte jen příkaz ```dotnet new console```. 

Měl by se vám vytvořit adresář obj, bin, soubor *.csproj a Program.cs. Program.cs je implicitní vstupní kód naší aplikace, jelikož obsahuje statickou metodu Main(). Zkuste spustit hello world kód v tomto souboru terminálem.

```
#spusteni projektu 
dotnet run
```

**Úkol OS1.2 Vytvoření třídy:**

Vytvořte třídu Vlak, která obsahuje základní proměnné (fields) vhodné pro vlak a konstruktor. Vytvořte ve třídě Main instanci této třídy.

```
class Vlak
    {
        //fields
        private int _pocetVagonu;
        public string StrojVedouci {get; private set; }
        private int _vykon;
        private List<Pruvodci> _seznamPruvodcich;

        //konstruktor
        public Vlak(int pocetVagonu, int vykon){
             this._pocetVagonu = pocetVagonu;
             this._vykon = vykon;
             this.StrojVedouci = null;
             this._seznamPruvodcich = new List<Pruvodci>();
        }
    }

class Program
    {
        static void Main(string[] args)
        {
            Vlak pepa = new Vlak(5, 28000);
        }
    }
```

**Úkol OS1.3 Vlastnosti:**

Pro třídu Vlak vytvořte přístupové metody (accesory a mutatory) pomocí tří různých způsobů:
1. Pomocí metoda GetProperty a SetProperty
2. Pomocí vlastnosti Get a Set
3. Pomocí specifikace přístupnosti get a set při deklaraci fieldu

```
        //fields
        private int _pocetVagonu;
        public string StrojVedouci {get; private set; }
        private int _vykon;

        //getter/accessor
        public int GetPocetVagonu(){
            return this._pocetVagonu;
        }

        //setter/mutator
        public void SetPocetVagonu(int novyPocet){
            this._pocetVagonu = novyPocet;
        }

        //vlastnosti
        public int Vykon{
            get {return this._vykon;}
            set {this._vykon = value;}
        }
```

**Úkol OS1.4 Metody:**

Přidejte vlaku metodu pro troubení. Tato metoda bude procedurou (nic nevrací) a bude na standardní výstup vypisovat řetězec, představující intenzitu houkání. Jaký řetězec se vypíše závisí na zvolené intenzitě, která je parametrem metody.

```
//metody
        public void Zatrub(int silaTroubeni = 1){
            if (silaTroubeni <= 0){
                System.Console.WriteLine("hu ...");
            } else if (silaTroubeni == 1){
                System.Console.WriteLine("HUhUHUhU!!!!");
            } else {
                System.Console.WriteLine("HU! HU! HU!");
            }
        }
```

**Úkol OS1.5 Agregace objektů:**

Chování objektů lze rozšiřovat (přidávat funkcionality) pomocí dvou technik:
1. Dědičnost
2. Vkládáním objektů do jiných 

V tomto cvičení se zaměříme na rozšiřování chování pomocí vkládání. Existují dva typy vkládání a to kompozice a agregace. Při kompozici vložený objekt nemůže existovat bez objektu vnějšího. Například stránka knížky by měla být vždy součástí knížky a její existence sama o sobě je k ničemu (=kompozice). U agregace existují objekty i mimo vnější objekt. Například motor auta určitě má smysl někde zavádět v databázi nebo přenášet mezi sklady i bez toho, aniž by musel být aktuálně v nějakém automobilu. 

Do našeho vlaku budeme agregovat průvodčí. Vytvořte třídu průvodčí a dejte mu nějaké vhodné vlastnosti. Dejte mu také metodu pro kontrolu lístku. Implementaci metody nechám na vaší kreativitě. Do třídy Vlak vytvořte seznam průvodčích a přidejte vlaku metodu pro přidávání průvodčích do svého seznamu. Následně dejte vlaku metodu SpustKontrolu(), která zavolá všechny průvodčí ze svého seznamu a ti začnou kontrolovat lístky. Tím jsme rozšířili chování třídy Vlak.

```
class Pruvodci{

        public string Jmeno {get; private set;}
        public string Prijmeni {get; private set;}
        public int Praxe {get; private set;}

        public Pruvodci(string jmeno, string prijmeni, int praxe){
            this.Jmeno = jmeno;
            this.Prijmeni = prijmeni;
            this.Praxe = praxe;
        }

        public void KontrolujListky(){
            System.Console.WriteLine("Zkontroloval jsem vsechny vagony");
        }
    }

class Vlak
    {
        //fields
        private int _pocetVagonu;
        public string StrojVedouci {get; private set; }
        private int _vykon;
        private List<Pruvodci> _seznamPruvodcich;

        //konstruktor
        public Vlak(int pocetVagonu, int vykon){
             this._pocetVagonu = pocetVagonu;
             this._vykon = vykon;
             this.StrojVedouci = null;
             this._seznamPruvodcich = new List<Pruvodci>();
        }

        //getter/accessor
        public int GetPocetVagonu(){
            return this._pocetVagonu;
        }

        //setter/mutator
        public void SetPocetVagonu(int novyPocet){
            this._pocetVagonu = novyPocet;
        }

        //vlastnosti
        public int Vykon{
            get {return this._vykon;}
            set {this._vykon = value;}
        }

        //metody
        public void Zatrub(int silaTroubeni = 1){
            if (silaTroubeni <= 0){
                System.Console.WriteLine("hu ...");
            } else if (silaTroubeni == 1){
                System.Console.WriteLine("HUhUHUhU!!!!");
            } else {
                System.Console.WriteLine("HU! HU! HU!");
            }
        }

        public void PridejPruvodciho(Pruvodci pruvodci){
            this._seznamPruvodcich.Add(pruvodci);
        }

        public void SpustKontrolu(){
            foreach (Pruvodci pruvodci in this._seznamPruvodcich)
            {
                pruvodci.KontrolujListky();
            }
        }

    }

class Program
    {
        static void Main(string[] args)
        {
            Vlak elephant = new Vlak(5, 28000);
            elephant.PridejPruvodciho(new Pruvodci("Honza", "Novotny", 3));
            elephant.PridejPruvodciho(new Pruvodci("Alena", "Skvorova", 2));
            elephant.SpustKontrolu();
        }
    }
```

**Domácí úkol HW1.1 Cestující:**

Vytvořte třídu Cestující. Naplňte instance třídy vlak cestujícími. Cestující má možnost do vlaku nastoupit a vystoupit (udělejte příslušné metody). Také může nastoupit do jiného vlaku (vymyslete vhodný mechanismus referencí).

**Domácí úkol HW1.2 Cestující vs. Průvodčí:**

Cestující může mít platný lístek nebo neplatný. Při spuštěné kontrole ve vlaku bude šance 50 procent, že bude černý pasažér přistižen a bude z přepravy vyloučen.

**Domácí úkol HW1.3 Zkušení průvodčí:**

V mém kódě mají průvodčí i počet let praxe. Zaveďte do kódu mechanismus, který při chytání černých pasažérů zohledňuje zkušenost průvodčích.

**Domácí úkol HW1.4 Přepravní společnosti:**

Vlaky patří různým přepravním společnostem. Tyto společnosti mohou mít dohodu o tom, že lístek platí vzájemně mezi nimi nebo chtějí specifický lístek pro danou společnost. Vytvořte objekt Lístek a dejte je cestujícím. Tento lístek bude mít u sebe informaci o tom, pro jaké dopravní společnosti platí. Vytvořte třídu DopravníSpolečnost a přidejte vlaky do příslušných společností. Pokud při kontrole bude mít Cestující neplatný lístek, bude z přepravy vyloučen.

**Domácí úkol HW1.5 Movitý cestující:**

Přidejte poslední funkcionalitu vašeho systému a to, že cestující si mohou u průvodčího lístek zakoupit, pokud mají lístek špatný nebo jedou na černo. Pokud jeli na černo, tak si za lístek připlatí penále. Pokud peníze nemají, tak je z přepravy vyhoďte.

**Úkol OS2.1 Rozhraní:**

Rozhraní je způsob v jazyce C#, jak nutit třídy, aby si implementoval nějaké chování. Pokud nějaká třída implementuje rozhraní, tak říkáme, že se zavazuje toho chování umět. Způsob implementace zůstává na ní, avšak já musím být schopen se na tento závazek spolehnout. Rozhraní se vytváří klíčovým slovem ```interface``` a jee zvykem název rozhraní začínat velkým písmenkem I. 

**Zadání**

Naprogramujte rozhraní IPojízdné, které nutí implementující třídy implementovat následující metody: 
1. zatocDoleva, kde parametrem je počet stupňů
2. zatocDoprava, kde parametrem je počet stupňů
3. dopredu, kde parametrem je vzdalenost
4. zpatky, kde parametrem je vzdalenost

**Řešení**

```
interface IPojizdne{
    void zatocDoleva(float pocetStupnu);
    void zatocDoprava(float pocetStupnu);
    void dopredu(float vzdalenost);
    void zpatky(float vzdalenost);
}
```

**Úkol OS2.2 Rozhraní sdílené chování:**

C# neumí vícenásobnou dědičnost. Důvodem je problém smrtícího diamantu smrti (viz. wikipedie - deadly diamond of death). Z toho důvodu pokud chceme, aby třída uměla metody, které nedědila od svého předka a zároveň tyto metody umí i jiná třída, je možné je abstrahovat do rozhraní, které slouží jako náhražka vícenásobné dědičnosti. Z pohledu objektového návrhu je to však na polemiku. Rozhraní by měl být závazek o chování a ne způsob, jak vynutit něco připomínající vícenásobnou dědičnost.

**Zadání**

Napište dvě třídy - kačenka a automobil, které implementují rozhraní a jeho metody. Dejte jim také nějakou vlastní metodu a atribut. Metody z rozhraní budou pracovat se stavem objektů třídy, takže nezapomeňte vhodne vyřešit atributy.

**Řešení**

```
class Kacenka : IPojizdne{
    private string jmeno;
    private double[] pozice;

    public Kacenka(string jmeno){
        this.jmeno = jmeno;
        this.pozice = new double[2]{0, 0};
    }

    //vlastní metoda kačenky
    public void zakvakej() {
        Console.WriteLine("Kvááák kvák");
    }

    //plnění závazku rozhraní
    public void zatocDoprava(float pocetStupnu){
        this.pozice[0] += Math.Sin(pocetStupnu > 180? 180: pocetStupnu);
    }

    public void zatocDoleva(float pocetStupnu){
        this.pozice[0] -= Math.Sin(pocetStupnu > 180? 180: pocetStupnu);
    }

    public void dopredu(float vzdalenost){
        this.pozice[1] += vzdalenost;
    }

    public void zpatky(float vzdalenost){
        this.pozice[1] -= vzdalenost;
    }
}
```

```
class Automobil : IPojizdne
{

    private string _znacka;
    private double[] _pozice;

    public Automobil(string znacka){
        this._znacka = znacka;
        this._pozice = new double[2]{0, 0};
    }

    public string Znacka{
        get { return this._znacka;}
    }

    public double[] Pozice{
        get {return this._pozice;}
    }

    public void zatrub() {
        Console.WriteLine("Tuuuu Tuuuu");
    }

    public void zatocDoprava(float pocetStupnu){
        this._pozice[0] += Math.Sin(pocetStupnu > 180? 180: pocetStupnu);
    }
    public void zatocDoleva(float pocetStupnu){
        this._pozice[0] -= Math.Sin(pocetStupnu > 180? 180: pocetStupnu);
    }

    public void dopredu(float vzdalenost){
        this._pozice[1] += vzdalenost;
    }

    public void zpatky(float vzdalenost){
        this._pozice[1] -= vzdalenost;
    }
}
```

**Úkol OS2.3 Využívání rozhraní jako generalizace:**

Rozhraní přináší zajímavou vlastnost do systému. Můžeme donutit uživatele vložit do metody nějakého objektu pouze takový objekt, který je ze třídy implementující požadované rozhraní. Tím se můžeme spolehnout na to, že uvnitř metody mohu zavolat metodu rozhraní a objekt ji bude umět. Nevýhodou je, že bude umět pouze metody rozhraní a ztratí vlastní metody - k objektu přistupujeme z abstraktnějšího hlediska, tedy generalizujeme.

**Zadání**

Vytvořte třídu Řidič, který si přiřazuje dopravní prostředek vhodným způsobem. Zamyslete se nad tím, zda je přiřazení dopravního prostředku nutné již v konstruktoru - co tím vlastně říkáte z pohledu objektového návrhu? Přiřazený dopravní prostředek musí implementovat rozhraní IPojizdne. Naprogramujte mu nějakou metodu, které využívá metody dopravního prostředku

**Řešení**

```
class Ridic
{
    public string Jmeno {get; private set;}
    public IPojizdne? DopravniProstredek {get; private set;};

    public Ridic(string jmeno){
        this.Jmeno = jmeno;
        this.DopravniProstredek = null;
    }

    public void obstarejsiDopravniProstredek(IPojizdne dopravniProstredek) {
        this.DopravniProstredek = dopravniProstredek;
    }

    public void jedDoPrace(){
        if (this.DopravniProstredek != null){
            this.DopravniProstredek.dopredu(20);
            this.DopravniProstredek.zatocDoprava(10);
            this.DopravniProstredek.dopredu(20);
            this.DopravniProstredek.zatocDoleva(30);
            this.DopravniProstredek.dopredu(20);
        } else {
            System.Console.WriteLine("Nemám čím!");
        }
    }
}
```

**Úkol OS2.4 Seznam s rozhraním:**

**Zadání**

Vytvořte třídu garáž, která obsahuje metodu zaparkuj. Do tohoto seznamu půjdou vložit pouze takové objekty, které implementují rozhraní IZaparkovatelné. Třída automobil bude implementovat toho rozhraní, třída Kačenka nebude. Implementaci třídy a rozhraní je na vás, ať si trošku procvičíte kreativitu návrhu. Budete muset pravděpodobně i trošku upravit předchozí třídy.

**Řešení**

```
interface IZaparkovatelne{
    void zaparkuj(Garaz garaz);
    void vyparkuj(Garaz garaz);
}
```

Myšlenka je zde taková, že prostředek, který implementuje tohoto rozhraní, tak si řekne o zaparkování a zvolí garáž.

```
class Garaz
{
    public List<IZaparkovatelne> ZaparkovaneProstredky {get; private set;}
    public double[] GPSSouradnice {get; private set;}

    public Garaz(double GPSX, double GPSY){
        this.GPSSouradnice = new double[2]{GPSX, GPSY};
        this.ZaparkovaneProstredky = new List<IZaparkovatelne>();
    }

    public void umistiDopravniProstredek(IZaparkovatelne dopravniProstredek) {
        this.ZaparkovaneProstredky.Add(dopravniProstredek);
    }
    public void uvolniDopravniProstredek(IZaparkovatelne dopravniProstredek) {
        this.ZaparkovaneProstredky.Remove(dopravniProstredek);
    }
}
```

Myšlenka je taková, že garáž obsahuje seznam zaparkovatelných a má vlastní umístění na mapě pomocí GPS douřadnic. Pokud se chce nějaký prostředek umístit do garáže, pak musí zavolat její metodu a požádat o umístění. To půjde provést jen tehdy, když dopravní prostředek implementuje rozhraní IZaparkovatelne.

```
class Automobil : IPojizdne, IZaparkovatelne
{
    private string _znacka;
    private double[] _pozice;

    public bool Zaparkovano {get; private set;}

    public Garaz? ParkovaciGaraz {get; private set;}

    public Automobil(string znacka){
        this._znacka = znacka;
        this._pozice = new double[2]{0, 0};
        this.Zaparkovano = false;
        this.ParkovaciGaraz = null;
    }

    public string Znacka{
        get { return this._znacka;}
    }

    public double[] Pozice{
        get {return this._pozice;}
    }

    public void zatrub() {
        Console.WriteLine("Tuuuu Tuuuu");
    }

    public void zatocDoprava(float pocetStupnu){
        if (this.Zaparkovano == false){
            this._pozice[0] += Math.Sin(pocetStupnu > 180? 180: pocetStupnu);
        } else {
            System.Console.WriteLine("Nejdriv musíš vyparkovat!");
        }
    }
    public void zatocDoleva(float pocetStupnu){
        if (this.Zaparkovano == false){
            this._pozice[0] -= Math.Sin(pocetStupnu > 180? 180: pocetStupnu);
        } else {
            System.Console.WriteLine("Nejdriv musíš vyparkovat!");
        }
    }

    public void dopredu(float vzdalenost){
        if (this.Zaparkovano == false){
            this._pozice[1] += vzdalenost;
        } else {
            System.Console.WriteLine("Nejdriv musíš vyparkovat!");
        }
    }

    public void zpatky(float vzdalenost){
        if (this.Zaparkovano == false){
            this._pozice[1] -= vzdalenost;
        } else {
            System.Console.WriteLine("Nejdriv musíš vyparkovat!");
        }
    }

    public void zaparkuj(Garaz garaz){
        this._pozice[0] = garaz.GPSSouradnice[0];
        this._pozice[1] = garaz.GPSSouradnice[1];
        this.ParkovaciGaraz = garaz;
        garaz.umistiDopravniProstredek(this);
        this.Zaparkovano = true;
    }
    public void vyparkuj(Garaz garaz){
        if (this.ParkovaciGaraz == null){
            System.Console.WriteLine("Vždyť nejsi zaparkován!");
        } else {
            this.ParkovaciGaraz.uvolniDopravniProstredek(this);
            this.Zaparkovano = false;
        }
    }
}
```

Třídu automobil jsem musel pozměnit. Teď nelze s automobilem řídit metodami s IPojizdne do té doby, dokavaď je zaparkován. Přidal jsem mu tedy atribut s příznakem zaparkování. Tento atribut se nastavuje při zaparkování do garáže a při vyparkování z garáže. Dále jsem mu přidal odkaz na garáž, ve které je zaparkován. Tím jsem propojil obě třídy do vztahu a komunikují spolu. Při zaparkování do garáže přejímá automobil pozici z GPS garáže.

**Úkol OS2.5 Statické typování a rozhraní:**

**Zadání**

Předešlými úkoly jste vytvořili relativně robustní návrh informačního systému. Vyzkoušejte si teď sílu statického typování. Proveďte následující experimenty v třídě Main:
1. Zkuste s kačenkou dojet do práce.
2. Zkuste kačenku zaparkovat do garáže
3. Vytvořte třídu Hrábě, která neimplementuje ani jedno z rozhraní.
4. Zkuste hrábě přidělit řidičovi jako dopravní prostředek.
5. Nakonec prozkoumejte chování vašeho automobilu.

**Řešení**

```
class Hrabe
{

    public string Znacka {get; private set;}

    public Hrabe(string znacka){
        this.Znacka = znacka;
    }

    public void hrabej() {
        Console.WriteLine("Hrááb Hrááb");
    }
}
```

```
using System;
using System.Collections.Generic;

namespace ws
{
    class Program
    {
        static void Main(string[] args)
        {
            Ridic pavel = new Ridic("Pavel Beránek");   
            Kacenka kacka = new Kacenka("Pepina");
            pavel.obstarejsiDopravniProstredek(kacka);
            pavel.jedDoPrace();
            //pavel.DopravniProstredek.zaparkuj(parkovisteUjepCPTO); - nelze

            Hrabe hrabitchky = new Hrabe("Hornybach");
            //pavel.obstarejsiDopravniProstredek(hrabitchky); - nelze
            
            Automobil mojeKara = new Automobil("BMW");
            Garaz parkovisteUjepCPTO = new Garaz(50.66, 14.02);
            pavel.obstarejsiDopravniProstredek(mojeKara);
            pavel.jedDoPrace();
            //pavel.DopravniProstredek.zaparkuj(parkovisteUjepCPTO); - nelze, špatný návrh

        }
    }
}
```

Zatraceně. Chyba v návrhu (pokud jste to ode mě jen opisovali). Jelikož uvnitř řidiče jsou dopravní prostředky generalizované objekty s IPojizdne, tak nemohu volat metody z rozhraní IZaparkovatelné :( ... Chyby v návrhu jsou běžné a proto je nutné si návrh architektury aplikace řádně rozmyslet. Doporučuji metodu tužka papír a přemýšlet dřív, než začnete psát kód. V této fázi musím začít přepisovat značnou část návrhu, nebo vymyslet nějaký hack (nedoporučuji, vrátí se vám to).

**Domácí úkol HW2.1 Oprava návrhu:**

Pokud jste bezrozmyšlenkovitě opisovali můj návrh, tak teď se vám to vrátilo. Opravte návrh mé architektury tak, aby šlo zaparkovat dopravním prostředkem. Budete muset opravit třídu Ridic nebo vymyslet jiný mechanismus parkování. Například přirazení instance garáže Ridicovi, který pak volá metody pro zaparkování v garáži.

**Domácí úkol HW2.2 Zaparkovatelné ale nepojízdné:**

Vytvořte nějakou třídu, která je zaparkovatelné, ale není pojízdná. Zkuste s ní provést experimenty.

**Domácí úkol HW2.3 Palivo:**

Doplňte třídám mechanismus, který neumožňuje jezdit, pokud dopravnímu prostředku dojde palivo. Palivo ubyde v případě, že dopravní prostředek jede dopředu nebo dozadu.

**Domácí úkol HW2.4 Benzínka:**

Vytvořte třídu Benzínka (nebo krmírna ... i Kačenka potřebuje palivo, takže zkuste vymyslet univerzální název, možná DoplňovačkaPaliva???), která umožňuje dvě věci:
1. Doplnit palivo do dopravního prostředku
2. Vzít si sebou v kanistrech/pytlech na zrní palivo do garáže v omezeném počtu a doplnit ho v garáži

**Domácí úkol HW2.5 Více dopravních prostředků a omezená garáž:**

Doprogramujte mechanismus, který umožňuje řidiči vlastnit více dopravních prostředků, které jsou umístěné v garáži. Řidič si může vybrat, kterým prostředkem vyjede z garáže. Garáž je však omezená kapacitou, což by bylo asi vhodné dát rovnou do konstruktoru (garáž se staví s nějakou kapacitou). Pokud by vás mrzela pevná velikost garáže, tak můžete vytvořit ještě třídu StavebníFirma, která kapacitu garáže dostaví :).




### 5. On-site cvičení 2 - Vybrané návrhové vzory

### 6. Náměty na seminární práce