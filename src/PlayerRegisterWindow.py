from tkinter import *
from DbHandler import DbHandler
class PlayerRegisterWindow:
    def __init__(self):
        self.root = Toplevel()
        self.root.title("Register a Player")
        self.root.geometry("400x300")
        for i in range(5):
            self.root.rowconfigure(i, weight=1)
        for i in range(2):
            self.root.columnconfigure(i, weight=1)

        # row 1
        Label(self.root, text="Username:").grid(row=0, column=0, sticky="nsew")
        # row 2
        usernameEntry = Entry(self.root,font=("Arial", 20))
        usernameEntry.grid(column=0, row=1, sticky="nsew")
        # row 3
        Label(self.root, text="Password:").grid(row=2, column=0, sticky="nsew")
        # row 4
        passwordEntry = Entry(self.root,font=("Arial", 20))
        passwordEntry.config(show="*")
        passwordEntry.grid(column=0, row=3, sticky="nsew")
        # row 5
        self.responseLabel = Label(self.root, fg = "Blue")
        self.responseLabel.grid(row=4, column=0, sticky="nsew")

        #submit
        Button(self.root,text = "submit",command= lambda: self.tryRegister(usernameEntry.get(),passwordEntry.get()) ).grid(row=0, rowspan=5, column=1, sticky="nsew")



    def tryRegister(self,username,password):
        self.responseLabel.config(text = DbHandler.register(username, password))