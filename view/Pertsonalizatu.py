import tkinter as tk
import sys

import view
# from view.Profila import Profila
from view.JokatuLehioa import JokatuLehioa, TableroaPanela
# from decimal import *

# Defektuzko koloreak
botoi_kolor = "#ffffff"
atzeko_kolor = "#7ec0ee"

class Pertsonalizatu(object):

    def __init__(self, erabiltzaile):
        super(Pertsonalizatu, self).__init__()
        self.erabiltzaile=erabiltzaile
        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)  # "X" botoia erabiltzean programa gelditzea ahalbidetzen du
        self.window.geometry('400x400')
        self.window.title("Pertsonalizazio Menua")
        self.window['bg']=atzeko_kolor
        self.window.resizable(False, False)


        espacio = tk.Label(self.window, bg=atzeko_kolor, text="")
        titulo = tk.Label(self.window, bg=atzeko_kolor, text="Jokoaren pertsonalizazioa", font=("Times New Roman",25))
        titulo.pack()
        espacio.pack()

        mensaje = tk.Label(self.window, bg=atzeko_kolor, text="Jokoaren ezugarriak eta itxura aukeratu. ", font=("Calibri", 14))
        mensaje.pack()

        mensaje2 = tk.Label(self.window, bg=atzeko_kolor, text="(Bana aukeratu arte ezingo da partida hasi) ", font=("Calibri", 14))
        mensaje2.pack()

        espacio.pack()

        titulo_kolorea = tk.Label(self.window, bg=atzeko_kolor, text="Kolorea:", font=("Calibri", 14))
        titulo_kolorea.place(x=60, y= 120)

        self.opcion = tk.IntVar()
        self.opcion.set(value=1)

        tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="1", variable=self.opcion, value=1).place(x=50, y=150)
        tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="2", variable=self.opcion, value=2).place(x=130, y=150)
        tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="3", variable=self.opcion, value=3).place(x=210, y=150)
        tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="4", variable=self.opcion, value=4).place(x=280, y=150)

        titulo_adreiluak = tk.Label(self.window, bg=atzeko_kolor, text="Adreiluak:", font=("Calibri", 10))
        titulo_adreiluak.place(x=60, y=190)

        self.opcion2 = tk.IntVar()
        self.opcion2.set(value=1)

        tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="1", variable=self.opcion2, value=1).place(x=50, y=230)
        tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="2", variable=self.opcion2, value=2).place(x=130, y=230)
        tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor,text="3", variable=self.opcion2, value=3).place(x=210, y=230)
        tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="4", variable=self.opcion2, value=4).place(x=280, y=230)

        titulo_soinua= tk.Label(self.window, bg=atzeko_kolor, text="Adreiluak:", font=("Calibri", 14))
        titulo_soinua.place(x=60, y=190)

        self.opcion2 = tk.IntVar()
        self.opcion2.set(value=1)

        tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="1", variable=self.opcion2, value=1).place(x=50, y=230)
        tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="2", variable=self.opcion2, value=2).place(x=130, y=230)
        tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="3", variable=self.opcion2, value=3).place(x=210, y=230)
        tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="4", variable=self.opcion2, value=4).place(x=280, y=230)

        buttonirten = tk.Button(self.window, cursor="hand2", bg=botoi_kolor, text="Irten", width=8, font=("Calibri"), command=self.irten)
        buttonirten.place(x=60, y=300)
        buttonGorde = tk.Button(self.window, cursor="hand2", bg=botoi_kolor, text="Aldaketak gorde", width=14, font=("Calibri"), command=self.aldaketak)
        buttonGorde.place(x=220, y=300)


        self.window.mainloop()

    # PANTAILETAN MUGITZEKO
    def irten(self):
        self.window.destroy()
        if(self.erabiltzaile is None):
            view.HasierakoMenua.HasierakoMenua().__init__()
        else:
            view.Profila.Profila(self.erabiltzaile).__init__()


    def aldaketak(self):
        self.window.destroy()
        atzeko_kolor = "#ffffff"
        print(self.opcion.get())
        print(self.opcion2.get())

        if (self.opcion.get() == 1):
            atzeko_kolor = "Red"
            bg = atzeko_kolor
        elif (self.opcion.get() == 2):
            atzeko_kolor = "Red"
            bg = atzeko_kolor
        elif (self.opcion.get() == 3):
            atzeko_kolor = "Red"
            bg = atzeko_kolor
        elif (self.opcion.get() == 4):
            atzeko_kolor = "Red"
            bg = atzeko_kolor

        pieza_kolorea = "#ffffff"
        if (self.opcion2.get() == 1):
            atzeko_kolor = "Red"
            bg = atzeko_kolor
        elif (self.opcion2.get() == 2):
            atzeko_kolor = "Red"
            bg = atzeko_kolor
        elif (self.opcion2.get() == 3):
            atzeko_kolor = "Red"
            bg = atzeko_kolor
        elif (self.opcion2.get() == 4):
            atzeko_kolor = "Red"
            bg = atzeko_kolor

        JokatuLehioa(atzeko_kolor, atzeko_kolor, self.erabiltzaile).__init__()
