# Domácí úkol 1 - zobrazení

## Motivace
Vzpomeňte si na prváckou kartografii a na mapu zobrazení. Počítat polohu
jednotlivých poledníků a rovnoběžek bylo na kalkulačce nepohodlné, GISy jste
ještě všichni neznali a tak to dalo docela práci. Protože se jedná o nudnou
výpočetní činnost, je nejpohodlnější si ji automatizovat pomocí programu.

## Zadání
Pro zvolené zobrazení a měřítko vypište souřadnice rovnoběžek a poledníků.
Pro tento úkol budeme uvažovat pouze válcová tečná zobrazení, a to Marinovo,
Lambertovo, Braunovo a Mercatorovo. Vašim úkolem bude vypsat, na jakých
souřadnicích na papíře byste kreslili rovnoběžky a poledníky, kdybyste chtěli
vykreslit souřadnicovou síť pro dané zobrazení. Protože poledníky a rovnoběžky
jsou svislé respektive vodorovné, budete vypisovat pouze vzdálenost po vodorovné
repsektive svislé ose. Rovnoběžky i poledníky chcete vypisovat po 10 stupních.
Poloměr Země budiž pro tento úkol 6371,11 km.

### Vstup
Program bude interaktivní. Nejprve se zeptá uživatele na použité zobrazení,
odpovědí bude jedno písmeno: 
- `L` - Lambertovo zobrazení
- `A` - Marinovo zobrazení 
- `B` - Braunovo zobrazení 
- `M` - Mercatorovo zobrazení 

Definice zobrazení najdete v souboru [zobrazeni_vzorce.pdf](zobrazeni_vzorce.pdf).
Následně se zeptá uživatele na měřítko mapy, uživatel zadá číslo `x`, které bude
odpovídat měřítku 1:x, například pokud zadá 50000000, bude se počítat s měřítkem
1:50 000 000. Měřítko bude vždy celočíselné.

### Výstup
Po zadání parametrů program vypíše `Rovnobezky:` a následně seznam vzdáleností
na svislé ose, kde byste kreslili rovnoběžky, od -90 po 90 stupňů. 
Poté vypíše `Poledniky:` a seznam vzdáleností na vodorovné ose, kde byste
kreslili poledníky, od -180 po 180 stupňů. Poté program skončí (úspěšně, nikoli pádem).
Všechny vypisované vzdálenosti se vypisují v centimetrech s přesností na
milimetry, tedy například `23.7`. Pokud místo desetinné tečky program vypisuje
desetinnou čárku, je to v pořádku.
Pokud by některá vzdálenost překročila 1 metr, vypište místo ní pomlčku.
Při výpočtu souřadnic počítejte s tím, že bod (0,0) se zobrazí na bod (0,0). 

### Další požadavky
Program by se měl vypořádat s nekorektním vstupem v tom rozsahu, který zatím
umíte. Pokud například zadáte písmeno, které nekóduje žádné zobrazení, měl by
si program postěžovat a skončit.

Pokud vypadne výjimka z funkce `int` nebo `float`, nemusíte
ji ošetřovat (ani to zatím neumíte). V ostatních případech by ale program neměl
skončit výjimkou. Pokud si myslíte, že takový případ existuje, napište mi email.

### Doporučení
Pro načítání znaků použijte funkci `input`, pro převedení na čísla pak `float` a `int` 

Projděte si poznámky z cvičení, naleznete tam odpověď na mnoho ze svých otázek.

Testujte aplikaci nejen na korektní, ale i nekorektní vstupy.

Odevzdejte úkol pár dní i týden dopředu, ať mám čas vám ho zkontrolovat a případně
vrátit k dodělání / přepracování. 

Pište aplikaci jednoduše, nevytvářejte zbytečné vzdušné zámky. Napište si
nejprve funkční kostru, která např. nebere žádné paramtery od uživatele a umí
jen jedno zobrazení a pak dopisujte další funkcinalitu

Použijte Git či jiný verzovací systém, nebo si aspoň před tím, než smažete kus
kódu proto, že si myslíte, že je špatně, udělejte zálohu bokem.

### Odevzdání
Odevzdávat budete zdrojový kód projektu a soubor s dokumentací. Vše
bude zabalené v zip souboru, který bude obsahovat adresář `du1_jmeno_prijmeni`,
ve kterém bude soubor se zdrojovým kódem a soubor s dokumentací, tedy například:
```
du1.zip
|
\du1_tomas_pokorny
  |- dokumentace.md
  \- du1.py
```
Zip archiv mi pošlete mailem. 

Deadline bude 25.11. 8.03. Úkoly odeslané po deadlinu budou brány jako neodevzdané. Pokud
odevzdáte úkol vícekrát, budu hodnotit poslední odevzdání před deadlinem.
Každému, kdo mi pošle úkol, odpovím, že jsem ho přijal a že se mi podařilo zip
rozbalit. Pokud neodpovím, urgujte.

