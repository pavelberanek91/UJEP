# Dependabilita informačních systémů

## Cvičení 1 - Samokontrola a samodiagnostika na systémové úrovni

### On-site cvičení

**1.1 Dependabilita**

Základním pojmem v našem světě je informační systém. Systém je ohraničený kus reality (má své dílčí části-komponenty a vztahy mezi komponenty), o kterém se můžeme bavit, studovat ho, používat ho. Informační systém je takový systém, který pracuje s informacemi. Informace jsou jsoucna (něco existujícího, viz fyzika), co snižuje naší nejistotu o světě (měříme entropií). 

Př.1: Nevím, kdy mi jede autobus na UJEP, tak se podívám na dopravní informační systém idos.

Př.2: Netuším, zda se mám obávat konkurenčního eshopu. Podívám se do svého manažerského reportního systému a na základě dat z grafů zjístím potřebné informace pro rozhodnutí o obavách.

Každý informační systém poskytuje jejich uživatelům (lidé, zvířata, příroda) nějaké informační služby (zkrátíme na služby, jelikož i objednání zboží na eshopu lze s trochou mentální gymnastiky převést na snižování entropie).

Co je tedy dependabilita informačních systémů?

Definice 1: *Dependabilita je schopnost výpočetního systému poskytovat službu "na niž se lze spolehnout"*

Tato definice není příliš vhodná kvůli své vágnosti (nejasnosti). Pojďme se podívat na komplexnější definici.

Definice 2: *Dependabilita je schopnost systému vyhnout se takovým selháním, jejichž četnost výskytu a závažnost by byla větší než přípustná úroveň pro uživatele.*

Much better :)

**1.2 Fasety dependability**

Dependabilita je podle zmíněné definice komplexní pojem, který v sobě zahrnuje vícero atributů (vlastností) systému. Tyto atributy se často zobrazují jako fasety (face, stěny) drahokamu. Rozdělujeme je na primární (=základní/nedělitelné) a sekundární (=odvozené/složené).

Mezi primární fasety dependability řadíme:
1. Dostupnost (availability) - pohotovost k poskytnutí služby
2. Spolehlivost (reliability) - kontinuita poskytování služby
3. Zabezpečení (safety) - absence katastrofických následků
4. Důvěrnost (confidentility) - absence neautorizovaného poskytnutí informací
5. Integritu (integrity) - absence nevhodných změn stavu
6. Udržovatelnost (maintainability) - schopnost podstoupit opravy a úpravy

Mezi sekundární fasety dependability řadíme (jen příklady, je jich spousty):
1. Zodpovědnost (responsibility) - dostupnost + integrita totožnosti osoby provádějící službu
2. Originalita (originality) - integrita obsahu služby a metadat
3. Nepopíratelnost (undeniability) - dostupnost + integrita totožnosti odesílatele/příjemce
4. Bezpečnost (security) - absence neopravnáněného přístupu ke službě
5. Robustnost (robustness) - odolnost služby proti chybným vstupním datům
6. ... a mnoho dalších

**1.3 Řetězec závada-chyba-selhání**

Podle definice v odstavci článku 1.1 je dependabilita míra vyhnutí se selháním. Co je tedy to selhání?

Selhání (failure) je stav systému, který vznikl šířením chyby až k rozhraní služby a tento stav je pro uživatele neakceptovatelný. Tzn. v systému může vzniknout spousty chyb. Některé uživatel vůbec nepocítí, jelikož se nedostanou k rozhraní služby (to, přes co službu používáme a vidíme výsledky - např.: webová stránka s objednávkovým formulářem), takové nezpůsobí selháná. Některé se dostanou k rozhraní, ale jsou pro nás akceptovalné (na displeji telefonu je text rozházený kvůli špatně nastaveným kaskádovým stylům). Selhání je tedy takový stav vzniklý díky chybám, který pociťujeme a vadí nám natolik, že to neakceptujeme (budeme nadávat, vyhodíme zaměstance, neobjednáme si na eshopu, apod.). Teď zbývá si vysvětlit pojem chyba.

