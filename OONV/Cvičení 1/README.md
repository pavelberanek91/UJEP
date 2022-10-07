# Objektově-orientované návrhové vzory

**Obsah přednášky 1**:
* Typový systém ve staticky typovaných objektových programovacích jazycích

**Obsah cvičení 1**:
* Úvod do jazyka Csharp (podmínky, cyklus, podprogramy, třídy)
* Statické typování

## On-site cvičení 1

### Cognitive apprenticeship

### Úkol OS1.1 Založení .NET projektu:

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

### Úkol OS1.2 Vytvoření třídy:

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

### Úkol OS1.3 Vlastnosti:

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

### Úkol OS1.4 Metody:

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

### Úkol OS1.5 Agregace objektů:

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

## Domácí cvičení 1

### Úkol HW1.1 Cestující:

Vytvořte třídu Cestující. Naplňte instance třídy vlak cestujícími. Cestující má možnost do vlaku nastoupit a vystoupit (udělejte příslušné metody). Také může nastoupit do jiného vlaku (vymyslete vhodný mechanismus referencí).

### Úkol HW1.2 Cestující vs. Průvodčí:

Cestující může mít platný lístek nebo neplatný. Při spuštěné kontrole ve vlaku bude šance 50 procent, že bude černý pasažér přistižen a bude z přepravy vyloučen.

### Úkol HW1.3 Zkušení průvodčí:

V mém kódě mají průvodčí i počet let praxe. Zaveďte do kódu mechanismus, který při chytání černých pasažérů zohledňuje zkušenost průvodčích.

### Úkol HW1.4 Přepravní společnosti:

Vlaky patří různým přepravním společnostem. Tyto společnosti mohou mít dohodu o tom, že lístek platí vzájemně mezi nimi nebo chtějí specifický lístek pro danou společnost. Vytvořte objekt Lístek a dejte je cestujícím. Tento lístek bude mít u sebe informaci o tom, pro jaké dopravní společnosti platí. Vytvořte třídu DopravníSpolečnost a přidejte vlaky do příslušných společností. Pokud při kontrole bude mít Cestující neplatný lístek, bude z přepravy vyloučen.

### Úkol HW1.5 Movitý cestující:

Přidejte poslední funkcionalitu vašeho systému a to, že cestující si mohou u průvodčího lístek zakoupit, pokud mají lístek špatný nebo jedou na černo. Pokud jeli na černo, tak si za lístek připlatí penále. Pokud peníze nemají, tak je z přepravy vyhoďte.

**Video týdne: Kontroverzní názory ve vývoji**

Na internetu se od spousty přispěvovatelů na diskuzních portálech dočtete, že objektově-orientované programování je nejhorší paradigmat vývoje, který můžete zvolit. Jelikož se brzy dostanete do praxe, pojďme se podívat na některé další kontroverzní názory se kterými se ve vývoji setkáte. Časem si uděláte vlastní názor. [ZDE](https://www.youtube.com/watch?v=goy4lZfDtCE)