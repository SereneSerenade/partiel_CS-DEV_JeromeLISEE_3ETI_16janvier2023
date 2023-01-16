'''

fichier player : classe de l'objet ball que le joueur uilise pour détruire
 les bricks en le faisant rebondir sur l'objet player
Jerome Lisee
16 janvier 2023

'''

class Ball():
    
    def __init__(self, x, y, rad, xSpeed = 0, ySpeed = 0): #initialise les coordonnées, le radius et la direction de mouvement de la ball

        #en entrée : les coordonnées, le radius, et la direction de la balle
        #pas de sortie
        
        self.x = x 
        self.y = y 
        self.rad = rad #constante
        self.xSpeed = xSpeed #sans mouvement au spawn
        self.ySpeed = ySpeed #sans mouvement au spawn

    def move(self): #déplace la ball dans les directions xspeed et yspeed

        #pas d'entrée
        #pas de sortie

        self.x += self.xSpeed
        self.y += self.ySpeed
