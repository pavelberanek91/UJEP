# Softwarové inženýrství

## Seminář 11 - Správa softwarových služeb

### Samostudium před seminářem

#### S11.1 - Servisně-orientované architektury

lorem ...


#### S11.2 - Inženýrství služeb

Doporučený doprovodný materiál: [ZDE](https://www.youtube.com/watch?v=GZvSYJDk-us)

**Aplikační programové rozhraní**

lorem

Služby jsou využivané klienty pomocí jejich aplikačního programového rozhraní (API). Pojďme si rozebrat trochu podrobněji tento důležitý termín. Rozhraní je prostor mezi dvěma systémy, v tomto případě mezi aplikací a klientem. Jedná se o komponentu systému, která umožňuje uživateli se systémem pracovat. Můžeme si to představit na příkladu rádia. Rozhraní jsou všechna tlačítka, posouvátka a jiné ovládací prvky, které umožňují klientovi rádio využívat. Rádio poskytuje službu pro poslouchání hudby. Klient vůbec nemusí vědět, jak rádio uvnitř funguje na základě nastavených posouvátek a tlačítek, aby mohl službu rádia využívat (i když znalost středoškolské fyziky z oblasti fyziky obvodů střídavého proudu vám to dokáží skvěle vysvětlit). Tvůrce rádia pomocí rozhraní udává možnosti klientovi pro použití rádia. Co není v rozhraní, tak není možné klientem využít, tedy pokud nevezme šroubovák a nerozebere rádio na tištěné spoje, což může být obdoba prolomení bezpečnosti webové aplikace. 

**Služby představují způsob uvažování**

Klient tedy závisí na abstrakci a nikoliv na konkrétnosti (pokud si pamatuje SOLID principy, tak se jedná o D = dependency inversion). Tato poučka bylo zmiňována v oblasti implementace softwaru, kde se o služby nejednalo. Z toho nám vyplývá, že s využitím pohledu volání služeb lze uvažovat i o vývoji každého systému, kde instance tříd obsahují své služby ve formě metod, které se volají přes rozhraní (interface/protokol). Textový procesor typu Word volá služby operačního systému (tzv. systémová volání) a žádá od něj služby typu ulož soubor na pevný disk. Samotná specifikace programovacího jazyka není vlastně nic jiného než soustava rozhraní, které mohou být na různých operačních systémech různě implementovány a programátor to nepozná. Rozhraní v programování tedy slouží pro vytvoření závazku implementace (pokud třída implementuje rozhraní, tak se zavazuje o implementaci kódu metod rozhraní) a vytvoření abstrakce nad implementací (objekt volá služby=metody jiného objektu přes veřejné rozhraní). Ve zbytku této kapitoly se budeme bavit pouze o webových službách, tedy službách, kde klientské zařízení svým programem volá službu serveru pomocí jeho API (podobně jako když ovládáte televizi dálkovým ovladačem).


#### S11.3 - Vývoj software založeném na službách

#### S11.4 - RESTful aplikace

#### S11.5 - Správa a spolehlivost služeb

### On-site cvičení

#### C11.1 - Vývoj aplikace využívající služby

#### C11.2 - Návrh služby

#### C11.3 - REST aplikace pomocí FastAPI

#### C11.4 - CRUD operace

#### C11.5 - Dokumentace rozhraní služeb