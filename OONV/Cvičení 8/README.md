# Objektově-orientované návrhové vzory

## Strukturální vzory - Adaptér, Fasáda

Strukturální vzory řeší problémy, které vycházejí ze struktury již vytvořených objektů, jejichž struktura nám za běhu nevyhovuje. Mezi první probírané patří:
1. Adaptér - umožňuje komunikaci dvou objektů, které mají nekompatibilní rozhraní
2. Fasáda - umožňuje snadněji používat objekt díky zjednodušenému rozhraní

### Adaptér

Nejjednodušší příklad pro vysvětlení adaptéru je problém s formátem datových zdrojů. Typickým příkladem je aplikace nebo knihovna, která na svém vstupu pracuje s XML soubory, avšak vaše data jsou z webové aplikace, která zasílá JSON soubory. Abyste nemuseli hledat jiné technologie, tak si vytvoříte adaptér, mezi dvěmi aplikacemi.

Více o návrhovém vzoru naleznete [ZDE](https://refactoring.guru/design-patterns/adapter) a [ZDE](https://www.dofactory.com/net/adapter-design-pattern).

**Cvičení**

Budete dělat adaptér mezi dvěma datovými zdroji: adaptér z XML na JSON. Datový zdroj bude vypadat následovně:

```
<menu>
  <nápoj>
    <název>Cuba Libre</název>
    <ingredience>
      <položka díly="2">Bílý rum</položka>
      <položka díly="1">Cola</položka>
    </ingredience>
  </nápoj>
  <nápoj>
    <název>Aperol Spritz</název>
    <ingredience>
      <položka díly="3">Proseco</položka>
      <položka díly="2">Aperol</položka>
      <položka díly="1">Soda</položka>
    </ingredience>
  </nápoj>
  <nápoj>
    <název>Blue Lagoon</název>
    <ingredience>
      <položka díly="1">Vodka</položka>
      <položka díly="1">Curacao</položka>
      <položka díly="4">Citrónová limonáda</položka>
    </ingredience>
  </nápoj>
</menu>
```

1. Vytvořte třídu DrinkViewer, která obsahuje metodu showDrink. Tato metoda přijímá jako parametr datový soubor ve formátu JSON a zobrazí ho jako HTML kód.
2. Vytvořte třídu DrinkDatabase, která ve svém konstruktoru přijme cestu ke XML souboru, kde je menu s recepty na drinky.
3. Třída DrinkDatabase obsahuje metodu showMenu, která chce využít metodu showDrink ze DrinkViewer pro zobrazení všech receptů ve své XML databázi. Bohužel, tyto metody nejsou konzistentní, jelikož showDrink vyžaduje data v JSON formátu.
4. Napište adaptér XMLtoJSONAdapter, který obsahuje metodu showDrink, která adaptuje kód tak, aby instance třídy mohly spolu komunikovat.

### Fasáda

Cílem návrhového vzoru fasáda je skrýt/zaobalit komplexitu závislostí instancí tříd na sobě do jedné třídy. Představme si například následující didaktický příklad z oblasti počítačové grafiky. Uživatel chcete vykreslit na obrazovku graf typu histogram. Vstup mají být data ze souboru a výstupem má být graf na obrazovce. Tento graf si vytváří uživatel svépomocí pomocí geometrických útvarů. Vytvoření takového grafu bude zahrnovat přečtení dat ze souboru, rozklíčování dat ve formě řetězce do popisků os (osa x) a kategorií (osa y), vykreslení plátna, vykreslení obdélníků na plátno, jejichž velikost závisí na načtených datech, vykreslení šipek jako os, dodání ticků a popisků osy, atd. Tyto grafické prvky jsou na sebe v určitém pořadí závislé. Přesto se celé volání dá shrnout jedním příkazem - vytvoř histogram. Tvořič histogramů bude fasáda.

Více se o fasádě dočtete [ZDE](https://refactoring.guru/design-patterns/facade) nebo [ZDE](https://www.dofactory.com/net/facade-design-pattern).

**Cvičení**

V tomto cvičení vytvoříte registrační systém do eshopu.
1. Vytvořte třídu Formulář, které požádá uživatele o zadání uživatelského jména a hesla.
2. Formulář si volá třídu ValidátorNeprázdnýchVstupů, který pro Formulář zjistí, zda jsou vstupy neprázdné. Pokud nejsou, tak Formulář požádá opět o zadaní dat.
3. Vytvořte třídu PřihlašovačDoDB, která zjistí, zda se uživatel s daným jméném a heslem nachází v databázi nebo ne.
4. Formulář předá data PřihlašovaciDoDB, který přihlásí uživatele, pokud se tam nachází uživatel.
4. Vytvořte třídu Registrovač, která umožní zaregistrovat nového uživatele se zadaným jménem a heslem do databáze.
5. Vytvořte třídu ZjišťovačSílyHesla, která zjistí, jak moc je silné zadané heslo.
6. Pokud PřihlašovačDoDB zjistí, že se uživatel se zadaným jménem a heslem nenachází v DB, tak zavolá Registrovač.
7. Registrovač se zeptá uživatele, zda se chce zaregistrovat do DB.
8. Pokud se chce uživatel zaregistrovat, tak registrovač zavolá ZjišťovačSílyHesla, který ověří, zda heslo je dostatečně silné, tento poznatek navrátí Registrovači.
9. Podle síly hesla Registrovač zavolá objekt třídy Databáze a zaregistruje uživatele nebo ho požádá o nové silnější heslo.
10. Vytvořte k této komplexní komunikaci různých objektů fasádu s názvem RegistračníSystém, který celou komunikaci obaluje.
