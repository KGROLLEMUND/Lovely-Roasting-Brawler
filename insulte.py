import random  # Pour l'aléatoire.

"""
/!\ Veuillez SVP lire le readME pour mieux comprendre le fonctionnement du code. Merci bonne lecture.
#-----------------------------------------------------------------------------------------------------------------
# Déclaration des variables des textes du joueur 1, seules les variables verbe et again sont les mêmes.
# Lecture des fichiers txt
#-----------------------------------------------------------------------------------------------------------------
"""
player1adj = open('player1adj.txt').read().split('\n')           
player1noms= open('player1noms.txt').read().split('\n')
player1insulte = open('player1insulte.txt').read().split('\n')   
verbe = open('verbe.txt').read().split('\n')
again = open('again.txt').read().split('\n')                     

"""
#-----------------------------------------------------------------------------------------------------------------#
# Déclaration des variables des textes du joueur 2. Pour les joueurs. Nous avons en tous 8 fichier textes txt.
#-----------------------------------------------------------------------------------------------------------------#
"""

player2adj = open('player2adj.txt').read().split('\n')
player2noms= open('player2noms.txt').read().split('\n')
player2insulte = open('player2insulte.txt').read().split('\n')


"""
#-----------------------------------------------------------------------------------------------------------------#
# Déclaration des prénoms, ça serait une liste des prénoms à sélectionnés. Vous êtes même dedans.
#-----------------------------------------------------------------------------------------------------------------#
"""
prenom =["Marc","Eric","KEVIN", "KILLIAN","Melvin LEVANNHAN","Jorge","Melvin","Jonathan graux","Vitaly","Axel","Hadil Friaa", "Janin LOIC"]
player1adj_choice =player1adj
player1noms_choice = player1noms
player1insulte_choice =player1insulte
player2adj_choice =player2adj
player2noms_choice = player2noms
player2insulte_choice =player2insulte
verbe_choice = verbe
again_choice = again

"""
#-----------------------------------------------------------------------------------#
# L'interface de la fonction du joueur 1
# On a un compteur pour les listes d'adjectif,de noms,de verbe et d'insulte pour la sélection
# Des saisies de texte sur le Terminal
# Enfin des dégâts aléatoire enfin des choix de sélections des verbes,noms,adj et d'insultes
#-----------------------------------------------------------------------------------#
"""


def playerOne(list_insult):
    sentencePlayerOne = []
    trashtalkPlayerOne = ""
    counterPlayerOne = 0
    damagePlayerOne=0
   

    for verbal_abuse in list_insult:

        text = " ═ ═ ═ ═ ═ ═(JOUEUR 1) ═ ═ ═ ═ ═ ═\n"
        for elem in verbal_abuse:
            text += elem + "\n"
        text += " ═ ═ ═ ═ ═ ═(JOUEUR 1) ═ ═ ═ ═ ═ ═\n"

        

        print(text)

        valide = False
       
        while not valide:
            counterPlayerOne = counterPlayerOne+ 1
            choicePlayerOne = input(" Joueur 1 à toi de choisir un mot dans la liste : ")
            if choicePlayerOne not in verbal_abuse:
                print(f"{choicePlayerOne} joue pas au con et sélectionne bien un mot dans la liste ! :")
            else:
                print(f"{choicePlayerOne} a été sélectionné.")
                valide = True
                print("\n")

                if (counterPlayerOne == 1) : # Lorsqu'on choisit un prénom, les dégâts sont aléatoire c'est des dégâts entre 0 à 50
                    damagePlayerOne = damagePlayerOne + random.randint(0, 50)
                    print("Sacrée prénom dis-donc. Les dégâts infligées sont de", damagePlayerOne,"dégâts")
                    
                    
                if (counterPlayerOne == 2) :  # Lorsqu'on choisit un nom, le dégât sont aléatoire c'est des dégâts entre 0 à 20
                    damagePlayerOne = damagePlayerOne + random.randint(0, 20)
                    print("Whaou eh bien les dégâts sont de ", damagePlayerOne,"dégâts")

                if (counterPlayerOne == 3) : # Lorsqu'on choisit un verbe, les dégât sont aléatoire c'est des dégâts entre 0 à 60
                    damagePlayerOne = damagePlayerOne + random.randint(0, 60)
                    print("Incroyable les dégâts ! ", damagePlayerOne,"dégâts")

                if (counterPlayerOne == 4) : # Lorsqu'on choisit un prénom, les dégâts sont aléatoire c'est des dégâts entre 0 à 100
                    damagePlayerOne = damagePlayerOne + random.randint(0, 100)
                    print("Tu as un problème toi ! : ", damagePlayerOne,"dégâts")

                if (counterPlayerOne == 5) : # Lorsqu'on choisit un adjectif, les dégâts sont aléatoire c'est des dégâts entre 0 à 100
                    damagePlayerOne = damagePlayerOne + random.randint(0, 100)
                    print("Le grand Malade tu es pire que Janin Loic en trashtalk ", damagePlayerOne,"dégâts")

                if (counterPlayerOne == 6) : # Lorsqu'on choisit une insulte, les dégâts sont aléatoire c'est des dégâts entre 0 à 100
                    damagePlayerOne = damagePlayerOne + random.randint(0, 100)
                    print("Tu connais pas Janin Loic ? C'est le plus grand trashtalker du monde. Il peut t'insulter même quand il dort  ", damagePlayerOne,"dégâts")

                #if (counterPlayerOne == 7) :
                  #  damagePlayerOne = damagePlayerOne + random.randint(0, 100)
                   # print("dégat est ", damagePlayerOne)
                 

                 
        trashtalkPlayerOne += choicePlayerOne + " "
        print("\n")


    print(trashtalkPlayerOne + "!" )
    print("Vous avez fait", damagePlayerOne , "dégâts")
    if damagePlayerOne > 200 :
        print("Et bien toi tu es un(e) petit(e) morveux(se) dis-donc t'aime bien insulter les gens. Bravo pour ta performance Joueur 1")
    elif damagePlayerOne < 200 :
        print("Bof c'est pas terrible tes insultes peut mieux faire. Tu es vraiment une crotte joueur 1 ")

      
   

    return damagePlayerOne


