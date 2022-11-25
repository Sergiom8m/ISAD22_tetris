#   ERREGISTROAREN INTERFAZEA   #

import tkinter as tk
import sys

import view
from view.Profila import Profila
from controller.db_conn import DbConn

# Koloreak
botoi_kolor = "#ffffff"
atzeko_kolor = "#7ec0ee"



class Erregistroa(object):

    def __init__(self):
        super(Erregistroa, self).__init__()
        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)  # "X" botoia erabiltzean programa gelditzea ahalbidetzen du
        self.window.geometry('420x420')
        self.window.title("Erregistroa")
        self.window['bg']=atzeko_kolor
        self.window.resizable(False, False)



        # IZENBURUA
        izena = tk.Label(self.window, bg=atzeko_kolor, text="ERREGISTROA", font=("Times New Roman", 25))
        izena.pack()



        # AZPIZENBURUA
        testua = tk.Label(self.window, bg=atzeko_kolor,text="Mesedez, zeure burua erregistratu", font = ("Times New Roman", 10))
        testua.pack()


        #EGUNERAPENAK
        identifik = tk.StringVar()
        g= tk.StringVar()
        eran = tk.StringVar()
        pasahitza1 = tk.StringVar()
        pasahitza2 = tk.StringVar()

        # Identifikatzailearen sarrera
        erab = tk.Label(self.window, bg=atzeko_kolor,text='Identifikatzailea... ', font=("Times New Roman", 12))
        erab.place(x=60, y=70)

        self.erabil = tk.Entry(self.window, textvar=identifik, width=32, bg=botoi_kolor, font=("Times New Roman", 14))
        self.erabil.place(x=60, y=90)

        # Galderaren sarrera
        b=tk.Label(self.window,bg=atzeko_kolor, text='Berreskurapen galdera sartu (pasahitzarako)', font=("Times New Roman", 12))
        b.place(x=60, y=130)


        self.galdera = tk.Entry(self.window, textvar=g, width=32, bg=botoi_kolor, font=("Times New Roman", 14))
        self.galdera.place(x=60, y=150)

        #Erantzunaren sarrera
        mezu = tk.Label(self.window, bg=atzeko_kolor, text='Berreskurapen galderari erantzuna eman: ',
                     font=("Times New Roman", 12))
        mezu.place(x=60, y=190)

        self.erantzuna = tk.Entry(self.window, textvar=eran, width=32, bg=botoi_kolor, font=("Times New Roman", 14))
        self.erantzuna.place(x=60, y=210)

        # Pasahitzaren sarrera
        pas1 = tk.Label(self.window,bg=atzeko_kolor, text='Pasahitza... ', font=("Times New Roman", 12))
        pas1.place(x=60, y=250)

        self.pasahitz1 = tk.Entry(self.window, textvar=pasahitza1, width=32, bg=botoi_kolor, font=("Times New Roman", 14))
        self.pasahitz1.place(x=60, y=270)

        pas2 = tk.Label(self.window,bg=atzeko_kolor, text='Pasahitza errepikatu... ', font=("Times New Roman", 12))
        pas2.place(x=60, y=310)

        self.pasahitz2 = tk.Entry(self.window, textvar=pasahitza2, width=32, bg=botoi_kolor, font=("Times New Roman", 14))
        self.pasahitz2.place(x=60, y=330)


        # BOTOIAK
        sartu = tk.Button(self.window, text="Sartu", cursor="hand2", bg=botoi_kolor, width=8, font=("Times New Roman", 14),
                          command=self.erabiltzaileaGorde)
        sartu.place(x=240, y=370)

        irten = tk.Button(self.window, text="Irten", cursor="hand2", bg=botoi_kolor, width=8, font=("Times New Roman", 14), command=self.irten)
        irten.place(x=60, y=370)

        self.window.mainloop()

    #PANTAILA ALDATZEKO
    def irten(self):
        self.window.destroy()
        view.HasierakoMenua.HasierakoMenua().__init__()

    def erabiltzaileaGorde(self):
        id = self.erabil.get()
        galdera = self.galdera.get()
        erantzuna = self.erantzuna.get()
        p1 = self.pasahitz1.get()
        p2 = self.pasahitz2.get()

        if (len(id) != 0) & (len(galdera) != 0) & (len(p1) != 0) & (len(p2) != 0):
            erabiltzailea = DbConn.erabiltzailea_idz_lortu(DbConn(), id)
            if erabiltzailea is None:
                if p1 == p2:
                    DbConn.erabiltzaile_berria_erregistratu(DbConn(), id, galdera, erantzuna, p1, 0, "#", "original", 1)
                    # PROFIL PANTAILARA ALDATZEKO:
                    self.window.destroy()
                    Profila(id).__init__()
                else:
                    error = tk.Label(self.window, bg=atzeko_kolor,  fg="red", text='Pasahitza ez du koinziditzen               ',
                                     font=("Times New Roman", 12))
                    error.place(x=60, y=310)
            else:
                error = tk.Label(self.window,bg=atzeko_kolor,fg="red",  text='Erabiltzailea jada existitzen da                  ',
                                 font=("Times New Roman", 12))
                error.place(x=60, y=310)
        else:
            error = tk.Label(self.window, bg=atzeko_kolor, fg="red", text='Sar itzazu datu guztiak                                   ',
                             font=("Times New Roman", 12))
            error.place(x=60, y=310)
