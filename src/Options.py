from tkinter import *
import json

class Options:
    def __init__(self):
        self.OptionValues = OptionValues()
        self.root = Toplevel()
        self.root.title("Options")
        for i in range(5):
            self.root.rowconfigure(i, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        Label(self.root, text="Tile Size:").grid(row=0, column=0, sticky="nsew")
        self.tilesizeEntry = Entry(self.root, font=("Arial", 15))
        self.tilesizeEntry.grid(row=0, column=1, sticky="nsew")
        self.tilesizeEntry.insert(0,self.OptionValues.tilesize)

        Label(self.root, text="Animation speed:").grid(row=1, column=0, sticky="nsew")
        self.speedEntry = Entry(self.root, font=("Arial", 15))
        self.speedEntry.grid(row=1, column=1, sticky="nsew")
        self.speedEntry.insert(0,self.OptionValues.animationSpeed)

        Label(self.root, text="Leave base when you roll:").grid(row=2, column=0, sticky="nsew")
        self.progEntry = Entry(self.root, font=("Arial", 15))
        self.progEntry.grid(row=2, column=1, sticky="nsew")
        self.progEntry.insert(0,self.OptionValues.progWyjscia)

        Label(self.root, text="How many pawns:").grid(row=3, column=0, sticky="nsew")
        self.pawnsEntry = Entry(self.root, font=("Arial", 15))
        self.pawnsEntry.grid(row=3, column=1, sticky="nsew")
        self.pawnsEntry.insert(0,self.OptionValues.howManyPawns)

        Button(self.root, text="apply",command= self.apply).grid(row=4, column=0, columnspan=2, sticky="nsew")


    def apply(self):
        try:
            if self.tilesizeEntry.get() != "" and int(self.tilesizeEntry.get()) > 0:
                self.OptionValues.tilesize = int(self.tilesizeEntry.get())
        except ValueError:
            pass

        try:
            if self.speedEntry.get() != "" and int(self.speedEntry.get()) > 0:
                self.OptionValues.animationSpeed = int(self.speedEntry.get())
        except ValueError:
            pass

        try:
            if self.progEntry.get() != "" and 0 < int(self.progEntry.get()) < 7:
                self.OptionValues.progWyjscia = int(self.progEntry.get())
        except ValueError:
            pass

        try:
            if self.pawnsEntry.get() != "" and int(self.pawnsEntry.get()) > 0:
                self.OptionValues.howManyPawns = int(self.pawnsEntry.get())
        except ValueError:
            pass

        self.OptionValues.toJSON()



class OptionValues:
    def __init__(self):
        data = self.fromJSON()
        self.tilesize = data['tilesize']
        self.animationSpeed = data['animationSpeed']
        self.progWyjscia = data['progWyjscia']
        self.howManyPawns = data['howManyPawns']

    def fromJSON(self):
        with open("options.json", "r") as file:
            return json.load(file)


    def toJSON(self):
        with open("options.json", "w") as file:
            json.dump(vars(self), file)

