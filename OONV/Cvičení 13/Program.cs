using System;
using System.Collections.Generic;

namespace ws
{
    class Program
    {
        static void Main(string[] args)
        {

        }
    }

    class Hrac{}

    abstract class NPCAI{

        public int[] pocatecni_souradnice {get; private set;}
        public int zasahoveBody {get; private set;}
        public int utocneBody {get; private set;}
        public int obranneBody {get; private set;}
        
        public NPCAI(int[] pocatecni_souradnice, int zasahoveBody, int utocneBody, int obranneBody){
            this.pocatecni_souradnice = pocatecni_souradnice;
            this.zasahoveBody = zasahoveBody;
            this.utocneBody = utocneBody;
            this.obranneBody = obranneBody;
        }

        public void zmenPoziciNaMape(int[] souradnice){
            Random random = new Random();
            for (int idim = 0; idim < pocatecni_souradnice.Length; idim++){
                pocatecni_souradnice[idim] += random.Next(1, 5);
            }
        }

        public abstract void pockejNaMiste();

        public abstract void interakceSHracem(Hrac hrac);

        public abstract void utekZBoje(int[] souradniceBojiste);
    }

    class NeagresivniNPC: NPCAI{

        public override void pockejNaMiste(){
            Console.WriteLine("Cekam na miste 5 sekund");
        }

        public override void interakceSHracem(Hrac hrac){
            Console.WriteLine("Co si preješ statný hrdino?");
        }

        public override void utekZBoje(int[] souradniceBojiste){
            for (int i = 0; i < 10; i++){
                
            }
        }
    }

    class AgresivniNPC: NPCAI{

        public override void pockejNaMiste(){

        }

        public override void interakceSHracem(Hrac hrac){

        }

        public override void utekZBoje(int[] souradniceBojiste){

        }
    }

    class Protihrac: NPCAI{

        public override void pockejNaMiste(){

        }

        public override void interakceSHracem(Hrac hrac){

        }

        public override void utekZBoje(int[] souradniceBojiste){

        }
    }


}