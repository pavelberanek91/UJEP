using System;
using System.Collections.Generic;

namespace ws
{
    class Program
    {
        static void Main(string[] args)
        {
            Vlak pepa = new Vlak(5, 28000);
            pepa.PridejPruvodciho(new Pruvodci("Honza", "Novotny", 3));
            pepa.PridejPruvodciho(new Pruvodci("Alena", "Skvorova", 2));
            pepa.KontrolaListku();
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

        public void KontrolaListku(){
            foreach (Pruvodci pruvodci in this._seznamPruvodcich)
            {
                pruvodci.KontrolujListky(2);
            }
        }

    }

    class Pruvodci{

        public string Jmeno {get; private set;}
        public string Prijmeni {get; private set;}
        public int Praxe {get; private set;}

        public Pruvodci(string jmeno, string prijmeni, int praxe){
            this.Jmeno = jmeno;
            this.Prijmeni = prijmeni;
            this.Praxe = praxe;
        }

        public void KontrolujListky(int pocetVagonu){
            System.Console.WriteLine("Zkontroloval jsem {0} vagonu", pocetVagonu);
            //algoritmus dodelat
        }
    }
}