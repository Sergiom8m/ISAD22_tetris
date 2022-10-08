import tkinter as tk
from tkinter import ttk

class Profila(object):

    window = tk.Tk()
    window.geometry('400x400')
    window.title("Jokalariaren Profila")
    window.resizable(False, False)

    separador = ttk.Label(window, text='       ', font=("Times New Roman", 25))

    separador.pack()

    izenburua = ttk.Label(window, text='ZURE PROFILA', font=("Calibri", 25))

    izenburua.pack()

    separador = ttk.Label(window, text='       ', font=("Calibri", 25))

    separador.pack()

    button = tk.Button(window, text="Partida berria hasi", width=30)
    button.pack(ipadx=10, ipady=10)

    separador = ttk.Label(window, text='       ', font=("Calibri", 2))

    separador.pack()

    button = tk.Button(window, text="Zure pasahitza aldatu", width=30)
    button.pack(ipadx=10, ipady=10)

    separador = ttk.Label(window, text='       ', font=("Calibri", 2))

    separador.pack()

    button = tk.Button(window, text="Erabiltzaileak ezabatu", width=30)
    button.pack(ipadx=10, ipady=10)

    separador = ttk.Label(window, text='       ', font=("Calibri", 25))

    separador.pack()

    button = tk.Button(window, text="Irten")
    button.pack(ipadx=10, ipady=10)


    window.mainloop()