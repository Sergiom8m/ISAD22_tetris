#   ERREGISTROAREN INTERFAZEA   #

import tkinter as tk
from tkinter import ttk

# Koloreak
botoi_kolor = "#fdb4bf"
sarrera_kolor = "#f99aaa"


class Erregistroa(object):

    window = tk.Tk()
    window.geometry('400x400')
    window.title("ERREGISTROA")

    # IZENBURUA
    izena = ttk.Label(window, text="ERREGISTROA", font=("Times New Roman", 25))
    izena.pack()

    tab = ttk.Label(window, text="  ")
    tab.pack()

    # AZPIZENBURUA
    testua = ttk.Label(window, text="Mesedez, zeure burua erregistratu", font = ("Times New Roman", 16))
    testua.pack()
    tab.pack()

    # BOTOIAK
    sartu = tk.Button(window, text="Sartu", cursor="hand2", bg=botoi_kolor, width=8, font=("Times New Roman", 14))
    sartu.place(x=60, y=350)

    irten = tk.Button(window, text="Irten", cursor="hand2", bg=botoi_kolor, width=8, font=("Times New Roman", 14))
    irten.place(x=220, y=350)

    #EGUNERAPENAK
    identifik = tk.StringVar()
    pasahitza1 = tk.StringVar()
    pasahitza2 = tk.StringVar()

    # Identifikatzailearen sarrera
    erab = ttk.Label(window, text='Identifikatzailea... ', font=("Times New Roman", 16))
    erab.place(x=60, y=120)

    erabil = tk.Entry(window, textvar=identifik, width=25, bg=sarrera_kolor, font=("Times New Roman", 16))
    erabil.place(x=60, y=140)
    identifik = ttk.Entry(justify=tk.LEFT)

    # Pasahitzaren sarrera
    pas1 = ttk.Label(window, text='Pasahitza... ', font=("Times New Roman", 16))
    pas1.place(x=60, y=180)

    pasahitz1 = tk.Entry(window, textvar=pasahitza1, width=25, bg=sarrera_kolor, font=("Times New Roman", 16))
    pasahitz1.place(x=60, y=200)
    pasahitz1 = ttk.Entry(justify=tk.LEFT)

    pas2 = ttk.Label(window, text='Pasahitza errepikatu... ', font=("Times New Roman", 16))
    pas2.place(x=60, y=240)

    pasahitz2 = tk.Entry(window, textvar=pasahitza2, width=25, bg=sarrera_kolor, font=("Times New Roman", 16))
    pasahitz2.place(x=60, y=260)
    pasahitz2 = ttk.Entry(justify=tk.LEFT)


    window.mainloop()