from math import*
a = True

while a :
    nbr = int(input('etrez un nombre entre 2 et 12 : ' ))

    if nbr > 12 or nbr < 2 :
        print('merci d entrer un nombre compris entre 2 et 12 compris')
    else :
        a = False

def nbrpossibilité() : 
    print('il y a ', nbr-1, 'pour une combinaison de deux dé avec comme somme ', nbr)
nbrpossibilité()

def dépossibilité(nbr) :
    i = 1
    while i < nbr :
        valeur1 = i
        valeur2 = abs(nbr - i)
        print('dé 1 : ', valeur1, ' dé 2 : ', valeur2)
        i += 1

dépossibilité(nbr)

def allpossibility() :
    i = 2
    while i  <= 12 :
        dépossibilité(i)
        i += 1
allpossibility()

def possibilité3dés(objectif):

    for d1 in range(1, 7):
        for d2 in range(1, 7):
            for d3 in range(1, 7):
                somme_des = d1 + d2 + d3
                if somme_des == objectif:
                    print(f"{d1} + {d2} + {d3} = {somme_des}")
possibilité3dés(nbr)