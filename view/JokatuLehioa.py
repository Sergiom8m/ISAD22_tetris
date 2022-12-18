import random
import tkinter as tk

import view
from model.Tableroa import Tableroa
from model.Piezak import *
import sys
import model.Piezak as piezak
from tkinter import *
from controller.Soinuak import Soinuak
from model.JokalariZerrenda import JokalariZerrenda

abiadura = 1
tamaina2 = 2
tamaina2 = 2
erabiltzailea= None
botoi_kolor = "#ffffff"
atzeko_kolor = "#7ec0ee"


class JokatuLehioa(object):
    """docstring for JokatuLeioa"""

    def __init__(self, abiadura_param, tamaina_param, erab, puntuazioa_param, partida):
        super(JokatuLehioa, self).__init__()

        self.abiadura = abiadura_param
        self.tamaina = tamaina_param

        self.erabiltzaile = erab
        global erabiltzailea
        erabiltzailea = self.erabiltzaile
        piezak.erabiltzailea = erabiltzailea

        if self.erabiltzaile is not None:
            Soinuak.play_music(Soinuak(), self.erabiltzaile.soinua)
        self.window = tk.Tk()

        self.window.protocol("WM_DELETE_WINDOW", sys.exit)
        leihoTamaina = (str(self.tamaina * 27) + "x" + "700")
        self.window.geometry(leihoTamaina)
        self.window.title("Tetris Jokoa")

        global atzeko_kolor
        atzeko_kolor = self.erabiltzaile.atzeko_kolore if not None else "#7ec0ee"
        global botoi_kolor
        botoi_kolor = self.erabiltzaile.botoi_kolore if not None else "#ffffff"
        self.window['bg'] = atzeko_kolor

        global abiadura
        global tamaina2
        abiadura = self.abiadura
        tamaina2 = self.tamaina

        button = tk.Button(self.window, cursor="hand2", text="Partida hasi", bg=botoi_kolor)
        button.pack()

        puntuazioa = tk.StringVar()
        puntuazioa.set(f"Puntuazioa: {puntuazioa_param}")

        puntuazioalabel = tk.Label(self.window, textvariable=puntuazioa, bg=botoi_kolor)
        puntuazioalabel.pack()

        self.canvas = TableroaPanela(master=self.window, erab=self.erabiltzaile, tamaina=(tamaina2, 30), puntuazioalabel=puntuazioa,
                                     partida=partida)
        button.configure(command=self.canvas.jolastu)
        self.canvas.pack()
        if self.erabiltzaile is not None:
            Button(self.window, text="Partida Gorde", bg=botoi_kolor, command=self.partidaGorde).pack()
        Button(self.window, text="Irten", bg=botoi_kolor, command=self.irten).pack()
        self.window.bind("<Up>", self.canvas.joku_kontrola)
        self.window.bind("<Down>", self.canvas.joku_kontrola)
        self.window.bind("<Right>", self.canvas.joku_kontrola)
        self.window.bind("<Left>", self.canvas.joku_kontrola)

        self.window.mainloop()

    # Irtetzeko metodoa:
    def irten(self):
        Soinuak.quit_music(Soinuak())
        self.window.destroy()
        if self.erabiltzaile is None:
            view.HasierakoMenua.HasierakoMenua().__init__()
        else:
            view.Profila.Profila(self.erabiltzaile).__init__()

    def partidaGorde(self):
        self.canvas.after_cancel(self.canvas.jokatzen)
        matrizea = self.canvas.tab
        gorde = str(matrizea.puntuazioa) + "#" + str(tamaina2) + "#" + str(self.abiadura) + "#"
        for i in range(matrizea.tamaina[1]):
            for j in range(matrizea.tamaina[0]):

                if matrizea.tab[i][j] is None:
                    gorde = gorde + "None#"
                else:
                    gorde = gorde + matrizea.tab[i][j] + "#"
        self.erabiltzaile.partida_gorde(gorde, self.canvas.tab.puntuazioa) # TODO la puntacion ya se guarda en "gorde"
        self.irten()


