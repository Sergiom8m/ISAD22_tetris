import tkinter as tk
from tkinter import ttk


class PasahitzaAldatu(object):
    def __init__(self):
        super(PasahitzaAldatu, self).__init__()
        window = tk.Tk()
        window.title("PASAHITZA ALDATU")
        window.geometry('400x400')
        window.resizable(False, False)
        espacio= ttk.Label(window, text="")
        izenburua = ttk.Label(window, text='PASAHITZA ALDATU', font=("Times New Roman", 25))
        izenburua.pack()

        espacio.pack()

        azpiIzenb = ttk.Label(window, text='Zure pasahitza berria idatz ezazu: ', font=("Calibri"))
        azpiIzenb.pack()

        espacio.pack()

        passwd = ttk.Label(window, text='Pasahitza: ', font=("Times New Roman", 16))
        passwd.place(x=70, y=100)

        pasahitz = ttk.Entry(window, justify=tk.LEFT, width=23 ,textvariable="Pasahitza", font=("Times New Roman", 16))
        pasahitz.place(x=70,y=130)

        passwd2 = ttk.Label(window, text='Pasahitza errepikatu:', font=("Times New Roman", 16))
        passwd2.place(x=70, y=170)

        pasahitz2 = ttk.Entry(window, justify=tk.LEFT, width=23, textvariable="Pasahitza2", font=("Times New Roman", 16))
        pasahitz2.place(x=70, y=200)

        buttonirten = tk.Button(window, text="Irten", width=8, font=("Calibri"))
        buttonirten.place(x=70, y=300)
        buttonados = tk.Button(window, text="Ados", width=8, font=("Calibri"))
        buttonados.place(x=220, y=300)


        window.mainloop()




