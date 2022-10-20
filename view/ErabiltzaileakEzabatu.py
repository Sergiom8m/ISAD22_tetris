import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
import sys
from view import Profila


# https://www.youtube.com/watch?v=0WafQCaok6g ESTA ES LA QUE ESTA PUESTA, PERO NO FUNCIONA... CREO Q ES POR LAMBDA
# https://www.youtube.com/watch?v=VmlgrrXAqb4 ESTE ES PARECIDO PERO EL LAMBDA CAMBIA....PERO TAMPOCO VA
# https://www.tutorialspoint.com/python/tk_scrollbar.htm ESTE VA PERO ES MUY SIMPLE Y NO SE SI NOS SIRVE PARA LO QUE QUEREMOS
# https://www.aprendeaprogramar.com/mod/forum/discuss.php?d=2839 ESTE CREO QUE MEZCLA LAS PRIMERAS CON LA TERCERA PERO NO LO ENTIENDO BIEN

# https://www.youtube.com/watch?v=hL2tMm1FNkE el que esta ahora
class ErabiltzaileakEzabatu(object):

    def __init__(self):
        super(ErabiltzaileakEzabatu, self).__init__()
        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)  # "X" botoia erabiltzean programa gelditzea ahalbidetzen du
        self.window.title("ERABILTZAILEAK EZABATU")
        self.window.geometry('400x400')
        self.window.resizable(False, False)

        # 1 create a main frame
        nagusia = Frame(self.window)
        nagusia.pack(fill=BOTH, expand=1)

        # 2 create a canvas
        nire_canvas = Canvas(nagusia)
        nire_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # 3 add a scrollbar to the canvas
        scrollbar = ttk.Scrollbar(nagusia, orient=VERTICAL, command=nire_canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # 4 configure the canvas
        nire_canvas.configure(yscrollcommand=scrollbar.set)
        nire_canvas.bind('<Configure>', lambda e: nire_canvas.configure(scrollregion=nire_canvas.bbox("all")))

        # 5 create another frame inside canvas
        self.marko = Frame(nire_canvas)

        # 6 add that new frame to a window in the canvas
        nire_canvas.create_window((0, 0), window=self.marko, anchor="nw")

        emaitza = self.erabiltzailea_guztiak_lortu()
        lerroKop = 0

        Label(self.marko, text="Erabiltzaile izena", font="Helvetica 12 bold").grid(row=0, column=0, pady=10, padx=10)
        for i in range(len(emaitza)):
            Label(self.marko, text=emaitza[i][0]).grid(row=i+1, column=0, pady=10, padx=10)
            Button(self.marko, text="Ezabatu", command=lambda: self.erabiltzailea_ezabatu(i, emaitza)).grid(row=i+1, column=1, pady=10, padx=10)
            lerroKop = i
        Button(self.marko, text="Irten", width=8, font=("Times New Roman", 16), command=self.irten).grid(row=lerroKop+2, column=1, pady=10, padx=10)

        self.window.mainloop()

    def erabiltzailea_guztiak_lortu(self):
        con = sqlite3.connect("datubase.db")  # konexioa ezarri
        cur = con.cursor()
        emaitza = cur.execute("SELECT erabiltzailea FROM jokalariak").fetchall()
        print(emaitza)
        con.close()
        return emaitza

    def erabiltzailea_ezabatu(self, row_numb, kontsulta):
        con = sqlite3.connect("datubase.db")  # konexioa ezarri
        cur = con.cursor()
        cur.execute("DELETE FROM jokalariak WHERE erabiltzailea=(?)", (kontsulta[row_numb][0],))
        con.commit()
        con.close()
        self.window.destroy()
        ErabiltzaileakEzabatu().__init__()

    def irten(self):
        self.window.destroy()
        Profila.Profila("admin").__init__("admin")