playerOne([prenom,player1noms_choice, verbe_choice, player1adj_choice,again_choice,player1insulte_choice])


"""
#-----------------------------------------------------------------------------------#
# L'interface de la fonction du joueur 
#-----------------------------------------------------------------------------------#
"""

def playerTwo(list_insult):
    sentencePlayerTwo = []
    trashtalkPlayerTwo = ""
    counterPlayerTwo = 0
    damagePlayerTwo=0

    for verbal_insult in list_insult:

        text = " ═ ═ ═ ═ ═ (JOUEUR 2) ═ ═ ═ ═ ═ ═ ═\n"
        for elem in verbal_insult:
            text += elem + "\n"
        text += " ═ ═ ═ ═ ═(JOUEUR 2)═ ═ ═ ═ ═ ═ ═\n"

        

        print(text)

        valide = False
       
        while not valide:
            counterPlayerTwo = counterPlayerTwo+ 1
            choicePlayerTwo = input(" Joueur 2, bon courage ! Choisis un mot : ")
            if choicePlayerTwo not in verbal_insult:
                print(f"{choicePlayerTwo} Vous êtes cons joueur 1 ou joueur 2, vous ne savez pas lire allez choissiisez un mot sur la liste ! :")
            else:
                print(f"{choicePlayerTwo} a été sélectionné.")
                valide = True
                print("\n")

                if (counterPlayerTwo == 1) :
                    damagePlayerTwo = damagePlayerTwo + random.randint(0, 50)
                    print("Tu as infligées ", damagePlayerTwo, "dégâts")
                if (counterPlayerTwo == 2) :
                    damagePlayerTwo = damagePlayerTwo + random.randint(0, 20)
                    print("Tu es un vrai beauf ", damagePlayerTwo, "dégâts")
                if (counterPlayerTwo == 3) :
                    damagePlayerTwo = damagePlayerTwo + random.randint(0, 60)
                    print("Tu te débrouilles bien ", damagePlayerTwo,"dégâts")

                if (counterPlayerTwo== 4) :
                    damagePlayerTwo = damagePlayerTwo + random.randint(0, 100)
                    print("Janin Loic sera PTDR hahaha ", damagePlayerTwo,"dégâts")

                if (counterPlayerTwo == 5) :
                    damagePlayerTwo = damagePlayerTwo + random.randint(0, 100)
                    print("Alors là chapeau  ", damagePlayerTwo,"dégâts")

                if (counterPlayerTwo == 6) :
                    damagePlayerTwo = damagePlayerTwo + random.randint(0, 100)
                    print("Arrêtes de me faire rire stp hahahaa ", damagePlayerTwo,"dégâts")

                #if (i == 7) :
                  #  damagePlayerOne = damagePlayerOne + random.randint(0, 100)
                   # print("dégat est ", damagePlayerOne)
                 

                 
        trashtalkPlayerTwo += choicePlayerTwo + " "
        print("\n")

    print(trashtalkPlayerTwo + "!" )
    print("Vous avez fait", damagePlayerTwo , "dégâts")
    if damagePlayerTwo > 200 :
        print("Mais tu es un fou, tu m'as fais trop rire Joueur 2")
    elif damagePlayerTwo < 200 :
        print("Je n'ai pas rigolé aujourd'hui. Tu me dégoûtes hors de ma vu sale Joueur 2 ")
    print("Eh bien joueur(se) 2 , tu es aussi malade que le joeur(se)1. C'est bien tu fais honneur à ton professeur Janin Loic !!!")
    return damagePlayerTwo
    #print("Partie Terminée",damagePlayerOne, damagedamagePlayerTwo)


playerTwo([prenom,player2noms_choice,verbe_choice, player2adj_choice, again_choice, player2insulte_choice])

    
print("Partie Terminée, vous êtes tous les 2 fous. Je vous ai donné le score mais j'ai la flemme de calculer alors démerdez-vous les macaques ")

"""
#-----------------------------------------------------------------------------------------------------------------
# Si les dégats son supérieur à 200 on a un commentaire positif
# Sinon si les dégâts sont inférieur à 200 on a un commentaire négatif
#-----------------------------------------------------------------------------------------------------------------
"""
