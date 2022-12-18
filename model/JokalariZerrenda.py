from controller.db_conn import DbConn
from model.Jokalari import Jokalari


class JokalariZerrenda(object):
    __instance = None

    def __new__(cls):
        if JokalariZerrenda.__instance is None:
            JokalariZerrenda.__instance = object.__new__(cls)
        return JokalariZerrenda.__instance

    def get_erabiltzailearen_pasahitza(self, id):
        return DbConn().erabiltzailearen_pasahitza_lortu(id)

    def get_erabiltzaile_guztiak(self):
        return DbConn().erabiltzaile_guztiak_lortu()

    def get_erabiltzailea_idz(self, id):
        emaitza = DbConn().erabiltzailea_idz_lortu(id)
        if emaitza is not None:
            jokalari = Jokalari(emaitza[0], emaitza[1], emaitza[2],
                                emaitza[3], emaitza[4], emaitza[5],
                                emaitza[6], emaitza[7], emaitza[8], emaitza[9])
            return jokalari
        return None

    def erabiltzailea_gehitu(self, jokalari):
        DbConn().erabiltzaile_berria_erregistratu(
            jokalari.erabiltzaile_id,
            jokalari.galdera,
            jokalari.erantzuna,
            jokalari.pasahitza,
            jokalari.puntuazioa,
            jokalari.partida,
            jokalari.soinua,
            jokalari.atzeko_kolore,
            jokalari.botoi_kolore,
            jokalari.paleta
        )

    def erabiltzailea_ezabatu(self, erabiltzaile):
        DbConn().erabiltzaile_ezabatu(erabiltzaile)

    def erabiltzailearen_pasahitza_aldatu(self, id, pasahitza, galdera, erantzuna):
        DbConn().pasahitza_aldatu(id, pasahitza, galdera, erantzuna)

    def get_jokalari_gordetako_partida(self, erabiltzaile):
        return DbConn().partida_kargatuta(erabiltzaile)
