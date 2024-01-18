'''
Mini Projet : A l'aide du cours page 108 à 111

Creer un programme qui trie par ordre croissant une liste de nombre 800 nombres entiers
mesurant la duree et le nombre d'itération pour trier cette liste par insertion et 
selection pour 3 cas 

=> liste deja trier
=> liste ordre decroissant
=> liste mélangé
'''
from random import * 
import time

def trie_selection(liste) : 
    liste_trié = []
    iteration = 0
    while len(liste) > 0 : 
        minimum = liste[0]

        for i in range(1, len(liste)) :
            if liste[i] < minimum :
                minimum = liste[i]


        index = liste.index(minimum)
        liste.pop(index)
        liste_trié.append(minimum)
        iteration += 1
    print(liste_trié)
    return iteration




def trie_insertion(liste) : 
    liste_trié =  [liste[0]]
    iteration = 0 
    for i in range(1, len(liste)) : 
        j = 0 
        continuer = True

        elm = liste[i]
        if elm > liste_trié[-1] : 
            liste_trié.append(elm)
            continuer = False
        elif elm < liste_trié[0] : 
            liste_trié = [elm] + liste_trié
            iteration += 1
            continuer = False
        
        while j < len(liste_trié) and continuer : 
            iteration += 1
            if elm < liste_trié[j] :
                liste_trié.insert(j, elm)
                continuer = False
            j += 1
    return iteration


print('-------------------------------------------')
print('------------------ TEST -------------------')
print('-------------------------------------------')

print('\n')

print('============ TRI PAR SELECTION ============')

print('\n')

liste = [i for i in range(800)]
liste2 = liste[:]
shuffle(liste2)
liste3 = liste[::-1]

print('______________MEILLEUR DES CAS_____________')
time_init = time.time()
iteration = trie_selection(liste)
time_final = time.time()
print(f'-> le nombre d iteration est de {iteration}')
print(f'-> le temps d execution est de {time_final - time_init} s')

print('________________PIRE DES CAS_______________')

time_init = time.time()
iteration = trie_selection(liste3)
time_final = time.time()
print(f'-> le nombre d iteration est de {iteration}')
print(f'-> le temps d execution est de {time_final - time_init} s')

print('_________________CAS MOYEN_________________')

time_init = time.time()
iteration = trie_selection(liste2)
time_final = time.time()
print(f'-> le nombre d iteration est de {iteration}')
print(f'-> le temps d execution est de {time_final - time_init} s')

print('\n')

print('============ TRI PAR INSERTION ============')

print('\n')

liste = [i for i in range(800)]
liste2 = liste[:]
shuffle(liste2)
liste3 = liste[::-1]

print('______________MEILLEUR DES CAS_____________')

time_init = time.time()
iteration = trie_insertion(liste)
time_final = time.time()
print(f'-> le nombre d iteration est de {iteration}')
print(f'-> le temps d execution est de {time_final - time_init} s')

print('________________PIRE DES CAS_______________')

time_init = time.time() 
iteration = trie_insertion(liste3)
time_final = time.time()
print(f'-> le nombre d iteration est de {iteration}')
print(f'-> le temps d execution est de {time_final - time_init} s')

print('_________________CAS MOYEN_________________')

time_init = time.time()
iteration = trie_insertion(liste2)
time_final = time.time()
print(f'-> le nombre d iteration est de {iteration}')
print(f'-> le temps d execution est de {time_final - time_init} s')

print('\n')
