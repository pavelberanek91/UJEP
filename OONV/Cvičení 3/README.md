# Objektově-orientované návrhové vzory

## On-site cvičení 3 - dědičnost

### Cognitive apprenticeship

### Úkol OS3.1 Dědičnost:

Dědičnost je jedním ze tří základních pilířů objektově-orientovaného návrhu (zapouzdření, polymorfismus a dědičnost). Tento mechanismus umožňuje rozšiřování chování instancí tříd bezpečným způsobem. Princip spočívá ve vytvoření nějaké třídy (normální či už od prvotní myšlenky obecné). V určité fázi psaní kódu budu potřebovat doplňkové chování. To se zprostředkuje vytvořením potomka této obecnější třídy. Potomek obsahuje všechny atributy a metody rodiče a navíc vše, co do něj doimplementuji. V jazyce C# může mít potomek pouze jednoho rodiče. Pokud byste potřeboval po třídě různorodá chování, která nemají společného předka, pak můžete využít rozhraní z předchozí lekce.

**Zadání**

Naprogramujte třídu Postava, která má následující atributy:
1. Zásahové body
2. Útočné body
3. Obranné body

a následující metody:
1. Zaútoč
2. PřijmiZásah

Vytvořte primitivní implementace metod podle vašeho uvážení. Atributy postav můžete náhodně generovat nebo je dát na pevno.

**Řešení**

```
class Postava
{
    private int Hp {get; private set;} //Zásahové body
    private int Atk {get; private set;} //Útočné body
    private int Def {get; private set;} //obranné body

    public Postava(){
        Random random = new Random();
        this.Hp = random.next(10, 20);
        this.Atk = random.next(1, 3);
        this.Def = random.next(1, 3);
    }

    public void zautoc(Postava nepritel){
        Random random = new Random();
        poskozeni = random.next(0, this.Atk);
        nepritel.prijmiZasah(poskozeni);
    }

    public void prijmiZasah(int poskozeni){
        poskozeni = this.Def >= poskozeni? 0: poskozeni - this.Def;
        this.Hp -= poskozeni;
    }
}
```

### Úkol OS3.2 Tvorba potomků:

**Zadání**

Postava bude mít dva potomky:
1. Nepřítel
2. Hrdina

Dále vytvoře třídu Bitva, která obsahuje následující atributy:
1. Skupina hrdinů
2. Skupina nepřátel

Chování Bitvy je realizováno následujícími metodami:
1. Vylosuj náhodné Nepřátelé
2. Začni bitvu

Nechám na vás, zda budete i náhodně losovat partu hrdinů nebo nebo bude nějaká předpřipravená.

Třída nepřítel má navíc následující atribut:
1. Obsažené zkušeností body (po jeho porážce je získá hrdina, případně se přerozdělí mezi partu)

Chování nepřítele se liší od postavy v následujícím:
1. Při útoku se útočí na náhodného hrdinu (musí být živý)

Třída Hrdina bude mít navíc následující atributy:
1. Dovedností body (tzv. MP/AP, slouží pro aktivaci schopností jako kouzla, speciální útoky, aj.)
2. Úroveň postavy (tzv. Level, slouží pro ohodnocení síly postavy)
3. Dosažené zkušenostní body (tzv. EXP, slouží pro navyšování úrovně postavy při dosažení určité hodnoty)
4. Potřebné zkušenostní body (EXP body, při jejichž překročení se navýší úroveň postavy)
5. Seznam speciálních dovedností (seznam != datová struktura seznam, nechám to na vás)

Chování hrdiny se liší od postavy v následujícím:
1. Při útoku si vybírá, zda provede speciální útok/magii nebo obyčejný útok
2. Při speciálním útok se zobrazí seznam dovedností k dispozici s jejich cenou za provedení
3. Při útotku si postava vybírá na jakého nepřítele zaútočí


**Řešení**

