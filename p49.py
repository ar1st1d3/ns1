from turtle import*
from nsi_ui import*

def polygone(n, cote):
    for i in range(n):
        forward(cote)
        right(360/n)

tirette_taille = slider("Taille", 10,100)
tirette_nbr_cote = slider("nombre de coté", 10,100)
def creer_polygone():
    polygone(get_int(tirette_nbr_cote),get_int(tirette_taille))

button("Polygone", creer_polygone)
button("clear", clear)
exitonclick()

def avance():
    forward(10)
turtle.Terminator
onkey(avance, "Up")
onkey(avance, "Rigth")
onkey(avance, "Left")