import tkinter as tk
import sys
import view
from model.JokalariZerrenda import JokalariZerrenda
from controller.db_conn import DbConn

botoi_kolor = "#ffffff"
atzeko_kolor = "#7ec0ee"

class GalderaErantzun(object):


    def __init__(self, id):
        super(GalderaErantzun, self).__init__()

        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)  # "X" botoia erabiltzean programa gelditzea ahalbidetzen du
        self.window.title("Galdera Erantzun")
        self.window.geometry('400x400')
        self.window['bg']= atzeko_kolor
        self.window.resizable(False, False)
        izenburu1 = tk.Label(self.window, bg=atzeko_kolor, text='GALDERA', font=("Times New Roman", 25))
        izenburu1.pack()
        izenburu2 = tk.Label(self.window, bg=atzeko_kolor, text='ERANTZUN', font=("Times New Roman", 25))
        izenburu2.pack()
        self.id = id

        g = JokalariZerrenda().get_erabiltzailea_idz(id).galdera

        mezu = tk.Label(self.window, bg=atzeko_kolor, text='Erantzun ezazu galdera... ',
                        font=("Times New Roman", 16))
        mezu.place(x=60, y=100)
        mezu2 = tk.Label(self.window, bg=atzeko_kolor, text=f'{g}',
                         font=("Times New Roman", 16))
        mezu2.place(x=60, y=170)

        self.erantzuna = tk.Entry(self.window, bg=botoi_kolor, justify=tk.LEFT, width=26,
                             font=("Times New Roman", 16))
        self.erantzuna.place(x=60, y=200)


        buttonirten = tk.Button(self.window, cursor="hand2", bg=botoi_kolor, text="Irten", width=8, font=("Calibri"), command=self.irten)
        buttonirten.place(x=70, y=350)
        self.berresk = tk.Button(self.window, cursor="hand2", bg=botoi_kolor, text="Berreskuratu", width=8,
                                 font=("Calibri"),
                                 command=self.konprobatu)
        self.berresk.place(x=220, y=350)


        self.window.mainloop()

    #DATU BASEAREKIN KONEKTATZEKO METODOA:


    #BESTE PANTAILETARA JOTZEKO METODAK:
    def irten(self):
        self.window.destroy()
        view.Identifikazioa.Identifikazioa().__init__()

    def konprobatu(self):

        ondo = DbConn.erantzuna_ondo_dago(DbConn(), self.id, self.erantzuna.get())
        if(ondo):
            self.window.destroy()
            view.PasahitzaAldatu.PasahitzaAldatu(self.id).__init__()
        else:
            mezu = tk.Label(self.window, bg=atzeko_kolor, fg="red", text='Erantzuna ez da egokia', font=("Calibri"))
            mezu.place(x=60, y=250)
