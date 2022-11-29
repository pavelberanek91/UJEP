# Objektově-orientované návrhové vzory

## Strukturální vzory - Most, Muší váha, Kompozit

Strukturální vzory řeší problémy, které vycházejí ze struktury již vytvořených objektů, jejichž struktura nám za běhu nevyhovuje. Mezi první probírané patří:
1. Most - umožňuje přepínat typ generalizace z dědičnosti na kompozici
2. Muší váha - umožňuje šetření operační paměti sdílením stav objektů
3. Kompozit - umožňuje rozdělit komplexní objekt do stromové struktury z jednodušších objektů

### Most

Ideálním příkladem pro vysvětlení návrhového vzoru most je příklad z refactoring guru, který je pod těmito odstavci přiložen. Mějme dva geometrické tvary, např.: krychle a kouli. Tyto geometrické útvary mohou mít dvě hodnoty vlastnosti barva - červená a modrá. Entity v našem programu mají tedy dvě dimenze - tvar a barva. Pokud bychom řešili problém zcela správně pomocí OOP, pak potřebujeme třídu geometrický tvar, který bude mít potomky koule a krychle. Pokud chceme ještě dodat barvu, pak koule bude mít potomky modráKoule a červenáKoule. To samé platí pro krychli. Přidáním dalšího geometrického tvaru nebo barvy se nám rozširí mnohonásobně počet tříd. 

Někdo z vás může namítnout, že by mohl vytvořit atribut barva a ten nastavovat v konstruktoru. Bohužel v realitě jsou případy generalizací složitější a barva v našem školním příkladě může představovat vlastnost, která značně ovlivňuje chování objektu a není jen kosmetickou vlastností. Příkladem mohou být různí typy vojáků ve videohře z různých ras, kde typ vojáka i rasa určuje výsledné chování, které se může značně lišit.

Řešením problému s explozí dědičnosti je návrhový vzor most, který umí separovat vlastnosti objektů a nahradit je kompozicí. To funguje pouze v tom případě, že tyto vlastnosti jsou na sobě nezávislé (ortogonální). Řešením je tedy extrahovat v našem příkladě s geometrickým tvarem barvu zvlášť do třídy barva a vytvořit její potomky červenáBarva a modráBarva. Odkazy na instance těchto potomků si pak ukládají instance geometrických tvarů do sebe (kompozice, případně agregace).

