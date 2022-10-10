import tkinter as tk
from _curses import window
from tkinter import ttk

from view.Ezarpenak import Ezarpenak


class HasierakoMenua(object):

    def __init__(self):
        super(HasierakoMenua, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('400x400')
        self.window.title("Hasierako Menua")
        self.window.resizable(False, False)


        separador = ttk.Label(window, text='       ', font=("Calibri", 25))

        separador.pack()

        izenburua = ttk.Label(window, text='TETRIS', font=("Calibri", 25))

        izenburua.pack()

        separador = ttk.Label(window, text='       ', font=("Calibri", 25))

        separador.pack()

        buttonPartidaBerria = tk.Button(window, text="Partida berria hasi", width=30)
        buttonPartidaBerria.pack(ipadx=10, ipady=10)

        separador = ttk.Label(window, text='       ', font=("Calibri", 2))

        separador.pack()

        buttonIdentifikatu = tk.Button(window, text="Identifikatu", width=30)
        buttonIdentifikatu.pack(ipadx=10, ipady=10)

        separador = ttk.Label(window, text='       ', font=("Calibri", 2))

        separador.pack()

        buttonErregistratu = tk.Button(window, text="Erregistratu", width=30)
        buttonErregistratu.pack(ipadx=10, ipady=10)

        separador = ttk.Label(window, text='       ', font=("Calibri", 25))

        separador.pack()

        buttonIrten = tk.Button(window, text="Irten")
        buttonIrten.pack(ipadx=10, ipady=10)

        window.mainloop()