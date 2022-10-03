namespace Cviceni1
{
    class Program
    {
        static void Main(string[] args)
        {
            //Zamestnanec pepa = new Zamestnanec("Pepa", "Skvor", 20);

            
            Console.Write($"{Environment.NewLine}Press any key to exit...");
            Console.ReadKey(true);
        }
    }

    abstract class Zamestnanec{

        //fields
        private string _jmeno;
        private string _prijmeni;
        public int _vek {get; private set; }
        private string? _pozice;

        //konstruktor
        public Zamestnanec(string jmeno, string prijmeni, int vek){
            this._jmeno = jmeno;
            this._prijmeni = prijmeni;
            this._vek = vek;
            this._pozice = null;
        }

        //vlastnosti
        public string? Pozice{
            get {return this._pozice;}
            set {this._pozice = value;}
        }

        public int GetVek(){
            return this._vek;
        }
        public void SetVek(int vek){
            this._vek = vek;
        }
    }
}