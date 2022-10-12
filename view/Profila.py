import tkinter as tk
from tkinter import ttk
from view.PasahitzaAldatu import PasahitzaAldatu
from view.Ezarpenak import Ezarpenak
from view.ErabiltzaileakEzabatu import ErabiltzaileakEzabatu


#Koloreak
botoi_kolor = "#ffffff"
atzeko_kolor = "khaki"

class Profila(object):

    def __init__(self, erabiltzaile):
        super(Profila, self).__init__()
        self.erabiltzaile=erabiltzaile
        self.window = tk.Tk()
        self.window.geometry('400x400')
        self.window['bg']=atzeko_kolor
        self.window.title("Jokalariaren Profila")
        self.window.resizable(False, False)

        separador = tk.Label(self.window, text='       ', bg=atzeko_kolor, font=("Times New Roman", 25))

        separador.pack()

        izenburua = tk.Label(self.window, bg=atzeko_kolor, text='ZURE PROFILA', font=("Calibri", 25))

        izenburua.pack()

        separador = tk.Label(self.window, bg=atzeko_kolor, text='       ', font=("Calibri", 25))

        separador.pack()

        button = tk.Button(self.window,bg=botoi_kolor, text="Partida berria hasi", width=30, command=self.partidaHasi)
        button.pack(ipadx=10, ipady=10)

        separador = tk.Label(self.window, bg=atzeko_kolor, text='       ', font=("Calibri", 2))

        separador.pack()

        button = tk.Button(self.window,bg=botoi_kolor, text="Zure pasahitza aldatu", width=30, command=self.pasahitzaAldatu)
        button.pack(ipadx=10, ipady=10)

        separador = tk.Label(self.window,  bg=atzeko_kolor, text='       ', font=("Calibri", 2))

        separador.pack()

        if(self.erabiltzaile=="admin"):
            buttonBerezi = tk.Button(self.window, bg=botoi_kolor, text="Erabiltzaileak ezabatu", width=30)
            buttonBerezi.pack(ipadx=10, ipady=10)
        else:
            buttonBerezi = tk.Button(self.window,bg=botoi_kolor, text="Erabiltzaileak ezabatu", width=30, state="disabled")
            buttonBerezi.pack(ipadx=10, ipady=10)

        separador = tk.Label(self.window, bg=atzeko_kolor, text='       ', font=("Calibri", 25))

        separador.pack()

        button = tk.Button(self.window,bg=botoi_kolor, text="Irten")
        button.pack(ipadx=10, ipady=10)


        self.window.mainloop()

    #BESTE PANTAILETARA JOTZEKO METODOAK
    def pasahitzaAldatu(self):
        i=self.erabiltzaile
        print(i)
        self.window.destroy()
        PasahitzaAldatu(i).__init__()

    def erabiltzaileakEzabatu(self):
        self.window.destroy()
        Ezarpenak().__init__()
    def partidaHasi(self):
        self.window.destroy()
        Ezarpenak().__init__()