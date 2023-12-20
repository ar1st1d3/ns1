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

def add(bin1, bin2):

    resultat = [0]*8
    somme = 0
    retenu = 0

    for i in range(7, 0, -1):
        somme = bin1[i] + bin2[i] + retenu
        if somme == 1 :
            resultat[i] = 1
            retenu = 0  
        elif somme == 0 :
            resultat[i] = 0
            retenu = 0
        elif somme == 2 :
            resultat[i] = 0
            retenu = 1
        else :
            retenu = 1
            resultat[i] = 1
    if retenu == 1 and bin1[0] == bin2[0] == 0 : 
        print("Il y a un dépassement. Ce calcul ne peut pas etre effectué avec ces deux nombres")
    else :
        return resultat

def inversion(n) : 
    print(n)
    n_inversé = [0]*8
    for i in range(8):
        if n[i] == 0 :
            n_inversé[i] = 1
    un = [0,0,0,0,0,0,0,1]
    print(n_inversé)
    n_inversé = add(n_inversé, un)
    print(n_inversé)
    return n_inversé

def binaire(n):

    n_binaire = [0]*8

    N = abs(n)
    for i in range(1, 8):
        n_binaire[abs(i - 8)] = N%2
        N = N//2 
    if n < 0 :
        n_binaire = inversion(n_binaire)
        print(n_binaire)
    return n_binaire




def main(): 

    n1, n2 = entree()
    bin1 =  binaire(n1)
    print(f'votre nombre 1 en binaire vaut {"".join(map(str, bin1))}')
    bin2 =  binaire(n2)
    print(f'votre nombre 2 en binaire vaut {"".join(map(str, bin2))}')
    if add(bin1, bin2) != None :
        print(f'la somme des deux nombres est {add(bin1, bin2)}(en binaire) et vaut à (en decimal   )')

main()
