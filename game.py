'''
fichier game : classe "game" qui gere l'interaction entre les classes des objets du jeu et le déroulement des fonctionalités du jeu
Jerome Lisee
16 janvier 2023 

'''


from window import Window
from entities.player import Player
from entities.brick import Brick
from entities.ball import Ball

class Game(Window): #Classe Jeu héritée de la classe Fenêtre (gestion de l'interface)
    
    def GameLaunch(self): #Fonction Initialisant le jeu

        #en entrée : vide
        #en sortie : vide 

        self.score = 0
        Window.attributeLink(Game,self.score)
        Window.functionLink(Game,self.startGame)
        self.mainMenu()
        self.mainWindow.mainloop()


    def startGame(self): #Fonction qui met en place le lancement d'une partie et gère la boucle principale (agit aussi comme un innit)

        #en entrée : vide
        #en sortie : vide 

        self.Canvas.delete('all')
        self.level = 0
        self.score = 0
        self.lstPlayer = []
        self.lstBall =[]
        self.gameLoop(3, 0)

    def gameLoop(self, score, level): #Boucle principale du jeu

        #en entrée : le nombre de vies restantes, le niveau de difficulté (pas implémenté)
        # en sortie : vide

        self.level = level
        self.life = score
        self.spawnBricks()
        self.spawnBall()
        self.moveBall()
        self.spawnPlayer()
        self.keybindPlayer()
        self.playerMove()

    
    def spawnBricks(self): #fonction qui gere l'apparition des bricks

        #pas d'entrée
        #en sortie : une liste de listes des bricks et leur représentation sur le canvas

        self.lstBrick=[]
        for i in range(3, 10):
            brick = Brick(i*100, 200, 60, 40)
            brickDisp = self.brickDisplay(brick.x, brick.y, brick.w, brick.h)
            self.lstBrick.append([brick, brickDisp])
        return self.lstBrick
    
    def spawnBall(self): #fonction qui gere l'apparition de la ball

        #en entrée : vide
        #en sortie : l'objet de la classe ball qui rebondit entre le joueur et les bricks

        self.ball = Ball(500, 500, 10)
        self.ballDisp = self.ballDisplay(self.ball.x, self.ball.y, self.ball.rad)
        self.lstBall.append([self.ball, self.ballDisp])
        return self.ball

    def moveBall(self): #fonction qui gere le déplacement de la balle

        #pas d'entrée
        #pas de sortie
        
        if self.ball.xSpeed == self.ball.ySpeed == 0:
            self.ball.xSpeed = 5 #vers la droite
            self.ball.ySpeed = 5 #vers le bas
        self.ball.move()
        self.Canvas.coords(self.ball.x + self.ball.xSpeed, self.ball.y + self.ball.ySpeed, self.ball.rad)
        self.Canvas.after(3, self.moveBall)

    def spawnPlayer(self): #Fonction qui gère l'apparition du joueur

        #en entrée : vide
        #en sortie : l'objet de classe player contrôlé par le joueur

        self.player = Player(600, 600, 80, 20)
        self.playerDisp = self.playerDisplay(self.player.x, self.player.y, self.player.w, self.player.h)
        self.lstPlayer.append([self.player, self.playerDisp])
        return self.player

    def playerMove(self): #Fonction qui gère le déplacement du joueur

        #en entrée : vide
        #en sortie : vide

        self.Canvas.coords(self.playerSprite, self.player.x, self.player.y, self.player.x + self.player.w, self.player.y + self.player.h)
        self.Canvas.after(5, self.playerMove)

    #def collisionBall(self, lstBrick): #fonction qui gere la collision entre la ball, la brick,  le player ou les murs. lorsque la collision a lieu, inverse xSpeed et ySpeed de la ball

    #en entrée : la liste des bricks
    #en sortie : True si une collision a eu lieu, False sinon
    
    def keybindPlayer(self): #Fonction qui gère la liaison entre les touches du clavier et le déplacement du player

        #en entrée : vide
        #en sortie : vide

        self.mainWindow.bind('<Left>', self.player.moveLeft)
        self.mainWindow.bind('<Right>', self.player.moveRight)


Jeu = Game(1280, 720)
Jeu.GameLaunch()