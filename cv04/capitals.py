# Nacitej staty a hlavni mesta
 # Zde je sdileny pouze seznam statu s hlavnimi mesty
# Hadej hlavni mesta
def nacti_stat_a_hlavni_mesto(staty):
    # Načtu od uživatele stát
    stat = input("Zadej stat")
    # Pokud je stát 'x', vrátím False
    if stat == 'x':
        return False
    # Načtu od uživatele hlavní město
    mesto = input('Zadej hlavni mesto')
    # Přidám stát a město do seznamu staty a vrátím True
    staty.append((stat,mesto))
    return True

def nacti_staty_a_hlavni_mesta():
    staty1 = []
    # Dokud uživatel nezadal 'x', načítám stát a hlavní město
    while True:
        vysl = nacti_stat_a_hlavni_mesto(staty1)
        if not vysl:
            return staty1

def hadej_hlavni_mesta(staty3):
    pass # Pass nic nedělá, jen zajištuje existenci odsazeného bloku
    # Dokud uživatel nezadal 'x', ptám se na hlavní město

staty2 = nacti_staty_a_hlavni_mesta()
print(staty2)
hadej_hlavni_mesta(staty2)