Více o návrhovém vzoru most naleznete [ZDE](https://refactoring.guru/design-patterns/bridge) nebo [ZDE]().

**Cvičení**

Představte si, že píšete univerzální prohlížeč souborů (file explorer) do operačního systému. Tento prohlížeč je multiplatformní (telefon, notebook) a zároveň umožňuje ovládání klávesnicí i dotykem. Předělejte přiložený kód pomocí dekorátoru most.

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
            TradicniTelefon aligator = new TradicniTelefon();
            aligator.vyberAdresareKlavesnici("obrazky");
            aligator.vyberSouboruKlavesnici("rodina.jpg");

            DotykovyTelefon samsung_galaxy_note = new DotykovyTelefon();
            samsung_galaxy_note.dotykNaIkonkuAdresare("obrazky");
            samsung_galaxy_note.dotykNaIkonkuSouboru("rodina.jpg");

            TradicniPocitac thinkpadT400 = new TradicniPocitac();
            thinkpadT400.vyberAdresareKlavesnici("obrazky");
            thinkpadT400.vyberSouboruKlavesnici("rodina.jpg");
        }
    }

    interface IZarizeni{
        void otevriSoubor(string cesta);
        void otevriSlozku(string cesta);
        void vratSeZpet();
        void vratSeDopredu();
    }

    abstract class Pocitac: IZarizeni{
        public void otevriSoubor(string cesta){
            Console.WriteLine("Linux->syscall.openFile: {0}", cesta);
        }
        public void otevriSlozku(string cesta){
            Console.WriteLine("Linux->syscall.openFolder: {0}", cesta);
        }
        public void vratSeZpet(){
            Console.WriteLine("Linux->syscall.returnPrev");
        }
        public void vratSeDopredu(){
            Console.WriteLine("Linux->syscall.returnNext");
        }
    }

    abstract class MobilniTelefon: IZarizeni{
        public void otevriSoubor(string cesta){
            Console.WriteLine("Android->android_system.FileOpen: {0}", cesta);
        }
        public void otevriSlozku(string cesta){
            Console.WriteLine("Android->android_system.FolderOpen: {0}", cesta);
        }
        public void vratSeZpet(){
            Console.WriteLine("Android->android_system.PrevFolder");
        }
        public void vratSeDopredu(){
            Console.WriteLine("Android->android_system.CancelReturnFolder");
        }

    }

    class DotykovyPocitac: Pocitac{

        public DotykovyPocitac(){}

        public void dotykNaIkonkuAdresare(string cesta){
            otevriSlozku(cesta);
        }

        public void dotykNaIkonkuSouboru(string cesta){
            otevriSoubor(cesta);
        }

        public void dotykNaSipkuZpet(){
            vratSeZpet();
        }

        public void dotykNaSipkuDopredu(){
            vratSeDopredu();
        }
    }

    class TradicniPocitac: Pocitac{
        
        public TradicniPocitac(){}

        public void vyberAdresareKlavesnici(string cesta){
            otevriSlozku(cesta);
        }

        public void vyberSouboruKlavesnici(string cesta){
            otevriSoubor(cesta);
        }

        public void stiskSipkyDoleva(){
            vratSeZpet();
        }

        public void stiskSipkyDoprava(){
            vratSeDopredu();
        }
    }

    class DotykovyTelefon: MobilniTelefon{

        public DotykovyTelefon(){}

        public void dotykNaIkonkuAdresare(string cesta){
            otevriSlozku(cesta);
        }

        public void dotykNaIkonkuSouboru(string cesta){
            otevriSoubor(cesta);
        }

        public void dotykNaSipkuZpet(){
            vratSeZpet();
        }

        public void dotykNaSipkuDopredu(){
            vratSeDopredu();
        }
    }

    class TradicniTelefon: MobilniTelefon{

        public TradicniTelefon(){}

        public void vyberAdresareKlavesnici(string cesta){
            otevriSlozku(cesta);
        }

        public void vyberSouboruKlavesnici(string cesta){
            otevriSoubor(cesta);
        }

        public void stiskSipkyDoleva(){
            vratSeZpet();
        }

        public void stiskSipkyDoprava(){
            vratSeDopredu();
        }
    }

}
```

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
            TradicniZarizeni aligator = new TradicniZarizeni(new MobilniTelefon());
            aligator.vyberAdresareKlavesnici("obrazky");
            aligator.vyberSouboruKlavesnici("rodina.jpg");

            DotykoveZarizeni samsung_galaxy_note = new DotykoveZarizeni(new MobilniTelefon());
            samsung_galaxy_note.dotykNaIkonkuAdresare("obrazky");
            samsung_galaxy_note.dotykNaIkonkuSouboru("rodina.jpg");

            TradicniZarizeni thinkpadT400 = new TradicniZarizeni(new Pocitac());
            thinkpadT400.vyberAdresareKlavesnici("obrazky");
            thinkpadT400.vyberSouboruKlavesnici("rodina.jpg");
        }
    }

    interface IZarizeni{
        void otevriSoubor(string cesta);
        void otevriSlozku(string cesta);
        void vratSeZpet();
        void vratSeDopredu();
    }

    class Pocitac: IZarizeni{
        public void otevriSoubor(string cesta){
            Console.WriteLine("Linux->syscall.openFile: {0}", cesta);
        }
        public void otevriSlozku(string cesta){
            Console.WriteLine("Linux->syscall.openFolder: {0}", cesta);
        }
        public void vratSeZpet(){
            Console.WriteLine("Linux->syscall.returnPrev");
        }
        public void vratSeDopredu(){
            Console.WriteLine("Linux->syscall.returnNext");
        }
    }

    class MobilniTelefon: IZarizeni{
        public void otevriSoubor(string cesta){
            Console.WriteLine("Android->android_system.FileOpen: {0}", cesta);
        }
        public void otevriSlozku(string cesta){
            Console.WriteLine("Android->android_system.FolderOpen: {0}", cesta);
        }
        public void vratSeZpet(){
            Console.WriteLine("Android->android_system.PrevFolder");
        }
        public void vratSeDopredu(){
            Console.WriteLine("Android->android_system.CancelReturnFolder");
        }

    }

    class DotykoveZarizeni{

        private IZarizeni zarizeni;

        public DotykoveZarizeni(IZarizeni zarizeni){
            this.zarizeni = zarizeni;
        }

        public void dotykNaIkonkuAdresare(string cesta){
            zarizeni.otevriSlozku(cesta);
        }

        public void dotykNaIkonkuSouboru(string cesta){
            zarizeni.otevriSoubor(cesta);
        }

        public void dotykNaSipkuZpet(){
            zarizeni.vratSeZpet();
        }

        public void dotykNaSipkuDopredu(){
            zarizeni.vratSeDopredu();
        }
    }

    class TradicniZarizeni{
        
        private IZarizeni zarizeni;

        public TradicniZarizeni(IZarizeni zarizeni){
            this.zarizeni = zarizeni;
        }

        public void vyberAdresareKlavesnici(string cesta){
            zarizeni.otevriSlozku(cesta);
        }

        public void vyberSouboruKlavesnici(string cesta){
            zarizeni.otevriSoubor(cesta);
        }

        public void stiskSipkyDoleva(){
            zarizeni.vratSeZpet();
        }

        public void stiskSipkyDoprava(){
            zarizeni.vratSeDopredu();
        }
    }
}
```

