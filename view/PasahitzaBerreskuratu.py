import tkinter as tk
from tkinter import ttk


class PasahitzaBerreskuratu(object):

    window = tk.Tk()
    window.title("PASAHITZA BERRESKURATU")
    window.geometry('400x400')
    window.resizable(False, False)
    espacio= ttk.Label(window, text="")
    izenburu1 = ttk.Label(window, text='PASAHITZA', font=("Times New Roman", 25))
    izenburu1.pack()
    izenburu2 = ttk.Label(window, text='BERRESKURATU', font=("Times New Roman", 25))
    izenburu2.pack()

    azpiIzenb = ttk.Label(window, text='Zure pasahitza berreskuratzeko: ', font=("Calibri"))
    azpiIzenb.pack()

    espacio.pack()

    erab = ttk.Label(window, text='Sartu zure erabiltzailearen izena... ', font=("Times New Roman", 16))
    erab.place(x=60, y=150)

    lehio = ttk.Entry(window, justify=tk.LEFT, width=26 ,textvariable="Pasahitza", font=("Times New Roman", 16))
    lehio.place(x=60,y=180)



    buttonirten = tk.Button(window, text="Irten", width=8, font=("Calibri"))
    buttonirten.place(x=70, y=300)
    buttonados = tk.Button(window, text="Ados", width=8, font=("Calibri"))
    buttonados.place(x=220, y=300)


    window.mainloop()
