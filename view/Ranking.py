import tkinter as tk
from tkinter import *
from tkinter import ttk
import sys
from view import Profila
from model.JokalariZerrenda import JokalariZerrenda
from model.Ranking import Ranking as modRanking

# https://www.youtube.com/watch?v=0WafQCaok6g scrollbar

# Koloreak
botoi_kolor = "#ffffff"
atzeko_kolor = "#7ec0ee"


class Ranking(object):

    def __init__(self, erabiltzaile, tamaina, abiadura):
        super(Ranking, self).__init__()
        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)  # "X" botoia erabiltzean programa gelditzea ahalbidetzen du
        self.window.title("Ranking")
        self.window.geometry('400x400')

        self.tamaina=tamaina
        self.abiadura=abiadura
        self.erabiltzaile=erabiltzaile
        global atzeko_kolor
        atzeko_kolor = JokalariZerrenda().get_erabiltzailea_idz("admin").atzeko_kolore if not None else "#7ec0ee"
        global botoi_kolor
        botoi_kolor = JokalariZerrenda().get_erabiltzailea_idz("admin").botoi_kolore if not None else "#ffffff"
        self.window['bg'] = atzeko_kolor
        self.window.resizable(False, False)


        # 1 create a main frame
        nagusia = Frame(self.window, bg=atzeko_kolor)
        nagusia.pack(fill=BOTH, expand=1)

        # 2 create a canvas
        nire_canvas = Canvas(nagusia, bg=atzeko_kolor)
        nire_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # 3 add a scrollbar to the canvas
        scrollbar = ttk.Scrollbar(nagusia, orient=VERTICAL, command=nire_canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # 4 configure the canvas
        nire_canvas.configure(yscrollcommand=scrollbar.set)
        nire_canvas.bind('<Configure>', lambda e: nire_canvas.configure(scrollregion=nire_canvas.bbox("all")))

        # 5 create another frame inside canvas
        self.marko = Frame(nire_canvas, bg=atzeko_kolor)

        # 6 add that new frame to a window in the canvas
        nire_canvas.create_window((0, 0), window=self.marko, anchor="nw")

        if tamaina is None:
            ranking = modRanking().get_ranking(0, 0)
            nire_pos = erabiltzaile.nire_posizioa_rankingean(0, 0)
        else:
            ranking = modRanking().get_ranking(self.tamaina, self.abiadura)
            nire_pos = erabiltzaile.nire_posizioa_rankingean(self.tamaina, self.abiadura)

        lerroKop = len(ranking)

        if lerroKop == 0:
            Label(self.marko, text="Ez da partidarik jolastu konfigurazio honekin", font="Helvetica", bg=atzeko_kolor).grid(row=lerroKop, column=0, pady=10, padx=10)
            Button(self.marko, text="Irten", cursor="hand2", width=8, font=("Times New Roman", 16), bg=botoi_kolor,
                   command=self.irten).grid(row=10, column=0, pady=10, padx=10)
        else:
            Label(self.marko, text="Posizioa", bg=atzeko_kolor).grid(row=1, column=0, pady=10, padx=10)
            Label(self.marko, text="Puntuazioa", bg=atzeko_kolor).grid(row=1, column=1, pady=10, padx=10)
            Label(self.marko, text="Erabiltzailea", bg=atzeko_kolor).grid(row=1, column=2, pady=10, padx=10)
            for i in range(3):
                if lerroKop > i:
                    Label(self.marko, text=ranking[i][2], bg=atzeko_kolor).grid(row=i + 2, column=0, pady=10, padx=10)
                    Label(self.marko, text=ranking[i][1], bg=atzeko_kolor).grid(row=i + 2, column=1, pady=10, padx=10)
                    Label(self.marko, text=ranking[i][0], bg=atzeko_kolor).grid(row=i + 2, column=2, pady=10, padx=10)
                else:
                    Label(self.marko, text=i+1, bg=atzeko_kolor).grid(row=i + 2, column=0, pady=10, padx=10)
                    Label(self.marko, text='XXXXX', bg=atzeko_kolor).grid(row=i + 2, column=1, pady=10, padx=10)
                    Label(self.marko, text='XXXXX', bg=atzeko_kolor).grid(row=i + 2, column=2, pady=10, padx=10)

            Label(self.marko, text="...", bg=atzeko_kolor).grid(row=6, column=1, pady=10, padx=10)

            if nire_pos is None:
                Label(self.marko, text="Ez zaude ranking-ean", bg=atzeko_kolor).grid(row=7, column=0, pady=10, padx=10)
            else:
                Label(self.marko, text=nire_pos[0], bg=atzeko_kolor).grid(row=7, column=0, pady=10, padx=10)
                Label(self.marko, text=nire_pos[1], bg=atzeko_kolor).grid(row=7, column=1, pady=10, padx=10)
                Label(self.marko, text=erabiltzaile, bg=atzeko_kolor).grid(row=7, column=2, pady=10, padx=10)

            Button(self.marko, text="Irten", cursor="hand2", width=8, font=("Times New Roman", 16), bg=botoi_kolor,
                   command=self.irten).grid(row=10, column=1, pady=10, padx=10)
        self.window.mainloop()

    def irten(self):
        self.window.destroy()
        Profila.Profila(self.erabiltzaile).__init__()
