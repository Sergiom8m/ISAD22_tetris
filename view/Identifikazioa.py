import sys
import tkinter as tk

import view.HasierakoMenua
from view.Profila import Profila
from view.PasahitzaBerreskuratu import PasahitzaBerreskuratu
from model.JokalariZerrenda import JokalariZerrenda

# Koloreak
botoi_kolor = "#ffffff"
atzeko_kolor = "#7ec0ee"


class Identifikazioa(object):

    def __init__(self):
        super(Identifikazioa, self).__init__()
        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)  # "X" botoia erabiltzean programa gelditzea ahalbidetzen du
        self.window.title("Identifikazioa")
        self.window.geometry('400x400')
        self.window['bg'] = atzeko_kolor
        self.window.resizable(False, False)

        espacio = tk.Label(self.window, bg=atzeko_kolor, text="")

        # Izenburua
        tk.Label(self.window, bg=atzeko_kolor, text='IDENTIFIKAZIOA', font=("Times New Roman", 25)).pack()

        espacio.pack()

        # Azpi-izenburua
        tk.Label(self.window, bg=atzeko_kolor, text='Mesedez, zure burua identifikatu', font=("Calibri")).pack()

        espacio.pack()

        # "Erabiltzaile" label
        tk.Label(self.window, bg=atzeko_kolor, text='Erabiltzailea: ', font=("Times New Roman", 16)).place(x=70, y=100)

        self.erabiltzaile = tk.Entry(self.window, bg=botoi_kolor, justify=tk.LEFT, width=23,
                                     textvariable="Erabiltzailea",
                                     font=("Times New Roman", 16))
        self.erabiltzaile.place(x=70, y=130)

        # "Password" label
        tk.Label(self.window, bg=atzeko_kolor, text='Pasahitza: ', font=("Times New Roman", 16)).place(x=70, y=170)

        self.pasahitza = tk.Entry(self.window, bg=botoi_kolor, justify=tk.LEFT, width=23, textvariable="Pasahitza",
                                  font=("Times New Roman", 16))
        self.pasahitza.place(x=70, y=200)

        # "Pasahitza berreskuratu" botoia
        tk.Button(self.window, cursor="hand2", bg=botoi_kolor, text="Pasahitza berreskuratu", font=("Times New Roman", 16),
                            command=self.identifik_berresk).place(x=90, y=250)

        # "Irten" botoia
        tk.Button(self.window,
                  cursor="hand2",
                  bg=botoi_kolor,
                  text="Irten",
                  width=8,
                  font=("Times New Roman", 16),
                  command=self.irten).place(x=70, y=350)

        buttonerr = tk.Button(self.window, cursor="hand2", bg=botoi_kolor, text="Sartu", width=8, font=("Times New Roman", 16),
                              command=self.identifik_erregis)
        buttonerr.place(x=220, y=350)

        self.window.mainloop()

    # DATU BASEAREKIN KONEKTATZEKO:
    def identifik_erregis(self):
        id = self.erabiltzaile.get()
        sartutako_pasahitza = self.pasahitza.get()

        if (len(id) != 0) & (len(sartutako_pasahitza) != 0):
            jokalaria = JokalariZerrenda().get_erabiltzailea_idz(id)

            if jokalaria is None:
                error = tk.Label(self.window, bg=atzeko_kolor, fg="red",
                                 text='Ez dago erabiltzaile hori                  ', font=("Times New Roman", 16))
                error.place(x=70, y=300)
            else:
                if sartutako_pasahitza != jokalaria.pasahitza:
                    error = tk.Label(self.window, bg=atzeko_kolor, fg="red",
                                 text='Pasahitza ez du koinziditzen                ',
                                 font=("Times New Roman", 16))
                    error.place(x=70, y=300)
                else:
                    # PROFIL PANTAILARA JOTZEKO
                    self.window.destroy()
                    Profila(jokalaria).__init__(jokalaria)
        else:
            error = tk.Label(self.window, bg=atzeko_kolor, fg="red", text='Sar itzazu datu guztiak                  ',
                             font=("Times New Roman", 16))
            error.place(x=70, y=300)

    # BESTE PANTAILETARA JOTZEKO:
    def identifik_berresk(self):
        self.window.destroy()
        PasahitzaBerreskuratu().__init__()

    def irten(self):
        self.window.destroy()
        view.HasierakoMenua.HasierakoMenua().__init__()
