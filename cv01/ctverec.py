n_iter = 5
for _ in range(n_iter):
    a = int(input("Zadej délku strany:"))
    if a < 0:
        print("Císlo je záporné, to se mi nelíbí")
        quit()
    elif a == 0:
        print("Císlo je nula")
    elif a > 5:
        print("Císlo je moc velké")
    else:
        print("Císlo je kladné, děkujeme")
    print("Obvod",4*a,"obsah",a*a)
print("Hotovo")
