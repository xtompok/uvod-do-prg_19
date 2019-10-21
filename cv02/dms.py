a = float(input("Zadej stupně: "))

d = int(a)
m = (a - int(a))*60
s = (m - int(m))*60
m = int(m)

print("Výsledek je",end=' ')
print(d,"stupnů",m,"minut a ",s,"vteřin")
