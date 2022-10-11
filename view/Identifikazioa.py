import tkinter as tk
from tkinter import ttk
import sqlite3
from view.Profila import Profila
from view.PasahitzaBerreskuratu import PasahitzaBerreskuratu



class Identifikazioa(object):


    def __init__(self):
        super(Identifikazioa, self).__init__()
        self.window = tk.Tk()
        self.window.title("IDENTIFIKAZIOA")
        self.window.geometry('400x400')
        self.window.resizable(False, False)


        espacio = ttk.Label(self.window, text="")
        izenburua = ttk.Label(self.window, text='IDENTIFIKAZIOA', font=("Times New Roman", 25))
        izenburua.pack()

        espacio.pack()

        azpiIzenb = ttk.Label(self.window, text='Mesedez, zure burua identifikatu', font=("Calibri"))
        azpiIzenb.pack()

        espacio.pack()

        erab = ttk.Label(self.window, text='Erabiltzailea: ', font=("Times New Roman", 16))
        erab.place(x=70, y=100)

        self.erabiltzaile = ttk.Entry(self.window, justify=tk.LEFT, width=23, textvariable="Erabiltzailea",
                                 font=("Times New Roman", 16))
        self.erabiltzaile.place(x=70, y=130)

        passwd = ttk.Label(self.window, text='Pasahitza: ', font=("Times New Roman", 16))
        passwd.place(x=70, y=170)

        self.pasahitza = ttk.Entry(self.window, justify=tk.LEFT, width=23, textvariable="Pasahitza", font=("Times New Roman", 16))
        self.pasahitza.place(x=70, y=200)

        buttonb = tk.Button(self.window, text="Pasahitza berreskuratu", font=("Times New Roman", 16), command=self.identifik_berresk)
        buttonb.place(x=90, y=250)
        buttonb.bind("<Button-1>", )

        buttonirten = tk.Button(self.window, text="Irten", width=8, font=("Times New Roman", 16))
        buttonirten.place(x=70, y=350)
        #buttonirten.bind("<Button-1>", self.identifik_hasiera)

        buttonerr = tk.Button(self.window, text="Sartu", width=8, font=("Calibri"), command=self.identifik_erregis)
        buttonerr.place(x=220, y=350)

        self.window.mainloop()

    #DATU BASEAREKIN KONEKTATZEKO:
    def identifik_erregis(self):
        con = sqlite3.connect("datubase.db")  # konexioa ezarri
        cur = con.cursor()
        id = self.erabiltzaile.get()
        p = self.pasahitza.get()

        if ((len(id) != 0) & (len(p) != 0)):
            res = cur.execute("SELECT pasahitza FROM JOKALARIAK WHERE erabiltzailea=(?)", (id,))
            res = res.fetchone()[0]
            ezDago = res is None
            if (ezDago):
                error = ttk.Label(self.window, text='Ez dago erabiltzaile hori                 : ', font=("Times New Roman", 16))
                error.place(x=70, y=290)
            else:
                print(res)
                if (p != res):
                    error = ttk.Label(self.window, text='Pasahitza ez du koinziditzen                : ',
                                      font=("Times New Roman", 16))
                    error.place(x=70, y=290)
                else:
                    #PROFIL PANTAILARA JOTZEKO
                    self.window.destroy()
                    Profila(id).__init__()
        else:
            error = ttk.Label(self.window, text='Sar itzazu datu guztiak                 : ',
                              font=("Times New Roman", 16))
            error.place(x=70, y=290)

    #BESTE PANTAILETARA JOTZEKO:
    def identifik_berresk(self):
        self.window.destroy()
        PasahitzaBerreskuratu().__init__()

    # def identifik_hasiera(self):
    # self.window.destroy()
    #   HasierakoMenua().__init__()
