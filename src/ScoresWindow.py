import os
from tkinter import *
from reportlab.pdfgen import canvas

from DbHandler import DbHandler


class ScoresWindow:
    def __init__(self):
        c = canvas.Canvas("wyniki.pdf")
        c.setFont("Times-Roman", 15)
        results = DbHandler.get_scores()
        x = 50
        y = 750
        for result in results:
            if result[2] != 0:
                wlr = float(result[1])/float(result[2])
            else:
                wlr = float(result[1])
            c.drawString(x, y, f"Gracz: {result[0]}   Wygrane: {result[1]}   Przegrane: {result[2]}   W/L: {wlr}")
            y -= 20
            if y <= 20:
                c.showPage()
        c.save()
        os.startfile("wyniki.pdf")