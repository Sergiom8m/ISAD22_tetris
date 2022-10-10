import tkinter as tk
from tkinter import ttk

class HasierakoMenua(object):
    """docstring for JokatuLeioa"""

    def __init__(self):
        super(HasierakoMenua, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('400x400')
        self.window.title("Hasierako Menua")

        separador = ttk.Label(self.window, text='       ', font=("Calibri", 25))

        separador.pack()

        izenburua = ttk.Label(self.window, text='TETRIS', font=("Calibri", 25))

        izenburua.pack()

        separador = ttk.Label(self.window, text='       ', font=("Calibri", 25))

        separador.pack()

        button = tk.Button(self.window, text="Partida berria hasi", width=30)
        button.pack(ipadx=10, ipady=10)

        separador = ttk.Label(self.window, text='       ', font=("Calibri", 2))

        separador.pack()

        button = tk.Button(self.window, text="Identifikatu", width=30)
        button.pack(ipadx=10, ipady=10)

        separador = ttk.Label(self.window, text='       ', font=("Calibri", 2))

        separador.pack()

        button = tk.Button(self.window, text="Erregistratu", width=30)
        button.pack(ipadx=10, ipady=10)

        separador = ttk.Label(self.window, text='       ', font=("Calibri", 25))

        separador.pack()

        button = tk.Button(self.window, text="Irten")
        button.pack(ipadx=10, ipady=10)


        self.window.mainloop()