Detaily pro odevzdání přes GitHub viz sekce *Odevzdání přes GitHub*.


### Předčasné odevzdání
Pokud odevzdáte úkol dopředu, zkusím se na něj podívat a napsat vám případné
nedostatky. Tato možnost není garantovaná, ale budu se snažit odbavovat úkoly co
nejrychleji. Zaručuji vám pouze to, že na úkoly se budu dívat v tom pořadí, v
jakém mi budou doručeny. Rovněž nezaručuji, že najdu v programu všechny chyby
napoprvé, tudíž pokud si nějaké nevšimnu, není to garance, že máte program
správně, závazné je pouze hodnocení po deadlinu. Pokud budete odevzdávat přes
GitHub, chyby vám vystavím jako Issue. 

### Bodování
- 1b za funkční aplikaci pro korektní vstupy
- 6b za funkční aplikaci ošetřující nekorektní vstupy
- 2b za kvalitu kódu
- 1b za komentáře v kódu
- 1b za dokumentaci

Kvalitou kódu se rozumí použití vhodných prostředků k dosažení cíle,
minimalizace opakujícího se kódu, vhodné odsazení a oddělení funkčních celků,
použití funkcí tam, kde to dává smysl.

Komentáře v kódu jsou důležité, aby člověk, co si váš kód čte, získal přehled o
tom, co kód dělá. Nekomentujte každý řádek, ale jednotlivé funkční celky. Pokud
používáte metody (a že byste měli), u každé napište, jaké má vstupy a co vrací
jako výstup, ideálně jako [Docstring](https://www.python.org/dev/peps/pep-0257/).
Komentářů by mělo být výrazně méně než kódu.

Dokumentací se rozumí textový soubor (ve formě čistého textu, např. .txt), kde
bude popsána fuknčnost programu, funkce programu a stručný popis, jak program
pracuje. Nepište romány, mělo by stačit 50 -- 75 řádků při 80 znacích na řádek.
Neopisujte přesně zadání, jen ho stručně shrňte, zadání si může každý přečíst
tady. Soubor vhodně formátujte, například pomocí
[MarkDownu](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet),
inspiraci si vezměte například z tohoto souboru.

Postup, jak domácí úkol napsat, spolu klidně konzultujte, ale kód pište každý
sám. Pokud objevím identické či nápadně podobné řešení, oboduji je jednou a body
rovnoměrně rozdělím mezi autory. 

### Příklad běhu programu
```
Zadejte zobrazeni:L
Zadejte meritko:50000000
Rovnobezky:-12,7 -12,5 -12,0 -11,0 -9,8 -8,2 -6,4 -4,4 -2,2 0,0 2,2 4,4 6,4 8,2
9,8 11,0 12,0 12,5 12,7
Poledniky:-40,0 -37,8 -35,6 -33,4 -31,1 -28,9 -26,7 -24,5 -22,2 -20,0 -17,8
-15,6 -13,3 -11,1 -8,9 -6,7 -4,4 -2,2 0,0 2,2 4,4 6,7 8,9 11,1 13,3 15,6 17,8
20,0 22,2 24,5 26,7 28,9 31,1 33,4 35,6 37,8 40,0
```


## Bonusové body

Za různé nadstavby k zadání můžete získat bonusové body. Bonusové body se
počítají pouze tehdy, pokud bude program fungovat korektně včetně ošetření
všech nesprávných vstupů, i těch z bonusové části. Pokud je chyba pouze v
bonusové části (bude hodnoceno individuálně), pak se aplikace považuje za
funkční a propadají pouze body z bonusové části.

### Odevzdání před GitHub (1 b)

Pokud budete pro verzování používat Git, vytvořte si účet na
[GitHubu](https://github.com) nebo jiné podobné stránce a úkol můžete odevzdat
přes něj. Repozitář by měl obsahovat jak program, tak případný soubor s
dokumentací, za hodnocenou verzi se počítá poslední commit pushnutý na GitHub
před deadlinem. Pokud budete potřebovat pomoct, pište mi.

### Volitelný poloměr Země (1 b)

Program se po zadání zobrazení a měřítka zeptá na poloměr Země a použije ten,
který mu zadá uživatel. Pokud uživatel zadá 0, pak se použije poloměr ze zadání.

### Výpočet souřadnic bodů (2b)

Program se po vypsání souřadnic rovnoběžek a poledníků zeptá na zeměpisnou šířku
a délku bodu a následně vypíše jeho přepočtené souřadnice. Poté se opět ptá. Po
zadání bodu (0,0) program skončí.

### Grafické znázornění (3 b)
Program po textovém výpisu souřadnic zobrazí okno, kde "želví grafikou" nakreslí souřadnicovou síť pro dané zobrazení. Pro zjednodušení při kreslení počítejte 1 mm == 1 px. 
