import random

#---------version1---------#

def load_mot(): #recupere un mot aleatoire du fichier mots.txt

    a = random.randrange(0,10,1)

    with open('/fs03/share/users/jerome.lisee/home/mots.txt','r') as fich:
        return fich.readlines()[a]
    
    

    
def remplace_lettre(lettre, lst_mot, lst_cache): # remplace l'underscore de lst_cache par la lettre appropriée

    for i,val in enumerate(lst_mot):
        if val == lettre:
            lst_cache[i] = val

    return lst_cache    


def choisir_lettre(): #recursive de combat pour saisie protegee

    lettre = str(input("choisir une lettre (minuscule) : "))

    if lettre not in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        print("ce n'est pas une lettre minuscule, petit filou")
        choisir_lettre()

    else :
        return lettre


def saisie_protegee_yn(): #recursive de combat pour saisie protegee

    yn = str(input("Voulez vous jouer au pendu (Y/N) ? : "))

    if yn not in ['Y','N']:
        print("ce n'est pas Y ou N, petit filou")
        saisie_protegee_yn()

    else :
        return yn


def jouer_au_jeu(mot): #fait jouer l'utilisateur au pendu 

    lst_mot = list(mot)[:-1]
    lst_cache = [lst_mot[0]]
    str_echecs = " "
    chance = 8

    for i in range(len(lst_mot) - 1):
        lst_cache.append("_")

    while chance > 0 and "_" in lst_cache:
        print("chances restantes = ", chance)
        print(lst_cache)
        print("tentatives erronées : ",str_echecs )
        lettre = choisir_lettre()

        if lettre in lst_cache:
            print("cette lettre est deja placée")

        elif lettre not in lst_mot:
            if lettre not in list(str_echecs):
                str_echecs += str(lettre)
            chance -= 1

        else :
            lst_cache = remplace_lettre(lettre, lst_mot, lst_cache)
        print("")

    if chance > 0:
        print("Bravo ! Vous avez réussi !")
        return 1, 0, chance

    else :
        print("Dommage, vous avez perdu :(")
        return 0, 1, 0


wanna_play = saisie_protegee_yn()
best_score = -1
wins = 0
loses = 0
score = 0
while wanna_play == 'Y':
    
    wins, loses, score +=jouer_au_jeu(load_mot())

    if best_score < score:
        best_score = score

    print("meilleur score (nombre de vies restantes) de ", best_score, ", ", wins, " victoires", loses, " défaites, pour un ratio de victoire de ", wins/loses)
    wanna_play = saisie_protegee_yn()

print(" à la prochaine fois !")



            
