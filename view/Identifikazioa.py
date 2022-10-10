import tkinter as tk
from tkinter import ttk

from view.Erregistroa import Erregistroa
from view.HasierakoMenua import HasierakoMenua


class Identifikazioa(object):

    def identifik_erregis(self):
        self.window.destroy()
        Erregistroa().__init__()
    def identifik_hasiera(self):
        self.window.destroy()
        HasierakoMenua().__init__()

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

        erabiltzaile = ttk.Entry(self.window, justify=tk.LEFT, width=23, textvariable="Erabiltzailea",
                                 font=("Times New Roman", 16))
        erabiltzaile.place(x=70, y=130)

        passwd = ttk.Label(self.window, text='Pasahitza: ', font=("Times New Roman", 16))
        passwd.place(x=70, y=170)

        pasahitza = ttk.Entry(self.window, justify=tk.LEFT, width=23, textvariable="Pasahitza", font=("Times New Roman", 16))
        pasahitza.place(x=70, y=200)

        buttonb = tk.Button(self.window, text="Pasahitza berreskuratu", font=("Times New Roman", 16))
        buttonb.place(x=90, y=250)
        buttonb.bind("<Button-1>", )

        buttonirten = tk.Button(self.window, text="Irten", width=8, font=("Times New Roman", 16), command=self.identifik_hasiera)
        buttonirten.place(x=70, y=350)
        #buttonirten.bind("<Button-1>", self.identifik_hasiera)

        buttonerr = tk.Button(self.window, text="Erregistratu", width=8, font=("Calibri"), command=self.identifik_erregis)
        buttonerr.place(x=220, y=350)

        self.window.mainloop()