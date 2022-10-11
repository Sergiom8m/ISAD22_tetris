#   ERREGISTROAREN INTERFAZEA   #

import tkinter as tk
from tkinter import ttk
import sqlite3
from view.Profila import Profila


# Koloreak
botoi_kolor = "#fdb4bf"
sarrera_kolor = "#f99aaa"



class Erregistroa(object):

        def __init__(self):
                super(Erregistroa, self).__init__()
                self.window = tk.Tk()
                self.window.geometry('400x400')
                self.window.title("ERREGISTROA")
                self.window.resizable(False, False)



                # IZENBURUA
                izena = ttk.Label(self.window, text="ERREGISTROA", font=("Times New Roman", 25))
                izena.pack()



                # AZPIZENBURUA
                testua = ttk.Label(self.window, text="Mesedez, zeure burua erregistratu", font = ("Times New Roman", 10))
                testua.pack()


                #EGUNERAPENAK
                identifik = tk.StringVar()
                e= tk.StringVar()
                pasahitza1 = tk.StringVar()
                pasahitza2 = tk.StringVar()

                # Identifikatzailearen sarrera
                erab = ttk.Label(self.window, text='Identifikatzailea... ', font=("Times New Roman", 12))
                erab.place(x=60, y=70)

                self.erabil = tk.Entry(self.window, textvar=identifik, width=32, bg=sarrera_kolor, font=("Times New Roman", 14))
                self.erabil.place(x=60, y=90)

                # Emailaren sarrera
                b=ttk.Label(self.window, text='Berreskurapen galdera sartu (pasahitzarako)', font=("Times New Roman", 12))
                b.place(x=60, y=130)


                self.galdera = tk.Entry(self.window, textvar=e, width=32, bg=sarrera_kolor, font=("Times New Roman", 14))
                self.galdera.place(x=60, y=150)

                # Pasahitzaren sarrera
                pas1 = ttk.Label(self.window, text='Pasahitza... ', font=("Times New Roman", 12))
                pas1.place(x=60, y=190)

                self.pasahitz1 = tk.Entry(self.window, textvar=pasahitza1, width=32, bg=sarrera_kolor, font=("Times New Roman", 14))
                self.pasahitz1.place(x=60, y=210)

                pas2 = ttk.Label(self.window, text='Pasahitza errepikatu... ', font=("Times New Roman", 12))
                pas2.place(x=60, y=250)

                self.pasahitz2 = tk.Entry(self.window, textvar=pasahitza2, width=32, bg=sarrera_kolor, font=("Times New Roman", 14))
                self.pasahitz2.place(x=60, y=270)


                # BOTOIAK
                sartu = tk.Button(self.window, text="Sartu", cursor="hand2", bg=botoi_kolor, width=8, font=("Times New Roman", 14),
                                  command=self.erabiltzaileaGorde)
                sartu.place(x=60, y=360)

                irten = tk.Button(self.window, text="Irten", cursor="hand2", bg=botoi_kolor, width=8, font=("Times New Roman", 14))
                irten.place(x=220, y=360)

                self.window.mainloop()

        #DATUBASEARI KONEKTATZEKO METODOA

        def erabiltzaileaGorde(self):
                con = sqlite3.connect("datubase.db")  # konexioa ezarri
                cur = con.cursor()
                id=self.erabil.get()
                galdera=self.galdera.get()
                p1=self.pasahitz1.get()
                p2=self.pasahitz2.get()

                if ((len(id) != 0) & (len(galdera) != 0) & (len(p1) != 0) & (len(p2) != 0)):
                        cur.execute("CREATE TABLE IF NOT EXISTS JOKALARIAK(erabiltzailea, galdera, pasahitza, puntuazioa)")
                        res = cur.execute("SELECT erabiltzailea FROM JOKALARIAK WHERE erabiltzailea=(?)", (id,))
                        ezDago = res.fetchone() is None
                        if (ezDago):
                                if (p1 == p2):

                                        cur.execute("INSERT INTO JOKALARIAK VALUES (?, ?, ?, ?)", (id, galdera, p1, 0))
                                        con.commit()

                                        #PROFIL PANTAILARA ALDATZEKO:
                                        self.window.destroy()
                                        Profila(id).__init__()
                                else:
                                        error = ttk.Label(self.window, text='Pasahitza ez du koinziditzen               ',
                                                          font=("Times New Roman", 12))
                                        error.place(x=60, y=310)
                        else:
                                error = ttk.Label(self.window, text='Erabiltzailea jada existitzen da                  ',
                                                  font=("Times New Roman", 12))
                                error.place(x=60, y=310)
                else:
                        error = ttk.Label(self.window, text='Sar itzazu datu guztiak                                   ',
                                          font=("Times New Roman", 12))
                        error.place(x=60, y=310)




