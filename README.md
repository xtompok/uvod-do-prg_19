# Úvod do programování (2019 edition)
Zdrojové kódy a poznámky ke cvičení z Úvodu do programování.

[Stránky](http://web.natur.cuni.cz/~bayertom/index.php/9-teaching/10-uvod-do-programovani) přednášky.

Věci probírané na jednotlivých cvičeních najdete na [samostatné stránce](prubeh.md).
Cvičení probíhá rámcově podle kurzu [Nauč se Python!](https://naucse.python.cz/course/pyladies/).

Cvičení probíhá v jazyku Python 3. Možná jste se setkali, například na Programování pro GIS, s Pythonem 2, pak pozor, jazyky jsou podobné, ale ne stejné, například `print` v Pythonu 3 se vždy volá se závorkami.

## Programové vybavení
Na cvičení budeme programovat v Pythonu 3 v prostředí [PyCharm](https://www.jetbrains.com/pycharm/), stáhněte si zdarma dostupnou Community Edition. Můžete samozřejmě použít i jiná prostředí, pokud jsou vám bližší.

## Poznámky ze cvičení
 * pokud importujete nějaký modul, tak se hlavní program nesmí jmenovat stejně jako tento modul. Tedy např. pokud ve svém kódu máte `from turtle import ...`, tak se váš soubor nesmí jmenovat `turtle.py`
 * nápovědu k tomu, jak se daná funkce volá a co dělá získáte pomocí zavolání `help(jmeno_funkce)`. Obvykle se používá v interaktivním režimu (v Python konzoli)

## Git
Git je jeden z nejrozšířenějších verzovacích systémů. Tyto systémy umožňují
průběžně ukládat vestav nějakého souboru či adresáře, například zdrojového kódu
programu, diplomové práce či zdrojáku webové stránky. Mimo to umožňují se ke
straším verzím vracet, větvit se (ze společného základu se vydat nezávisle více
směry) a opět větve slučovat a spolupracovat s ostatními na nějakém větším
díle. 
Pro informace o Gitu a jeho používání z příkazové řádky doporučuji [zápisky z
Gitového workshopu](https://naucse.python.cz/2019/gitworking-openalt/). 

## Git v PyCharmu
V programu PyCharm naleznete všechny klikací možnosti na práci s Gitem pod
položkou VCS (version control systems) v menu. Abyste mohli Git z PyCharmu
používat, musíte ho mít na svém počítači nainstalovaný (viz zápisky z
workshopu). 

Užitečné položky menu:
 * VCS -> Import -> Create... - založení Gitového repozitáře pro aktuální projekt
 * VCS -> Git -> Commit File - commit akutálního souboru / souborů
 * VCS -> Git -> Show history - zobrazení historie současného repozitáře
 * VCS -> Git -> Remotes -> + - přidání vzdáleného repozitáře (např z GitHubu)
 * VCS -> Git -> Push - nahrát změny z lokálního repozitáře na vzdálený
 * VCS -> Git -> Pull - stáhnout změny ze vzdáleného repozitáře do lokálního



## Speciální znaky (nejen) v řetězcích
Pokud potřebujeme do řetězce vložit nějaký speciální znak, využíváme k tomu
zpětné lomítko (`\`). Zpětné lomítko způsobí, že znak bezprostředně za ním bude
chápán ve speciálním významu. Převážně se používá v řetězcích, ale lze ho
použít i v kodu a to nejčastěji pro zalomení řádku tam, kde by to Python
normálně neumožňoval (například uvnitř podmínky `if`u). Zpětné lomítko se vloží
úplně na konec řádku, tím pádem další znak je zalomení řádku, které je chápáno
speciálně, v tomto případě tak, že se ignoruje. Lze tak tedy napsat program:

`if a == 10\
    or a == 50:`

Stejným způsobem lze pak zpětné lomítko použít i pro zapsání jednořádkového
řetězce na víc řádků. V řetězcích má ale zpětné lomítko i další využití:
 * `\n` vloží do řetězce zalomení řádku `\\` vloží do řetězce zpětné lomítko
 * (protože jinak bychom ho neuměli napsat) `\'` vloží do řetězce apostrof `\"`
 * vloží do řetězce uvozovku
Více o použití různých typů uvozovek najdete v [kapitole o
řetězcích](https://naucse.python.cz/2019/pyladies-brno-podzim-st/beginners/str/)
v kurzu, podle kterého přibližně jdeme.

