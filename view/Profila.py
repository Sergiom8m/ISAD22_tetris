import tkinter as tk
import sys

import view
from view.JokatuLehioa import JokatuLehioa
from view.PasahitzaAldatu import PasahitzaAldatu
from view.Ezarpenak import Ezarpenak
from view.ErabiltzaileakEzabatu import ErabiltzaileakEzabatu
from view.Pertsonalizatu import Pertsonalizatu
from controller.db_conn import DbConn


#Koloreak
botoi_kolor = "#ffffff"
atzeko_kolor = "#7ec0ee"

class Profila(object):

    def __init__(self, erabiltzaile):
        super(Profila, self).__init__()
        self.erabiltzaile = erabiltzaile
        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)  # "X" botoia erabiltzean programa gelditzea ahalbidetzen du
        self.window.geometry('400x400')
        global atzeko_kolor
        atzeko_kolor = DbConn.get_jokalari_fondoa(DbConn(), self.erabiltzaile)
        global botoi_kolor
        atzeko_kolor = DbConn.get_jokalari_fondoa(DbConn(), self.erabiltzaile)
        self.window['bg']=atzeko_kolor
        self.window.title("Jokalariaren Profila")
        self.window.resizable(False, False)

        separador = tk.Label(self.window, text='       ', bg=atzeko_kolor, font=("Times New Roman", 10))

        separador.pack()

        izenburua = tk.Label(self.window, bg=atzeko_kolor, text='ZURE PROFILA', font=("Calibri", 25))

        izenburua.pack()

        separador = tk.Label(self.window, bg=atzeko_kolor, text='       ', font=("Calibri", 8))

        separador.pack()

        button = tk.Button(self.window,bg=botoi_kolor, text="Partida berria hasi", cursor="hand2", width=30, command=self.partidaHasi)
        button.pack(ipadx=10, ipady=8)

        separador = tk.Label(self.window, bg=atzeko_kolor, text='       ', font=("Calibri", 2))

        separador.pack()

        button = tk.Button(self.window,bg=botoi_kolor, text="Zure pasahitza aldatu", cursor="hand2", width=30, command=self.pasahitzaAldatu)
        button.pack(ipadx=10, ipady=8)

        separador = tk.Label(self.window,  bg=atzeko_kolor, text='       ', font=("Calibri", 2))

        separador.pack()

        self.erantzuna = DbConn.partida_kargatuta(DbConn(), self.erabiltzaile)

        if self.erantzuna == "#":
            button = tk.Button(self.window,bg=botoi_kolor, text="Gordetako partida kargatu", cursor="hand2", width=30, state="disabled")
            button.pack(ipadx=10, ipady=8)

        else:
            button = tk.Button(self.window, bg=botoi_kolor, text="Gordetako partida kargatu", cursor="hand2", width=30, command=self.partidaKargatu)
            button.pack(ipadx=10, ipady=8)

        separador = tk.Label(self.window, bg=atzeko_kolor, text='       ', font=("Calibri", 2))
        separador.pack()

        # Jokoa Pertsonalizatzeko

        button = tk.Button(self.window, bg=botoi_kolor, text="Jokoa Pertsonalizatu", cursor="hand2", width=30,
                           command=self.pertsonalizazioa)
        button.pack(ipadx=10, ipady=8)

        separador = tk.Label(self.window, bg=atzeko_kolor, text='       ', font=("Calibri", 2))

        separador.pack()

        if self.erabiltzaile == "admin":
            buttonBerezi = tk.Button(self.window, bg=botoi_kolor, text="Erabiltzaileak ezabatu", cursor="hand2", width=30, command=self.erabiltzaileakEzabatu)
            buttonBerezi.pack(ipadx=10, ipady=8)
        else:
            buttonBerezi = tk.Button(self.window,bg=botoi_kolor, text="Erabiltzaileak ezabatu", cursor="hand2", width=30, state="disabled")
            buttonBerezi.pack(ipadx=10, ipady=8)


        separador = tk.Label(self.window, bg=atzeko_kolor, text='       ', font=("Calibri", 6))
        separador.pack()

        button = tk.Button(self.window,bg=botoi_kolor, text="Irten", cursor="hand2", command=self.irten)
        button.pack(ipadx=10, ipady=8)


        self.window.mainloop()

    #BESTE PANTAILETARA JOTZEKO METODOAK
    def pasahitzaAldatu(self):
        i=self.erabiltzaile
        self.window.destroy()
        PasahitzaAldatu(i).__init__()

    def pertsonalizazioa(self):
        self.window.destroy()
        Pertsonalizatu(self.erabiltzaile).__init__()
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
        self.window.destroy() #Por esto no funcionaba (no estaba esta linea de codigo)
        datuak = str(self.erantzuna).split(sep='#')
        puntuazioa = int(datuak[0])
        tamaina = int(datuak[1])
        abiadura = int(datuak[2])
        JokatuLehioa(abiadura, tamaina, self.erabiltzaile, puntuazioa, self.erantzuna).__init__()

