from controller.db_conn import DbConn

from model.Ranking import Ranking


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

    def set_pasahitza_berria(self, new_pasahitza, new_galdera, new_erantzuna):
        self.pasahitza = new_pasahitza
        self.galdera = new_galdera
        self.erantzuna = new_erantzuna
        DbConn().erabiltzailea_eguneratu(self)  #TODO igual se puede hacer solo cuando cierre sesión y no aquí

    def set_pertsonalizazio_berria(self, soinua, atzeko_kol, botoi_kol, adreilu_kol):
        if soinua is not None:
            self.soinua = soinua
        if atzeko_kol is not None:
            self.atzeko_kolore = atzeko_kol
        if botoi_kol is not None:
            self.botoi_kolore = botoi_kol
        if adreilu_kol is not None:
            self.paleta = adreilu_kol
        DbConn().erabiltzailea_eguneratu(self)  #TODO igual se puede hacer solo cuando cierre sesión y no aquí


    def partida_gorde(self, partida, puntuazioa):
        self.partida = partida
        self.puntuazioa = puntuazioa
        DbConn().erabiltzailea_eguneratu(self)  #TODO igual se puede hacer solo cuando cierre sesión y no aquí

    def saria_du(self, tamaina, abiadura, izena):
        emaitza = DbConn().saria_du(self.erabiltzaile_id, izena, tamaina, abiadura)
        return True if emaitza is not None else False

    def nire_posizioa_rankingean(self, tamaina, abiadura):
        ranking = Ranking().get_ranking(tamaina, abiadura)
        lerroKop = len(ranking)
        for i in range(lerroKop):
            if ranking[i][0].__eq__(self.erabiltzaile_id):
                return [i + 1, ranking[i][1]]
        return None

    def erantzuna_ondo_dago(self, idatzitako_erantzuna):
        return self.erantzuna.__eq__(idatzitako_erantzuna)
