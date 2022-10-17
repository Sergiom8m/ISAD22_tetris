import tkinter as tk
from _curses import window
from tkinter import ttk

from view.Ezarpenak import Ezarpenak
from view.Erregistroa import Erregistroa
from view.Identifikazioa import Identifikazioa


# Koloreak
botoi_kolor = "#ffffff"
atzeko_kolor = "#7ec0ee"

class HasierakoMenua(object):


    def __init__(self):
        super(HasierakoMenua, self).__init__()
        self.erabiltzaile = None
        self.window = tk.Tk()
        self.window.geometry('400x400')
        self.window.title("Hasierako Menua")
        self.window['bg']=atzeko_kolor
        self.window.resizable(False, False)


        separador = tk.Label(self.window,bg=atzeko_kolor, text='       ',  font=("Calibri", 20))

        separador.pack()

        izenburua = tk.Label(self.window,bg=atzeko_kolor,text='TETRIS', font=("Times New Roman", 35))

        izenburua.pack()

        separador = tk.Label(self.window, bg=atzeko_kolor, text='       ', font=("Calibri", 20))

        separador.pack()

        buttonPartidaBerria = tk.Button(self.window,bg=botoi_kolor, text="Partida berria hasi", width=30, command=self.pantailaPartidaBerria)
        buttonPartidaBerria.pack(ipadx=10, ipady=10)

        separador = tk.Label(self.window, bg=atzeko_kolor, text='       ', font=("Calibri", 2))

        separador.pack()

        buttonIdentifikatu = tk.Button(self.window,bg=botoi_kolor, text="Identifikatu", width=30, command=self.pantailaIdentifikatu)
        buttonIdentifikatu.pack(ipadx=10, ipady=10)

        separador = tk.Label(self.window,bg=atzeko_kolor, text='       ', font=("Calibri", 2))

        separador.pack()

        buttonErregistratu = tk.Button(self.window,bg=botoi_kolor, text="Erregistratu", width=30, command=self.pantailaErregistratu)
        buttonErregistratu.pack(ipadx=10, ipady=10)

        separador = tk.Label(self.window, bg=atzeko_kolor, text='       ', font=("Calibri", 20))

        separador.pack()

        buttonIrten = tk.Button(self.window,bg=botoi_kolor, text="Irten", command=self.jokoaAmaitu)
        buttonIrten.pack(ipadx=10, ipady=10)

        self.window.mainloop()

    #PANTAILAZ ALDATZEKO  METODOAK:
    def pantailaPartidaBerria(self):
        self.window.destroy()
        Ezarpenak(self.erabiltzaile).__init__()

    def pantailaIdentifikatu(self):
        self.window.destroy()
        Identifikazioa().__init__()

    def pantailaErregistratu(self):
        self.window.destroy()
        Erregistroa().__init__()

    def jokoaAmaitu(self):
        self.window.destroy()