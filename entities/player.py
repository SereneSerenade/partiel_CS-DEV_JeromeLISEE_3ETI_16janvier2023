'''

fichier player : classe de l'objet controlé par le joueur
Jerome Lisee
16 janvier 2023

'''

class Player():

    def __init__(self, x, y, w, h): #initialise les coordonnées et la taille du player

        #en entrée : les coordonnées et la taille 
        #pas de sortie

        self.x = x
        self.y = y #constante
        self.w = w #constante
        self.h = h #constante


    def getCoords(self): #donne les coordonnées
        return  self.x, self.y 
    
    def moveLeft(self, event): #déplace vers la gauche le player 
        if self.x > 0:
            self.x -= 12

    def moveRight(self, event): #déplace vers la droite le player
        if self.x < 1220:
            self.x += 12