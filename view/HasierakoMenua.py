import sys
import tkinter as tk

from view import Erregistroa
from view import Ezarpenak
from view import Identifikazioa
from tkinter import PhotoImage,Label

# Koloreak
botoi_kolor = "#ffffff"
atzeko_kolor = "#7ec0ee"


class HasierakoMenua(object):

    def __init__(self):
        super(HasierakoMenua, self).__init__()
        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)  # "X" botoia erabiltzean programa gelditzea ahalbidetzen du
        self.window.geometry('400x400')
        self.window.title("Hasierako Menua")
        self.window['bg'] = atzeko_kolor
        self.window.resizable(False, False)

        #TODO
        #IrudiBerriaGehitu
        #self.irudia = tk.PhotoImage(file="Irudiak/HasierakoMenua.png")
        #self.irudia1 = tk.Label(self.window, image=self.irudia).place(x=0,y=0, relwidth=1,relheight=1)

        # Separador
        tk.Label(self.window, bg=atzeko_kolor, text='       ', font=("Calibri", 20)).pack()

        # Izenburua
        tk.Label(self.window, bg=atzeko_kolor, text='TETRIS', font=("Times New Roman", 35)).pack()

        # Separador
        tk.Label(self.window, bg=atzeko_kolor, text='       ', font=("Calibri", 20)).pack()

        # "Partida Berria" botoia
        tk.Button(self.window, cursor="hand2", bg=botoi_kolor, text="Partida berria hasi", width=30, command=self.pantailaPartidaBerria).pack(ipadx=10, ipady=10)

        # Seprador
        tk.Label(self.window, bg=atzeko_kolor, text='       ', font=("Calibri", 2)).pack()

        # "Identifikatu" botoia
        tk.Button(self.window, cursor="hand2", bg=botoi_kolor, text="Identifikatu", width=30, command=self.pantailaIdentifikatu).pack(ipadx=10, ipady=10)

        # Separador
        tk.Label(self.window, bg=atzeko_kolor, text='       ', font=("Calibri", 2)).pack()

        # "Erregistratu" botoia
        tk.Button(self.window, cursor="hand2", bg=botoi_kolor, text="Erregistratu", width=30, command=self.pantailaErregistratu).pack(ipadx=10, ipady=10)

        # Separador
        tk.Label(self.window, bg=atzeko_kolor, text='       ', font=("Calibri", 20)).pack()

        # "Irten" botoia
        tk.Button(self.window, cursor="hand2", bg=botoi_kolor, text="Irten", command=self.jokoaAmaitu).pack(ipadx=10, ipady=10)

        self.window.mainloop()

    # PANTAILAZ ALDATZEKO  METODOAK:
    def pantailaPartidaBerria(self):
        self.window.destroy()
        Ezarpenak.Ezarpenak(None).__init__(None)

    def pantailaIdentifikatu(self):
        self.window.destroy()
        Identifikazioa.Identifikazioa().__init__()

    def pantailaErregistratu(self):
        self.window.destroy()
        Erregistroa.Erregistroa().__init__()

    def jokoaAmaitu(self):
        sys.exit()
