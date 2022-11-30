# Objektově-orientované návrhové vzory

## Strukturální vzory - Strategie, Šablona metoda, Návštěvník

Behaviorální vzory řeší problémy, které vycházejí z dělby odpovědnosti mezi objekty. Mezi první probírané patří:
1. Strategie - umožňuje zaměňovat algoritmy v rámci rodiny
2. Šablona metoda - umožňuje vytvořit kostru algoritmu v rodiči s implementačními detaily v potomcích
3. Návštěvník - umožňuje oddělit algoritmy od objektů, na které působí

### Strategie


Více o návrhovém vzoru Stategie naleznete [ZDE](https://refactoring.guru/design-patterns/strategy) nebo [ZDE](https://www.dofactory.com/net/strategy-design-pattern).

**Cvičení**

Vytvořte rodinu metod pro třídění čísel v poli od nejmenšího po největší. Tyto metody budou mezi sebou zaměnitelné. Implementujte například třídící algoritmy: BubbleSort, QuickSort, BogoSort.

1. Vytvořte třídu ŘadičČísel, která obsahuje metodu zvolAlgoritmus a seřaďČísla. Metoda seřaďČísla má dva parametry: pole čísel a vzestupnost/sestupnost řazení.
2. Vytvořte rozhraní IŘadič, které obsahuje předpisy vzestupnéŘazení a sestupnéŘazení.
3. Vytvořte třídy BubbleSort, QuickSort a BogoSort, které implementují rozhraní IŘadič. Implementuje metody.
4. Vyzkoušejte zaměnitelnost algoritmů na nějakých datech.

```

```

**Řešení**

```

```

### Šablona metoda


Více se o Template method dočtete [ZDE]() nebo [ZDE](https://www.dofactory.com/net/template-method-design-pattern).

**Cvičení**

```

```

**Řešení**

```

```

### Návštěvník


Více se o návrhovém vzoru Návštěvník dočtete [ZDE]() nebo [ZDE](https://www.dofactory.com/net/visitor-design-pattern).

**Cvičení**


**Řešení**

```

```
