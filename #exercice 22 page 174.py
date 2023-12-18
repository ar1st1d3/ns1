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
    print(f'la somme des nombres {n1} et {n2} est égale à {n1 + n2}')
    bin1 = binaire(n1)
    bin2 = binaire(n2)
    somme = [0] * 8
    retenu = 0
    for i in range(7) : 
        j = abs(i - 8)
        addition = bin1[j] + bin2[j] + retenu
        if addition == 2 : 
            somme[j] = 0
            retenu = 1
        elif addition == 3 :
            somme[j] = 1
            retenu = 1
        else : 
            somme = 0
            retenu = 0

        if i == 7 and retenu == 1 : 
            print('Erreur il y a un dépassement lors de la somme de ces deux nombres')
    print('la somme de ces deux nombres en base 2 est de ', int(''.join(map(str, somme))))


def main(): 

    n1, n2 = entree()
    bin1 =  int(''.join(map(str, binaire(n1)))) 
    print(f'{bin1 = }')
    bin2 =  int(''.join(map(str, binaire(n2)))) 
    print(f'{bin2 = }')
    add(n1, n2)

main()