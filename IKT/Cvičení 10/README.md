# Informační a komunikační technologie

## Cvičení 10 - Vizualizace dat

### 10.1 Instalace softwaru gnuplot

#### Linux
```sudo apt-get install gnuplot```

#### MacOS


#### Windows


### 10.2 Jednoduché grafy

V GNUPlotu se grafy vykreslují příkazem plot. V manuálu je napsán seznam všech funkcí, které lze vykreslit.
```
plot sin(x)
```

GNUPlot umí vykreslit i 3D grafy pomocí funkce splot. 
```
splot sin(x*y/20)
```

Do jednoho grafu lze vykreslit i více funkcí a přiřadit jim název do legendy. Pro různé parametry funkcí lze použít i zkratky (t místo title)
```
plot sin(x) title 'sin(x)', tan(x) t 'tan(x)'
```

### 10.3 Externí data

Data jsou běžně uložena v externích souborech z počítačových simulací a to nejčastěji v tabulkové podobě (záznamy jsou řádky, sloupce jsou vlastnosti). Pomocí příkazu using lze vybrat, jaká data vůči sobě vykreslíme
```
set datafile commentschars "#%?"
plot 'pocasi.dat' using 1:2 title 'teplota' with lines, "pocasi.dat" u 1:3 t 'tlak' w linespoints
```

Pro grafy existuje spousty nastavení - název grafu a os, rozsah os, mřížka a dělení os, typ osy (linární/logaritmická) atd.
```
set title "Počasí" font "Helvetica, 20"
set xlabel "Čas [h]"
set ylabel "Teplota [°C]"
set xrange [0:24]
set yrange [5:30]
set grid
#set autoscale
set arrow from 0, 28 to 13, 28
#unset arrow
set label "max T" at 14, 28
#unset label
#set logscale
#set logscale y
#unset logscale
set xtics (0, 4, 8, 12, 16, 20, 24)
#set xtics auto
set mxtics 4
set mytics 2
```

### 10.4 Multi-plot

Pokud chceme do jednoho grafu vložit více podgrafů, můžeme využít příkaz multiplot. Příkazem size se nastaví, jak mají být podgrafy na osách děleny. Příkazem set origin se vybírá souřadnice podgrafu.
```
set multiplot
set size 1, 0.5
set origin 0.0, 0.0; plot sin(x)
set origin 0.0, 0.5; plot cos(x)
unset multiplot
```

Pro pochopení soustavy souřadné u podgrafů je vhodné si vykreslit 4 podgrafy.
```
set multiplot
set size 0.5, 0.5
set origin 0.0, 0.0; plot sin(x)
set origin 0.5, 0.0; plot cos(x)
set origin 0.0, 0.5; plot tan(x)
set origin 0.5, 0.5; plot 1/tan(x)
unset multiplot
```

### 10.5 Aproximace dat
Pro diskrétní data lze najít parametry funkce, která je aproximuje co nejlépe ve smyslu nejmenších čtverců. 
```
phi(x) = a*x**2 + b*x + c                       #aproximacni funkce
a = 0; b = 0; c = 0                             #puvodni nastrel koeficientu
fit phi(x) 'pocasi.dat' using 1:2 via a, b, c   #nalezení koeficientů aproximační funkce
```

Získané parametry funkce je možné využít pro vykreslení aproximační funkce vedle diskrétních dat. 
```
plot 'pocasi.dat' u 1:2 t 'f(x)' with points pointtype 7 pointsize 2, a*x**2 + b*x + c t 'phi(x)' lw 3 lt 8
```

### 10.6 Tabulkové výpočty
S daty ve sloupcích je možné zacházet obdobně jako v excelu a provádět na celém vektoru matematické transformace.
```
plot 'pocasi.dat' u (60*$1):($2 + 273.15)
```

