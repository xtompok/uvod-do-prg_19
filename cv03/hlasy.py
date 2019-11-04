
stranaA = 0
stranaB = 0
stranaC = 0
stranaD = 0

strana = ""

while True:
	strana = input("Zadej stranu: ")
	if strana == "A":
		stranaA += 1
	elif strana == "B":
		stranaB += 1
	elif strana == "C":
		stranaC += 1
	elif strana == "D":
		stranaD += 1
	elif strana == "x":
		break
	else:
		print("Zadána neplatná strana, zadejte prosím znovu")

# Ukázka zalomení řádku pomocí \
a = 120
if a == 2 or \
    a == 3:
    pass

print("Strana A:",stranaA,"Strana B:",stranaB)
print("Strana A: {stranaA}, strana B: {stranaB}, strana C: {stranaC}, stranaD: {stranaD}")
# Python od verze 3.7
print(f"Strana A: {stranaA}\nstrana B: {stranaB}\n\
strana C: {stranaC}\nstrana D: {stranaD}")
# Python před verzí 3.7
print("Strana A: {stranaA}, strana B: {stranaB}, strana C: {stranaC}, stranaD: {stranaD}".format(
    stranaA=stranaA,stranaB=stranaB,stranaC=stranaC,stranaD=stranaD))
print("\"Ahoj\",řek'")
print(f"""Strana A: {stranaA}
Strana B: {stranaB}""")