```
using System.Collections;

class Hrdina: Postava
{
    public int Ap {get; private set;} //dovednostni body
    public int Lvl {get; private set;} //úroveň postavy
    public int Exp {get; private set;} //zkušenostní body
    public int NextLvlExp {get; private set;} //zkušenostní body pro další úroveň postavy

    public Dictionary<string, int> Dovednosti {get; private set;}

    public Hrdina(string jmeno):base(jmeno){
        Random random = new Random();
        this.Ap = random.Next(3, 10);
        this.Exp = 0;
        this.NextLvlExp = 10;
        this.Dovednosti = new Dictionary<string, int>(){
            {"Ohnivá koule", 2},
            {"Ledová sprcha", 3},
            {"Kyselinový déšť", 3}
        };
    }

    public override void zautoc(Postava nepritel){
        Random random = new Random();
        System.Console.WriteLine("1: Útok");
        int index_dovednosti = 2;
        int poskozeni = 0;
        foreach(KeyValuePair<string, int> dovednost in this.Dovednosti){
            System.Console.WriteLine("{0}: {1}({2} AP)", index_dovednosti, dovednost.Key, dovednost.Value);
            index_dovednosti++;
        }
        switch(System.Console.ReadLine()){
            case "1":
                poskozeni = random.Next(0, this.Atk);
                break;
            case "2":
                poskozeni = random.Next(5, this.Atk+5);
                break;
            case "3":
                poskozeni = random.Next(0, this.Atk+20);
                break;
            case "4":
                poskozeni = random.Next(10, this.Atk+10);
                break;
            default:
                System.Console.WriteLine("Zvolen neplatný útok");
                break;
        }
        nepritel.prijmiZasah(poskozeni);
    }
}
```

```
using System.Collections;

class Nepritel: Postava
{
    public int Exp {get; private set;} //zkušenostní body, které odevzdá hrdinům

    public Nepritel(string jmeno):base(jmeno){
        Random random = new Random();
        this.Exp = random.Next(1, 3);
    }

    public void zautoc(Hrdina hrdina){
        Random random = new Random();
        int poskozeni = random.Next(0, this.Atk);
        hrdina.prijmiZasah(poskozeni);
    }
}
```

```
class Bitva
{
    public List<Hrdina> Hrdinove {get; private set;}
    public List<Nepritel> Nepratele {get; private set;}
    public List<string> JmenaNepratel {get; private set;}

    public Bitva(){
        this.JmenaNepratel = new List<string>(){
            "Skřet", "Harpije", "Beránek", "Vlkodlak", "Upír"
        };
        this.Hrdinove = new List<Hrdina>(){
            new Hrdina("Geralt"),
            new Hrdina("Gandalf"),
            new Hrdina("Itachi"),
            new Hrdina("Noctis"),
        };
        this.Nepratele = this.vylosujNahodneNepratele();
    }

    public List<Nepritel> vylosujNahodneNepratele(){
        Random random = new Random();
        int pocetNepratel = random.Next(1, 5);
        List<Nepritel> nepratele = new List<Nepritel>();
        for (int inepritel = 1; inepritel <= pocetNepratel; inepritel++){
            nepratele.Add(new Nepritel(
                this.JmenaNepratel[random.Next(this.JmenaNepratel.Count)]
            ));
        }
        return nepratele;
    }

    public void zacniBitvu(){
        
        foreach(Hrdina hrdina in this.Hrdinove){
            if (this.Nepratele.Count > 0){
                System.Console.WriteLine("{0} (HP={1}): Na koho chceš zaútočit?", 
                    hrdina.Jmeno, hrdina.Hp);
                int index = 1;
                foreach(Nepritel nepritel in this.Nepratele){
                    System.Console.WriteLine("{0}: {1} (HP={2})", index, nepritel.Jmeno, nepritel.Hp);
                    index++;
                }
                System.Console.Write(">");
                index = Convert.ToInt32(Console.ReadLine());
                hrdina.zautoc(this.Nepratele[index-1]);
                if (this.Nepratele[index-1].Hp <= 0){
                    this.Nepratele.Remove(this.Nepratele[index-1]);
                }
            } else{
                System.Console.WriteLine("Nepřátelé byli poraženi.");
            }
        }

        foreach(Nepritel nepritel in this.Nepratele){
            Random random = new Random();
            int index_ublizeneho = random.Next(this.Hrdinove.Count);
            System.Console.WriteLine("{0} utoci na {1} (HP={2})", 
                nepritel.Jmeno, this.Hrdinove[index_ublizeneho].Jmeno, 
                this.Hrdinove[index_ublizeneho].Hp);
        }
    }
}
```

### Úkol OS3.3 Abstraktní třída:

