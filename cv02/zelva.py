from turtle import forward,left,right,exitonclick,speed

# Ctverec
for _ in range(4):
    forward(50)
    right(90)

a = 50
x = 4
y = 4

# Nakresli čtvercovou sít
for yi in range(y):
    # nakreslí řádek
    for xi in range(x):
        # nakreslí čtvereček
        for i in range(4):
            forward(a)
            left(90)
        # posune se o čtvereček doprava
        forward(a)
    # vrátí se na začátek
    left(180)
    forward(x*a)
    left(180)
    # posune se o řádek nahoru
    left(90)
    forward(a)
    right(90)

left(45)
forward(100)

# Šestiúhelník
for i in range(6):
    forward(a)
    left(60)

forward(100)

# Nakresli "kytičku"
for i in range(6):
	for j in range(6):
		forward(a)
		left(60)
	forward(a)
	right(60)

exitonclick()
