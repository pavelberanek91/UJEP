# Algoritmizace a programování

**Video týdne 1: idiom Main**

Většina programovacích jazyků má vstupní bod s názvem Main. Python takový bod nemá. Další problém je dán tím, že soubory v pythonu mohou být jak moduly, tak skripty. Pokud má kód s logikou v prvním bloku - globálním (plně neodsazeno), tak se kód spustí při importu. Proto použití idiomu Main je možné oddělit chování programu při importování a při používání ve formě programu. Více o tom v následujícím videu: [ZDE](https://www.youtube.com/watch?v=g_wlZ9IhbTs)

**Video týdne 2: zacyklené importování**

Ze cvičení jste se dozvěděli, že funkce lze rozdělit do více souborů a vytvářet tak moduly jazyka Python. Při importování můžete narazit na to, že program A vyžaduje balíček B, balíček B vyžaduje funkce balíčku C a balíček C vyžaduje program jako balíček A. Tím jste v cyklu podobnému slepice a vejce. V následujícím videu se dozvíte, jak se vypořádat s tímto problémem. [ZDE](https://www.youtube.com/watch?v=UnKa_t-M_kM)
