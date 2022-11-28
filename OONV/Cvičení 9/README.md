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

Dekorátor je třída, která rozšiřuje chování jiné třídy a nevyužívá k tomu genelizační struktury jako je dědičnost nebo agregaci/kompozici. Kód (klient) za běhu rozhodne, jaké chování navíc bude umět dekorovaná třída a to tím, že ji obalí dekorátory. Příkladem může být například marketingová aplikace, která slouží pro zasílání příspěvku nebo příběhů na všechny sociální sítě (Instagram, Tik-Tok, Facebook). Podmínkou je, aby základní aplikace pro sociální sítě byla nainstalovaná nebo byla nakonfigurovaná. Takže chcete za běhu pro všechny dostupné aplikace pro správu sociálních sítí zaslat váš příspěvek, aniž byste chtěli vytvářet pro každý typ příspěvku potomka. Oproti předchozímu cvičení vidíme, že záleží spíše na klientovo straně ohledně toho, o jaké chování bude objekt rozšířen. U návrhového vzoru Proxy záleželo spíš na serverové straně.

Více se o dekorátoru dočtete [ZDE](https://refactoring.guru/design-patterns/decorator) nebo [ZDE](https://www.dofactory.com/net/decorator-design-pattern).

**Cvičení**

V tomto cvičení vytvoříte dekorátory pro zápis textového obsahu do více možných formátů.
1. Vytvořte třídu ZapisovačDoSouboru, která zapíše vložený text do souboru pomocí metody zapišText(string text, string cesta).
2. Vytvořte dekorátor HTMLZapisovač, který upravuje chování zapisovačů tím, že obalí jejich text do HTML značek a vygeneruje při zápisu validní HTML kód.
3. Vytvořte dekorátor LaTeXZapisovač, který upravuje chování zapisovačů tím, že obalí jejich text do LaTeX značek a vygeneruje při zápisu validní LaTeX kód.
4. Co se stane, když ve vašem případě obalíte ZapisovačDoSouboru oběma dekorátory? :)
