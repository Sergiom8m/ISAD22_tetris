import tkinter as tk
from tkinter import *
from tkinter import ttk
import sys
from view import Profila
from model.JokalariZerrenda import JokalariZerrenda

# https://www.youtube.com/watch?v=0WafQCaok6g scrollbar

# Koloreak
botoi_kolor = "#ffffff"
atzeko_kolor = "#7ec0ee"


class ErabiltzaileakEzabatu(object):

    def __init__(self, erabiltzailea):
        super(ErabiltzaileakEzabatu, self).__init__()
        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)  # "X" botoia erabiltzean programa gelditzea ahalbidetzen du
        self.window.title("Erabiltzaileak Ezabatu")
        self.window.geometry('400x400')

        self.erabiltzailea= erabiltzailea

        global atzeko_kolor
        atzeko_kolor = erabiltzailea.atzeko_kolore if not None else "#7ec0ee"
        global botoi_kolor
        botoi_kolor = erabiltzailea.botoi_kolore if not None else "#ffffff"
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

        emaitza = JokalariZerrenda().get_erabiltzaile_guztiak()
        lerro_kop = len(emaitza)

        Label(self.marko, text="Datu baseko erabiltzaileak:", font="Helvetica 12 bold", bg=atzeko_kolor).grid(row=0,
                                                                                                              column=0,
                                                                                                              pady=10,
                                                                                                              padx=10)
        for i in range(len(emaitza)):
            if emaitza[i][0] != "admin":  # "admin" ezin denez ezabatu, ezin da inprimatuko
                Label(self.marko,
                      text=emaitza[i][0],
                      bg=atzeko_kolor).grid(row=i+1,
                                            column=0,
                                            pady=10,
                                            padx=10)
                Button(self.marko,
                       text="Ezabatu",
                       cursor="hand2",
                       bg=botoi_kolor,
                       command=lambda lerro=i: self.erabiltzailea_ezabatu(emaitza[lerro][0])).grid(row=i+1,
                                                                                                   column=1,
                                                                                                   pady=10,
                                                                                                   padx=10)
        if lerro_kop == 1:  # beti egongo da erabiltzaile bat, "admin"
            Label(self.marko,
                  text="Ez dago erabiltzailerik",
                  font="Helvetica",
                  bg=atzeko_kolor).grid(row=lerro_kop,
                                        column=0,
                                        pady=10,
                                        padx=10)
        Button(self.marko,
               text="Irten",
               cursor="hand2",
               width=8,
               font=("Times New Roman", 16),
               bg=botoi_kolor,
               command=self.irten).grid(row=lerro_kop+2,
                                        column=1,
                                        pady=10,
                                        padx=10)
        self.window.mainloop()

    def erabiltzailea_ezabatu(self, erabiltzaile):
        JokalariZerrenda().erabiltzailea_ezabatu(erabiltzaile)
        self.window.destroy()
        ErabiltzaileakEzabatu(self.erabiltzailea).__init__()

    def irten(self):
        self.window.destroy()
        Profila.Profila(self.erabiltzailea).__init__()
