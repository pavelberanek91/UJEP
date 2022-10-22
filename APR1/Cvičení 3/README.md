# Algoritmizace a programování

## Cvičení 3 - Opakování pomocí cyklů

### On-site

**OS3.3 - Manipulace s pixely**

For cyklus je ideálním cyklem pro procházení grafických dat. Obrázek je vlastně seznam řádků a každý řádek je seznam hodnot barev. Pro procházení takové struktury je potřeba využít dvojného cyklu. Vnější cyklus se v následujícím případě bude opakovat tolikrát, kolik má obrázek řádků. V řádku projdeme každý pixel, tedy budeme vnitřní cyklus opakovat tolikrát, kolik má obrázek sloupců. Počet řádku a sloupců zjistíme z velikosti obrázku. Abychom však dostali do paměti obrázek v podově schopné procházení bude nutné využít nějakou knihovnu. Takovou knihovnou může být např.: PIL. Následující kód vezme nahraný obrázek s názvem prase.jpeg a provede binarizace jeho pixelů, tedy na základě průměrné hodnoty z intenzit pixelů přebarví pixely na černou nebo bílou. Rozhodnutí o barvě závisí na práhové hodnotě (threshold).

```
import PIL #Python Image Library, Pillow

obrazek = PIL.Image.open("prase.jpeg")
sirka, vyska = obrazek.size

for y in range(vyska):
    for x in range(sirka):
        r, g, b = obrazek.getpixel( (x, y) )
        prumer = (r + g + b)//3 #    R        G       B
        if prumer > 170:
            obrazek.putpixel( (x, y), (255, 255, 255) )
        else:
            obrazek.putpixel( (x, y), (0, 0, 0) )

display(obrazek) #obrazek.show()

```

### Domácí cvičení

#### Cvičení 3.1

**Video týdne 1: Porovnání rychlosti cyklů**

V tomto cvičení jste se naučili provádět opakování příkazů pomocí cyklů. Otázkou tedy zůstává, jaký cyklus použít, pokud chci provést nějakou aritmeticko-logickou operaci nad kolekcí objektů (například sečti všechna čísla v kolekci). Odpovědí je: pokud můžete, nepoužívejte cyklus. Vysvětlení této odpovědi naleznete v tomto videu: [ZDE](https://www.youtube.com/watch?v=Qgevy75co8c)

**Video týdne 2: Příkaz Else na konci cyklu**

Python obsahuje možnost využít příkazu Else i na konci cyklu while a for. Jedná se o vlastnost jazyka, kterou sám tvůrce nemá v oblibě. Pojďte se podívat na detailní video o tom, jaký je mechanismus tohoto příkazu u cyklů. [ZDE](https://www.youtube.com/watch?v=6Im38sF-sjo)
