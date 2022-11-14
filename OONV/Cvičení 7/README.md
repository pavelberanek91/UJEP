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

Návrhový vzor abstract factory představuje typické rozšíření návrhového vzoru Factory method. S narůstajícím množstvím typů instancí, které je nutné vytvářet podle kontextu, by rostl počet Creatorů ve Factory method. Navíc některé Creatory mohou tvořit rodinu, kterou v návrhovém vzory Factory method vytvoříte maximálně podle podobného jména (CreatorHTMLForm, CreatorHTMLList, CreatorAndroidForm, CreatorAndroiList, atd.). Proto se Factory method s rostoucí komplexností přepíše do jiného návrhového vzoru jako je Prototype nebo právě Abstract factory.

Abstract factory slouží pro vytváření související rodiny objektů podle kontextu, nikoliv tedy jen jednoho objektu. Můžete vytvářet kolekci Android widgetů, kolekci HTML5 prvků, atd. V návrhovém vzoru se nachází tyto třídy:
1. Abstraktní továrna - rozhraní továrních metod (VytvořTlačítko, VytvořFormulář, VytvořSeznam, aj.)
2. Konkrétní továrny - implementují rozhraní abstraktní továrny, obsahují tedy implementace toho, jak vytvořit např. HTML5 tlačítko, Android tlačítko, aj.
3. Abstraktní produkt - rozhraní metod produktů, například OnClick pro tlačítko (ať už Android nebo HTML5), Select pro seznamy, aj.
4. Konkrétní produkty - obsahují implementaci metod z rozhraní pro produkty, tedy konkrétní chování produktu při zavolání této metody
5. Klientský kód - 

Více se dozvíte o návrhovém vzoru abstract factory [ZDE](https://refactoring.guru/design-patterns/abstract-factory) a [ZDE](https://www.dofactory.com/net/abstract-factory-design-pattern)

**Úkol**

1. Vytvořte abstraktní třídy pro všechny varianty produktu: BluePrintRevolver, BluePrintCombatRifle, BluePrintShotgun, BluePrintSniperRifle.
2. Abstraktní třídy budou obsahovat různé abstraktní metody, které jsou pro typ zbraně specifické, např.: Shoot, Reload, Melee, Zoom, AltShoot; a atributy: Ammunition, Attack, Durability, atd..
3. Vytvořte třídy pro konkrétní produkty, které implementují rozhraní abstraktních produktů a to třídy: Revolver, CombatRifle, Shotgun, SniperRifle. Tyto třídy budete muset udělat pro všechny značky zbraní (Dahl, Hyperion, Jacobs).
4. Implementujte metody pro tyto konkrétní produkty.
5. Vytvořte abstraktní továrnu s názvem GunFactory, která bude obsahovat tovární metody pro tvorbu všech typů abstraktních produktů (BluePrintRevoler, BluePrintCombatRifle, atd.).
6. Vytvořte konkrétní továrny: Dahl, Hyperion, Jacobs, které budou obsahovat implementace továrních metod z GunFactory
7. Nasimulujte případ, kdy klient (hráč) otevře truhlu a nalezne v ní nějakou ze zbraní (Revoler, CombatRifle, aj.) od dané značky (Dahl, Hyperion, aj.).
8. Značka je pevně daná a souvisí s tím, do jaké frakce hráč patří (Dahl, Hyperion, aj.), typ produktu (Revolver, CombatRifle, aj.) se vybírá náhodným generátorem.
9. Otestujte funkčnost továren.

**Řešení**

```
```
