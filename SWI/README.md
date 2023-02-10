# Softwarové inženýrství

## 1. Informace o předmětu

Cílem předmětu je seznámit studenty s dílčími aktivitami procesu vývoje softwaru a užitečnými nástroji, které mohou na různých pozicích v procesu vývoje využít. Předmět zahrnuje vybrané partie softwarového inženýrství tak, aby pokrývaly všechny základní fáze tvorby softwaru. Některé aspekty softwarového inženýrství spojené s fází implementace, testováním a tvorby dokumentace jsou navíc zahrnuty i v předmětu Objektově orientovaný návrh. Důraz je kladen na praktické využití existujících nástrojů a na praktické znalosti a poznatky zprostředkovávané odborníky z praxe.

## 2. Informace o seminářích

Semináře jsou vedeny částečně samostatnou prací studentů na úkolech ze zadání na tomto repozitáři a částečně výkladem teoretických poznatků. Cvičící slouží jako mentor během hodin: pomáhá s vysvětlováním problematiky, hledá chyby v případě "záseku" studenta a radí, jak nejlépe cvičení vyřešit, vysvětluje problematické teoretické partie a dává příklady ze své praktické zkušenosti. Odpovědnost za učení je převážně na studentovi. Teorii potřebnou na cvičení získá z materiálů, které jsou ke každé lekci uvedené v tabulce sylabus seminářů. Student si musí tyto materiály před samotným seminářem projít, aby semináři rozuměl.

