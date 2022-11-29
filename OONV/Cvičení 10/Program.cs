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