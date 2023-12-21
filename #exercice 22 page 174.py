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
    elif bin1[0] != bin2[0] :
        somme = bin1[0] + bin2[0] + retenu
        if somme == 1 :     
            resultat[0] = 1
            retenu = 0  
        elif somme == 0 :
            resultat[0] = 0
            retenu = 0
        elif somme == 2 :
            resultat[0] = 0
            retenu = 1
        else :
            retenu = 1
            resultat[0] = 1
        return resultat
    elif retenu == 0 and bin1[0] == bin2[0] == 1 : 
        print("Il y a un dépassement. Ce calcul ne peut pas etre effectué avec ces deux nombres")
    else :
        return resultat

def inversion(n) : 
    n_inversé = [0]*8
    for i in range(8):
        if n[i] == 0 :
            n_inversé[i] = 1
    un = [0,0,0,0,0,0,0,1]
    n_inversé = add(n_inversé, un)
    if n[0] == 0 : 
        n_inversé[0] = 1
    return n_inversé

def binaire(n):

    n_binaire = [0]*8

    N = abs(n)
    for i in range(1, 8):
        n_binaire[abs(i - 8)] = N%2
        N = N//2 
    if n < 0 :
        n_binaire = inversion(n_binaire)
    return n_binaire

def decimal(n) : 
    dec = ""
    n_dec = 0
    if n[0] == 1 : 
        dec = "-"
        n = inversion(n)
    for i in range(7, 0, -1) :
        n_dec += n[i] * 2**(abs(i - 7))
    dec = dec + str(n_dec)
    return dec

def main(): 

    print("----- SAISIE -----")
    n1, n2 = entree()
    bin1 =  binaire(n1)
    print(f'votre nombre 1 en binaire vaut {"".join(map(str, bin1))}')
    bin2 =  binaire(n2)
    print(f'votre nombre 2 en binaire vaut {"".join(map(str, bin2))}')
    print("---- ADDITION ----")
    if add(bin1, bin2) != None :
        resultat = add(bin1, bin2)
        print(f'la somme des deux nombres est {"".join(map(str, resultat))} (en binaire) et vaut à {decimal(resultat)} (en decimal)')
    print("-- SOUSTRACTION --")
    print("n1 - n2 : ")
    if add(bin1, inversion(bin2)) != None :
        resultat = add(bin1, inversion(bin2))
        print(f"La difference du nombre 1 et du nombre 2 est {"".join(map(str, resultat))} (en binaire) et vaut à {decimal(resultat)} (en decimal)")
    print("n2 - n1 :")
    if add(bin2, inversion(bin1)) != None :
        resultat = add(bin2, inversion(bin1))
        print(f"La difference du nombre 1 et du nombre 2 est {"".join(map(str, resultat))} (en binaire) et vaut à {decimal(resultat)} (en decimal)")
    

main()
 
