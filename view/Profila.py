import tkinter as tk
import sys

import view
from view.JokatuLehioa import JokatuLehioa
from view.PasahitzaAldatu import PasahitzaAldatu
from view.Ezarpenak import Ezarpenak
from view.ErabiltzaileakEzabatu import ErabiltzaileakEzabatu
from controller.db_conn import DbConn


#Koloreak
botoi_kolor = "#ffffff"
atzeko_kolor = "#7ec0ee"

class Profila(object):

    def __init__(self, erabiltzaile):
        super(Profila, self).__init__()
        self.erabiltzaile=erabiltzaile
        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)  # "X" botoia erabiltzean programa gelditzea ahalbidetzen du
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

        button = tk.Button(self.window,bg=botoi_kolor, text="Partida berria hasi", cursor="hand2", width=30, command=self.partidaHasi)
        button.pack(ipadx=10, ipady=10)

        separador = tk.Label(self.window, bg=atzeko_kolor, text='       ', font=("Calibri", 2))

        separador.pack()

        button = tk.Button(self.window,bg=botoi_kolor, text="Zure pasahitza aldatu", cursor="hand2", width=30, command=self.pasahitzaAldatu)
        button.pack(ipadx=10, ipady=10)

        separador = tk.Label(self.window,  bg=atzeko_kolor, text='       ', font=("Calibri", 2))

        separador.pack()

        self.erantzuna = DbConn.partida_kargatuta(DbConn(), self.erabiltzaile)

        if self.erantzuna == "#":
            button = tk.Button(self.window,bg=botoi_kolor, text="Gordetako partida kargatu", cursor="hand2", width=30, state="disabled")
            button.pack(ipadx=10, ipady=10)

        else:
            button = tk.Button(self.window, bg=botoi_kolor, text="Gordetako partida kargatu", cursor="hand2", width=30, command=self.partidaKargatu)
            button.pack(ipadx=10, ipady=10)

        if self.erabiltzaile == "admin":
            buttonBerezi = tk.Button(self.window, bg=botoi_kolor, text="Erabiltzaileak ezabatu", cursor="hand2", width=30, command=self.erabiltzaileakEzabatu)
            buttonBerezi.pack(ipadx=10, ipady=10)
        else:
            buttonBerezi = tk.Button(self.window,bg=botoi_kolor, text="Erabiltzaileak ezabatu", cursor="hand2", width=30, state="disabled")
            buttonBerezi.pack(ipadx=10, ipady=10)

        separador = tk.Label(self.window, bg=atzeko_kolor, text='       ', font=("Calibri", 25))

        separador.pack()

        button = tk.Button(self.window,bg=botoi_kolor, text="Irten", cursor="hand2", command=self.irten)
        button.pack(ipadx=10, ipady=10)


        self.window.mainloop()

    #BESTE PANTAILETARA JOTZEKO METODOAK
    def pasahitzaAldatu(self):
        i=self.erabiltzaile
        self.window.destroy()
        PasahitzaAldatu(i).__init__()

    def erabiltzaileakEzabatu(self):
        self.window.destroy()
        ErabiltzaileakEzabatu().__init__()
    def partidaHasi(self):
        self.window.destroy()
        Ezarpenak(self.erabiltzaile).__init__()

    def irten(self):
        self.window.destroy()
        view.HasierakoMenua.HasierakoMenua().__init__()

    def partidaKargatu(self):

        self.puntuazioa = DbConn.puntuazioa_lortu(DbConn(), self.erabiltzaile)
        JokatuLehioa(None, None, self.erabiltzaile, self.puntuazioa, self.erantzuna).__init__()



