'''

fichier player : classe de l'objet brick que le joueur doit détruire pour gagner
Jerome Lisee
16 janvier 2023

'''

class Brick():
    
    def __init__(self, x, y, w, h): #initialise les coordonnées et la taille du player

        #en entrée : les coordonnées et la taille 
        #pas de sortie
        
        self.x = x #constante 
        self.y = y #constante
        self.w = w #constante
        self.h = h #constante