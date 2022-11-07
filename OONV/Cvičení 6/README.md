# Objektově-orientované návrhové vzory

## Cvičení 6 - Tvořící vzory

### Singleton

Návrhový vzor singleton se používá v případech, kdy chcete zaručit, aby šlo vytvořit pouze jednu instanci dané třídy. Pokud někdo požádá o vytvoření nové instance této třídy, tak se mu vrátí již existující instance.

Více se dozvíte o návrhovém vzoru singleton [ZDE](https://refactoring.guru/design-patterns/singleton)

**Úkol**

1. Vytvořte třídu CSVDatabáze.
2. Třída bude obsahovat jeden atribut: cesta_k_csv_souboru.
3. Třída bude obsahovat vše potřebné pro to, aby byla technicky singletonem.
4. Vytvořte třídu Analytik, která umí zapsat a číst z CSV souboru (metody). 
5. V konstruktoru přiřaďte instancím třídy Analytik CSV soubor, do kterého bude zapisovat nebo z něj bude číst.
6. Vytvořte dvě instance Analytika a přiřaďte jim singleton CSV soubor.
7. Ověřte, že obě instance čtou a zapisují do stejného CSV souboru. Pokud byla cesta k CSV souboru změněna, bude změněna pro oba analytiky.

### Prototype

Návrhový vzor prototype se používá v případech, kdy potřebujete vytvořit kopii instance třídy. Problém spočívá v tom, že instance třídy mají některé atributy a metody privátní. Svět kolem je zná jen díky jejich veřejnému rozhraní (veřejné metody, metody z rozhraní interface, veřejné proměnné a gettery a settery). Mnoho atributů vám může být skryto při vytváření kopie instance. Řešením je vytvořit rozhraní s metodou clone, kterou si musí klonovatelné třídy implementovat. Jelikož klonování probíhá uvnitř třídy, pak jsou jim známé i privátní atributy.

Více se dozvíte o návrhovém vzoru prototype [ZDE](https://refactoring.guru/design-patterns/prototype)

**Úkol**

1. Vytvořte třídu Nepřítel.
2. Třída bude obsahovat následující privátní atributy: druh, HP, MP, Attack, Defense, poziceX, poziceY.
3. Třída bude obsahovat metodu PohniSe (pokud chcete další, tak můžete podle libosti)
4. Privátní atributy budou odkryty veřejnosti pomocí getterů a setterů
5. Vytvořte rozhraní ICLoneable s metodou clone. 
6. Třída Nepřítel bude toto rozhraní implementovat.
7. Napište implementaci metody clone.
8. Vytvořte instanci třídy Nepřítel s nějakými atributy pro parametry konstruktoru.
9. Vytvořte kopii této třídy.
10. Pohněte se s oběmi instancemi a zkontrolujte, že mají tytéž informace a rozdílné poziceX a Y.


### Builder


