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

        erabil = tk.Entry(window, textvar=identifik, width=25, bg=sarrera_kolor, font=("Times New Roman", 16))
        erabil.place(x=60, y=100)
        identifik = ttk.Entry(justify=tk.LEFT)

        # Emailaren sarrera
        email=ttk.Label(window, text='Emaila...', font=("Times New Roman", 16))
        email.place(x=60, y=140)

        emaila = tk.Entry(window, textvar=e, width=25, bg=sarrera_kolor, font=("Times New Roman", 16))
        emaila.place(x=60, y=170)
        e = ttk.Entry(justify=tk.LEFT)

        # Pasahitzaren sarrera
        pas1 = ttk.Label(window, text='Pasahitza... ', font=("Times New Roman", 16))
        pas1.place(x=60, y=210)

        pasahitz1 = tk.Entry(window, textvar=pasahitza1, width=25, bg=sarrera_kolor, font=("Times New Roman", 16))
        pasahitz1.place(x=60, y=240)
        pasahitz1 = ttk.Entry(justify=tk.LEFT)

        pas2 = ttk.Label(window, text='Pasahitza errepikatu... ', font=("Times New Roman", 16))
        pas2.place(x=60, y=280)

        pasahitz2 = tk.Entry(window, textvar=pasahitza2, width=25, bg=sarrera_kolor, font=("Times New Roman", 16))
        pasahitz2.place(x=60, y=310)
        pasahitz2 = ttk.Entry(justify=tk.LEFT)

        def erabiltzaileaGorde():
                con = sqlite3.connect("datubase.db")  # konexioa ezarri
                cur = con.cursor()
                id=Erregistroa.erabil.get()
                email=Erregistroa.emaila.get()
                p1=Erregistroa.pasahitz1.get()
                p2=Erregistroa.pasahitz2.get()

                if ((len(id) != 0) & (len(email) != 0) & (len(p1) != 0) & (len(p2) != 0)):
                        res = cur.execute("SELECT erabiltzailea FROM JOKALARIAK WHERE erabiltzailea=(?)", (id,))
                        ezDago = res.fetchone() is None
                        if (ezDago):
                                print("Erabiltzaile zuzena sartu da")
                                if (p1 == p2):
                                        print("Erregistratu zaitugu: " + id)
                                        cur.execute(
                                                "CREATE TABLE IF NOT EXISTS JOKALARIAK(erabiltzailea, email, pasahitza, puntuazioa)")
                                        cur.execute("INSERT INTO JOKALARIAK VALUES (?, ?, ?, ?)", (id, email, p1, 0))
                                        con.commit()
                                else:
                                        print("Pasahitza ez du koinziditzen")
                        else:
                                print("Jada existitzen da erabiltzailea")
                else:
                        print("Sar itzazu datu guztiak")

        # BOTOIAK
        sartu = tk.Button(window, text="Sartu", cursor="hand2", bg=botoi_kolor, width=8, font=("Times New Roman", 14),
                          command=erabiltzaileaGorde)
        sartu.place(x=60, y=350)

        irten = tk.Button(window, text="Irten", cursor="hand2", bg=botoi_kolor, width=8, font=("Times New Roman", 14))
        irten.place(x=220, y=350)



        window.mainloop()


