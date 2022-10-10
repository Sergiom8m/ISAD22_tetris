#   ERREGISTROAREN INTERFAZEA   #

import tkinter as tk
from tkinter import ttk
import sqlite3
from view.Profila import Profila


# Koloreak
botoi_kolor = "#fdb4bf"
sarrera_kolor = "#f99aaa"



class Erregistroa(object):

        #cur.execute("CREATE TABLE JOKALARIAK(erabiltzailea, email, pasahitza, puntuazioa)")
        #cur.execute("INSERT INTO JOKALARIAK VALUES ('admin',12345, 0 )")
        #for row in cur.execute("SELECT erabiltzailea, puntuazioa FROM JOKALARIAK"):
        #       print(row)


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
                erab = ttk.Label(self.window, text='Identifikatzailea... ', font=("Times New Roman", 16))
                erab.place(x=60, y=60)

                self.erabil = tk.Entry(self.window, textvar=identifik, width=25, bg=sarrera_kolor, font=("Times New Roman", 16))
                self.erabil.place(x=60, y=90)

                # Emailaren sarrera
                b=ttk.Label(self.window, text='Berreskurapen galdera sartu', font=("Times New Roman", 16))
                b.place(x=60, y=130)
                b2 = ttk.Label(self.window, text='(pasahitza berreskuratzeko)', font=("Times New Roman", 16))
                b2.place(x=60, y=155)

                self.galdera = tk.Entry(self.window, textvar=e, width=25, bg=sarrera_kolor, font=("Times New Roman", 16))
                self.galdera.place(x=60, y=185)

                # Pasahitzaren sarrera
                pas1 = ttk.Label(self.window, text='Pasahitza... ', font=("Times New Roman", 16))
                pas1.place(x=60, y=225)

                self.pasahitz1 = tk.Entry(self.window, textvar=pasahitza1, width=25, bg=sarrera_kolor, font=("Times New Roman", 16))
                self.pasahitz1.place(x=60, y=255)

                pas2 = ttk.Label(self.window, text='Pasahitza errepikatu... ', font=("Times New Roman", 16))
                pas2.place(x=60, y=295)

                self.pasahitz2 = tk.Entry(self.window, textvar=pasahitza2, width=25, bg=sarrera_kolor, font=("Times New Roman", 16))
                self.pasahitz2.place(x=60, y=325)

                # BOTOIAK
                sartu = tk.Button(self.window, text="Sartu", cursor="hand2", bg=botoi_kolor, width=8, font=("Times New Roman", 14),
                                  command=self.erabiltzaileaGorde)
                sartu.place(x=60, y=360)

                irten = tk.Button(self.window, text="Irten", cursor="hand2", bg=botoi_kolor, width=8, font=("Times New Roman", 14))
                irten.place(x=220, y=360)

                self.window.mainloop()

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
                                        print("Erregistratu zaitugu: " + id)
                                        cur.execute("INSERT INTO JOKALARIAK VALUES (?, ?, ?, ?)", (id, galdera, p1, 0))
                                        con.commit()
                                        print("ESTAS REGISTRADO Y TE METEMOS A PERFIL")
                                        self.window.destroy()
                                        Profila(id).__init__()
                                else:
                                        print("Pasahitza ez du koinziditzen")
                        else:
                                print("Jada existitzen da erabiltzailea")
                else:
                        print("Sar itzazu datu guztiak")




