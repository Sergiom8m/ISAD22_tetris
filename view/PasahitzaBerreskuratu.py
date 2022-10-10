import tkinter as tk
from tkinter import ttk
import sqlite3


class PasahitzaBerreskuratu(object):

    def berreskuratuta(self):
        id = self.lehio.get()
        if(len(id) != 0):
            self.pasahitzaBerreskuratu()
        else:
            mezu = ttk.Label(self.window, text='Sartu erabiltzaile bat',font=("Calibri"))
            mezu.place(x=60, y=210)


    def __init__(self):
        super(PasahitzaBerreskuratu, self).__init__()

        self.window = tk.Tk()
        self.window.title("PASAHITZA BERRESKURATU")
        self.window.geometry('400x400')
        self.window.resizable(False, False)
        espacio= ttk.Label(self.window, text="")
        izenburu1 = ttk.Label(self.window, text='PASAHITZA', font=("Times New Roman", 25))
        izenburu1.pack()
        izenburu2 = ttk.Label(self.window, text='BERRESKURATU', font=("Times New Roman", 25))
        izenburu2.pack()

        azpiIzenb = ttk.Label(self.window, text='Zure pasahitza berreskuratzeko: ', font=("Calibri"))
        azpiIzenb.pack()

        espacio.pack()

        erab = ttk.Label(self.window, text='Sartu zure erabiltzailearen izena... ', font=("Times New Roman", 16))
        erab.place(x=60, y=150)

        self.lehio = ttk.Entry(self.window, justify=tk.LEFT, width=26 ,font=("Times New Roman", 16))
        self.lehio.place(x=60,y=180)



        buttonirten = tk.Button(self.window, text="Irten", width=8, font=("Calibri"))
        buttonirten.place(x=70, y=300)
        buttonados = tk.Button(self.window, text="Ados", width=8, font=("Calibri"), command=self.berreskuratuta)
        buttonados.place(x=220, y=300)


        self.window.mainloop()

    def pasahitzaBerreskuratu(self):
        con = sqlite3.connect("datubase.db")  # konexioa ezarri
        cur = con.cursor()
        id = self.lehio.get()
        res = cur.execute("SELECT galdera FROM JOKALARIAK WHERE erabiltzailea=(?)", (id,))
        g=res.fetchone()[0]
        ezDago = g is None
        if (ezDago):
            mezu = ttk.Label(self.window, text='Erabiltzailea ez da existitzen', font=("Calibri"))
            mezu.place(x=60, y=210)
        else:
            pista = ttk.Label(self.window, text='Jarritako pista hurrengoa da: ', font=("Calibri"))
            pista.place(x=60, y=210)
            pista = ttk.Label(self.window, text=f'{g}', font=("Calibri"))
            pista.place(x=60, y=240)

