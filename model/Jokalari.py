

class Jokalari(object):

    # Init with default values
    def __init__(self, id, galdera, erantzuna, pasahitza,
                 puntuazioa=0,
                 partida="#",
                 soinua="original",
                 atzeko_kol="#7ec0ee",
                 botoi_kol="#ffffff",
                 paleta=1):
        self.erabiltzaile_id = id
        self.galdera = galdera
        self.erantzuna = erantzuna
        self.pasahitza = pasahitza
        self.puntuazioa = puntuazioa
        self.partida = partida
        self.soinua = soinua
        self.atzeko_kolore = atzeko_kol
        self.botoi_kolore = botoi_kol
        self.paleta = paleta