Cvičí:
1. [doc. RNDr. Viktor Maškov, DrSc.](https://ki.ujep.cz/cs/personalni-slozeni/viktor-maskov/)
2. Petr Hřebejk, Ph.D
3. [Ing. Mgr. Pavel Beránek, MBA, LL.M.](https://ki.ujep.cz/cs/personalni-slozeni/pavel-beranek/)

## 3. Sylabus seminářů

Tento obsah odpovídá mé představě o kurzu, kdybych ho vyučoval v celé míře. Mnou nevyučovaná témata se mohou značně lišit obsahem a formou výuky. Materiály přesto můžete použít k přípravě na zkoušku a svou budoucí kariéru.

<table>
    <thead>
        <tr>
            <th>Týden</th><th>Téma</th><th>Materiály</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td><td>Proces vývoje softwaru</td><td><a href="./sem1/README.md">Seminář 1</a></td>
        </tr>
        <tr>
            <td>2</td><td>Inženýrství požadavků</td><td>[Sem2]()</td>
        </tr>
        <tr>
            <td>3</td><td>Návrh architektury</td><td>[Sem3]()</td>
        </tr>
        <tr>
            <td>4</td><td>Proces implementace</td><td>[Sem4]()</td>
        </tr>
        <tr>
            <td>5</td><td>Verzování softwaru</td><td>[Sem5]()</td>
        </tr>
        <tr>
            <td>6</td><td>Systémy pro správu verzí</td><td>[Sem6]()</td>
        </tr>
        <tr>
            <td>7</td><td>DevOps</td><td>[Sem7]()</td>
        </tr>
        <tr>
            <td>8</td><td>Verifikace softwaru</td><td>[Sem8]()</td>
        </tr>
        <tr>
            <td>9</td><td>Validace požadavků</td><td>[Sem9]()</td>
        </tr>
        <tr>
            <td>10</td><td>Evoluce softwaru</td><td>[Sem10]()</td>
        </tr>
        <tr>
            <td>11</td><td>Správa softwarových služeb</td><td>[Sem11]()</td>
        </tr>
        <tr>
            <td>12</td><td>Nasazení a správa softwaru</td><td>[Sem12]()</td>
        </tr>
        <tr>
            <td>13</td><td>Správa softwarových projektů</td><td>[Sem14]()</td>
        </tr>
    </tbody>
</table>

## 4. Podmínky získání zápočtu

Podmínkou získání zápočtu je vypracování praktické úlohy v nástroji Git. Bližší informace budou sděleny cvičícím na semináře o verzování softwaru.

## 5. Zkouška

Zkouška je formou klasifikované seminární práce v oblasti softwarového inženýrství a diskuze nad ní. Práce je vypracována ve skupinkách po třech studentech (počet se může změnit podle počtu návštěvníků kurzu). Cílem práce vytvořit jednoduchou REST API aplikaci, která bude uložena v kontejneru a připravena pro nasazení. Kódová báze bude splňovat zásady dobré implementace kódu a bude řádně otestována automatizovanými testy. Téma aplikace je zcela na studentovi, jelikož nejde prioritně o samotný kód, jako spíš o proces.

Skupina studentů odevzdá následující:
1. obraz softwaru připraven pro nasazení (ideálně docker obraz na docker hubu)
2. odkaz na git repozitář (github, gitlab), kde bude řádně vyplněný README file
3. dokumentace API (například swagger)
4. text seminární práce v PDF

Text seminární práce bude obsahovat:
1. Úvodní stránku a jiné formální náležitosti seminární prácí (obsah, zdroje, atd.)
2. Popis řešitelského týmu - dosavadní zkušenosti a odpovědnost ve vyvíjeném projektu
3. Popis softwaru - k čemu slouží a jaké problémy uživatelů řeší
4. Popis procesu vývoje softwaru a jeho konkrétní nastavení (jaké techniky, jak dlouho trvaly iterace)
5. Seznam funkčních a mimofunkčních požadavků (můžete přiložit i vybrané user-stories)
6. UML diagramy popisující architekturu softwaru
7. Popis implementovaných služeb
8. Vybrané důležité partie kódu a jejich vysvětlení
9. Návod k nasazení a co je nutné monitorovat?
10. Budoucnost softwaru - jak bude probíhat evoluce, jaké technologické problémy mohou nastat v budoucnu?

Seminární práce nemá být dlouhá. Měla by být stručná a jasná. Mělo by z ní být poznat, že jste ovládli proces vývoje softwaru.

Diskuze bude provedena nad následujícími tématy:
1. Jak vypadala vaše metodika vývoje softwaru?
2. Jaké nástroje jste využili během jednotlivých fází vývoje softwaru?
3. Jaké strategie kolaborace jste měli pro efektivní verzování softwaru?
4. Jak nasadit a monitorovat vaši aplikaci na server? Má nějaká omezení?
5. Jaké problémy během vývoje nastaly a jak jste je vyřešili?

Seminární práce a nad ní provedená diskuze se hodnotí následujím kritériem:
* výborně (1) = text seminární práce byl kvalitní, neobsahoval pravopisné a typografické chyby, odpovědi v diskuzi byly věcné, student prokázal ovládnutí všech partií procesu SWI
* velmi dobře (2) = text seminární práce měl vady ve formě nižší kvality, pravopisných a typografických chyb, v diskuzi student neodpovídal věcně a nebyl zřejmé, že ovládl všechny partie SWI
* dobře (3) = text seminární práce měl značné množství vad nebo neobsahoval všechny některé požadované partie, v diskuzi student odpovídal váhavě nebo špatně, avšak stále si z kurzu odnesl alespoň znalosti z některých partií a bude schopen se do praxe doučit
* nevyhověl (4) = seminární práce nebyl odevzdaná nebo student nedokázal při diskuzi prokázat, že by za celý semestr získal nějaké znalosti o procesu SWI

## 6. Doporučená literatura

Základní: Bruckner, T., Voříšek, J., Buchalcevová, A., Stanovská I., Chlapek, D., Řepa, V. Tvorba informačních systémů: principy, metodiky, architektury. Praha: Grada Publishing, 2012. ISBN 978-80-247-7902-7.

Základní: Vondrák, I. Úvod do softwarového inženýrství [online]. Ostrava: VŠB-TUO, 2002..

Základní: Monson- Haefel, R. 97 klíčových znalostí softwarového architekta: [zkušenosti expertů z praxe]. Brno: Computer Press, 2010. Zkušenosti expertů z praxe. ISBN 978-80-251-3313-2.

Doporučená: Cha, S., Taylor, R.N., Kang, K., ed. Handbook of Software Engineering. Cham: Springer International Publishing, 2019. ISBN 978-3-030-00261-9.

Doporučená: Chacon, S. Pro Git. Praha: CZ.NIC, z.s.p.o., 2009. CZ.NIC. ISBN 978-80-904248-1-4..

Doporučená: Sommerville, I. Softwarové inženýrství. Brno: Computer Press, 2013. ISBN 978-80-251-3826-7.

## 7. Kombinované studium

Pro kombinované studium platí stejné podmínky jako pro prezenční. V případě nízkého počtu studentů bude klasifikovaný zápočet ve formě přípravy softwaru pro nasazení nahrazen teoretičtější prací na vybrané téma softwarového inženýrství (nové trendy, výsledky výzkumu, aj.).

Studium je naplánováno do dvou setkání o délce 4 hodin.

<table>
    <thead>
        <tr>
            <th>Setkání číslo</th><th>Počet hodin</th><th>Téma</th><th>Přednášející</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td><td>2</td><td>Proces vývoje softwaru, návrh architektury softwaru</td><td>Berának Pavel</td>
        </tr>
        <tr>
            <td>1</td><td>2</td><td>Verzování softwaru</td><td>Hřebejk Petr</td>
        </tr>
        <tr>
            <td>2</td><td>2</td><td>Návrh služeb</td><td>Hřebejk Petr, Beránek Pavel</td>
        </tr>
        <tr>
            <td>2</td><td>2</td><td>Testování a spolehlivost softwaru</td><td>Maškov Viktor</td>
        </tr>
    </tbody>
</table>
