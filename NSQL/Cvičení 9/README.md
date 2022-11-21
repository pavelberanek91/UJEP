# NoSQL databázové systémy

## Cvičení 9 - Map-reduce

Map-reduce je model pro zpracování dat, který umožňuje provádět operace na velké datové sadě a shrnout je do agregované informace (součet, součin, počet, maximum, průměr, medián, modus, aj.). MongoDB obsahuje pro tento model agregačních operací funkci mapReduce(), která přebírá mapovací funkci a redukovací funkci. Mapovací funkce slouží pro shluknutí dat do kolekce, která nás zajímá. Na tuto nalezenou kolekci bude následně proveden algoritmus redukovací funkce.

Více informací o map-reduce naleznete [ZDE](https://www.geeksforgeeks.org/mongodb-map-reduce/) a [ZDE](https://www.mongodb.com/docs/manual/core/map-reduce/).

### Zadání

Aplikujte ve vašem kódu map-reduce operaci a ze své MongoDB získejte nějaké dvě agregační informace. Techniky postupujte podle následujícího kódu, který si po vyzkoušení upravte na váš kontext [ZDE](http://aimotion.blogspot.com/2010/08/mapreduce-with-mongodb-and-python.html)


