import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class Identifikazioa(object):

    window = tk.Tk()
    window.title("IDENTIFIKAZIOA")
    window.geometry('400x400')
    espacio= ttk.Label(window, text="")
    izenburua = ttk.Label(window, text='IDENTIFIKAZIOA', font=("Times New Roman", 25))
    izenburua.pack()

    espacio.pack()

    azpiIzenb = ttk.Label(window, text='Mesedez, zure burua identifikatu', font=("Calibri"))
    azpiIzenb.pack()

    espacio.pack()

    erab = ttk.Label(window, text='Erabiltzailea: ', font=("Calibri"))
    erab.place(x=70, y=100)

    erabiltzaile = ttk.Entry(window, justify=tk.LEFT, width=32 ,textvariable="Erabiltzailea")
    erabiltzaile.place(x=70,y=120)

    passwd = ttk.Label(window, text='Pasahitza: ', font=("Calibri"))
    passwd.place(x=70, y=160)

    pasahitza = ttk.Entry(window, justify=tk.LEFT, width=32, textvariable="Pasahitza")
    pasahitza.place(x=70, y=180)

    buttonb = tk.Button(window, text="Pasahitza berreskuratu", width=23, font=("Calibri"))
    buttonb.place(x=70, y=230)

    buttonirten = tk.Button(window, text="Irten", width=8, font=("Calibri"))
    buttonirten.place(x=70, y=350)
    buttonerr = tk.Button(window, text="Erregistratu", width=8, font=("Calibri"))
    buttonerr.place(x=220, y=350)


    window.mainloop()




