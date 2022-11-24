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

        self.opcion = tk.IntVar()
        self.opcion.set(value=1)

        tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="1", variable=self.opcion, value=1).place(x=50, y=150)
        tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="2", variable=self.opcion, value=2).place(x=130, y=150)
        tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="3", variable=self.opcion, value=3).place(x=210, y=150)
        tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="4", variable=self.opcion, value=4).place(x=280, y=150)

        # ************** BOTOIEN KOLOREA *******************

        titulo_botoiak = tk.Label(self.window, bg=atzeko_kolor, text="Botoien kolorea:", font=("Calibri", 14))
        titulo_botoiak.place(x=60, y=200)

        self.opcion2 = tk.IntVar()
        self.opcion2.set(value=1)

        tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="1", variable=self.opcion2, value=1).place(x=50, y=230)
        tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="2", variable=self.opcion2, value=2).place(x=130, y=230)
        tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="3", variable=self.opcion2, value=3).place(x=210, y=230)
        tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="4", variable=self.opcion2, value=4).place(x=280, y=230)

        # ************** ADREILUEN KOLOREA *******************

        titulo_adreiluak = tk.Label(self.window, bg=atzeko_kolor, text="Adreiluak:", font=("Calibri", 14))
        titulo_adreiluak.place(x=60, y=280)

        self.opcion3 = tk.IntVar()
        self.opcion3.set(value=1)

        tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="1", variable=self.opcion3, value=1).place(x=50, y=310)
        tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="2", variable=self.opcion3, value=2).place(x=130, y=310)
        tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor,text="3", variable=self.opcion3, value=3).place(x=210, y=310)
        tk.Radiobutton(self.window, cursor="hand2", bg=atzeko_kolor, text="4", variable=self.opcion3, value=4).place(x=280, y=310)

        # ************** SONINUA *******************

        titulo_soinua = tk.Label(self.window, bg=atzeko_kolor, text="Musika:", font=("Calibri", 14))
        titulo_soinua.place(x=60, y=360)

        self.musika_com_box = ttk.Combobox(self.window, state="readonly", values=["(Musikarik gabe)", "Original Theme", "99s Theme", "Orchestra Theme", "Piano Theme"])
        self.musika_com_box.place(x=150, y=390)

        buttonirten = tk.Button(self.window, cursor="hand2", bg=botoi_kolor, text="Irten", width=8, font=("Calibri"), command=self.irten)
        buttonirten.place(x=60, y=500)
        buttonGorde = tk.Button(self.window, cursor="hand2", bg=botoi_kolor, text="Aldaketak gorde", width=14, font=("Calibri"), command=self.aldaketak)
        buttonGorde.place(x=220, y=500)


        self.window.mainloop()

    # PANTAILETAN MUGITZEKO
    def irten(self):
        self.window.destroy()
        view.Profila.Profila(self.erabiltzaile).__init__()


    def aldaketak(self):
        atzeko_kolor = "#ffffff"
        print(self.opcion.get())
        print(self.opcion2.get())

        if self.opcion.get() == 1:
            atzeko_kolor = "Red"
            bg = atzeko_kolor
        elif self.opcion.get() == 2:
            atzeko_kolor = "Red"
            bg = atzeko_kolor
        elif self.opcion.get() == 3:
            atzeko_kolor = "Red"
            bg = atzeko_kolor
        elif self.opcion.get() == 4:
            atzeko_kolor = "Red"
            bg = atzeko_kolor

        pieza_kolorea = "#ffffff"
        if self.opcion2.get() == 1:
            botoien_kolor = "Red"
            bg = atzeko_kolor
        elif self.opcion2.get() == 2:
            botoien_kolor = "Red"
            bg = atzeko_kolor
        elif self.opcion2.get() == 3:
            botoien_kolor = "Red"
            bg = atzeko_kolor
        elif self.opcion2.get() == 4:
            botoien_kolor = "Red"
            bg = atzeko_kolor

        pieza_kolorea = "#ffffff"
        if self.opcion3.get() == 1:
            adreilu_kolor = "Red"
            bg = atzeko_kolor
        elif self.opcion3.get() == 2:
            adreilu_kolor = "Red"
            bg = atzeko_kolor
        elif self.opcion3.get() == 3:
            adreilu_kolor = "Red"
            bg = atzeko_kolor
        elif self.opcion3.get() == 4:
            adreilu_kolor = "Red"
            bg = atzeko_kolor

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

        self.window.destroy()
        DbConn.pertsonalizazioa_aldatu(DbConn(), atzeko_kolor, botoien_kolor, adreilu_kolor, musika, self.erabiltzaile)
        #JokatuLehioa(atzeko_kolor, atzeko_kolor, self.erabiltzaile).__init__()7