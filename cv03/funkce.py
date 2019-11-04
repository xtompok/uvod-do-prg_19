from turtle import forward,left,right,exitonclick,speed

def vypis_ahoj():
    print("Ahoj")

def vypis_vice_ahoj(pocet):
    for i in range(pocet):
        print("Ahoj")

vypis_ahoj()
vypis_vice_ahoj(10)
for i in range(2):
    vypis_vice_ahoj(10)

def ctverecek(delka_strany):
    for i in range(4):
        forward(delka_strany)
        left(90)

def nakresli_radek(pocet_sloupcu,delka_strany):
    for xi in range(pocet_sloupcu):
        # nakreslí čtvereček
        ctverecek(delka_strany)
        # posune se o čtvereček doprava
        forward(delka_strany)
	
def nakresli_sit(pocet_radku,pocet_sloupcu,delka_strany):
	for yi in range(pocet_radku):
	    # nakreslí řádek
	    nakresli_radek(pocet_sloupcu,delka_strany)
	    # vrátí se na začátek
	    left(180)
	    forward(pocet_sloupcu*delka_strany)
	    left(180)
	    # posune se o řádek nahoru
	    left(90)
	    forward(delka_strany)
	    right(90)



nakresli_sit(5,5,10)
