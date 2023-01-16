'''

fichier window : gere l'affichage de la fenetre et de ses elements
de Jerome Lisee 
16 janvier 2023

'''


from tkinter import Canvas, Tk, Button, Label

class Window():

    def __init__(self, w, h): #Initialisation de l'interface graphique avec le module tkinter

        #en entrée : la largeure w et hauteur h de la fenetre
        #pas de sortie

        self.mainWindow = Tk()
        self.mainWindow.title('block breaker')
        self.mainWindow.geometry(f"{w}x{h}")
        self.Canvas = Canvas(self.mainWindow, width = 1280, height = 720, background = "#000144")


    def mainMenu(self): #Fenêtre du menu principal

        #pas d'entrée
        #pas de sortie

        newgame = Button(self.mainWindow ,text = "New Game" ,command = self.newGame)
        quit = Button(self.mainWindow ,text = "Quit" ,command = self.mainWindow.destroy)
        score = Label(self.mainWindow ,text = "score : " + str(self.score))     
        self.title = self.Canvas.create_text(640,360, fill = '#FF822C' ,text = 'block breaker' ,font = ("arial", 30))

        quit.pack(side = 'top' , padx = 0 , pady = 0)
        newgame.pack(side = 'top' , padx = 0 , pady = 0)
        score.pack(side = 'top' ,padx = 0 ,pady = 0)
        self.Canvas.pack(padx = 5,pady = 5)

    def playerDisplay(self, x, y, w, h): #Fonction qui gère l'affichage du joueur

        #en entrée : les coordonnées et la taille du player
        #en sortie : le rectangle représentant le joueur

        self.playerSprite = self.Canvas.create_rectangle(x, y, x + w, y + h, outline = "#ff0000", fill = "#ff0000")
        return self.playerSprite


    def brickDisplay(self, x, y, w, h): #Affichage d'une brick sur le Canvas

        #en entrée : les coordonnées et la taille de la brick
        #en sortie : le rectangle représentant brick
        
        self.brickSprite = self.Canvas.create_rectangle(x, y, x + w, y + h, outline = "#fb0", fill = "#fb0")
        return self.brickSprite

    def ballDisplay(self, x, y, rad): #Affichage de la ball sur le Canvas

        #en entrée : les coordonnées et la taille de la ball
        #en sortie : le cercle représentant la ball
        
        self.ballSprite = self.Canvas.create_oval(x - rad, y-rad, x + rad, y + rad, width = 0, outline = "#fb0", fill = "#fb0")
        return self.ballSprite


    def functionLink(self, newGame): #Méthode qui fait le lien entre le jeu et l'interface graphique 

        #en entrée : la fonction newGame (renommée GameStart dans la classe game)
        #pas de sortie

        self.newGame = newGame

    

    def attributeLink(self,score): #permet de lier le score de la classe game a l'affichage dans la classe window

        #en entrée : le score
        #pas de sortie

        self.score = score

