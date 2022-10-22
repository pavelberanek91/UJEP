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


**Úkol OS2.1: Řešitel kvadratických rovnic**

Napište program, který přijme naráz ze standardního vstupu oddělené mezerou koeficienty kvadratické rovnice. Program následně spočítá a vypíše na obrazovku kořeny této rovnice. V případě neexistujícího řešení v oblasti reálných čísel vypíše na obrazovku informační hlášku.

**Úkol OS2.2: Jednokolová verze kámen-nůžky-papír**

Napište program, který realizuje jedno kolo hry kámen-nůžky-papír. Hráč volí mezi třemi symboly (kámen, nůžky, papír) pomocí standardního vstupu. Protihráčem je umělá inteligence, která vybírá symboly náhodně. Vypište na obrazovku informační hlášku o tom, kdo si vybral jaký symobl a jak kolo hry dopadlo.

## Domácí cvičení 2

**Úkol HW2.1: Kalkulačka**

Napište program, ve kterém na standardní vstup napíše uživatel sadu čísel oddělených čárkou. Následně ve druhém vstupu zvolí slovy jakou operaci chce s čísly v kolekci provést (například: sečti, vynásob). Program podle výběru spustí příslušný algoritmus, který čísla vzájemně sečte, vynásobí nebo provede další jiné operace, které zavedete.

**Úkol HW2.2: Seznamka**

Napište program, do kterého uživatel zadá svůj věk, výšku a záliby. Řekněme, že na seznamce je již registrována jedna osoba jménem Pepina. Uživatel s ní bude mít match, pokud nejsou příliš daleko od sebe svým věkem, výškou a mají alespoň 2 společné záliby. Realizujte takový algoritmus.

**Úkol HW2.3: Palindrom**

Napište program, který zjistí zda zadané slovo je palindrom, Tedy čte se z obou stran stejně. Takové slovo je například "kunanesenanuk" nebo "jelenovipivonelej".

**Úkol HW2.4: Silné heslo**

Napište program, který zjistí, zda zadané heslo uživatelem je silné. heslo musí mít alespoň jedno velké písmeno, jedno malé písmeno, jednu číslici, jeden speciální znak a minimální délka musí být alespoň 8 znaků.

**Úkol HW2.5: Trefa do kulatého terče**

Napište program, který vystřelí náhodně do čtverce. V tomto čtverci je umístěna kružnice s daným středem a poloměrem. Program zahlásí výstřel, pokud souřadnice náhodného výstřelu jsou uvnitř kružnice (terč).

**Úkol HW2.6: Narozeniny**

Napište program, do kterého zadáte datum vašeho narození. Program se podívá na dnešní datum pomocí knihovny datetime a vypíše, kolik zbývá dnu do vašich narozenin. Pokud máte narozeniny dnes, tak vám navíc ještě pogratuluje.

**Video týdne 1: Case match v pythonu 3.10**

Python ve verzi 3.10 přidává novou možnost, jak řešit rozhodování. Využívá k tomu příkaz case match. Podívejte se na jeho syntaxi a pokud máte python alespoň verze 3.10, pak můžete tyto příkazy využít pro lepší přehlednost vašeho kódu. [ZDE](https://www.youtube.com/watch?v=-79HGfWmH_w)

**Video týdne 2: Programátorské stereotypy**

Lidé nejsou tak unikátní. Na základě typologií jako je například Jungova typologie spojená s MB typovými indikátory je možné zařadit lidi do kategorií jako je INFT (určitě znáte z Tinderu). Tyto stereotypy existovaly již v době antiky, kde se lidé rozdělovali podle extroverze a neurotismu na choleriky, sangviniky, flegmatiky a melancholiky (dneska bychom je nazvali emo). I programátoři mají své stereotypy. Jednoho dne se určitě do některé z nich zařadíte. [ZDE](https://www.youtube.com/watch?v=_k-F-MMvQV4)
