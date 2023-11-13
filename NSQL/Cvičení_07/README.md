# NoSQL databázové systémy

## Cvičení 7 - Dokumentová databáze MongoDB

V tomto cvičení budete realizovat jednoduchou aplikaci, která využívá nejzákladnější příkazy MongoDB pro CRUD operace. Začnete s tutoriálem z W3Schools na základě kterého vytvoříte aplikaci podle zadání.

### Zadání

Pojedeme podle nejjednoduššího možného tutoriálu (tj. tutoriál z newbie websitu w3schools.com).
1. Nainstalujte si PyMongo: [ZDE](https://www.w3schools.com/python/python_mongodb_getstarted.asp)
2. Vytvořte v MongoDB první databázi: [ZDE](https://www.w3schools.com/python/python_mongodb_create_db.asp)
3. Vytvořte v MongoDB první kolekci: [ZDE](https://www.w3schools.com/python/python_mongodb_create_collection.asp)
4. Vložte do vytvořené kolekce první záznam: [ZDE](https://www.w3schools.com/python/python_mongodb_insert.asp)
5. Vložte do kolekce více záznamů a zkuste je vyhledat pomocí find_one() a find() metod: [ZDE](https://www.w3schools.com/python/python_mongodb_find.asp)
6. Vložte si do kolekce více záznamů a zkuste je filtrovat pomocí regulárních výrazů: [ZDE](https://www.w3schools.com/python/python_mongodb_query.asp)
7. Seřaďte záznamy: [ZDE](https://www.w3schools.com/python/python_mongodb_sort.asp)
8. Smažte některé záznamy: [ZDE](https://www.w3schools.com/python/python_mongodb_delete.asp)
9. Upravte některý záznam: [ZDE](https://www.w3schools.com/python/python_mongodb_update.asp)
10. Smažte celou kolekci: [ZDE](https://www.w3schools.com/python/python_mongodb_drop_collection.asp)

Teď jste připravení na pravé zadání k dnešnímu cvičení :).

Vytvořte aplikaci, která slouží jako receptář studentských receptů. Funkcionální požadavky:
1. Aplikace bude mít 3 stránky: Domů (popis, co je to za projekt), Recepty (vypsaný seznam všech receptů z MongoDB), PřidejRecept (formulář, kterým může zaslat kdokoliv recept do systému). Recept bude mít tři informace: jméno receptu, jméno zadavatele, popis receptu.
2. Naplňte MongoDB několika prvotníma receptama a vypište si je na stránce Recepty na obrazovku.
3. Zpracujte formulář a přidejte zadaný recept z formuláře do MongoDB. 
4. Navrhněte si webové API rozhraní pro komunikaci se serverem na všechny CRUD operace (Create, Read, Update, Delete). 
5. Create přidává recept přes API. Pokud recept s daným názvem od daného uživatele již existuje v MongoDB, tak nebude přidan.
6. Read vrátí recept podle zadaného jména a zadaného uživatele.
7. Update upraví existující recept podle zadaného jména a zadaného receptu, pokud uživatel dodal správné tajné heslo k příslušnému záznamu.
8. Delete smaže existující recept podle zadného jména a zadaného receptu, pokud uživatel dodal správné tajné heslo k příslušnému záznamu.

## Materiály k samostudiu

Modelování API je důležitou součástí dnešních vývojových procesů. Podívejte se na jazyk RAML a proveďte modelování vašeho API a zdokumentujte si ho: [ZDE](https://raml.org/)