### Muší váha

Muší váha je důležitým návrhovým vzorem ve vývoji videoher a počítačové grafice. V počítačové grafice jsou důležité tzv. particle systémy (částicové). Jedná se o množinu částic, které se objevují například při demolici nějakého objektu (zdi), kdy zeď se rozpadne na mnoho drobných částí. V moderních hrách se jedná i o částice prachu, sněhu a podobně. V jedné videoherní scéně (nebo multiplayerové mapě) se nachází spousty částic, které obsahují atributy se svým stavem (pozice, rychlost), ale i konstantní nebo po určitou dobu konstantní atributy (barva, textura). Některé z těchto informací mohou být sdílené, čímž se ušetří značná část operační paměti. Bohužel se tím zvýší nároky na CPU.

Více se o muší váze dočtete [ZDE](https://refactoring.guru/design-patterns/flyweight) nebo [ZDE]().

**Cvičení**

Mějme online FPS hru typu Call of Duty, Fortnite, Unreal Tournament, aj. Předělejte přiložený kód tak, aby byl úsporný na paměť.

Postup:

1. Identifikujte nemutabilní a mutabilní atributy třídy Projektil.
2. Vytvořte třídu PohybujícíSeProjektil a přesuňte do ní mutabilní atributy ze třídy Projektil.
3. Propojte instanci pohybujícího se projektilu s jeho nemutabilními atributy v instanci třídy Projektil.
4. Protože projektily mohou být z různých zbraní, tak některé mají jiné nemutabilní vlastnosti.  Vytvořte tedy více typů projektilů, které se liší svou rychlostí.
5. Vytvořte v klientovi (main) seznam N pohybujících se projektilů o M typech.

```

```

**Námět na seminární práce na OONV:**

Aplikujte návrhový vzor v nějakém videoherním enginu (Unity, Unreal) a změřte reálný dopad na vaší RAM.

### Kompozit

Podobně jako muší váha i kompozit je specifický svým využitím. Zatímco u muší váhy musí být atributy objektu rozdělitelné na mutabilní a nemutabilní, tak u kompozitu musí být objekty rozdělitelné do stromové struktury. Taková struktura je typická pro informační systémy pro správu zaměstnanců. Vrcholový manažer řídí funkcionální manažery (účetnictví, finance, logistika), kteří řídí své zaměstnance. Podobné příklady nalezneme i u informačních systémů pro správu podnikových zdrojů (ERP systémy), kde podnik mé své divize, které se dále dělí.

Návrhový vzor kompozit použijeme v případě, kdy chceme provést operaci na uzlech, ale chceme stejným způsobem přistupovat (stejné rozhraní) i k uzlům, které listy nebo další uzly obsahují. Například pokud mějme metodu spust(). Tuto metodu mohu spustit na libovolném uzlu, ať už je uzlem jako takovým nebo listem. Pokud je uzel listem, pak metoda spust() vyvolá požadované chování. Pokud je uzlem skutečným uzlem, tedy obsahuje další uzly, tak zavolá své potomky (uzly) a na nich spustí metodu spust(). Vidíme, že z pohledu klienta nerozlišujeme typ uzlu. Klient v praxi zavolá metodu na jednom komplexním objektu, který se rozloží přes dílčí komponenty až na listy, které metodu spustí.

Více se o kompozitu dočtete [ZDE](https://refactoring.guru/design-patterns/composite) nebo [ZDE]().

**Cvičení**




