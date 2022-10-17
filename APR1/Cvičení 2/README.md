# Algoritmizace a programování

## On-site cvičení 2

Cílem tohoto cvičení je naučit program rozhodovat o dalším průběhu, tedy o příkazech, které se vykonají za splnění určité podmínky. Budeme k tomu využívat konstrukce IF-ELIF-ELIF-...-ELIF-ELSE. 

Rozhodování vždy začíná příkazem IF. Za tento příkaz píšete podmínku, které pokud bude vyhodnocena jako pravdivá, tak se vykoná blok kódu k ní náležící. Blok se pozná podle odsazení o pevný počet mezer. K psaní podmínky můžete využít veškeré relace z matematiky (<, <=, >, >=, ==, !=) a logické operátory (and, or, not). Také můžete využívat příslušnost prvku ke kolekci pomocí příkazu in.

Pokud byste rozhodovali pouze pomocí struktury IF a měli více podmíněných rozhodnutí, pak se některá z nich mohou vyhodnocovat zbytečně. Příkladem může být: uživatel zadal login a heslo správně nebo nezadal. Jedná se o dichotomickou možnost. Testovat obě podmínky je zbytečné. Proto musí v programovacích jazycích existovat konstrukce pro "tak jinak". Této konstrukci říkáme ELIF (zkratka pro ELSE IF). Tato konsturkce následuje po příkazu IF a rozhodovací blok může obsahovat kolik jen ELIFů chcete. 

Občas se vám hodí i blok, který se vykoná ze všech ostatních okolností, tedy když IF ani žádný z ELIFů nebude vyhodnocen. Této konstrukci se říká ELSE a píše se na konec rozhodování. Nepíše se k ní podmínka a rozhodovací blok obsahuje pouze jeden příkaz ELSE.

Rozhodování lze do sebe zanořovat, takže můžete při splnění nějakého IFu testovat vně dalším rozhodováním o průchodu programu. 

Následující program vám bude sloužit jako šablona pro vyřešení samostatných cvičení:
```
disponibilni_hodiny = 5
znamka = int(input("Znamka: "))

if znamka == 1:
    disponibilni_hodiny += 1
elif znamka in [2, 3]:
    pass
elif 4 <= znamka <= 5:
    disponibilni_hodiny -= 1
else:
    print("Chyba. Nevalidni znamka.")
print(f"Zbyva hodin: {disponibilni_hodiny}")
```


**Úkol OS2.1: Lorem**


**Úkol OS2.2: Lorem**


**Úkol OS2.3: Lorem**



## Domácí cvičení 2

**Úkol HW2.1: Lorem**

**Úkol HW2.2: Lorem**

**Úkol HW2.3: Lorem**

**Úkol HW2.4: Lorem**

**Úkol HW2.5: Lorem**

**Úkol HW2.6: Lorem**


**Video týdne 1: Case match v pythonu 3.10**

Python ve verzi 3.10 přidává novou možnost, jak řešit rozhodování. Využívá k tomu příkaz case match. Podívejte se na jeho syntaxi a pokud máte python alespoň verze 3.10, pak můžete tyto příkazy využít pro lepší přehlednost vašeho kódu. [ZDE](https://www.youtube.com/watch?v=-79HGfWmH_w)

**Video týdne 2: Programátorské stereotypy**

Lidé nejsou tak unikátní. Na základě typologií jako je například Jungova typologie spojená s MB typovými indikátory je možné zařadit lidi do kategorií jako je INFT (určitě znáte z Tinderu). Tyto stereotypy existovaly již v době antiky, kde se lidé rozdělovali podle extroverze a neurotismu na choleriky, sangviniky, flegmatiky a melancholiky (dneska bychom je nazvali emo). I programátoři mají své stereotypy. Jednoho dne se určitě do některé z nich zařadíte. [ZDE](https://www.youtube.com/watch?v=_k-F-MMvQV4)
