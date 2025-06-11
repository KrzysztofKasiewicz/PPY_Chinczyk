from tkinter import *
from PlayerRegisterWindow import PlayerRegisterWindow
from ScoresWindow import ScoresWindow
from Options import Options


class GameMenu:
    def __init__(self):
        self.root = Tk()
        self.root.title("Menu")
        self.root.geometry("400x600")

        for i in range(0, 6):
            self.root.rowconfigure(i, weight=1)
        self.root.columnconfigure(0, weight=1)

        for i in range(2,5):
            Button(self.root,text=f"{i} Players", command=lambda x=i: self.toLogin(x)).grid(row=i-2, column=0, sticky="nsew")

        Button(self.root,text="Register", command= self.toRegister).grid(row=3, column=0, sticky="nsew")
        Button(self.root,text="Scores", command= self.toScores).grid(row=4, column=0, sticky="nsew")
        Button(self.root, text="Options", command=self.toOptions).grid(row=5, column=0, sticky="nsew")

        self.root.mainloop()


    def toLogin(self,numberOfPlayers = int):
        self.root.destroy()
        from PlayerLoginWindow import PlayerLoginWindow
        PlayerLoginWindow(numberOfPlayers)


    def toRegister(self):
        PlayerRegisterWindow()

    def toScores(self):
        ScoresWindow()

    def toOptions(self):
        Options()