class TableroaPanela(tk.Frame):
    def __init__(self, erab, tamaina, gelazka_tamaina=20, puntuazioalabel=None, master=None, partida=None):
        tk.Frame.__init__(self, master)
        self.puntuazio_panela = puntuazioalabel
        self.tamaina = tamaina
        self.partida = partida
        self.erabiltzaile = erab
        self.gelazka_tamaina = gelazka_tamaina
        global abiadura

        # Irudia gehitu
        # bg = PhotoImage(file="Irudiak/fondo.png")

        # Canvas sortu eta bere ezaugarriak gehitu
        self.canvas = tk.Canvas(
            width=self.tamaina[0] * self.gelazka_tamaina + 1,
            height=self.tamaina[1] * self.gelazka_tamaina + 1,
            bg='#eee', borderwidth=0, highlightthickness=0
        )
        self.canvas.pack(expand=tk.YES, fill=None)

        self.tab = Tableroa(tamaina)
        self.jokatzen = None
        self.tableroa_ezabatu()

    def marratu_gelazka(self, x, y, color):
        self.canvas.create_rectangle(x * self.gelazka_tamaina, y * self.gelazka_tamaina,
                                     (x + 1) * self.gelazka_tamaina, (y + 1) * self.gelazka_tamaina, fill=color)

    def tableroa_ezabatu(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, self.tamaina[0] * self.gelazka_tamaina,
                                     self.tamaina[1] * self.gelazka_tamaina, fill='#eee')

    def marraztu_tableroa(self):
        self.tableroa_ezabatu()
        for i in range(self.tab.tamaina[1]):
            for j in range(self.tab.tamaina[0]):
                if self.tab.tab[i][j]:
                    self.marratu_gelazka(j, i, self.tab.tab[i][j])
        if self.tab.pieza:
            for i in range(4):
                x = self.tab.posizioa[0] + self.tab.pieza.get_x(i)
                y = self.tab.posizioa[1] + self.tab.pieza.get_y(i)
                self.marratu_gelazka(y, x, self.tab.pieza.get_kolorea())
        self.puntuazioa_eguneratu()

    def pausu_bat(self):
        try:
            self.tab.betetako_lerroak_ezabatu()
            self.tab.mugitu_behera()
        except Exception as error:
            try:
                self.tab.pieza_finkotu(self.tab.posizioa)
                pieza_posibleak = [Laukia, Zutabea, Lforma, LformaAlderantzizko, Zforma, ZformaAlderantzizko, Tforma]
                self.tab.sartu_pieza(random.choice(pieza_posibleak)())
            except Exception as e:
                print("GAMEOVER")
                if self.erabiltzaile is not None:
                    self.tab.puntuazioa_eguneratu_DBan(self.erabiltzaile, abiadura)
                self.tab.hasieratu_tableroa()
                return

        self.jokatzen = self.after(abiadura, self.pausu_bat)
        self.marraztu_tableroa()

    def puntuazioa_eguneratu(self):
        if self.puntuazio_panela:
            self.puntuazio_panela.set(f"Puntuazioa: {self.tab.puntuazioa}")

    def joku_kontrola(self, event):
        try:
            if event.keysym == 'Up':
                self.tab.biratu_pieza()
            if event.keysym == 'Down':
                self.tab.pieza_kokatu_behean()
            if event.keysym == 'Right':
                self.tab.mugitu_eskumara()
            if event.keysym == 'Left':
                self.tab.mugitu_ezkerrera()
        except Exception as error:
            pass
        finally:
            self.marraztu_tableroa()

    def jolastu(self):
        if self.jokatzen:
            self.after_cancel(self.jokatzen)
        if self.partida is None:
            self.tab.hasieratu_tableroa()
        else:
            self.tab.kargatu_partida(self.partida)
        pieza_posibleak = [Laukia, Zutabea, Lforma, LformaAlderantzizko, Zforma, ZformaAlderantzizko, Tforma]
        self.tab.sartu_pieza(random.choice(pieza_posibleak)())
        self.marraztu_tableroa()
        self.jokatzen = self.after(abiadura, self.pausu_bat)
