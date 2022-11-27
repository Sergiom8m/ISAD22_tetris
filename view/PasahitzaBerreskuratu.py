import tkinter as tk
from tkinter import ttk
import sqlite3
import sys
import view
from controller.db_conn import DbConn
from view.GalderaErantzun import GalderaErantzun

botoi_kolor = "#ffffff"
atzeko_kolor = "#7ec0ee"

class PasahitzaBerreskuratu(object):


    def __init__(self):
        super(PasahitzaBerreskuratu, self).__init__()

        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)  # "X" botoia erabiltzean programa gelditzea ahalbidetzen du
        self.window.title("Pasahitza Berreskuratu")
        self.window.geometry('400x400')
        self.window['bg']= atzeko_kolor
        self.window.resizable(False, False)
        espacio= tk.Label(self.window, bg=atzeko_kolor,  text="", font=("Times New Roman", 7))
        izenburu1 = tk.Label(self.window, bg=atzeko_kolor, text='PASAHITZA', font=("Times New Roman", 25))
        izenburu1.pack()
        izenburu2 = tk.Label(self.window, bg=atzeko_kolor, text='BERRESKURATU', font=("Times New Roman", 25))
        izenburu2.pack()

        azpiIzenb = tk.Label(self.window,  bg=atzeko_kolor,text='Zure pasahitza berreskuratzeko: ', font=("Calibri"))
        azpiIzenb.pack()

        espacio.pack()

        erab = tk.Label(self.window, bg=atzeko_kolor, text='Sartu zure erabiltzailearen izena... ', font=("Times New Roman", 16))
        erab.place(x=60, y=170)

        self.lehio = tk.Entry(self.window, bg=botoi_kolor, justify=tk.LEFT, width=26 ,font=("Times New Roman", 16))
        self.lehio.place(x=60,y=200)



        buttonirten = tk.Button(self.window, cursor="hand2", bg=botoi_kolor, text="Irten", width=8, font=("Calibri"), command=self.irten)
        buttonirten.place(x=70, y=350)
        self.buttonados = tk.Button(self.window, cursor="hand2", bg=botoi_kolor, text="Ados", width=8, font=("Calibri"), command=self.berreskuratuta)
        self.buttonados.place(x=220, y=350)



        self.window.mainloop()

    #DATU BASEAREKIN KONEKTATZEKO METODOA:


    #BESTE PANTAILETARA JOTZEKO METODAK:
    def irten(self):
        self.window.destroy()
        view.Identifikazioa.Identifikazioa().__init__()


    def berreskuratuta(self):
        id = self.lehio.get()
        if(len(id) != 0):
            erabiltzaile= DbConn.erabiltzailea_idz_lortu(DbConn(), id)
            if(erabiltzaile is None):
                mezu2 = tk.Label(self.window, bg=atzeko_kolor, fg="red", text='Erabiltzailea ez da existitzen', font=("Calibri"))
                mezu2.place(x=60, y=240)
            else:
                self.window.destroy()
                GalderaErantzun(id).__init__()
        else:
            mezu = tk.Label(self.window,  bg=atzeko_kolor,fg="red", text='Sartu erabiltzaile bat              ',font=("Calibri"))
            mezu.place(x=60, y=240)