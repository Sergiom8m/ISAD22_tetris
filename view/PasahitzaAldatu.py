import tkinter as tk
import sys
import sqlite3

import view

#Koloreak
botoi_kolor = "#ffffff"
atzeko_kolor = "#7ec0ee"

class PasahitzaAldatu(object):


    def __init__(self, erabiltzaile):
        super(PasahitzaAldatu, self).__init__()
        self.erabiltzaile=erabiltzaile
        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)  # "X" botoia erabiltzean programa gelditzea ahalbidetzen du
        self.window.title("Pasahitza Aldatu")
        self.window.geometry('400x400')
        self.window['bg']=atzeko_kolor
        self.window.resizable(False, False)
        espacio= tk.Label(self.window, bg=atzeko_kolor, text="")
        izenburua = tk.Label(self.window, bg=atzeko_kolor, text='PASAHITZA ALDATU', font=("Times New Roman", 25))
        izenburua.pack()

        espacio.pack()

        azpiIzenb = tk.Label(self.window, bg=atzeko_kolor, text='Zure pasahitza berria idatz ezazu: ', font=("Calibri"))
        azpiIzenb.pack()

        espacio.pack()

        passwd = tk.Label(self.window, bg=atzeko_kolor, text='Pasahitza: ', font=("Times New Roman", 16))
        passwd.place(x=70, y=100)

        self.pasahitz = tk.Entry(self.window,bg=botoi_kolor, justify=tk.LEFT, width=23 ,textvariable="Pasahitza", font=("Times New Roman", 16))
        self.pasahitz.place(x=70,y=130)

        passwd2 = tk.Label(self.window, bg=atzeko_kolor, text='Pasahitza errepikatu:', font=("Times New Roman", 16))
        passwd2.place(x=70, y=170)

        self.pasahitz2 = tk.Entry(self.window,bg=botoi_kolor, justify=tk.LEFT, width=23, textvariable="Pasahitza2", font=("Times New Roman", 16))
        self.pasahitz2.place(x=70, y=200)

        mezu = tk.Label(self.window, bg=atzeko_kolor, text='Berreskurapen pista sartu:', font=("Times New Roman", 16))
        mezu.place(x=70, y=240)

        self.galdera = tk.Entry(self.window,bg=botoi_kolor, justify=tk.LEFT, width=23, textvariable="Galdera",
                                   font=("Times New Roman", 16))
        self.galdera.place(x=70, y=270)

        buttonirten = tk.Button(self.window,bg=botoi_kolor, text="Irten", width=8, font=("Calibri"), command=self.irten)
        buttonirten.place(x=70, y=310)
        buttonados = tk.Button(self.window, bg=botoi_kolor, text="Ados", width=8, font=("Calibri"), command=self.aldatuta)
        buttonados.place(x=220, y=310)


        self.window.mainloop()

    #PANTAILETAN MUGITZEKO
    def irten(self):
        self.window.destroy()
        view.Profila.Profila(self.erabiltzaile).__init__()
    #DATU BASEAREKIN KONEKTATZEKO METODOA:

    def aldatuta(self):
        con = sqlite3.connect("datubase.db")  # konexioa ezarri
        cur = con.cursor()
        id = self.erabiltzaile
        p1 = self.pasahitz.get()
        p2 = self.pasahitz2.get()
        g = self.galdera.get()
        if ((len(p1) != 0) & (len(p2) != 0)):
            res = cur.execute("SELECT erabiltzailea FROM JOKALARIAK WHERE erabiltzailea=(?)", (id,))
            ezDago = res.fetchone() is None
            if (ezDago):
                mezu = tk.Label(self.window, bg=atzeko_kolor, fg="red", text='Erabiltzailea ez da existitzen          ',
                                font=("Calibri"))
                mezu.place(x=60, y=350)
            else:
                if(p1==p2):
                    cur.execute("UPDATE JOKALARIAK SET pasahitza=(?) WHERE erabiltzailea=(?)", (p1,id,))
                    cur.execute("UPDATE JOKALARIAK SET galdera=(?) WHERE erabiltzailea=(?)", (g, id,))
                    res = cur.execute("SELECT pasahitza FROM JOKALARIAK WHERE erabiltzailea=(?)", (id,))
                    con.commit()

                else:
                    mezu = tk.Label(self.window, bg=atzeko_kolor, fg="red", text='Pasahitzak ez dira berdinak        ',
                                    font=("Calibri"))
                    mezu.place(x=60, y=350)
        else:
            mezu = tk.Label(self.window, bg=atzeko_kolor, fg="red", text='Sar ezazu pasahitz berria                 ',
                            font=("Calibri"))
            mezu.place(x=60, y=350)
