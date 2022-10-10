import tkinter as tk
from tkinter import ttk
import sqlite3


class PasahitzaAldatu(object):

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
                print("ERROR EZ DAGO ERABILTZAILEA")
            else:
                if(p1==p2):
                    cur.execute("UPDATE JOKALARIAK SET pasahitza=(?) WHERE erabiltzailea=(?)", (p1,id,))
                    cur.execute("UPDATE JOKALARIAK SET galdera=(?) WHERE erabiltzailea=(?)", (g, id,))
                    res = cur.execute("SELECT pasahitza FROM JOKALARIAK WHERE erabiltzailea=(?)", (id,))
                    print(res.fetchone())
                    con.commit()

                else:
                    print("PASAHITZAK EZ DIRA BERDINAK")
        else:
            print("Sar ezazu pasahitz berria")


    def __init__(self, erabiltzaile):
        super(PasahitzaAldatu, self).__init__()
        self.erabiltzaile=erabiltzaile
        self.window = tk.Tk()
        self.window.title("PASAHITZA ALDATU")
        self.window.geometry('400x400')
        self.window.resizable(False, False)
        espacio= ttk.Label(self.window, text="")
        izenburua = ttk.Label(self.window, text='PASAHITZA ALDATU', font=("Times New Roman", 25))
        izenburua.pack()

        espacio.pack()

        azpiIzenb = ttk.Label(self.window, text='Zure pasahitza berria idatz ezazu: ', font=("Calibri"))
        azpiIzenb.pack()

        espacio.pack()

        passwd = ttk.Label(self.window, text='Pasahitza: ', font=("Times New Roman", 16))
        passwd.place(x=70, y=100)

        self.pasahitz = ttk.Entry(self.window, justify=tk.LEFT, width=23 ,textvariable="Pasahitza", font=("Times New Roman", 16))
        self.pasahitz.place(x=70,y=130)

        passwd2 = ttk.Label(self.window, text='Pasahitza errepikatu:', font=("Times New Roman", 16))
        passwd2.place(x=70, y=170)

        self.pasahitz2 = ttk.Entry(self.window, justify=tk.LEFT, width=23, textvariable="Pasahitza2", font=("Times New Roman", 16))
        self.pasahitz2.place(x=70, y=200)

        mezu = ttk.Label(self.window, text='Berreskurapen pista sartu:', font=("Times New Roman", 16))
        mezu.place(x=70, y=240)

        self.galdera = ttk.Entry(self.window, justify=tk.LEFT, width=23, textvariable="Galdera",
                                   font=("Times New Roman", 16))
        self.galdera.place(x=70, y=270)

        buttonirten = tk.Button(self.window, text="Irten", width=8, font=("Calibri"))
        buttonirten.place(x=70, y=300)
        buttonados = tk.Button(self.window, text="Ados", width=8, font=("Calibri"), command=self.aldatuta)
        buttonados.place(x=220, y=300)


        self.window.mainloop()




