# Domácí úkol 3 - sbíráme geodata v adresářové struktuře

Deadline je týden před potřebou zápočtu.

## Motivace

Někdy se stane, že dostaneme geodata ne pěkně rozdělená podle typu v několika
souborech, ale náhodně rozházená po adresářové struktuře, případně jako stovky
malých souborů v zipu. Abychom získali první náhled na získaná data, napíšeme si
skript, který najde všechna geodata v adresáři a jeho podadresářích a vytvoří
nám 3 soubory - s body, liniemi a polygony.

## Zadání

Napište neinteraktivní program, který projde adresář zadaný jako parametr
příkazové řádky a všechny jeho podadresáře. Zde bude hledat soubory s příponou
`.json` a `.geojson`. Každý takový soubor otevře a zjistí, zda se jedná o
validní GeoJSON. Ze všech featur ve validních GeoJSON souborech pak vytvoří 3
soubory - `points.geojson`, `lines.geojson` a `polygons.geojson`, které budou
obsahovat body, linie resp. polygony získané z procházených souborů. Ke každé
feature navíc program přidá novou property `filepath`, který bude obsahovat cestu
k souboru, ve kterém byla původní feature umístěná. Původní properties zůstanou
zachovány.

Program na standardní výstup průběžně vypisuje, který adresář zpracovává. Pokud
nějaký adresář nebo soubor `.json` či `.geojson` nelze otevřít, vypíše tuto
informaci a přeskočí ho. Chyby vztahující se k jiným souborům program
nevypisuje.

Validním [GeoJSON][2]em v tomto případě rozumíme [FeatureColection][3] obsahující
jednotlivé [Feature][5], které mohou mít geometrii [Point][6], [Linestring][7]
nebo [Polygon][8], pokud některý z těchto předpokladů neplatí, program vypíše
chybu a soubor přeskočí.

### Vstup

Program dostane jako vstup adresář, zadaný jako parametr příkazové řádky.
Program tedy bude spouštěn například jako `py geocrawler.py data`, pak bude
prozkoumávat adresář `data`.

Vzorový vstup [zde ke stažení][9].

### Výstup

Výstupem budou 3 soubory `points.geojson`, `lines.geojson` a `polygons.geojson`
v aktuálním adreáři + výpis procházených a případných problematických adresářů a
souborů v terminálu.

Přesný formát výpisu do terminálu není dán, ale měl by být pro uživatele skriptu
jasný a chyby by měly být zřetelně označeny.


Výstupní data můžete snadno vizualizovat například v QGISu, který GeoJSON
nativně podporuje (`Vrstva` -> `Přidat vrstvu` -> `Přidat vektorovou vrstvu`), nastavte si
kategorizovaný symbol podle `filepath`.

### Další požadavky

Program by se měl umět vypořádat s všemi obvyklými výjimkami, které mohou při
běhu programu nastat, měl by je umět oznámit uživateli a problematický soubor
nebo adresář přeskočit. Program by neměl spadnout, ani když uživatel zadá
nevalidní adresář k procházení, ale měl by na to uživatele upozornit a pak
skončit.

## Doporučení
Předtím, než začnete programovat, rozmyslete se, jak by měl program fungovat a
pro ucelené části používejte funkce. Napište si kostru programu a pak
implementujte jednotlivé funkce, průběžně ověřujte, zda se chovají dle
očekávání.

## Bodování
  * 1 b za funkční aplikaci pro zadaný adresář
  * 5 b za funkční aplikaci pro zadaný adresář a všechny jeho podadresáře
  * 3 b za kvalitu kódu
  * 2 b za dokumentaci

Více o jednotlivých kategoriích v minulém zadání.

## Bonusové body

### Používání Gitu pro vývoj (1 b)
Pokud budete pro verzování používat Git, vytvořte si účet na GitHubu nebo jiné
podobné stránce a úkol můžete odevzdat přes něj. Kromě samotného odevzdání je
třeba, aby byl repozitář používán i pro vývoj, tedy by měl obsahovat průběžně   
commitovanou práci a jednotlivé commity by měly mít smysluplné commit message, 
které popisují, co jste od minulého commitu změnili. Pokud budete potřebovat pomoct,
pište mi.

## Alternativa k domácímu úkolu
Pokud jste již využili znalostí z tohoto předmětu pro nějaký váš školní či jiný
programovací projekt, můžete místo (nebo navíc k) 3. úkolu odevzdat tento
projekt a dostanete za něj body dle obtížnosti. Tento projekt by kromě kódu
samotného měl obsahovat i uživatelskou dokumentaci a případně ukázková vstupní
data či odkaz na ně. Programovací jazyk nemusí být nutně Python 3, lze se
domluvit i na jiném, ale Python 2 to být nemůže. Pokud máte o tuto alternativu
zájem, napište mi email. 


[1]: https://en.wikipedia.org/wiki/Quadtree
[2]: https://tools.ietf.org/html/rfc7946
[3]: https://tools.ietf.org/html/rfc7946#section-3.3
[4]: https://overpass-turbo.eu/s/E9v
[5]: https://tools.ietf.org/html/rfc7946#section-3.2
[6]: https://tools.ietf.org/html/rfc7946#appendix-A.1
[7]: https://tools.ietf.org/html/rfc7946#appendix-A.2
[8]: https://tools.ietf.org/html/rfc7946#appendix-A.3
[9]: du3_testdata.zip

