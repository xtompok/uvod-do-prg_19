from random import shuffle

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
    staty = []
    # Dokud uživatel nezadal 'x', načítám stát a hlavní město
    while True:
        vysl = nacti_stat_a_hlavni_mesto(staty)
        if not vysl:
            return staty

def hadej_hlavni_mesto(stat,mesto):
    # Vypis stat
    print(stat)
    odpoved = input("Zadej mesto:")
    pokusu = 0
    # Dokud uzivatel nezadal spravne hlavni mesto:
    while odpoved != mesto:
        pokusu += 1
        # Rekni mu tolik pismen, kolikrat uz neuhodl
        print("Nápověda: {}".format(mesto[:pokusu]))
        # Zeptej se na hlavni mesto
        odpoved = input("Zadej mesto:")

def hadej_hlavni_mesta(staty):
    # Zamíchej státy
    shuffle(staty)
    # Dokud jsou nějaké státy v seznamu:
    while len(staty) > 0:
        # Vyzvedni dvojici stat,mesto ze seznamu statu
        sm = staty.pop()
        (stat,mesto) = sm
        #(stat,mesto) = staty3.pop()
        hadej_hlavni_mesto(stat,mesto)

# Nacitej staty a hlavni mesta
staty2 = nacti_staty_a_hlavni_mesta()
# Zde je sdileny pouze seznam statu s hlavnimi mesty
print(staty2)
# Hadej hlavni mesta
hadej_hlavni_mesta(staty2)

