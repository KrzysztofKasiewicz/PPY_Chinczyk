from tkinter import *

from DbHandler import DbHandler
from Game import Game


class PlayerLoginWindow:
    def __init__(self,numberOfPlayers):
        self.playerNames = []
        self.root = Tk()
        self.root.title("Login Players")

        for i in range(numberOfPlayers*2+4):
            self.root.rowconfigure(i, weight=1)
        self.root.columnconfigure(0, weight=1)

        for i in range(numberOfPlayers):
            self.playerNames.append("")
            Label(self.root,text = f"Player {i+1}").grid(row=i*2, column=0, sticky="nsew")
            self.playerLogin(i).grid(row=i*2+1, column=0, sticky="nsew")

        Button(self.root, text = "Start Game", command=self.startGame).grid(row=numberOfPlayers*2, column=0, sticky="nsew")

        self.startResponse = Label(self.root, fg = "Red")
        self.startResponse.grid(row=numberOfPlayers*2+1, column=0, sticky="nsew")

        Button(self.root,text = "Back", command = self.toMenu).grid(row=numberOfPlayers*2+2, column=0, sticky="nsew")



    def playerLogin(self,playerNumber):
        root = Frame(self.root)
        root.config(borderwidth=2, relief="ridge")

        for i in range(5):
            root.rowconfigure(i, weight=1)
        for i in range(2):
            root.columnconfigure(i, weight=1)

        # row 1
        Label(root, text="Username:").grid(row=0, column=0, sticky="nsew")
        # row 2
        usernameEntry = Entry(root, font=("Arial", 20))
        usernameEntry.grid(column=0, row=1, sticky="nsew")
        # row 3
        Label(root, text="Password:").grid(row=2, column=0, sticky="nsew")
        # row 4
        passwordEntry = Entry(root, font=("Arial", 20))
        passwordEntry.config(show="*")
        passwordEntry.grid(column=0, row=3, sticky="nsew")
        # row 5
        responseLabel = Label(root, fg="Blue")
        responseLabel.grid(row=4, column=0, sticky="nsew")

        # submit
        def tryLogin(username, password):
            responseLabel.config(text= DbHandler.login(username, password))
            self.playerNames[playerNumber] = username

        Button(root, text="submit",
               command=lambda: tryLogin(usernameEntry.get(), passwordEntry.get())).grid(row=0, rowspan=5,column=1, sticky="nsew")



        return root

    def startGame(self):
        if "" in self.playerNames:
            self.startResponse.config(text = "not all players are loggged in")
        else:
            self.root.destroy()
            Game(self.playerNames)

    def toMenu(self):
        self.root.destroy()
        from GameMenu import GameMenu
        GameMenu()
