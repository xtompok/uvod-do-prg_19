# Domácí úkol 2 - dělení adresních bodů

Deadline bude 22. 12. 2018 v 8.03.

## Motivace

V některých situacích nechceme zpracovávat data pro každou jednu jednotku, ale
chceme z jednotek vytvořit skupiny a zpracovávat data dohromady pro celou
skupinu, například pro vyloučení extrémních případů. Jednotky chceme seskupovat
do skupin tak, aby vzniklé skupiny byly kompaktní a nebyly složeny z jednotek
roztroušených po celé mapě a měly nějakou maximální velikost.

## Zadání

Napište neinteraktivní program, který bude metodou [quadtree][1] dělit data do skupin
tak, aby žádná skupina neměla více než 50 jednotek. Program načte vstupní data
ze souboru `input.geojson`, jednotky ze vstupního souboru rozdělí do
skupin pomocí algoritmu quadtree, ke každé jednotce přidá informaci, do které
skupiny patří a jednotky s informacemi o skupinách vypíše do výstupního souboru
`output.geojson`.
Při programování počítejte s tím, že vstupních bodů můžou být desetitisíce.

Budeme uvažovat následující variantu quadtree. Výchozí obdélník je bounding box
množiny vstupních bodů. Pokud nějaká oblast obsahuje více než 50 bodů, rozdělí
se geometricky na čtvrtiny a opět je testována na toto kritérium. Pokud oblast obsahuje méně
než 50 bodů, dále se nedělí.  

### Vstup

Vstup je uložen ve formátu [GeoJSON][2] jako [FeatureColection][3] bodů. Každý bod má
nějaké properties, jejich hodnoty nás nezajímají, ale chceme je zachovat do
výstupního souboru.

Testovací vstupy si můžete vygenerovat například pomocí [Overpass Turbo][4],
uložíte pomocí `Export` -> `download as GeoJSON`, mapou můžete posouvat a měnit
zoom, nové body vygenerujete pomocí `Run`.

### Výstup

Výstup bude uložen také ve formátu GeoJSON, ke každému bodu přibude property
`cluster_id`, která bude určovat, do které skupiny bod patří. Můžete
předpokládat, že tuto property žádný bod ve vstupním souboru nemá. `cluster_id`
musí být jedinečné pro každou skupinu.

Výstupní data můžete snadno vizualizovat například v QGISu, který GeoJSON
nativně podporuje (`Vrstva` -> `Přidat vrstvu` -> `Přidat vektorovou vrstvu`), nastavte si
kategorizovaný symbol podle cluster_id.

### Další požadavky

Program by měl ošetřovat nekorektní vstupy a výjimky, v takovém případě by měl
vypsat chybovou hlášku a skončit s chybou (`exit(<cislo>)`, kde `cislo` je mezi
1 a 127).


## Doporučení
Předtím, než začnete programovat, rozmyslete se, jak by měl program fungovat a
pro ucelené části používejte funkce. Napište si kostru programu a pak
implementujte jednotlivé funkce, průběžně ověřujte, zda se chovají dle
očekávání.

## Bodování
  * 1 b za funkční aplikaci pro korektní vstupy
  * 4 b za funkční aplikaci pro nekorektní vstupy
  * 3 b za kvalitu kódu
  * 2 b za dokumentaci

Kvalita kódu nyní zahrnuje i komentáře v kódu, více o jednotlivých kategoriích v
minulém zadání.

## Bonusové body

### Používání Gitu pro vývoj (1 b)
Pokud budete pro verzování používat Git, vytvořte si účet na GitHubu nebo jiné
podobné stránce a úkol můžete odevzdat přes něj. Kromě samotného odevzdání je
třeba, aby byl repozitář používán i pro vývoj, tedy by měl obsahovat průběžně
commitovanou práci. Repozitář by měl obsahovat jak program, tak případný soubor
s dokumentací, za hodnocenou verzi se počítá poslední commit pushnutý na GitHub
před deadlinem. Repozitář nemusí, ani by neměl, obsahovat velká vstupní data,
naopak přítomnost malých vstupů pro účely testů je vhodná. Pokud budete potřebovat pomoct,
pište mi.

### Vykreslování průběhu algoritmu (2 b)
Program na začátku vykreslí všechny vstupní body a následně vykresluje, kde
právě probíhá dělení. Body jsou vykresleny tak, aby vhodně vyplňovaly okno. Může
se vám hodit funkce `turtle.screensize()`.

### Další algoritmy na dělení dat (1 -- 5 b dle složitosti)
Na začátku programu bude konstantou `ALGORITHM` zvolen algoritmus, kterým se
bude provádět dělení bodů. Můžete použít libovolný vhodný algoritmus, podle jeho
obtížnosti za něj získáte 1 -- 5 bodů (pokud mi dopředu napíšete, který
algoritmus budete implementovat, odpovím vám, kolik bodů za něj bude).
Implementace quadtree je samozřejmě povinná bez bonusových bodů.


[1]: https://en.wikipedia.org/wiki/Quadtree
[2]: https://tools.ietf.org/html/rfc7946
[3]: https://tools.ietf.org/html/rfc7946#section-3.3
[4]: https://overpass-turbo.eu/s/E9v
