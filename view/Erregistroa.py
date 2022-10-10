#   ERREGISTROAREN INTERFAZEA   #

import tkinter as tk
from tkinter import ttk
import sqlite3

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
                window = tk.Tk()
                window.geometry('400x400')
                window.title("ERREGISTROA")
                window.resizable(False, False)



                # IZENBURUA
                izena = ttk.Label(window, text="ERREGISTROA", font=("Times New Roman", 25))
                izena.pack()



                # AZPIZENBURUA
                testua = ttk.Label(window, text="Mesedez, zeure burua erregistratu", font = ("Times New Roman", 16))
                testua.pack()


                #EGUNERAPENAK
                identifik = tk.StringVar()
                e= tk.StringVar()
                pasahitza1 = tk.StringVar()
                pasahitza2 = tk.StringVar()

                # Identifikatzailearen sarrera
                erab = ttk.Label(window, text='Identifikatzailea... ', font=("Times New Roman", 16))
                erab.place(x=60, y=70)

                self.erabil = tk.Entry(window, textvar=identifik, width=25, bg=sarrera_kolor, font=("Times New Roman", 16))
                self.erabil.place(x=60, y=100)

                # Emailaren sarrera
                email=ttk.Label(window, text='Emaila...', font=("Times New Roman", 16))
                email.place(x=60, y=140)

                self.emaila = tk.Entry(window, textvar=e, width=25, bg=sarrera_kolor, font=("Times New Roman", 16))
                self.emaila.place(x=60, y=170)

                # Pasahitzaren sarrera
                pas1 = ttk.Label(window, text='Pasahitza... ', font=("Times New Roman", 16))
                pas1.place(x=60, y=210)

                self.pasahitz1 = tk.Entry(window, textvar=pasahitza1, width=25, bg=sarrera_kolor, font=("Times New Roman", 16))
                self.pasahitz1.place(x=60, y=240)

                pas2 = ttk.Label(window, text='Pasahitza errepikatu... ', font=("Times New Roman", 16))
                pas2.place(x=60, y=280)

                self.pasahitz2 = tk.Entry(window, textvar=pasahitza2, width=25, bg=sarrera_kolor, font=("Times New Roman", 16))
                self.pasahitz2.place(x=60, y=310)

                # BOTOIAK
                sartu = tk.Button(window, text="Sartu", cursor="hand2", bg=botoi_kolor, width=8, font=("Times New Roman", 14),
                                  command=self.erabiltzaileaGorde)
                sartu.place(x=60, y=350)

                irten = tk.Button(window, text="Irten", cursor="hand2", bg=botoi_kolor, width=8, font=("Times New Roman", 14))
                irten.place(x=220, y=350)

                window.mainloop()

        def erabiltzaileaGorde(self):
                con = sqlite3.connect("datubase.db")  # konexioa ezarri
                cur = con.cursor()
                id=self.erabil.get()
                email=self.emaila.get()
                p1=self.pasahitz1.get()
                p2=self.pasahitz2.get()

                if ((len(id) != 0) & (len(email) != 0) & (len(p1) != 0) & (len(p2) != 0)):
                        cur.execute("CREATE TABLE IF NOT EXISTS JOKALARIAK(erabiltzailea, email, pasahitza, puntuazioa)")
                        res = cur.execute("SELECT erabiltzailea FROM JOKALARIAK WHERE erabiltzailea=(?)", (id,))
                        ezDago = res.fetchone() is None
                        if (ezDago):
                                print("Erabiltzaile zuzena sartu da")
                                if (p1 == p2):
                                        print("Erregistratu zaitugu: " + id)
                                        cur.execute("INSERT INTO JOKALARIAK VALUES (?, ?, ?, ?)", (id, email, p1, 0))
                                        con.commit()
                                else:
                                        print("Pasahitza ez du koinziditzen")
                        else:
                                print("Jada existitzen da erabiltzailea")
                else:
                        print("Sar itzazu datu guztiak")