Chyba (error) je stav systému, který může vést k selhání. Zde je nutné si poprvé vysvětlit, co je stav systému. Stavem se například v termodynamickém systému myslí hodnoty termodynamických veličin. To je tlak, teplota, objem, počet částic, atd. Když popíšeme nějaký systém pomocí termodynamických veličin, tak jsme schopni usuzovat budoucí stav. Například pomocí rovnic izodějů, jak moc se nafoukne nafukovací lehátko na sluníčku. V informačních systémech bude stav také realizován hodnotami veličin. Veličiny jsou reprezentovány proměnnými. Takže stav systému bude u nás kolekce hodnot proměnných. Takže chyba jsou proměnné se špatnou hodnotou. Ty mohou vyvolat selhání (hodně špatný stav) nebo nemusí. Tyto chybné hodnoty vyvolá událost (úkon v čase), které říkáme závada.

Závada (fault) je událost, která způsobuje chyby, tedy špatně nastaví proměnné. Špatné nastavení proměnných může vyvolat v následném čase i další závadu. Př.: pokud je chybě načten věk z občanky do automatizovaného terminálu na pivo na nějaké exkurzi, tak místo věku 15 se načte do proměnné věk hodnota 19. Špatné načtení byla závada, chyba je špatná hodnota v proměnné věk. Následně automat může načepovat pivo studentovi, i když by neměl. To je také závada, jelikož čepování je událost. Nezletilý student to samozřejmě nebude brát jako selhání, jelikož je se službou velice spokojen. Pedagogický dozor však nikoliv. Závady tedy mohou vytvářet kauzální (příčinná souvislost) řetězec závad, tedy jedna závada vyvolá jinou závadu. Takto můžete jít však značně zpátky v řetězci, například závada byla unavený programátor, jehož závadou bylo nízkokalorické jídlo nebo přesčasy díky tvrdému managementu, atd. Je tedy nutné se někdy zastavit a říct, že toto je naše prvotní závada.

Tyto tři termíny tedy vytváří kauzální řetězec závada -> chyba -> selhání.

**1.4 Závada**

Vědci zkoumali závady a došli k tomu, že existuje 8 typů elementárních závad, na které lze odpovědět binárně (pouze dvě možné odpovědi). Tyto elementární závady mohou vzniknout naráz a tvořit tak až 6544 různorodých kombinovaných závad, avšak jen 31 z nich má smysl zkoumat. Pojďme se podívat na elementární závady, které jsou vlastně atributy kombinovaných závad:

1. fáze vzniku (kdy?) - návrh nebo používání?
2. umístění vzhledem k hranicím (kde?) - uvnitř systému nebo vně systému?
3. fenomenologická příčina (jak?) - přirozeně nebo lidským zásahem?
4. dimenze (typ?) - hardware nebo software?
5. cíl (proč?) - zlomyslná nebo nezlomyslná?
6. úmysl (plán?) - promyšlená nebo nepromyšlená?
7. kapacita (vznik?) - nahodilá nebo důsledek nekompetence?
8. persistence (setrvání?) - trvalá nebo přechodná?

Závady mají ještě dva stavy:
1. aktivní - závada je aktivní a způsobuje chybný stav
2. latentní - závada existuje, ale spí (čeká na aktivizaci)

**1.5 Chyba**

**1.6 Selhání**

**1.7 Prostředky pro zvýšení odolnosti proti selhání**

**1.8 Kdo stráží stráže?**

**1.9 Samokontrola a samodiagnostika**

**1.10 Atomická kontrola AT**

**1.11 Modul (komponenta) M**

**1.12 Diagnostický graf DG**

**1.13 Syndrom R = {rij}**

**1.14 Vybrané metriky spolehlivosti a dependability**