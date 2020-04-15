print("|================|")
print("| Épreuve du feu |")
print("|   L'escalier   |")
print("|================|")
print("")

nb_marche = int(input("Combien de marche pour votre escalier ? "))
hauteur = 0
n = 1

if nb_marche == 0 :
    print("Il me faut des marches pour pouvoir dessiner ! ")
else :
    while n != nb_marche + 1 :
        hauteur = nb_marche - n
        print((hauteur * " ") + ("#" * n))
        n += 1

# Résultats :
# | Combien de marche pour votre escalier ? 5
# |      #
# |     ##
# |    ###
# |   ####
# |  #####