Třída postava teď slouží pouze jako šablona. Přesto lze vytvořit instanci třídy Postava. To není zcela v pořádku. Řešením je udělat ze třídy tzv. abstraktní třídu. Abstraktní třídy obsahují dva typy metod:
1. Virtuální metoda - má implementaci a potomek ji dědí, může si ji však podle sebe přepsat
2. Abstraktní metoda - nemá implementaci a potom se zavazuje, že si ji implementuje

Abstraktní metoda slouží ke stejným účelům jako metody rozhraní. Potomek se zavazuje je implementovat, pokud chce být potomkem abstraktního rodiče.

**Zadání**

Udělejte z Postavy abstraktní třídu. Podle uvážení udělejte metodu zaútoč nebo přijmiZásah abstraktní nebo virtuální. Vyzkoušejte si, že nemůžete vytvořit instanci této třídy.

**Řešení**

```

```

### Úkol OS3.4 Potomci potomků:

**Zadání**

Pojďme ještě rozšířit Hrdinu. Vytvořte následující potomky:
1. Válečník
2. Lučištník
3. Klerik
4. Čaroděj

Dále rozšiřte třídu Nepřítel. Vytvořte si nějaké zajímavé potomky této třídy.

Podle vašeho uvážení implementujte jejich dovednosti a mechanismy útoků. Také nezapomeňte vhodně naložit s třídou Hrdina a Nepřitel.

**Řešení**

```

```

```

```


```

```


### Úkol OS3.5 Mechanismus tahového souboje:

**Zadání**

V této fázi stačí doprogramovat samotný tahový mechanismus soubojů. Party hrdinů a nepřátel by se měly postupně střídat v útocích. Budete muset doprogramovat textové rozhraní pro hraní hry (hráč rozhoduje co děla s danou postavou za akci, hráč čte informace o aktuálním stavu své party a party nepřátel). Doprogramujte tento mechanismus.

**Řešení**

```

```

```

```

## Domácí cvičení 3

### Úkol HW3.1 Výstroj:

Postavy vlastní výstroj - brnění, zbraň, amulet. Pokud parta hrdinů vyhraje souboj, tak je určitá pravděpodobnost, že nejakou výstroj získají a mohou si ji navolit. Tato výstroj ovlivňuje jejich atributy. Doprogramujte tento mechanismus.

### Úkol HW3.2 Inventář:

Kromě výstroje vlastní postavy ještě výbavu v tzv. inventáři. Může se jednat o různé elixíry, magické hůlky a jiné předměty. Inventář je omezený a stejné položky se hromadí na sebe. Tuto výbavu můžete během souboje používat. Doprogramujte tento mechanismus.

### Úkol HW3.3 Zlepšování postav:

Pokud postava vyhraju bitvu, tak získá zkušenostní body (buď všechny za zabitého nepřítele, nebo poměrnou část vůči zbytku party hrdinů). Pokud dosáhne určité hodnoty, tak se mu úroveň (LVL) zvedne a zlepší se mu atributy. Zkuste rozvést trošku fantazii a doprogramovat navíc i mechanismus zlepšování dovedností. Při dosažení určité úrovně postavy může postava získat novou dovednout nebo může existovat strom dovedností pro odemykání nových dovedností.

### Úkol HW3.4 Unity Engine:

Zkuste si vytvořenou textovou hru doprogramovat v enginu Unity a dejte ji nějakou vhodnou grafiku. Na internetu naleznete předpřipravená digitální aktiva (assets).

### Úkol HW3.5 Dungeon:

Pokud se vám povedl v Unity Enginu doprogramovat grafický systém soubojů, tak si doprogramujte i chození po nějakém levelu, kde má parta hrdinů nějaký úkol (například sesbírat všechny zlaťáky). Během chůze se může náhodně spustit boj s partou nepřátel. Nezapomeňte také přidat na mapu předměty jako léčivé lektvary nebo lepší vybavení. Hra by měla končit úspěchem nebo neúspěchem (game over screen).


**Video týdne: Programming languages iceberg**

V tomto videu získáte přehled o programovacích jazycích ve videoformátu známém jako icerberg. Začnete od těch nejznámějších jazyků až po ty nejvíce obskurní. Video naleznete [ZDE](https://www.youtube.com/watch?v=pEfrdAtAmqk).
