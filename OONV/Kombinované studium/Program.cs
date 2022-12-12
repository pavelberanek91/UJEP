Kocicka mica = new Kocicka("princezna", 3.5f, 1.0);
System.Console.WriteLine(mica.vek);
mica.oslavNarozeniny();
System.Console.WriteLine(mica.vek);

abstract class Savec{
    public string jmeno {get; set;}
    public float hmotnost {get; private set;}
    public double delka {get; private set;}
    public int vek {get; private set;}
    private bool spokojenost;

    public Savec(string jmeno, float hmotnost, double delka){
        this.jmeno = jmeno;
        this.hmotnost = hmotnost;
        this.delka = delka;
        this.vek = 1;
        this.spokojenost = true;
    }

}

class Kocicka{

    
    

    public void oslavNarozeniny(){
        this.vek++;
    }


}


