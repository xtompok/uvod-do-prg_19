# Vytvoř prázdný seznam
shop_list = []

# Dokud není zadáno 'x':
while True:
    # Načti položku
    item = input("Zadej název")
    # Pokud zadáno 'x', skonči
    if item == 'x':
        break
    # Načti množství
    amount = input('Zadej množství')
    # Přidej (položku,množství) do seznamu
    shop_list.append((item,amount))

# Vypiš seznam
print(shop_list)
