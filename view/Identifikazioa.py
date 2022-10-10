import tkinter as tk
from tkinter import ttk

class Identifikazioa(object):

    def __init__(self):
        super(Identifikazioa, self).__init__()
        window = tk.Tk()
        window.title("IDENTIFIKAZIOA")
        window.geometry('400x400')
        window.resizable(False, False)


        espacio = ttk.Label(window, text="")
        izenburua = ttk.Label(window, text='IDENTIFIKAZIOA', font=("Times New Roman", 25))
        izenburua.pack()

        espacio.pack()

        azpiIzenb = ttk.Label(window, text='Mesedez, zure burua identifikatu', font=("Calibri"))
        azpiIzenb.pack()

        espacio.pack()

        erab = ttk.Label(window, text='Erabiltzailea: ', font=("Times New Roman", 16))
        erab.place(x=70, y=100)

        erabiltzaile = ttk.Entry(window, justify=tk.LEFT, width=23, textvariable="Erabiltzailea",
                                 font=("Times New Roman", 16))
        erabiltzaile.place(x=70, y=130)

        passwd = ttk.Label(window, text='Pasahitza: ', font=("Times New Roman", 16))
        passwd.place(x=70, y=170)

        pasahitza = ttk.Entry(window, justify=tk.LEFT, width=23, textvariable="Pasahitza", font=("Times New Roman", 16))
        pasahitza.place(x=70, y=200)

        buttonb = tk.Button(window, text="Pasahitza berreskuratu", font=("Times New Roman", 16))
        buttonb.place(x=90, y=250)
        buttonb.bind("<Button-1>", )

        buttonirten = tk.Button(window, text="Irten", width=8, font=("Times New Roman", 16))
        buttonirten.place(x=70, y=350)
        # buttonirten.bind("<Button-1>",identifik_hasiera(window))

        buttonerr = tk.Button(window, text="Erregistratu", width=8, font=("Calibri"))
        buttonerr.place(x=220, y=350)

        window.mainloop()