import tkinter as tk
import sys
import view
from view.JokatuLehioa import JokatuLehioa
from model.JokalariZerrenda import JokalariZerrenda

#Koloreak
botoi_kolor = "#ffffff"
atzeko_kolor = "#7ec0ee"

class Ezarpenak(object):

    def __init__(self, erabiltzaile):
        super(Ezarpenak, self).__init__()
        self.erabiltzaile=erabiltzaile
        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)  # "X" botoia erabiltzean programa gelditzea ahalbidetzen du
        self.window.geometry('400x400')
        self.window.title("Tetris Jokoa")
        global atzeko_kolor
        atzeko_kolor = JokalariZerrenda().get_erabiltzailea_idz("admin").atzeko_kolore if not None else "#7ec0ee"
        global botoi_kolor
        botoi_kolor = JokalariZerrenda().get_erabiltzailea_idz("admin").botoi_kolore if not None else "#ffffff"
        self.window['bg'] = atzeko_kolor
        self.window.resizable(False, False)


        espacio = tk.Label(self.window, bg=atzeko_kolor, text="")
        titulo = tk.Label(self.window, bg=atzeko_kolor, text="Partidaren ezarpenak", font=("Times New Roman",25))
        titulo.pack()
        espacio.pack()

        mensaje = tk.Label(self.window,
                           bg=atzeko_kolor,
                           text="Partidaren ezaugarriak aukera itzazu ",
                           font=("Calibri"))
        mensaje.pack()

        mensaje2 = tk.Label(self.window,
                            bg=atzeko_kolor,
                            text="(bana aukeratu arte ezingo da partida hasi) ",
                            font=("Calibri"))
        mensaje2.pack()

        espacio.pack()

        titulo_abiadura = tk.Label(self.window, bg=atzeko_kolor, text="Abiadura:", font=("Calibri", 14))
        titulo_abiadura.place(x=60, y= 110)

        self.opcion = tk.IntVar()
        self.opcion.set(value=1)

        tk.Radiobutton(self.window,
                       cursor="hand2",
                       bg=atzeko_kolor,
                       text="Erraza",
                       variable=self.opcion,
                       value=1).place(x=20, y=150)
        tk.Radiobutton(self.window,
                       cursor="hand2",
                       bg=atzeko_kolor,
                       text="Ertaina",
                       variable=self.opcion,
                       value=2).place(x=115, y=150)
        tk.Radiobutton(self.window,
                       cursor="hand2",
                       bg=atzeko_kolor,
                       text="Zaila",
                       variable=self.opcion,
                       value=3).place(x=210, y=150)
        tk.Radiobutton(self.window,
                       cursor="hand2",
                       bg=atzeko_kolor,
                       text="Oso zaila",
                       variable=self.opcion,
                       value=4).place(x=290, y=150)

        titulo_tamaina = tk.Label(self.window, bg=atzeko_kolor, text="Tamaina:", font=("Calibri", 14))
        titulo_tamaina.place(x=60, y=190)

        self.opcion2 = tk.IntVar()
        self.opcion2.set(value=1)

        tk.Radiobutton(self.window,
                       cursor="hand2",
                       bg=atzeko_kolor,
                       text="Txikia",
                       variable=self.opcion2,
                       value=1).place(x=20, y=230)
        tk.Radiobutton(self.window,
                       cursor="hand2",
                       bg=atzeko_kolor,
                       text="Ertaina",
                       variable=self.opcion2,
                       value=2).place(x=100, y=230)
        tk.Radiobutton(self.window,
                       cursor="hand2",
                       bg=atzeko_kolor,
                       text="Ertain-handia",
                       variable=self.opcion2,
                       value=3).place(x=185, y=230)
        tk.Radiobutton(self.window,
                       cursor="hand2",
                       bg=atzeko_kolor,
                       text="Handia",
                       variable=self.opcion2,
                       value=4).place(x=310, y=230)

        buttonirten = tk.Button(self.window,
                                cursor="hand2",
                                bg=botoi_kolor,
                                text="Irten",
                                width=8,
                                font="Calibri",
                                command=self.irten)
        buttonirten.place(x=60, y=300)
        buttonj = tk.Button(self.window,
                            cursor="hand2",
                            bg=botoi_kolor,
                            text="Jolastu",
                            width=8,
                            font="Calibri",
                            command=self.jolastenHasi)
        buttonj.place(x=220, y=300)

        self.window.mainloop()

    # PANTAILETAN MUGITZEKO
    def irten(self):
        self.window.destroy()
        if self.erabiltzaile is None:
            view.HasierakoMenua.HasierakoMenua().__init__()
        else:
            view.Profila.Profila(self.erabiltzaile).__init__()

    def jolastenHasi(self):
        self.window.destroy()
        abiadura = 1

        if self.opcion.get() == 1: abiadura = 800
        elif self.opcion.get() == 2: abiadura = 400
        elif self.opcion.get() == 3: abiadura = 200
        elif self.opcion.get() == 4: abiadura = 100

        tamaina = 1
        if self.opcion2.get() == 1: tamaina = 10
        elif self.opcion2.get() == 2: tamaina = 20
        elif self.opcion2.get() == 3: tamaina = 30
        elif self.opcion2.get() == 4: tamaina = 40

        JokatuLehioa(abiadura, tamaina, self.erabiltzaile, 0, None).__init__()
