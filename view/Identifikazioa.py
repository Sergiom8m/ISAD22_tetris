import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class Identifikazioa(object):

    window = tk.Tk()
    window.title("IDENTIFIKAZIOA")
    window.geometry('400x400')
    espacio= ttk.Label(window, text="")
    izenburua = ttk.Label(window, text='IDENTIFIKAZIOA', font=("Calibri", 25))
    izenburua.pack()

    espacio.pack()

    azpiIzenb = ttk.Label(window, text='Mesedez, zure burua identifikatu', font=("Calibri"))
    azpiIzenb.pack()

    espacio.pack()

    erab = ttk.Label(window, text='Erabiltzailea: ', font=("Calibri"))
    erab.pack()

    erabiltzaile = ttk.Entry(window, justify=tk.CENTER, width=20, textvariable="Erabiltzailea")
    erabiltzaile.pack()

    espacio.pack()

    window.mainloop()




