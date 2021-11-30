from math import sqrt

def second_degre () :
    a = float (input("Choisir un nombre a = "))
    b = float (input("Choisir un nombre b = "))
    c = float (input("Choisir un nombre c = "))
    delta = b**2 -4*a*c
    if a == 0 :
        print ("L'équation n'est pas du second degré.")
    else :
        if delta < 0 :
            texte = "On ne peut pas résoudre cette équation"
            print (texte)  
        elif delta == 0 :
            solution = -b /(2*a)
            texte = "L'unique solution de l'équation est " \
                    + str (solution)
            print (texte) 
        else :
            solution1 = (-b - sqrt (delta))/(2*a)
            solution2 = (-b + sqrt (delta))/(2*a)
            texte1 = "La premiere solution de l'equation est " \
                     + str (solution1) + " et "
            texte2 = "la seconde solution de l'equation est " \
                     + str (solution2) 
            print (texte1, texte2)
second_degre ()
 
            
