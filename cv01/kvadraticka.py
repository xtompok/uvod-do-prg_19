from math import sqrt

a = float(input("Zadej koeficient a:"))
b = float(input("Zadej koeficient b:"))
c = float(input("Zadej koeficient c:"))

D = b*b-4*a*c

if D < 0:
    print("Rovnice nemá řešení")
elif D == 0:
    x_12 = -b/(2*a)
    print("Rovnice má jedno dvojnásobné řešení: ",x_12)
else:
    x1 = -b+sqrt(D)/(2*a)
    x2 = -b-sqrt(D)/(2*a)
    print("Rovnice má 2 různá řešení: ",x1," a ",x2)
