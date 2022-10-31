# Objektově-orientované návrhové vzory

## On-site cvičení 5 - UML diagramy

### Cognitive apprenticeship

Cílem dnešního cvičení je naučit se modelovat informační systémy pomocí grafické notace ve formě UML diagramů. Veškeré diagramy budeme modelovat ve webové aplikace draw.io: [ZDE](https://app.diagrams.net/).

### Úkol OS5.1 Diagramy případů užití (Use-case diagrams):

Diagram případů užití zachycuje v grafické podobě interakce třídy účastníků (běžný uživatel, admin, aj.) se službami systému. Jedná se o vysokoúrovňový pohled na systém a možnosti komunikace s ním. Používá se jako základní nástroj pro komunikaci se zainteresovanými stranami.

Na následujícím obrázku vidíte diagram případů užití pro interakce v restauraci:
<img src="https://upload.wikimedia.org/wikipedia/commons/7/7b/Restaurant_Model.png"/>

V levé části diagramu vidíte účastníky-klienty, který chtějí po systému službu. V právé části vidíte účastníky-poskytovatele služby, kteří poskytují klientům službu. Nejčastěji se jedná o nějaké algoritmy, ale mohou to být i skuteční lidé. Do oválů se píšou samotné případy použití, což jsou jednotlivé akce se systémem. Případy užití mohou zahrnovat jiné případy užití pro své úspěšné vykonání (relace include) nebo mohou být rozšířeny o jiné případy užití (extend).

Návod na tvorbu diagramů případů užití v draw.io naleznete [ZDE](https://drawio-app.com/uml-use-case-diagrams-with-draw-io/).

**Zadání**

Nakreslete diagram případů užití pro bankomat (ATM stroj). 

**Řešení**

```

```

### Úkol OS5.2 Sekvenční diagram:

Diagram případů užití ukazuje interakce klient se systémem. Pro zobrazení interakcí částí systému v čase je zapotřebí silnější nástroj. Takovým je právě sekvenční diagram. Diagramy sekvencí popisují jeden konkrétní proces, proto je nutné v reálném projektu vytvořit spousty takových diagramů. Diagramy se skládají z účastníků , kteří posílají zprávy dál do systému a získávají zpět hodnoty. Dále mohou obsahovat smyčky a podmínky.

Následující diagram ukazuje proces přihlašování do systému: <img src=https://i.pinimg.com/736x/2a/31/0f/2a310f8da6b3179e2c5edf3d16f2c83b.jpg>

V diagramu je vidět podmínka nazvaná alt - jaká sekvence interakcí se má provést, pokud je přihlášení úspěšné nebo neúspěšné.

Návod na tvorbu sekvečních diagramů v draw.io naleznete [ZDE](https://drawio-app.com/create-uml-sequence-diagrams-in-draw-io/)

**Zadání**

Nakreslete sekvenční diagram pro objednávku jídla na dámejídlo.cz.

**Řešení**

```

```

### Úkol OS5.3 Diagram aktivit:

**Zadání**

Diagram aktivit představuje vysokoúrovňový pohled na vnitřní chování systému na základě akcí, provedených uživatelem. Konkrétně popisuje entitu z procesního managementu zvanou workflow. Diagram se skládá z akcí workflow, které se provádí na základě výsledku rozhodování. Každý workflow má svůj začátek a konec a je možné ho větvit do paralelních činností. Oproti sekvenčnímu diagramu se více rozhoduje na interakci s uživatelem a možnostmi, kam směrovat výsledek procesu na základě podmínek (je to takový vylepšený flowchart). 

Na následujícím obrázku vidíte diagram aktivit pro objednání zboží na eshopu.

<img src="https://www.edrawsoft.com/templates/images/shopping-order-activity-diagram.png"/>

Návod na tvorbu diagramů aktivit v draw.io naleznete [ZDE](https://drawio-app.com/create-uml-activity-diagrams-in-draw-io/)

**Řešení**

Nakreslete diagram aktivit pro zápis předmětů v IS STAG.

```

```

### Úkol OS5.4 Diagram tříd:

**Zadání**

Diagram tříd je hlavním diagramem pro zobrazení struktury aplikace při využívání paradiagmatu objektově-orientovaného programování. Diagram tříd zobrazuje třídy z OOP včetně jejich atributů (vlastnosti, členské proměnné) a operací (metody). K atributům a operacím se uvádí i viditelnost (modifikátory přístupu). K názvu třídy, operací a atributů se dává příznak abstraktnosti nebo statičnosti třídy. Vztahy mezí třídami se zakreslují pomocí šipek a diamantů, kterými lze modelovat generalizaci (dědičnost) a agregaci (instance třídy v sobě obsahuje jinou instanci třídy se kterou komunikuje). Ke vztahům se často udává kardinalita nebo typ vztahu. Zde je krátký návod na notaci třídních diagramů: [ZDE](https://courses.cs.washington.edu/courses/cse403/11sp/lectures/lecture08-uml1.pdf)

Na následujícím obrázku můžete vidět diagram tříd k IS pro knihovníky.

<img src="https://images.edrawmax.com/images/knowledge/class-diagram-uml/example1.jpg"/>

Návod na tvorbu diagramů tříd v draw.io naleznete [ZDE](https://drawio-app.com/uml-class-diagrams-in-draw-io/)

**Řešení**

Nakreslete diagram tříd k vašemu vlastnímu konkurenčnímu systému k IS STAG.

```

```


## Domácí cvičení 5

### Úkol HW5.1 Lorem:

### Úkol HW5.2 Lorem:

### Úkol HW5.3 Lorem:

### Úkol HW5.4 Lorem:

### Úkol HW5.5 Lorem:


**Video týdne: Přehled návrhových vzorů**

Od příští lekce začneme již s implementací návrhových vzorů. V tomto videu uvidíte přehled 10 základních z nich. Kód je sice typescript, avšak myšlenka zůstává platná. Doporučuji udělat si zápisky o tom, kdy takový návrhový vzor použít a jeho hlavní myšlenku. [ZDE](https://www.youtube.com/watch?v=tv-_1er1mWI)
