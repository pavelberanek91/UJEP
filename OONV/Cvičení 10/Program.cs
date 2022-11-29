using System;
using System.Collections.Generic;
using System.IO;

namespace ws
{
    class Program
    {
        static void Main(string[] args)
        {
            Projektil sniperProjektil = new Projektil(
                cestaTextura: "textura.jpg",
                poskozeni: 10, 
                sanceKritickyZasah: 0.2f
            );

            Projektil brokovniceProjektil = new Projektil(
                cestaTextura: "brokovniceTextura.jpg",
                poskozeni: 5,
                sanceKritickyZasah: 0.1f
            );

            List<PohybujiciSeProjektil> projektilySniperGun = new List<PohybujiciSeProjektil>();
            for(int i = 0; i < 1000; i++){
                projektilySniperGun.Add(
                    new PohybujiciSeProjektil(
                        poloha: new float[]{0.0f, 0.0f, 0.0f}, 
                        rychlost: new float[]{0.0f, 0.0f, 0.0f}, 
                        projektil: sniperProjektil
                    )
                );        
            }

            List<PohybujiciSeProjektil> projektilyBrokovnice = new List<PohybujiciSeProjektil>();
            for(int i = 0; i < 1000; i++){
                projektilyBrokovnice.Add(
                    new PohybujiciSeProjektil(
                        poloha: new float[]{0.0f, 0.0f, 0.0f}, 
                        rychlost: new float[]{0.0f, 0.0f, 0.0f}, 
                        projektil: brokovniceProjektil
                    )
                );        
            }
        }
    }

    class PohybujiciSeProjektil{

        float[] poloha;
        float[] rychlost;
        Projektil projektil;

        public PohybujiciSeProjektil(float[] poloha, float[] rychlost, Projektil projektil){
            this.poloha = poloha;
            this.rychlost = rychlost;
            this.projektil = projektil;
        }

        public void inkrementacePohybu(float casovyKrok){
            for(int idim = 0; idim < 3; idim++){
                poloha[idim] += rychlost[idim]*casovyKrok;
            }
        }
    }

    class Projektil{

        public string cestaTextura;
        public int poskozeni;
        public float sanceKritickyZasah;

        public Projektil(string cestaTextura, int poskozeni, float sanceKritickyZasah){
            this.cestaTextura = cestaTextura;
            this.poskozeni = poskozeni;
            this.sanceKritickyZasah = sanceKritickyZasah;
        }
    }
}