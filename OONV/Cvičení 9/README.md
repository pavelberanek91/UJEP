# Objektově-orientované návrhové vzory

## Strukturální vzory - Proxy, Dekorátor

Strukturální vzory řeší problémy, které vycházejí ze struktury již vytvořených objektů, jejichž struktura nám za běhu nevyhovuje. Mezi první probírané patří:
1. Proxy - umožňuje nahradit jedne objekt jeho zástupným objektem
2. Dekorátor - umožňuje za běhu rozšiřovat chování objektu

Obě návrhové vzory nemění rozhraní, jen chování (adaptér měnil rozhraní). Dekorátor a Proxy vypadají na první pohled stejně z technického hlediska, ale liší se svým záměrem. Zatímco proxy upravuje chování objektu a není to v moci klienta, dekorátor je v moci klienta, jelikož vybírá nové upravené chování dekorováním objektu.

### Proxy

Klient chci využívat instanci nějaké třídy. Tato instance není optimální z hlediska svého chování. Příkladem může být situace, kde přístup k této instanci je náročný na prostředky (typicky přístup na pevný disk). Proto můžeme obalit chování této na prostředky náročné třídy Proxy třídou, která problém řeší aniž by se změnil způsob, jak se na prostředky náročná třída používá (nemění se rozhraní). Pro představu si vzpomeňte na oblíbenou NoSQL databázi typu klíč-hodnota s názvem Redis, která cachuje data z relačních databází.

Více o návrhovém vzoru proxy naleznete [ZDE](https://refactoring.guru/design-patterns/proxy) nebo [ZDE](https://www.dofactory.com/net/proxy-design-pattern).

**Cvičení**

Představte si, že často čtete data z CSV souborů, které jsou uložené na pevném disku. Tyto soubory mohou například obsahovat známky studentů:

```
Anička,4,1,2,3,5
Pepíček,5,5,1,1,2
František,1,1,2,1,1
```
Pokud pracujeme s třídou pro čtení této CSV "databáze" často, pak se vyplatí vytvořit kolem ní Proxy, která cachuje častá data. Naprogramujte následující:

1. Vytvořte rozhraní ČítačZnámek s metodou vypišZnámkuStudenta(string studentovoJméno).
2. Vytvořte třídu CSVČítačZnámek, který metodu implementuje. Když se metoda zavolá s jménem studenta, tak se z metody navrátí seznam jeho známek.
3. Vytvořte k ní proxy s názvem CSVedis (podoba s Redisem), která slouží jako cache databáze pro CSVČítačZnámek. Kdykoliv klient přes proxy CSVedis zavolá metodu vypišZnámkuStudenta, tak se databáze podívá, jestli známky studenta již nemá v sobě nacachované a vrátí nacachovaná data. Pokud ne, tak zavolá v sobě uloženou instanci CSVČítačZnámek a požádá ji o vyhledání dat, která následně vrátí a uloží si je do své cache struktury.
4. Pokud uběhne více jak 60 sekund od uložení, tak se data z cache databáze smažou.

Pokud byste měli problém úkol vyřešit, tak zde naleznete pro ukázku zajímavou úlohu na blokaci webových stránek [ZDE](https://www.geeksforgeeks.org/proxy-design-pattern/)

### Dekorátor


Více se o dekorátoru dočtete [ZDE](https://refactoring.guru/design-patterns/decorator) nebo [ZDE](https://www.dofactory.com/net/decorator-design-pattern).

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
