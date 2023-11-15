'''

import random
import string

def duplicate_lettres(mot):
    lettre_vue = []  # Liste pour stocker les lettres déjà vues

    for lettre in mot:
        if lettre in lettre_vue:
            return True  # La lettre a déjà été vue, il y a donc une duplication
        else:
            lettre_vue.append(lettre)  # Ajouter la lettre à la liste des lettres vues

    return False

def master_mind(mot) :
    while True : 
        tentative = input('entrez 5 lettres ( il n \' y a pas deux fois la meme lettre ) : ')  #saisie d'une tentative de deviner
        tentative = tentative.upper()
        if tentative.isalpha() and len(tentative) == 5 :    #verification des condition de saisie
            result = []

            tentative = list(tentative.strip()) #transformation en tableau

            for i in range(5) :
                #print(tentative[i])
                lettre = tentative[i]
                if lettre in mot : 

                    if lettre == mot[i]:
                        result.append('V')
                    else : 
                        result.append('F')

            print(sorted(result)) 

            print('-----------------------')
            print('----- EXPLICATION -----')
            print('-----------------------')

            print('V = une lettre est bien placé')
            print('F = une lettre est mal  placé')

            if tentative == mot : 
                print('BRAVO !!! vous avez trouvez le mot qui etait ' , ''.join(mot))
                return


#CHOIX DU MOT

while True : 
    #CHOIX DU MOT A DEVINER
    mot = input('Saissiez  5 lettres à faire deviner ( ne mettez pas 2 lettres identiques ) : ')    #saisie du mot
    mot = mot.upper()   #mise en majuscule
    if mot.isalpha() and len(mot) == 5 and duplicate_lettres(mot) == False :    #verification des condition de saisie
        mot = list(mot.strip()) #transformation en tableau
        for i in range(30):
            print('                     ')
        master_mind(mot)

'''
import random

def duplicate_digits(mot):
    digit_seen = set()  # Set to store the digits already seen

    for digit in mot:
        if digit in digit_seen:
            return True  # The digit has already been seen, so there is a duplication
        else:
            digit_seen.add(digit)  # Add the digit to the set of seen digits

    return False

def master_mind(mot) :
    while True : 
        tentative = input('Entrez 5 chiffres (il n\'y a pas deux fois le même chiffre) : ')  # Input a guess
        if tentative.isdigit() and len(tentative) == 5:  # Check input conditions
            result = []

            for i in range(5):
                digit = tentative[i]
                if digit in mot:
                    if digit == mot[i]:
                        result.append('V')
                    else : 
                        result.append('F')

            print(sorted(result)) 

            print('-----------------------')
            print('----- EXPLICATION -----')
            print('-----------------------')

            print('V = un chiffre est bien placé')
            print('F = un chiffre est mal placé')

            if result ==  ['V', 'V', 'V', 'V', 'V'] : 
                print('BRAVO !!! vous avez trouvé le nombre qui était ' , ''.join(mot))
                break


# CHOICE OF THE NUMBER

while True : 
    # CHOICE OF THE NUMBER TO GUESS
    mot = input('Entrez 5 chiffres à faire deviner (ne mettez pas 2 chiffres identiques) : ')    # Input the number
    if mot.isdigit() and len(mot) == 5 and not duplicate_digits(mot):    # Check input conditions
        for i in range(30):
            print('                     ')
        master_mind(mot)
