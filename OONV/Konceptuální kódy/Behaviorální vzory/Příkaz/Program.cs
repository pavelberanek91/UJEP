abstract class Prikaz // Command interface
{
    protected TextovyEditor editor; // Receiver
    protected List<string> parametry; // Params

    public Prikaz(TextovyEditor editor, List<string> parametry)
    {
        this.parametry = parametry;
        this.editor = editor;
    }

    public abstract void Spustit(); // Execute
}

class Ulozit : Prikaz // Concrete Command 1
{
    public Ulozit(TextovyEditor editor, List<string> parametry) : base(editor, parametry) { }

    public override void Spustit()
    {
        string obsah = this.editor.VratDataSouboru(true);
        this.editor.stav = "ulozeno do cesty " + this.parametry[0];
        System.Console.WriteLine(obsah);
    }
}

class Kopirovat : Prikaz // Concrete Command 2
{
    public Kopirovat(TextovyEditor editor, List<string> parametry) : base(editor, parametry) { }

    public override void Spustit()
    {
        string zkopirovanyText = this.editor.ZkopirujOznacenyText();
        System.Console.WriteLine(zkopirovanyText);
    }
}

class Tlacitko // Invoker
{
    private Prikaz pripojenyPrikaz;

    public Tlacitko(Prikaz pripojenyPrikaz)
    {
        this.pripojenyPrikaz = pripojenyPrikaz;
    }

    public void Kliknout()
    {
        pripojenyPrikaz.Spustit();
    }
}

class TextovyEditor // Receiver
{
    public string stav;

    public string ZkopirujOznacenyText()
    {
        return "jsem oznaceny text";
    }

    public string VratDataSouboru(bool vcetneMetaDat)
    {
        string aktualniObsahSouboru = "jsem text celeho souboru";
        string metadata = "jsme aktualni metadata";
        if (vcetneMetaDat)
        {
            return aktualniObsahSouboru + ";" + metadata;
        }
        else
        {
            return aktualniObsahSouboru;
        }
    }
}

class TestClass
{
    static void Main(string[] args)
    {
        TextovyEditor editor = new TextovyEditor();

        List<string> parametry = new List<string> { "cesta/k/souboru.txt" };
        Prikaz ulozit = new Ulozit(editor, parametry);
        Prikaz kopirovat = new Kopirovat(editor, null);

        Tlacitko ulozitTlacitko = new Tlacitko(ulozit);
        Tlacitko kopirovatTlacitko = new Tlacitko(kopirovat);

        ulozitTlacitko.Kliknout();
        kopirovatTlacitko.Kliknout();
    }
}
