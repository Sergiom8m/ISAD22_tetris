#   ERREGISTROAREN INTERFAZEA   #

import tkinter as tk
from tkinter import ttk
class Erregistroa(object):

    #super(HasierakoMenua, self) init()
    window = tk.Tk()
    window.config(width=780, height=780)
    window.title("ERREGISTROA")

    izena = tk.Label(window, text="ERREGISTROA")

    izena.pack()

    

    # Identifikatzailearen sarrera
    identifik = ttk.Entry()
    identifik.place(x=340, y=50)

    identifik = ttk.Entry(justify=tk.LEFT)

    # Pasahitzaren sarrera
    pasahitz = ttk.Entry()
    pasahitz.place(x=340, y=150)

    pasahitz = ttk.Entry(show="*")


    window.mainloop()