### 10.7 Export grafu do souboru
Grafické rozhraní GNUPlotu umožňuje export dat do souboru. Síla GNUPlotu je právě v možnosti ovládat ho automatizovaně přes příkažovou řádku. Je tedy nutné exportovat obrazy grafů do souborů. 
```
set terminal png size 400, 300 font "Helvetica, 20"
#set terminal pdf
#set term windows   #windows
#set term aqua      #macOS
#set term x11       #linux
set output 'teplota.png'
#set output 'teplota.pdf'
set key top left
set xlabel "t [h]"
set yrange[0:35]
set ylabel "T [°C]"
set y2range[-5:5]
set y2label "odchylka"
set ytics 10
set y2tics 2
set mytics 4
set mxtics 2
set xtics nomirror
a = 0; b = 0; c = 0
phi(x) = a*x**2 + b*x + c
fit phi(x) 'pocasi.dat' u 1:2 via a, b, c 
plot 'pocasi.dat' u 1:2:(sqrt($2)) t 'T [°C]' w yerr axis x1y1, phi(x) t 'aproximace' axis x1y1, 'pocasi.dat' u 1:($2*9/5 + 32) t 'T [°F]' axis x1y2
```

### 10.8 Skripty
Sadu příkazů si můžeme uložit do skriptového souboru s příponou .p. Tyto soubory pak lze volit v gnuplotu příkazem load.
```
gnuplot> load "skript.p"
```

Dále je lze volat z příkazové řádky. Pokud potřebujeme, ať okno čeká na manuální shlédnutí, pak přidáme příznak -p.
```
gnuplot -p skript.p
```

Skripty mohou přejímat argumenty z příkazové řádky. Do příkazové řádky lze napsat název proměnné s hodnotou a pak ji uvnitř skriptu používat. Využití najdeme např. při rozhodování o typu terminálu. 
```
gnuplot -e "vystup='png'" -p skript.p
```
nebo dodání argumentu příkazové řádky s příznakem -c (ve skriptu bude mít první z nich název ARG0, druhá ARG1, atd.). Pro rovnost řetězců se musí použít eq, pro numerické hodnota se využívá relace =. Pozor prvním argument programu je proměnná ARG0, což vždy představuje název spouštěného skriptu.
```
gnuplot -p -c skript.p png
```

```
if (ARG1 eq "png"){
    set terminal png
    set output "data.png"
} else {
    set terminal x11
}
...
zbytek skriptu
...
```

Ve skriptech lze kromě podmínek používat i cykly, např.: pro vykreselní sady datových souborů.
```
plot for [i=1:50] "data".i.".dat" using 1:2 title "test".i
```
### 10.9 Roura

V předchozím cvičení jsme viděli, že je možné využít GNUPlot přes příkažovou řádku a volat jeho skripty s argumenty. Při zvolení terminálu s výstupním souborem se chová gnuplot jako systém, který reaguje na vstup výstupem. Vstup by mohl být klidně z jiného programu a výstup by mohl pokračovat taky do jiného programu. Můžeme tedy využít linuxovský koncept roury pro složité automatizované činnosti.

Příkladem může být datový soubor, který obsahuje velké množství dat. Za každý den se do souboru mohou ukládat hodnoty teploty z meteostatnice v hodinách. Za několik dnů bude obsahovat soubor velké množství řádků. My si chceme vizualizovat pouze poslední den. Můžeme k tomu využít základní linuxovské aplikace, jako například tail -n, který vybere ze souboru n posledních řádků. Ty mohou být vstupem do gnuplotu. Pokud je výstupem pdf soubor, můžeme ho rovnou otevřít v prohlížeči pdf souborů.

```
tail -24 pocasi3dny.dat | gnuplot -e "set terminal pdf; set output 'pocasi.pdf'; plot '<cat' u 1:2 t 'teplota' w lp tp 6" && xdg-open pocasi.pdf
```

Příkaz na otevření pdf se může ve vašem Linuxovém operačním systému lišit, proto vám tento příkaz nemusí fungovat. Roura | přesměrovává v Linuxu výstup programu vlevo dna vstup programu vpravo. Dva znaky ampersandu spouští novou aplikaci po ukončení předešlé. Ještě by bylo možné využít přesměrování výstupu programu pomocí symbolu > do nějakého datového souboru a ten poté vykreslit. Pokud nepracujete v Linuxu, tak daleko jednodušší pro vás bude zatím psát komplexnější gnuplotovské skripty. Avšak mějte na paměti, že kombinací GNU nástrojů Linuxu, shellových/batchových skritpů a GNUPlot skriptů je možné docílit vysokého stupně automatizace, která vám ušetří drahocené hodiny a i dny života.

