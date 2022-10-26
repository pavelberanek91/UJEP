# Objektově-orientované návrhové vzory

## On-site cvičení 2 - rozhraní

### Cognitive apprenticeship

### Úkol OS2.1 Rozhraní:

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

### Úkol OS2.2 Rozhraní sdílené chování:

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

### Úkol OS2.3 Využívání rozhraní jako generalizace:

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

### Úkol OS2.4 Seznam s rozhraním:

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

### Úkol OS2.5 Statícké typování a rozhraní:

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


## Domácí cvičení 2

### Úkol HW2.1 Oprava návrhu:

Pokud jste bezrozmyšlenkovitě opisovali můj návrh, tak teď se vám to vrátilo. Opravte návrh mé architektury tak, aby šlo zaparkovat dopravním prostředkem. Budete muset opravit třídu Ridic nebo vymyslet jiný mechanismus parkování. Například přirazení instance garáže Ridicovi, který pak volá metody pro zaparkování v garáži.

### Úkol HW2.2 Zaparkovatelné ale nepojízdné:

Vytvořte nějakou třídu, která je zaparkovatelné, ale není pojízdná. Zkuste s ní provést experimenty.

### Úkol HW2.3 Palivo:

Doplňte třídám mechanismus, který neumožňuje jezdit, pokud dopravnímu prostředku dojde palivo. Palivo ubyde v případě, že dopravní prostředek jede dopředu nebo dozadu.

### Úkol HW2.4 Benzínka:

Vytvořte třídu Benzínka (nebo krmírna ... i Kačenka potřebuje palivo, takže zkuste vymyslet univerzální název, možná DoplňovačkaPaliva???), která umožňuje dvě věci:
1. Doplnit palivo do dopravního prostředku
2. Vzít si sebou v kanistrech/pytlech na zrní palivo do garáže v omezeném počtu a doplnit ho v garáži

### Úkol HW2.5 Více dopravních prostředků a omezená garáž:

Doprogramujte mechanismus, který umožňuje řidiči vlastnit více dopravních prostředků, které jsou umístěné v garáži. Řidič si může vybrat, kterým prostředkem vyjede z garáže. Garáž je však omezená kapacitou, což by bylo asi vhodné dát rovnou do konstruktoru (garáž se staví s nějakou kapacitou). Pokud by vás mrzela pevná velikost garáže, tak můžete vytvořit ještě třídu StavebníFirma, která kapacitu garáže dostaví :).

**Video týdne: Fancy slova**

V paradigmatu objektově-orientovaného programování přibývá spousty zvláštních slov, například návrhové vzory. Jiné paradigmaty, jako je funkcionální programování, mají také své fancy slova, například: monády. Pojďme se podívat na video, které některá důležitá slova vysvětluje, se kterými se setkáte v různých paradigmatech. [ZDE](https://www.youtube.com/watch?v=4Zc9ci9L5wY)

**Video týdne: Fancy slova**

V paradigmatu objektově-orientovaného programování přibývá spousty zvláštních slov, například návrhové vzory. Jiné paradigmaty, jako je funkcionální programování, mají také své fancy slova, například: monády. Pojďme se podívat na video, které některá důležitá slova vysvětluje, se kterými se setkáte v různých paradigmatech. [ZDE](https://www.youtube.com/watch?v=4Zc9ci9L5wY)

**Video týdne: Fancy slova**

V paradigmatu objektově-orientovaného programování přibývá spousty zvláštních slov, například návrhové vzory. Jiné paradigmaty, jako je funkcionální programování, mají také své fancy slova, například: monády. Pojďme se podívat na video, které některá důležitá slova vysvětluje, se kterými se setkáte v různých paradigmatech. [ZDE](https://www.youtube.com/watch?v=4Zc9ci9L5wY)
