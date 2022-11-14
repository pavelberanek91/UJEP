# Objektově-orientované návrhové vzory

## Cvičení 7 - Tvořící vzory

### Factory method

Návrhový vzor Factory method se používá v případech, kdy potřebujete pracovat jednotným způsobem s objektem, ale jeho vnitřní implementace se může měnit podle kontextu. Kontextem je například typ operačního systému, způsob zobrazení výstupu aplikace (web, nativní GUI, tabulkový kalkulátor) a nastavení uživatele. Typicky se načítá kontext z nějakého config souboru. Podle kontextu vygeneruje tovární třída tovární metodou instanci potřebné třídy (web, gui, kalkulátor) a vy ji používáte přes tovární třídu. Abyste mohli používat takovou instanci univerzálně, musí třídy těchto instanci implementovat jednotné rozhraní. Ve factory method se tedy setkáte se 4 typy tříd:
1. jednotné rozhraní pro společné operace
2. třídy, které jednotné rozhraní implementují a klient nebo jiná třída je využívá
3. tovární třída, která instance využívá a obsahuje tovární metodu (ta může být abstraktní nebo může defaultně obsahovat kód pro tvorbu instance)
4. tvořiče instancí, které si přepisují tovární metodu - důvodem může být unikátnost tvorby instance díky různým nastavením

Více se dozvíte o návrhovém vzoru factory method [ZDE](https://refactoring.guru/design-patterns/factory-method) a [ZDE](https://www.dofactory.com/net/factory-method-design-pattern) 

**Úkol**

1. Vytvořte rozhraní jednotné rozhraní IDatabase.
2. Rozhraní bude obsahovat předpis pro základní databázové operace - tzv. CRUD operace (Create, Read, Update, Delete). Všechny pracují nad jednou tabulkou.
3. Create má dva parametry - ID záznamu a hodnota. U Postgres bude ID záznamu číslo řádku, u redis to bude název proměnné a u mongo to bude ID dokumentu.
4. Read má jeden parametry - ID záznamu.
5. Update má dva parametry - ID záznamu a nová hodnota.
6. Delete má jeden parametry - ID záznamu
7. Vytvořte 3 třídy, které rozhraní implementují - Postgres, Redis, MongoDB.
8. Implementujte operace (stačí nasimulovat jednoduchým consolovým výpisem do standardního výstupu, jak by vypadal příslušný query). Kdo si to chce implementovat i technicky, tak samozřejmě může.
9. Vytvořte třídu tovární třídu DatabaseCreator.
10. DatabaseCreator si ve svém konstruktoru přečtě nastavenou DB ze souboru db.config (nechám na vás strukturu souboru).
11. DatabaseCreator má tovární metodu CreateDatabase, která může, ale nemusí mít implicitní implementaci (když config soubor neexistuje).
12. Vytvořte třídy PostgreCreator, RedisCreator a MongoCreator, které jsou potomci DatabaseCreator a přepíšou jeho metodu CreateDatabase
13. Metoda CreateDatabase vytvoří instance databáze podle příslušného controlleru (musíte mít nainstalován balíček) a připojí se connection stringem do databáze. Stačí to nasimulovat výpisem na standardní řádek, jak by připojení vypadalo.
14. Klient (třída main) vytvoří instanci továrny DatabaseCreator, která podle config souboru nastaví atribut db na třídu, jejíž instance má tvořit při volání žádosti klienta o tvorbu databáze.
15. Otestujte, že lze volat CRUD operace na vrácené databáze z továrny.

**Řešení**

```
```

### Abstract factory

Návrhový vzor prototype se používá v případech, kdy potřebujete vytvořit kopii instance třídy. Problém spočívá v tom, že instance třídy mají některé atributy a metody privátní. Svět kolem je zná jen díky jejich veřejnému rozhraní (veřejné metody, metody z rozhraní interface, veřejné proměnné a gettery a settery). Mnoho atributů vám může být skryto při vytváření kopie instance. Řešením je vytvořit rozhraní s metodou clone, kterou si musí klonovatelné třídy implementovat. Jelikož klonování probíhá uvnitř třídy, pak jsou jim známé i privátní atributy.

Více se dozvíte o návrhovém vzoru abstract factory [ZDE](https://refactoring.guru/design-patterns/abstract-factory) a [ZDE](https://www.dofactory.com/net/abstract-factory-design-pattern)

**Úkol**

1. Vytvořte třídu Nepřítel.
2. Třída bude obsahovat následující privátní atributy: druh, HP, MP, Attack, Defense, poziceX, poziceY.
3. Třída bude obsahovat metodu PohniSe (pokud chcete další, tak můžete podle libosti)
4. Privátní atributy budou odkryty veřejnosti pomocí getterů a setterů
5. Vytvořte rozhraní ICLoneable s metodou clone. 
6. Třída Nepřítel bude toto rozhraní implementovat.
7. Napište implementaci metody clone.
8. Vytvořte instanci třídy Nepřítel s nějakými atributy pro parametry konstruktoru.
9. Vytvořte kopii této třídy.
10. Pohněte se s oběmi instancemi a zkontrolujte, že mají tytéž informace a rozdílné poziceX a Y.

**Řešení**

```
```