## Domácí cvičení

### DÚ 10.1 Styly grafů
Gnuplotu je k dispozici velké množství typů grafů. Vyzkoušejte si vytvořit graf s těmito styly na vámi vytvořeném datovém souboru. Poznamenejte si, jaký typ grafu se hodí pro jaká data (pokud netušíte, tak dohledejte).

* lines
* points
* linespoints
* impulses
* dots
* steps
* fsteps
* histeps
* errorbars
* xerrorbars
* yerrorbars
* xyerrorbars
* boxes
* boxerrorbars
* boxxyerrorbars
* financebars
* candlesticks
* vector

### DÚ 10.2 Teplota v procentech
Vykreslete soubor pocasi.dat tak, aby na ose y byly hodnoty teploty v procentech z maximální teploty. Maximální teplota je 30 °C, pak této hodnotě odpovídá 100 %. Minimální teplota je 5 °C, pak této teplotě odpovídá 0 %. Teplota 17.5 °C je přesně v polovině mezi max a min teplotou, pak této hodnotě odpovídá 50 %. Použijte proto operace pro práci s tabulkou.

### DÚ 10.3 Vědecké grafy
V oblasti přírodních věd jsou velice důležité skalání a vektorová pole. Dobrým příkladem ze střední školy je intenzita elektrického pole, která se modeluje pomocí vektorového pole, a potenciál elektrického pole, který se modeluje jako skalární pole. Reálným příkladem může být pole, tvořené soustavu polárních molekul nebo náboje kolem drátu elektrického vedení. Pokud je zdrojem skalárního pole jeden zdroj (například úder blesku), pak lze skalární pole popsat soustavou ekvipotenciálních kružnic.

Váš úkol zní:
1. Spustťe program field_generator.py
2. Vizualizujte soubor "vec.dat" jako vektorové pole (googlete a experimentujte)
3. Vizualizujte soubor "scalar.dat" jako skalární pole (googlete a experimentujte, rada: pro začátek stačí vizualizovat jako obrázek s pixely)
4. Zkuste vhodnou vizualizací zjistit, jaký je smysl skalárních hodnot ve vygenerovaném souboru

Pokud budete potřebovat komplexní grafy, jako např.: vektorová mapa, kde jsou barvy vektorů odpovídají skalárním hodnotám pole a navíc jsou vektory ohraničené ekvipotenciálními plochy, tak GNUPlot tyto šikovné vizualizace zvládá. Velice kvalitní je i knihovna matplotlib pro programovací jazyk python.

### DÚ 10.4 Automatizovana tvorba GIFu
Přiložený program sum.py vygeneruje sadu 50 fotografií náhodného šumu s názvy sum01.dat az sum50.dat. Napište skript typu .sh nebo .bat, který:
1. spustí program sum,py
2. počká na vygenerování všech datových souborů sum01.dat až sum50.dat
3. spustí gnuplot skript, který vygeneruje ze všech datových souborů fotografie sum01.png až sum50.png
4. spusti program, který vytvoří z fotografií sum01.png až sum50.png animovaný gif

Můžete využít konceptu roury a předpřipraveného gnuplot skriptu.

### DÚ 10.5 Aproximace ceny bitcoinu
Přiložený soubor bitcoin_month.dat obsahuje časovou řadu s hodnotou ceny bitcoinu za jednotlivé měsíce v roce 2021. Soubor bitcoin_years.dat obsahuje časovou řadu s hodnotou ceny bitcoinu v jednotlivých letech. Nalezněte aproximační funkce a jejich koeficienty, která vhodně proloží tyto časovou řadu. Ověřte kvalitu aproximace vykreslením aproximační funkce s diskrétními daty do jednoho grafu. 
