import tkinter as tk
import sys
from tkinter import ttk
import view
from controller.db_conn import DbConn

# Defektuzko koloreak
botoi_kolor = "#ffffff"
atzeko_kolor = "#7ec0ee"


class Pertsonalizatu(object):

    def __init__(self, erabiltzaile):
        super(Pertsonalizatu, self).__init__()
        self.erabiltzaile = erabiltzaile
        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)  # "X" botoia erabiltzean programa gelditzea ahalbidetzen du
        self.window.geometry('400x800')
        self.window.title("Pertsonalizazio Menua")
        global atzeko_kolor
        atzeko_kolor = DbConn.get_jokalari_fondoa(DbConn(), self.erabiltzaile)
        self.window['bg'] = atzeko_kolor
        self.window.resizable(False, False)

        espacio = tk.Label(self.window, bg=atzeko_kolor, text="")
        titulo = tk.Label(self.window, bg=atzeko_kolor, text="Jokoaren pertsonalizazioa", font=("Times New Roman",25))
        titulo.pack()
        espacio.pack()

        mensaje = tk.Label(self.window, bg=atzeko_kolor, text="Jokoaren ezugarriak eta itxura aukeratu. ", font=("Calibri", 14))
        mensaje.pack()

        mensaje2 = tk.Label(self.window, bg=atzeko_kolor, text="(Bana aukeratu arte ezingo da partida hasi) ", font=("Calibri", 14))
        mensaje2.pack()

        espacio.pack()

        # ************** ATZEKO KOLOREA *******************

        titulo_fondo = tk.Label(self.window, bg=atzeko_kolor, text="Atzeko kolorea:", font=("Calibri", 14))
        titulo_fondo.place(x=60, y= 120)

        self.fondoa_com_box = ttk.Combobox(self.window, state="readonly",
                                           values=["Larrosa", "Gorria", "Urdina", "Berdea"])
        self.fondoa_com_box.place(x=150, y=150)

        #self.opcion = tk.IntVar()
        #self.opcion.set(value=1)

        #tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="1", variable=self.opcion, value=1).place(x=50, y=150)
        #tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="2", variable=self.opcion, value=2).place(x=130, y=150)
        #tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="3", variable=self.opcion, value=3).place(x=210, y=150)
        #tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="4", variable=self.opcion, value=4).place(x=280, y=150)

        # ************** BOTOIEN KOLOREA *******************

        #titulo_botoiak = tk.Label(self.window, bg=atzeko_kolor, text="Botoien kolorea:", font=("Calibri", 14))
        #titulo_botoiak.place(x=60, y=200)

        #self.opcion2 = tk.IntVar()
        #self.opcion2.set(value=1)


        #tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="1", variable=self.opcion2, value=1).place(x=50, y=230)
        #tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="2", variable=self.opcion2, value=2).place(x=130, y=230)
        #tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="3", variable=self.opcion2, value=3).place(x=210, y=230)
        #tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="4", variable=self.opcion2, value=4).place(x=280, y=230)

        # ************** ADREILUEN KOLOREA *******************

        titulo_adreiluak = tk.Label(self.window, bg=atzeko_kolor, text="Adreiluak:", font=("Calibri", 14))
        titulo_adreiluak.place(x=60, y=200)

        self.adreilu_com_box = ttk.Combobox(self.window, state="readonly",
                                          values=["(Default)", "Pastel", "Urdinak", "Berdeak"])
        self.adreilu_com_box.place(x=150, y=250)


        # ************** SOINUA *******************

        titulo_soinua = tk.Label(self.window, bg=atzeko_kolor, text="Musika:", font=("Calibri", 14))
        titulo_soinua.place(x=60, y=300)

        self.musika_com_box = ttk.Combobox(self.window, state="readonly", values=["(Musikarik gabe)", "Original Theme", "99s Theme", "Orchestra Theme", "Piano Theme"])
        self.musika_com_box.place(x=150, y=350)

        buttonirten = tk.Button(self.window, cursor="hand2", bg=botoi_kolor, text="Irten", width=8, font=("Calibri"), command=self.irten)
        buttonirten.place(x=60, y=400)
        buttonGorde = tk.Button(self.window, cursor="hand2", bg=botoi_kolor, text="Aldaketak gorde", width=14, font=("Calibri"), command=self.aldaketak)
        buttonGorde.place(x=220, y=400)


        self.window.mainloop()

    # PANTAILETAN MUGITZEKO


    def irten(self):
        self.window.destroy()
        view.Profila.Profila(self.erabiltzaile).__init__()


    def aldaketak(self):

        atzeko_kolor = None
        #Atzeko kolorea:
        if self.fondoa_com_box.get() == "Larrosa":
            atzeko_kolor = "Pink"
        elif self.fondoa_com_box.get() == "Gorria":
            atzeko_kolor = "tomato"
        elif self.fondoa_com_box.get() == "Urdina":
            atzeko_kolor = "#7ec0ee"
        elif self.fondoa_com_box.get() == "Berdea":
            atzeko_kolor = "pale green"

        self.window['bg'] = atzeko_kolor

        #Piezen kolorea:
        adreilu_kolor = None
        if self.adreilu_com_box.get() == "(Default)":
            adreilu_kolor = 1
        elif self.adreilu_com_box.get() == "Pastel":
            adreilu_kolor = 2
        elif self.adreilu_com_box.get() == "Urdinak":
            adreilu_kolor = 3
        elif self.adreilu_com_box.get() == "Berdeak":
            adreilu_kolor = 4

        #Musika:
        musika = None
        if self.musika_com_box.get() == "(Musikarik gabe)":
            musika = "ez"
        elif self.musika_com_box.get() == "Original Theme":
            musika = "original"
        elif self.musika_com_box.get() == "99s Theme":
            musika = "99"
        elif self.musika_com_box.get() == "Orchestra Theme":
            musika = "orchestra"
        elif self.musika_com_box.get() == "Piano Theme":
            musika = "piano"

        DbConn.pertsonalizazioa_aldatu(DbConn(), atzeko_kolor, adreilu_kolor, musika, self.erabiltzaile)
        self.irten()
        #JokatuLehioa(atzeko_kolor, atzeko_kolor, self.erabiltzaile).__init__()