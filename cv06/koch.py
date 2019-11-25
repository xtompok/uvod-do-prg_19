from turtle import forward,right,left, backward,exitonclick,speed

# Kochova vločka
def koch(length,depth):
    # Pokud je depth==0 nakresli úsečku délky length
    if depth == 0:
        forward(length)
        return
    # Jinak 4x zavolej koch(length/3,depth-1)
    # a nakresli tím čáru se "zubem"
    koch(length/3,depth-1)
    left(60)
    koch(length/3,depth-1)
    right(120)
    koch(length/3,depth-1)
    left(60)
    koch(length/3,depth-1)

speed(10)
koch(400,5)
right(120)
koch(400,5)
right(120)
koch(400,5)
exitonclick()