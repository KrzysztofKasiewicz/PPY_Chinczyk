from tkinter import *
import random

from DbHandler import DbHandler
from Options import OptionValues
#player1 = blue, player2 = red, player3 = yellow, player4 = green

class Game:
    def __init__(self,playerNames):
        self.root = Tk()
        self.root.title("Game")

        settings = OptionValues()
        self.tilesize = settings.tilesize
        self.progWyjscia = settings.progWyjscia
        self.animationSpeed = settings.animationSpeed
        self.howManyPawns = settings.howManyPawns

        self.blue = "blue"
        self.yellow = "#E1C143"
        self.green = "green"
        self.red = "red"
        self.highlightColor = "purple"


        self.fullDirections = ["START","E","E","E","E","E","E","E","N","N","N","N","N","N","N","E","E","S","S","S","S","S","S","S","E","E","E","E","E","E","E","S","S","W","W","W","W","W","W","W","S","S","S","S","S","S","S","W","W","N","N","N","N","N","N","N","W","W","W","W","W","W","W","N","E","E","E","E","E","E","E"]

        self.playerNames = playerNames
        self.numberOfPlayers = len(playerNames)
        self.playerTurn = random.randint(1,self.numberOfPlayers)
        self.tilesToMove = 0



        self.canvas = Canvas(self.root, width=self.tilesize*17, height=self.tilesize*17, bg="Black")
        self.canvas.pack()
        self.drawBoard()
        self.nextPlayer()

        self.pawns = []

        for i in range(1, self.numberOfPlayers+1):
            self.pawns.append([])
            for j in range(self.howManyPawns):
                self.createPawn(i)


        self.root.mainloop()

    def drawBoard(self):
        tilesize = self.tilesize

        self.canvas.create_rectangle(0, 0, tilesize*2, tilesize*2, fill=self.blue)
        self.canvas.create_rectangle(tilesize*15, 0, tilesize*17, tilesize*2, fill=self.yellow)
        self.canvas.create_rectangle(0, tilesize*15, tilesize*2, tilesize*17, fill=self.green)
        self.canvas.create_rectangle(tilesize*15, tilesize*15, tilesize*17, tilesize*17, fill=self.red)

        self.canvas.create_text(tilesize, tilesize, text = self.playerNames[0], font=("Arial",tilesize//3))
        self.canvas.create_text(tilesize*16, tilesize*16, text = self.playerNames[1], font=("Arial",tilesize//3))
        if self.numberOfPlayers > 2:
            self.canvas.create_text(tilesize*16, tilesize, text = self.playerNames[2], font=("Arial",tilesize//3))
        if self.numberOfPlayers > 3:
            self.canvas.create_text(tilesize, tilesize*16, text = self.playerNames[3], font=("Arial",tilesize//3))

        for i in range(8):
            self.canvas.create_rectangle(tilesize*7, tilesize*i, tilesize*8, tilesize*(i+1), fill="white", outline="black", width=2)
            self.canvas.create_rectangle(tilesize*7, tilesize*(9+i), tilesize*8, tilesize*(i+10), fill="white", outline="black", width=2)
            self.canvas.create_rectangle(tilesize*9, tilesize*i, tilesize*10, tilesize*(i+1), fill="white", outline="black", width=2)
            self.canvas.create_rectangle(tilesize*9, tilesize*(9+i), tilesize*10, tilesize*(i+10), fill="white", outline="black", width=2)

            self.canvas.create_rectangle(tilesize*i, tilesize*7, tilesize*(i+1), tilesize*8, fill="white", outline="black", width=2)
            self.canvas.create_rectangle(tilesize*(9+i), tilesize*7, tilesize*(i+10), tilesize*8, fill="white", outline="black", width=2)
            self.canvas.create_rectangle(tilesize*i, tilesize*9, tilesize*(i+1), tilesize*10, fill="white", outline="black", width=2)
            self.canvas.create_rectangle(tilesize*(9+i), tilesize*9, tilesize*(i+10), tilesize*10, fill="white", outline="black", width=2)

        self.canvas.create_rectangle(tilesize * 8, tilesize * 0, tilesize * 9, tilesize * 1, fill="white",outline="black", width=2)
        self.canvas.create_rectangle(tilesize * 8, tilesize * 16, tilesize * 9, tilesize * 17, fill="white",outline="black", width=2)
        self.canvas.create_rectangle(tilesize * 0, tilesize * 8, tilesize * 1, tilesize * 9, fill="white",outline="black", width=2)
        self.canvas.create_rectangle(tilesize * 16, tilesize * 8, tilesize * 17, tilesize * 9, fill="white",outline="black", width=2)

        self.canvas.create_line(tilesize*9+tilesize/2,tilesize*0,tilesize*10 - tilesize/2,tilesize*1, arrow ="last", fill = self.yellow,width = tilesize//7 +1)
        self.canvas.create_line(tilesize*7+tilesize/2,tilesize*16,tilesize*8 - tilesize/2,tilesize*17, arrow ="first", fill = self.green,width = tilesize//7 +1)
        self.canvas.create_line(tilesize*0,tilesize*7+tilesize/2,tilesize*1,tilesize*7+tilesize/2, arrow ="last", fill = self.blue,width = tilesize//7 +1)
        self.canvas.create_line(tilesize*16,tilesize*9+tilesize/2,tilesize*17,tilesize*9+tilesize/2, arrow ="first", fill = self.red,width = tilesize//7 +1)



        for i in range(6):
            self.canvas.create_rectangle(tilesize*8,tilesize*(i+1),tilesize*9,tilesize*(i+2), fill=self.yellow,outline="black", width=2)
            self.canvas.create_rectangle(tilesize*8,tilesize*(i+10),tilesize*9,tilesize*(i+11), fill=self.green,outline="black", width=2)
            self.canvas.create_rectangle(tilesize*(i+1),tilesize*8,tilesize*(i+2),tilesize*9, fill=self.blue,outline="black", width=2)
            self.canvas.create_rectangle(tilesize*(i+10),tilesize*8,tilesize*(i+11),tilesize*9, fill=self.red,outline="black", width=2)

        self.rollButton = Button(self.root, text = "Roll", command = self.rollDice, font=("Arial",tilesize//3))
        self.canvas.create_window(tilesize*8+tilesize/2,tilesize*8+tilesize/2, window = self.rollButton)

    def createPawn(self,team):
        sizeCorrection = self.tilesize / 5
        pawn = {"atTile": 0, "team": team, "direction": self.fullDirections.copy()}
        match team:
            case 1:
                pawn["id"] = self.canvas.create_oval(self.tilesize * 2 + sizeCorrection,
                                                     self.tilesize * 0 + sizeCorrection,
                                                     self.tilesize * 3 - sizeCorrection,
                                                     self.tilesize * 1 - sizeCorrection, fill=self.blue)
            case 2:
                pawn["id"] = self.canvas.create_oval(self.tilesize * 14 + sizeCorrection,
                                                     self.tilesize * 16 + sizeCorrection,
                                                     self.tilesize * 15 - sizeCorrection,
                                                     self.tilesize * 17 - sizeCorrection, fill=self.red)
            case 3:
                pawn["id"] = self.canvas.create_oval(self.tilesize * 14 + sizeCorrection,
                                                     self.tilesize * 0 + sizeCorrection,
                                                     self.tilesize * 15 - sizeCorrection,
                                                     self.tilesize * 1 - sizeCorrection, fill=self.yellow)
            case 4:
                pawn["id"] = self.canvas.create_oval(self.tilesize * 2 + sizeCorrection,
                                                     self.tilesize * 16 + sizeCorrection,
                                                     self.tilesize * 3 - sizeCorrection,
                                                     self.tilesize * 17 - sizeCorrection, fill=self.green)
        self.pawns[team-1].append(pawn)

    def nextPlayer(self):
        self.tilesToMove = 0
        self.playerTurn += 1
        if self.playerTurn > self.numberOfPlayers:
            self.playerTurn = 1

        match self.playerTurn:
            case 1:
                self.rollButton.config(bg = self.blue)
            case 2:
                self.rollButton.config(bg=self.red)
            case 3:
                self.rollButton.config(bg=self.yellow)
            case 4:
                self.rollButton.config(bg=self.green)



    def rollDice(self):

        if self.tilesToMove == 0:
            self.tilesToMove = random.randint(1,6)
            self.rollButton.config(text = self.tilesToMove)
            self.highlight()


    def deHighlight(self):
        self.rollButton.config(text="Roll")
        for pawn in self.pawns[self.playerTurn-1]:
            self.canvas.itemconfig(pawn["id"], outline="",width=0)
            self.canvas.tag_unbind(pawn["id"],"<Button-1>")

    def highlight(self):
        possibilities = []
        for pawn in self.pawns[self.playerTurn-1]:
            if self.willCollide(pawn["atTile"]):
                continue
            if pawn["direction"][0] == "START" and not self.tilesToMove>=self.progWyjscia:
                continue
            if len(pawn["direction"])<self.tilesToMove+1:
                continue
            else:
                self.canvas.itemconfig(pawn["id"],outline = self.highlightColor,width = 2)
                self.canvas.tag_bind(pawn["id"],"<Button-1>",lambda event, p=pawn:self.moveHandler(p))
                possibilities.append(pawn)
        if len(possibilities) == 0:
            self.nextPlayer()
            self.rollButton.config(text="Roll")


    def willCollide(self,atTile):
        for pawn in self.pawns[self.playerTurn - 1]:
            if pawn["atTile"]-self.tilesToMove == atTile:
                return True
        return False

    def moveHandler(self,pawn):
        self.deHighlight()
        while self.tilesToMove > 0:
            direction = pawn["direction"].pop(0)
            match direction:
                case "START":
                    self.moveToStart(pawn)
                case "N":
                    self.moveUp(pawn)
                case "S":
                    self.moveDown(pawn)
                case "E":
                    self.moveRight(pawn)
                case "W":
                    self.moveLeft(pawn)
            self.tilesToMove -= 1

        if len(pawn["direction"]) > 6:
            for i in range(len(self.pawns)):
                if i != pawn["team"]-1:
                    for p in self.pawns[i]:
                        if p["atTile"] == pawn["atTile"] and len(p["direction"])>6:
                            p["atTile"] = -1
                            self.canvas.delete(p["id"])
                            self.createPawn(p["team"])

            for i in range(len(self.pawns)):
                for p in self.pawns[i]:
                    if p["atTile"] == -1:
                        self.pawns[i].remove(p)

        if len(pawn["direction"]) == 0:
            if(len(self.pawns[pawn["team"] -1 ])  == 0):
                self.winner(pawn["team"])
            self.canvas.delete(pawn["id"])



        self.nextPlayer()

    def smoothMoves(self,id,x,y):
        tempX = x/100
        tempY = y/100

        for i in range(100):
            self.canvas.after((1000//self.animationSpeed)*i, lambda: self.canvas.move(id,tempX,tempY))


    def movePawn(self,pawn,direction):
        match direction:
            case "N":
                self.smoothMoves(pawn["id"],0,-self.tilesize)
            case "S":
                self.smoothMoves(pawn["id"],0,self.tilesize)
            case "W":
                self.smoothMoves(pawn["id"],-self.tilesize,0)
            case "E":
                self.smoothMoves(pawn["id"],self.tilesize,0)
        pawn["atTile"] +=1

    def moveToStart(self,pawn):
        match pawn["team"]:
            case 1:
                self.moveTo(pawn["id"],self.tilesize/2,self.tilesize*8 - self.tilesize/2)
                pawn["atTile"] = 1
            case 2:
                self.moveTo(pawn["id"],self.tilesize*17 -self.tilesize/2,self.tilesize*10 - self.tilesize/2)
                pawn["atTile"] = 33
            case 3:
                self.moveTo(pawn["id"],self.tilesize*10 - self.tilesize/2,self.tilesize/2)
                pawn["atTile"] = 17
            case 4:
                self.moveTo(pawn["id"],self.tilesize*8 - self.tilesize/2,self.tilesize*17 -self.tilesize/2)
                pawn["atTile"] = 49
        self.tilesToMove = 1

    def moveTo(self, id, x, y):
        coords = self.canvas.coords(id)

        currentX = (coords[0] + coords[2]) / 2
        currentY = (coords[1] + coords[3]) / 2

        self.smoothMoves(id, x - currentX, y - currentY)

    def moveUp(self,pawn):
        match pawn["team"]:
            case 1:
                self.movePawn(pawn,"N")
            case 2:
                self.movePawn(pawn,"S")
            case 3:
                self.movePawn(pawn,"E")
            case 4:
                self.movePawn(pawn,"W")

    def moveDown(self,pawn):
        match pawn["team"]:
            case 1:
                self.movePawn(pawn,"S")
            case 2:
                self.movePawn(pawn,"N")
            case 3:
                self.movePawn(pawn,"W")
            case 4:
                self.movePawn(pawn,"E")

    def moveLeft(self,pawn):
        match pawn["team"]:
            case 1:
                self.movePawn(pawn,"W")
            case 2:
                self.movePawn(pawn,"E")
            case 3:
                self.movePawn(pawn,"N")
            case 4:
                self.movePawn(pawn,"S")

    def moveRight(self,pawn):
        match pawn["team"]:
            case 1:
                self.movePawn(pawn,"E")
            case 2:
                self.movePawn(pawn,"W")
            case 3:
                self.movePawn(pawn,"S")
            case 4:
                self.movePawn(pawn,"N")

    def winner(self,winning_team):
        players1 = []
        players2 = []
        for i in range(self.playerNames):
            if i+1 == winning_team:
                players1.append(self.playerNames[i])
            else:
                players2.append(self.playerNames[i])

        for p in players2:
            players2.append(p)
        DbHandler.gameRecord(players1)

        self.root.destroy()
        Menu()