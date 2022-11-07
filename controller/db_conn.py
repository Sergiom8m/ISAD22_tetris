import sqlite3


class DbConn(object):

    def __init__(self):
        super(DbConn, self).__init__()
        self.con = sqlite3.connect("datubase.db")  # konexioa ezarri
        self.cur = self.con.cursor()

    def erabiltzailearen_pasahitza_lortu(self, id_erabiltzaile):
        self.cur.execute("CREATE TABLE IF NOT EXISTS JOKALARIAK(erabiltzailea, galdera, pasahitza, puntuazioa, partida)")
        res = self.cur.execute("SELECT pasahitza FROM JOKALARIAK WHERE erabiltzailea=(?)", (id_erabiltzaile,))
        pasahitza = res.fetchone()
        if pasahitza is None:
            return pasahitza
        else:
            return pasahitza[0]

    def erabiltzailea_idz_lortu(self, id_erabiltzaile):
        self.cur.execute("CREATE TABLE IF NOT EXISTS JOKALARIAK(erabiltzailea, galdera, pasahitza, puntuazioa, partida)")
        res = self.cur.execute("SELECT erabiltzailea FROM JOKALARIAK WHERE erabiltzailea=(?)", (id_erabiltzaile,))
        return res.fetchone()

    def erabiltzaile_berria_erregistratu(self, id_erabiltzaile, galdera, pasahitza, puntuazioa, partida):
        self.cur.execute("CREATE TABLE IF NOT EXISTS JOKALARIAK(erabiltzailea, galdera, pasahitza, puntuazioa, partida)")
        self.cur.execute("INSERT INTO JOKALARIAK VALUES (?, ?, ?, ?, ?)", (id_erabiltzaile, galdera, pasahitza, puntuazioa, partida))
        self.con.commit()  # Datu basean insert-aren commit-a egiten da

    def konexioa_itxi(self):
        self.con.close()

    def partida_gorde(self, id_erabiltzaile, partida, puntuazioa):
        self.cur.execute("UPDATE JOKALARIAK SET partida=(?), puntuazioa=(?) WHERE erabiltzailea=(?)", (partida, puntuazioa, id_erabiltzaile))
        self.con.commit()

    def partida_kargatuta(self, id_erabiltzaile):
        res = self.cur.execute("SELECT partida FROM JOKALARIAK WHERE erabiltzailea=(?)", (id_erabiltzaile,))
        return res.fetchone()[0]

    def puntuazioa_lortu(self, id_erabiltzaile):
        res = self.cur.execute("SELECT puntuazioa FROM JOKALARIAK WHERE erabiltzailea=(?)", (id_erabiltzaile,))
        return res.fetchone()[0]

