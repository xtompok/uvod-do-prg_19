# Úvod do programování (2019 edition)
Zdrojové kódy a poznámky ke cvičení z Úvodu do programování.

[Stránky](http://web.natur.cuni.cz/~bayertom/index.php/9-teaching/10-uvod-do-programovani) přednášky.

Věci probírané na jednotlivých cvičeních najdete na [samostatné stránce](prubeh.md).
Cvičení probíhá rámcově podle kurzu [Nauč se Python!](https://naucse.python.cz/course/pyladies/).
[Dokumentace](https://docs.python.org/3/) k Pythonu 3.

Cvičení probíhá v jazyku Python 3. Možná jste se setkali, například na Programování pro GIS, s Pythonem 2, pak pozor, jazyky jsou podobné, ale ne stejné, například `print` v Pythonu 3 se vždy volá se závorkami.


## Programové vybavení
Na cvičení budeme programovat v Pythonu 3 v prostředí [PyCharm](https://www.jetbrains.com/pycharm/), stáhněte si zdarma dostupnou Community Edition. Můžete samozřejmě použít i jiná prostředí, pokud jsou vám bližší.

## Poznámky ze cvičení
 * pokud importujete nějaký modul, tak se hlavní program nesmí jmenovat stejně jako tento modul. Tedy např. pokud ve svém kódu máte `from turtle import ...`, tak se váš soubor nesmí jmenovat `turtle.py`
 * nápovědu k tomu, jak se daná funkce volá a co dělá získáte pomocí zavolání `help(jmeno_funkce)`. Obvykle se používá v interaktivním režimu (v Python konzoli)

## Tipy a rady pro čitelný kód
### Magické konstanty
Pokud ve svém kódu používáte nějaké konstanty, ať už matematické (např. pi),
fyzikální nebo jste si jen pevně zvolili délku pole či např. rozestup
rovnoběžek, je vhodné tyto konstanty na začátku programu pojmenovat a pak
používat toto pojmenování místo jejich číselné hodnoty. Je pak jasné, co je v
daném místě sémanticky myšleno a pokud se nějakou z konstant později rozhodntete
změnit, lze to udělat snadno na jednom dobře definovaném místě.

Konstanty se obvykle pojmenovávají velkými písmeny, víceslovné se oddělují
podtržítkem. Např. `LIST_LEN` pro délku seznamu (pokud v programu je více
seznamů různých délek, je vhodné přidat do jména jednoznačný identifikátor, ke
kterému seznamu se konstanta vztahuje), `F_G = 9.81` pro gravitační zrychlení na
Zemi, `REC_DEPTH` pro hloubku rekurze. Pokud konstantu importujete z nějakého
modulu, nechte ji takové jméno, jaké má v daném modulu (např. `from math import
pi)`.

### Funkce
Funkce by měly používat pouze lokální proměnné, tedy takové proměnné, jaké buď
dostaly jako argumenty, nebo byly v dané funkci vytvořeny. V opačném případě,
pokud použijete funkci jinde, než bylo původně zamýšleno, může dojít k pádu
aplikace nebo neočekávanému chování, protože některé proměnné nemusí existovat.

Funkce je vhodné psát na začátek souboru za importy a definice konstant. Hlavní
kód by pak měl být na konci souboru pod všemi funkcemi, aby se s nimi nemíchal a
tím pádem nebyla některá jeho část snadno přehlédnutelná. Pokud je v programu
více funkcí vztahujících se k podobnému tématu, je vhodné je oddělit do
samostatného modulu. Usnadní to pak jejich znovupoužitelnost v dalších
programech.

### Nejprve validuj, pak počítej
Pokud program bere nějaká data od uživatele, ať už přímo přes `input`, pomocí
parametrů příkazové řádky nebo načítá ze souboru, je vhodné (pro některé
aplikace, například webové i nutné) takováto data kontrolovat, zda mají správný
formát a obsah. Tyto kontroly je vhodné provést co nejdříve a až po kontrole
všech vstupních dat s nimi zahájit výpočet. 

Tento postup má několik výhod:
 * Uživatel se dozví hned při spuštění, že data nejsou validní a má možnost data
   opravit a program spustit znovu. Pokud se po problému dozví po několika
   hodinách výpočtu, bude jeho práce výrazně méně efektivní
 * Výpočetní funkce již nemusí znovu ověřovat validitu dat, mohou se soustředit
   na samotný výpočet a vstup předpokládat validní. Pokud dojde v rámci úprav
   kódu k přehození pořadí výpočtů, nehrozí při tom práce s nezkontrolovanými
   daty.

Na časté kontroly je vhodné si napsat samostatné funkce, například funkci
`input_int(quest)`, která vypíše `quest` - otázku, kterou se ptáme uživatele,
načte, co uživatel napsal a zkusí to převést na `int` a podle výsledku buď vrátí
číslo, nebo se zeptá znovu. Obdobně lze vytvořit další pomocné funkce, které
povedou k výraznému zjednodušení získávání dat od uživatele.


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


## Volání funkcí a rekurze
### Zásobník a halda
Pokud v programu vytvoříme nějakou proměnnou, uloží se odkaz na ni (u čísel a
dalších jednoduchých typů sama proměnná) na zásobník, samotný objekt (bude
vysvětleno později, berte to nyní jako její obsah) se uloží do haldy někde v
paměti. Pokud zanikne odkaz na tento objekt, tzn. neexistuje v programu
proměnná, pomocí které se můžeme k danému objektu dostat, stává se objekt
nedosažitelný a časem je z haldy odstraněn. O tuto činnost se stará garbage
collector, který běží nezávisle na programu (ale stále je to součást Pythonu) a
zde jej dále nebudeme rozebírat.
Halda je v principu neomezeně velká (respektive omezená jen dostupnou pamětí),
zásobník má omezenou velikost. Pro vytváření proměnných nás to nemusí trápit,
ale při rekurzi je potřeba na to myslet.

### Volání funkce
Pokud z nějakého místa v kódu voláme funkci, musíme provést některé přípravy.
Protože je funkce samostatným celkem, který neví, odkud a kdy bude zavolán, je
potřeba ji předem někam nachystat argumenty a říct, kde se má pokračovat, když
funkce skončí. Také funkce potřebuje dalšímu kódu nějak předat to, co vrací. 
Pro tyto účely se využívá zásobník:
 - na zásobník se uloží, kde pokračovat po skončení funkce (návratová adresa)
 - na zásobník se uloží odkazy na argumenty funkce

Následně se začne vykonávat kód funkce, který nejprve vytvoří lokální proměnné
dle názvů argumentů funkce a přiřadí do nich hodnoty ze zásobníku. Poté se
pokračuje příkazy ve funkci. Pokud už není ve funkci další příkaz k vykonání
nebo byl zavolán `return`, vymaže se celý obsah zásobníku nad návratovou
adresou, pokud funkce něco vrací, tak je odkaz na vracený objekt přidán na
zásobník a skočí se tam, odkud byla funkce volána (což se zjistí z
návratové adresy). Pokud funkce něco vracela, uloží se do proměnné odkaz ze
zásobníku. Nakonec se smaže zásobník po návratovou adresu včetně a vykonávají se
příkazy dále tam, odkud byla funkce volána.

### Rekurze
Z výše zmíněného popisu volání funkce vyplývá, že nic nebrání tomu, aby funkce
volala sebe samu. Tomuto se říká rekurze. U rekurze je důležité, aby tento řetěz
volání sebe sama někdy skončil, jinak dojde k přeplnění zásobníku (stack
overflow) a program bude ukončen operačním systémem. K přeplnění dojde proto, že
každé volání funkce musí na zásobník uložit alespoň návratovou adresu, tedy
zásobník stále roste. Více na
[webu KSP](http://ksp.mff.cuni.cz/kucharky/zakladni-algoritmy/), v části
*Programátorské techniky*. 


## Dokumentace
Každý program by měl obsahovat alespoň základní uživatelskou dokumentaci,
rozsáhlejší programy pak i dokumentaci programátorskou.

### Uživatelská dokumentace
Představte si, že kamarádovi vysvětlujete, jak se ten program používá. Kamarád
se rámcově orientuje v tématu programu (tedy např. ví, co jsou to válcová
zobrazení), ale programovat neumí a chce jen program používat, tedy je vhodné
mu říct, jak má co kam zadat, co se případně stane, když něco zadá špatně a co
se vypíše a jak to má použít.

### Vývojářská dokumentace
Pokud je program rozsáhlejší, píše se i programátorská dokumentace,
tedy máte jiného kamaráda, který se opět rámcově orientuje v tématu
programu, ale navíc umí programovat, ale zdroják vašeho programu nikdy
neviděl. Tato část dokumentace by tedy měla obsahovat stručný popis
běhu programu a stručný popis složitějších funkcí. Také by měla
popisovat použité algoritmy. Doplňkem této dokumentace jsou docstringy
u jednotlivých funkcí, které říkají vstupní a výstupní parametry každé
funkce.
