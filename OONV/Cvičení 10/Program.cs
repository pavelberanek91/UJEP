using System;
using System.Collections.Generic;
using System.IO;

namespace ws
{
    class Program
    {
        static void Main(string[] args)
        {
            Soubor eva_vasek_lyrics = new Soubor("Jednu bílou orchidej, dals mi nic víc, ...");
            eva_vasek_lyrics.prectiObsah();
            
            Adresar metal = new Adresar(new List<IPrectitelne>(){
                new Soubor("Brothers everywhere, Raise your hands into the air."),
                new Soubor("Fear of the dark, I have a constant fear that something's always near")
            });

            Adresar pop = new Adresar(new List<IPrectitelne>(){
                new Soubor("I live for the applause, applause, applause"),
                new Soubor("Never gonna give you up, Never gonna let you down :)) Rick Rolled you")
            });

            Adresar punk = new Adresar(new List<IPrectitelne>(){
                new Adresar(
                    new List<IPrectitelne>(){
                        new Soubor("So am I still waiting, For this world to stop hating?"),
                        new Soubor("How can one little street swallow so many lives?")
                    }
                ),
                new Adresar(
                    new List<IPrectitelne>(){
                        new Soubor("The night will come, And rip away, Her wings of innocence through every word we say"),
                        new Soubor("The world I love, the tears I drop, To be part of the wave, can't stop")
                    }
                ),
            });

            Adresar hiphop = new Adresar(new List<IPrectitelne>(){
                new Soubor("When the pimp's in the crib ma, Drop it like it's hot")
            });

            Adresar hudba = new Adresar(new List<IPrectitelne>(){});
            hudba.pridejNovyUzel(metal);
            hudba.pridejNovyUzel(pop);
            hudba.pridejNovyUzel(punk);
            punk.pridejNovyUzel(new Soubor("Right now, Oh I am an anti-Christ"));
            hudba.pridejNovyUzel(hiphop);
            hudba.prectiObsah();
        }
    }

    interface IPrectitelne{
        void prectiObsah();
    }

    class Soubor:IPrectitelne{

        private string text;

        public Soubor(string text){
            this.text = text;
        }

        public void prectiObsah(){
            Console.WriteLine(this.text);
        }
    }

    class Adresar:IPrectitelne{

        List<IPrectitelne> potomci;

        public Adresar(List<IPrectitelne> potomci){
            this.potomci = potomci;
        }

        public void pridejNovyUzel(IPrectitelne potomek){
            this.potomci.Add(potomek);
        }

        public void smazExistujiciUzel(IPrectitelne potomek){
            this.potomci.Remove(potomek);
        }

        public void prectiObsah(){
            foreach(IPrectitelne potomek in potomci){
                potomek.prectiObsah();
            }
        }
    }
}