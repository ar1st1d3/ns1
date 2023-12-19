#exercice 22 page 174

def entree(): 

    nombre = [0, 0]
    for i in range(2):
        continuer = True

        while continuer:
            n = input("entrez un entier entre -128 et 127 : ")

            if n.lstrip('-').isdigit() and -128 <= int(n) <= 127:
                print(f'Le nombre {i + 1} a bien été pris en compte')
                continuer = False
                nombre[i] = int(n)
            else:
                print("Veuillez entrer un entier valide entre -128 et 127.")
    
    return nombre

def binaire(n):

    n_binaire = [0]*8
    if n < 0 : 
        n_binaire[0] = 1
    n = abs(n)
    for i in range(1, 7):
        n_binaire[abs(i - 8)] = n%2
        n = n//2 
    return n_binaire

def add(n1, n2):
    print(f'La somme des nombres {n1} et {n2} est égale à {n1 + n2}')
    bin1 = binaire(n1)
    bin2 = binaire(n2)
    somme = [0] * 8
    retenu = 0
    for i in range(7): 
        j = abs(i - 7)
        addition = bin1[j] + bin2[j] + retenu
        if addition == 2: 
            somme[j] = 0
            retenu = 1
        elif addition == 3:
            somme[j] = 1
            retenu = 1
        else: 
            somme[j] = addition
            retenu = 0

    if retenu == 1: 
        print('Erreur : il y a un dépassement lors cette operation avec ces deux nombres')

    print('La somme de ces deux nombres en base 2 est de', somme)

def sub(n1, n2):
    print(f'La différence des nombres {n1} et {n2} est égale à {n1 - n2}')
    bin1 = binaire(n1)
    bin2 = binaire(n2)
    difference = [0] * 8
    retenue = 0

    for i in range(7): 
        j = abs(i - 7)
        soustraction = bin1[j] - bin2[j] - retenue
        if soustraction == -1: 
            difference[j] = 1
            retenue = 1
        elif soustraction == -2:
            difference[j] = 0
            retenue = 1
        else: 
            difference[j] = soustraction
            retenue = 0

    if retenue == 1: 
        print('Erreur : il y a un dépassement lors de la soustraction de ces deux nombres')

    print('La différence de ces deux nombres en base 2 est de', difference)



def main(): 

    n1, n2 = entree()
    bin1 =  int(''.join(map(str, binaire(n1)))) 
    print(f'{bin1 = }')
    bin2 =  int(''.join(map(str, binaire(n2)))) 
    print(f'{bin2 = }')
    add(n1, n2)
    sub(n1, n2)

main()
