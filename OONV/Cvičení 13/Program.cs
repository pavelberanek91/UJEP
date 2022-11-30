using System;
using System.Collections.Generic;

namespace ws
{
    class Program
    {
        static void Main(string[] args)
        {
            RadicCisel radicCisel = new RadicCisel(new BubbleSort());

            int[] serazenaCisla = radicCisel.seradCisla(new int[]{1, 4, 2, 3, 5, 2, 3}, sestupne: false);
            Console.WriteLine("[{0}]", string.Join(", ", serazenaCisla));

            serazenaCisla = radicCisel.seradCisla(new int[]{1, 4, 2, 3, 5, 2, 3}, sestupne: true);
            Console.WriteLine("[{0}]", string.Join(", ", serazenaCisla));



            radicCisel = new RadicCisel(new QuickSort());
            
            serazenaCisla = radicCisel.seradCisla(new int[]{1, 4, 2, 3, 5, 2, 3}, sestupne: false);
            Console.WriteLine("[{0}]", string.Join(", ", serazenaCisla));

            serazenaCisla = radicCisel.seradCisla(new int[]{1, 4, 2, 3, 5, 2, 3}, sestupne: true);
            Console.WriteLine("[{0}]", string.Join(", ", serazenaCisla));



            radicCisel = new RadicCisel(new BogoSort());
            
            serazenaCisla = radicCisel.seradCisla(new int[]{1, 4, 2, 3, 5, 2, 3}, sestupne: false);
            Console.WriteLine("[{0}]", string.Join(", ", serazenaCisla));

            serazenaCisla = radicCisel.seradCisla(new int[]{1, 4, 2, 3, 5, 2, 3}, sestupne: true);
            Console.WriteLine("[{0}]", string.Join(", ", serazenaCisla));

        }
    } 

    interface IRadic{
        int[] vzestupneRazeni(int[] cisla);
        int[] sestupneRazeni(int[] cisla);
    }

    class RadicCisel{

        private IRadic strategieRazeni;

        public RadicCisel(IRadic strategieRazeni){
            this.strategieRazeni = strategieRazeni;
        }

        public void zvolAlgoritmus(IRadic strategieRazeni){
            this.strategieRazeni = strategieRazeni;
        }

        public int[] seradCisla(int[] cisla, bool sestupne){
            if (sestupne == true){
                return strategieRazeni.sestupneRazeni(cisla);
            } else{
                return strategieRazeni.vzestupneRazeni(cisla);
            }
        }
    }

    class BubbleSort: IRadic{

        public BubbleSort(){}

        public int[] sestupneRazeni(int[] cisla){
            int tmp = 0;
            for (int i = 0; i < cisla.Length; i++){
                for (int j = 0; j < cisla.Length-1-i; j++){
                    if (cisla[j] < cisla[j+1]){
                        tmp = cisla[j];
                        cisla[j] = cisla[j+1];
                        cisla[j+1] = tmp;
                    }
                }
            }
            return cisla;
        }

        public int[] vzestupneRazeni(int[] cisla){
            int tmp = 0;
            for (int i = 0; i < cisla.Length; i++){
                for (int j = 0; j < cisla.Length-1-i; j++){
                    if (cisla[j] > cisla[j+1]){
                        tmp = cisla[j];
                        cisla[j] = cisla[j+1];
                        cisla[j+1] = tmp;
                    }
                }
            }
            return cisla;
        }
    }

    class QuickSort: IRadic{

        public QuickSort(){}

        public int[] sestupneRazeni(int[] cisla){
             return sestupnyQuickSort(cisla, 0, cisla.Length - 1);
        }

        public int[] vzestupneRazeni(int[] cisla){
            return vzestupnyQuickSort(cisla, 0, cisla.Length - 1);
        }

        private int[] sestupnyQuickSort(int[] cisla, int levyIndex, int pravyIndex){
            int i = levyIndex;
            int j = pravyIndex;
            int pivot = cisla[levyIndex];
            
            while (i <= j){
        
                while (cisla[i] > pivot){
                    i++;
                }
        
                while (cisla[j] < pivot){
                    j--;
                }
        
                if (i <= j){
                    int temp = cisla[i];
                    cisla[i] = cisla[j];
                    cisla[j] = temp;
                    i++;
                    j--;
                }
            }
    
            if (levyIndex < j){
                sestupnyQuickSort(cisla, levyIndex, j);
            }
            if (i < pravyIndex){
                sestupnyQuickSort(cisla, i, pravyIndex);
            }
            
            return cisla;
        }

        private int[] vzestupnyQuickSort(int[] cisla, int levyIndex, int pravyIndex){
            int i = levyIndex;
            int j = pravyIndex;
            int pivot = cisla[levyIndex];
            
            while (i <= j){
        
                while (cisla[i] < pivot){
                    i++;
                }
        
                while (cisla[j] > pivot){
                    j--;
                }
        
                if (i <= j){
                    int temp = cisla[i];
                    cisla[i] = cisla[j];
                    cisla[j] = temp;
                    i++;
                    j--;
                }
            }
    
            if (levyIndex < j){
                vzestupnyQuickSort(cisla, levyIndex, j);
            }
            if (i < pravyIndex){
                vzestupnyQuickSort(cisla, i, pravyIndex);
            }
            
            return cisla;
        }
    }

    class BogoSort: IRadic{

        public BogoSort(){}

        public int[] sestupneRazeni(int[] cisla){
            List<int> bogoSeznam = new List<int>();
            foreach(int cislo in cisla){
                bogoSeznam.Add(cislo);
            }
            while (!jeSerazenoSestupne(bogoSeznam)){
                bogoSeznam = zamichej(bogoSeznam);
            }
            for(int i = 0; i < bogoSeznam.Count; i++){
                cisla[i] = bogoSeznam[i];
            }
            return cisla;
        }

        public int[] vzestupneRazeni(int[] cisla){
            List<int> bogoSeznam = new List<int>();
            foreach(int cislo in cisla){
                bogoSeznam.Add(cislo);
            }
            while (!jeSerazenoVzestupne(bogoSeznam)){
                bogoSeznam = zamichej(bogoSeznam);
            }
            for(int i = 0; i < bogoSeznam.Count; i++){
                cisla[i] = bogoSeznam[i];
            }
            return cisla;
        }

        private bool jeSerazenoVzestupne(List<int> bogoSeznam){
            for (int i = 0; i < bogoSeznam.Count - 1; i++){
                if (bogoSeznam[i] > bogoSeznam[i + 1]){
                    return false;
                }
            }
            return true;
        }

        private bool jeSerazenoSestupne(List<int> bogoSeznam){
            for (int i = 0; i < bogoSeznam.Count - 1; i++){
                if (bogoSeznam[i] < bogoSeznam[i + 1]){
                    return false;
                }
            }
            return true;
        }

        //michaci algoritmus zalozeny na metode Fisher-Yates.
        private List<int> zamichej(List<int> bogoSeznam){
            Random r = new Random();
            for (int n = bogoSeznam.Count - 1; n > 0; --n){
                int k = r.Next(n + 1);
                int temp = bogoSeznam[n];
                bogoSeznam[n] = bogoSeznam[k];
                bogoSeznam[k] = temp;
            }
            return bogoSeznam;
        }
    }
}