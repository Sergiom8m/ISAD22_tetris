import sys
import tkinter as tk
import sqlite3

import view.HasierakoMenua
from view.Profila import Profila
from view.PasahitzaBerreskuratu import PasahitzaBerreskuratu

# Koloreak
botoi_kolor = "#ffffff"
atzeko_kolor = "PaleGreen"


class Identifikazioa(object):

    def __init__(self):
        super(Identifikazioa, self).__init__()
        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)  # "X" botoia erabiltzean programa gelditzea ahalbidetzen du
        self.window.title("Identifikazioa")
        self.window.geometry('400x400')
        self.window['bg'] = atzeko_kolor
        self.window.resizable(False, False)

        espacio = tk.Label(self.window, bg=atzeko_kolor, text="")
        izenburua = tk.Label(self.window, bg=atzeko_kolor, text='IDENTIFIKAZIOA', font=("Times New Roman", 25))
        izenburua.pack()

        espacio.pack()

        azpiIzenb = tk.Label(self.window, bg=atzeko_kolor, text='Mesedez, zure burua identifikatu', font=("Calibri"))
        azpiIzenb.pack()

        espacio.pack()

        erab = tk.Label(self.window, bg=atzeko_kolor, text='Erabiltzailea: ', font=("Times New Roman", 16))
        erab.place(x=70, y=100)

        self.erabiltzaile = tk.Entry(self.window, bg=botoi_kolor, justify=tk.LEFT, width=23,
                                     textvariable="Erabiltzailea",
                                     font=("Times New Roman", 16))
        self.erabiltzaile.place(x=70, y=130)

        passwd = tk.Label(self.window, bg=atzeko_kolor, text='Pasahitza: ', font=("Times New Roman", 16))
        passwd.place(x=70, y=170)

        self.pasahitza = tk.Entry(self.window, bg=botoi_kolor, justify=tk.LEFT, width=23, textvariable="Pasahitza",
                                  font=("Times New Roman", 16))
        self.pasahitza.place(x=70, y=200)

        buttonb = tk.Button(self.window, bg=botoi_kolor, text="Pasahitza berreskuratu", font=("Times New Roman", 16),
                            command=self.identifik_berresk)
        buttonb.place(x=90, y=250)
        buttonb.bind("<Button-1>", )

        buttonirten = tk.Button(self.window, bg=botoi_kolor, text="Irten", width=8, font=("Times New Roman", 16),
                                command=self.irten)
        buttonirten.place(x=70, y=350)
        # buttonirten.bind("<Button-1>", self.identifik_hasiera)

        buttonerr = tk.Button(self.window, bg=botoi_kolor, text="Sartu", width=8, font=("Times New Roman", 16),
                              command=self.identifik_erregis)
        buttonerr.place(x=220, y=350)

        self.window.mainloop()

    # DATU BASEAREKIN KONEKTATZEKO:
    def identifik_erregis(self):
        con = sqlite3.connect("datubase.db")  # konexioa ezarri
        cur = con.cursor()
        id = self.erabiltzaile.get()
        p = self.pasahitza.get()

        if ((len(id) != 0) & (len(p) != 0)):
            cur.execute("CREATE TABLE IF NOT EXISTS JOKALARIAK(erabiltzailea, galdera, pasahitza, puntuazioa)")
            res = cur.execute("SELECT pasahitza FROM JOKALARIAK WHERE erabiltzailea=(?)", (id,))
            a = res.fetchone()
            ezDago = a is None
            if (ezDago):
                if(id == "admin" and p == "123"):
                    # PROFIL PANTAILARA JOTZEKO
                    self.window.destroy()
                    Profila(id).__init__(id)
                error = tk.Label(self.window, bg=atzeko_kolor, fg="red",
                                 text='Ez dago erabiltzaile hori                  ', font=("Times New Roman", 16))
                error.place(x=70, y=300)
            else:
                res = cur.execute("SELECT pasahitza FROM JOKALARIAK WHERE erabiltzailea=(?)", (id,))
                res = res.fetchone()[0]
                if (p != res):
                    error = tk.Label(self.window, bg=atzeko_kolor, fg="red",
                                     text='Pasahitza ez du koinziditzen                ',
                                     font=("Times New Roman", 16))
                    error.place(x=70, y=300)
                else:
                    # PROFIL PANTAILARA JOTZEKO
                    self.window.destroy()
                    Profila(id).__init__(id)
        else:
            error = tk.Label(self.window, bg=atzeko_kolor, fg="red", text='Sar itzazu datu guztiak                  ',
                             font=("Times New Roman", 16))
            error.place(x=70, y=300)

    # BESTE PANTAILETARA JOTZEKO:
    def identifik_berresk(self):
        self.window.destroy()
        PasahitzaBerreskuratu().__init__()

    def irten(self):
        self.window.destroy()
        view.HasierakoMenua.HasierakoMenua().__init__()
