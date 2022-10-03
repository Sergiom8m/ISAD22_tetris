import tkinter as tk
from tkinter import ttk


class PasahiztaAldatu(object):

    window = tk.Tk()
    window.title("PASAHITZA ALDATU")
    window.geometry('400x400')
    espacio= ttk.Label(window, text="")
    izenburua = ttk.Label(window, text='PASAHITZA ALDATU', font=("Times New Roman", 25))
    izenburua.pack()

    espacio.pack()

    azpiIzenb = ttk.Label(window, text='Zure pasahitza berria idatz ezazu:', font=("Calibri"))
    azpiIzenb.pack()

    espacio.pack()

    erab = ttk.Label(window, text='Pasahitza: ', font=("Calibri"))
    erab.place(x=70, y=100)

    passwd = ttk.Entry(window, justify=tk.LEFT, width=32 ,textvariable="Pasahitza")
    passwd.place(x=70,y=120)

    passwd2 = ttk.Label(window, text='Pasahitza errepikatu: ', font=("Calibri"))
    passwd2.place(x=70, y=160)

    pasahitza = ttk.Entry(window, justify=tk.LEFT, width=32, textvariable="Pasahitza2")
    pasahitza.place(x=70, y=180)

    buttonirten = tk.Button(window, text="Irten", width=8, font=("Calibri"))
    buttonirten.place(x=70, y=300)
    buttonados = tk.Button(window, text="Ados", width=8, font=("Calibri"))
    buttonados.place(x=220, y=300)

    window.mainloop()




