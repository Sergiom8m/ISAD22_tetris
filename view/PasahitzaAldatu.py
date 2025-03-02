import tkinter as tk
import sys

import view
from model.JokalariZerrenda import JokalariZerrenda

#Koloreak
botoi_kolor = "#ffffff"
atzeko_kolor = "#7ec0ee"

class PasahitzaAldatu(object):


    def __init__(self, erabiltzaile):
        super(PasahitzaAldatu, self).__init__()
        self.erabiltzaile=erabiltzaile
        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)  # "X" botoia erabiltzean programa gelditzea ahalbidetzen du
        self.window.title("Pasahitza Aldatu")
        self.window.geometry('420x420')
        global atzeko_kolor
        atzeko_kolor = JokalariZerrenda().get_erabiltzailea_idz("admin").atzeko_kolore if not None else "#7ec0ee"
        global botoi_kolor
        botoi_kolor = JokalariZerrenda().get_erabiltzailea_idz("admin").botoi_kolore if not None else "#ffffff"
        self.window['bg']=atzeko_kolor
        self.window.resizable(False, False)
        izenburua = tk.Label(self.window, bg=atzeko_kolor, text='PASAHITZA ALDATU', font=("Times New Roman", 25))
        izenburua.pack()

        azpiIzenb = tk.Label(self.window, bg=atzeko_kolor, text='Zure pasahitza berria idatz ezazu: ', font=("Calibri"))
        azpiIzenb.pack()

        passwd = tk.Label(self.window, bg=atzeko_kolor, text='Pasahitza: ', font=("Times New Roman", 16))
        passwd.place(x=70, y=70)

        self.pasahitz = tk.Entry(self.window,bg=botoi_kolor, justify=tk.LEFT, width=23 ,textvariable="Pasahitza", font=("Times New Roman", 16))
        self.pasahitz.place(x=70,y=100)

        passwd2 = tk.Label(self.window, bg=atzeko_kolor, text='Pasahitza errepikatu:', font=("Times New Roman", 16))
        passwd2.place(x=70, y=140)

        self.pasahitz2 = tk.Entry(self.window,bg=botoi_kolor, justify=tk.LEFT, width=23, textvariable="Pasahitza2", font=("Times New Roman", 16))
        self.pasahitz2.place(x=70, y=170)

        mezu = tk.Label(self.window, bg=atzeko_kolor, text='Galdera berria sartu: ', font=("Times New Roman", 16))
        mezu.place(x=70, y=210)

        self.galdera = tk.Entry(self.window,bg=botoi_kolor, justify=tk.LEFT, width=23, textvariable="Galdera",
                                   font=("Times New Roman", 16))
        self.galdera.place(x=70, y=240)

        mezu2 = tk.Label(self.window, bg=atzeko_kolor, text='Galderari erantzuna eman: ', font=("Times New Roman", 16))
        mezu2.place(x=70, y=280)

        self.erantzuna = tk.Entry(self.window, bg=botoi_kolor, justify=tk.LEFT, width=23, textvariable="Erantzuna",
                                font=("Times New Roman", 16))
        self.erantzuna.place(x=70, y=310)


        buttonirten = tk.Button(self.window,
                                bg=botoi_kolor,
                                text="Irten",
                                cursor="hand2",
                                width=8,
                                font="Calibri",
                                command=self.irten)
        buttonirten.place(x=70, y=375)
        buttonados = tk.Button(self.window, bg=botoi_kolor, text="Ados", cursor="hand2", width=8, font=("Calibri"), command=self.aldatuta)
        buttonados.place(x=220, y=375)

        self.window.mainloop()

    #PANTAILETAN MUGITZEKO
    def irten(self):
        self.window.destroy()
        view.Identifikazioa.Identifikazioa().__init__()

    #DATU BASEAREKIN KONEKTATZEKO METODOA:

    def aldatuta(self):
        pasahitza1 = self.pasahitz.get()
        pasahitza2 = self.pasahitz2.get()
        galdera = self.galdera.get()
        erantzuna = self.erantzuna.get()
        if (len(pasahitza1) != 0) & (len(pasahitza2) != 0):
            if pasahitza1 == pasahitza2:
                mezu = tk.Label(self.window, bg=atzeko_kolor, fg="green",
                                text='Ondo aldatu da      ',
                                font="Calibri")
                mezu.place(x=60, y=350)
                self.erabiltzaile.set_pasahitza_berria(pasahitza1, galdera, erantzuna)
            else:
                mezu = tk.Label(self.window, bg=atzeko_kolor, fg="red", text='Pasahitzak ez dira berdinak        ',
                                font="Calibri")
                mezu.place(x=60, y=350)
        else:
            mezu = tk.Label(self.window, bg=atzeko_kolor, fg="red", text='Sar ezazu pasahitz berria                 ',
                            font="Calibri")
            mezu.place(x=60, y=350)
