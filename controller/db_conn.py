import sqlite3


class DbConn(object):

    def __init__(self):
        super(DbConn, self).__init__()
        self.con = sqlite3.connect("datubase.db")  # konexioa ezarri
        self.cur = self.con.cursor()

        # "JOKALARIAK" Taula sortu:
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS JOKALARIAK(erabiltzailea, galdera, erantzuna, pasahitza, puntuazioa, partida, soinua)")
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS PALETAK(zenbakia, lauki, zutabe, lforma, lformaalderantzizko, zforma, zformaalderantzizko, tforma)")

        # "admin" erabiltzailea sortu eta taulan sartu:
        erabiltzaile_izena = "admin"
        query = self.cur.execute("SELECT * FROM JOKALARIAK WHERE erabiltzailea=(?)", (erabiltzaile_izena,))
        if query.fetchone() is None:
            galdera = "XXX"
            erantzuna= "XXX"
            pasahitza = "123"
            puntuazioa = "0"
            partida = "#"
            musika = "original"
            self.cur.execute("INSERT INTO JOKALARIAK VALUES (?, ?, ?, ?, ?, ?, ?)", (erabiltzaile_izena, galdera, erantzuna, pasahitza, puntuazioa, partida, musika))
            self.con.commit()

        query1 = self.cur.execute("SELECT * FROM PALETAK")
        if query1.fetchone() is None:
            self.paletak_sortu()


    def erabiltzailearen_pasahitza_lortu(self, id_erabiltzaile):
        res = self.cur.execute("SELECT pasahitza FROM JOKALARIAK WHERE erabiltzailea=(?)", (id_erabiltzaile,))
        pasahitza = res.fetchone()
        if pasahitza is None:
            return pasahitza
        else:
            return pasahitza[0]

    def erabiltzailea_idz_lortu(self, id_erabiltzaile):
        res = self.cur.execute("SELECT erabiltzailea FROM JOKALARIAK WHERE erabiltzailea=(?)", (id_erabiltzaile,))
        return res.fetchone()

    def erabiltzaile_berria_erregistratu(self, id_erabiltzaile, galdera, erantzuna, pasahitza, puntuazioa, partida, musika):
        self.cur.execute("INSERT INTO JOKALARIAK VALUES (?, ?, ?, ?, ?, ?, ?)", (id_erabiltzaile, galdera, erantzuna, pasahitza, puntuazioa, partida, musika))
        self.con.commit()  # Datu basean insert-aren commit-a egiten da

    def partida_gorde(self, id_erabiltzaile, partida, puntuazioa):
        self.cur.execute("UPDATE JOKALARIAK SET partida=(?), puntuazioa=(?) WHERE erabiltzailea=(?)", (partida, puntuazioa, id_erabiltzaile))
        self.con.commit()

    def partida_kargatuta(self, id_erabiltzaile):
        res = self.cur.execute("SELECT partida FROM JOKALARIAK WHERE erabiltzailea=(?)", (id_erabiltzaile,))
        return res.fetchone()[0]

    def puntuazioa_lortu(self, id_erabiltzaile):
        res = self.cur.execute("SELECT puntuazioa FROM JOKALARIAK WHERE erabiltzailea=(?)", (id_erabiltzaile,))
        return res.fetchone()[0]

    def erabiltzaile_guztiak_lortu(self):
        return self.cur.execute("SELECT erabiltzailea FROM jokalariak").fetchall()

    def erabiltzaile_ezabatu(self, id_erabiltzaile):
        self.cur.execute("DELETE FROM jokalariak WHERE erabiltzailea=(?)", (id_erabiltzaile,))
        self.con.commit()

    def pasahitza_aldatu(self, id_erabiltzaile, pasahitza, galdera, erantzuna):
        self.cur.execute("UPDATE JOKALARIAK SET pasahitza=(?) WHERE erabiltzailea=(?)", (pasahitza, id_erabiltzaile,))
        self.cur.execute("UPDATE JOKALARIAK SET galdera=(?) WHERE erabiltzailea=(?)", (galdera, id_erabiltzaile,))
        self.cur.execute("UPDATE JOKALARIAK SET erantzuna=(?) WHERE erabiltzailea=(?)", (erantzuna, id_erabiltzaile,))
        self.con.commit()

    def galdera_lortu(self, id_erabiltzaile):
        res = self.cur.execute("SELECT galdera FROM JOKALARIAK WHERE erabiltzailea=(?)", (id_erabiltzaile,))
        return res.fetchone()[0]

    def erantzuna_ondo_dago(self, id_erabiltzaile, erantzuna):
        res = self.cur.execute("SELECT erantzuna FROM JOKALARIAK WHERE erabiltzailea=(?)", (id_erabiltzaile,))
        erantzun_zuzen = res.fetchone()[0]
        if (erantzun_zuzen.__eq__(erantzuna)):
            return True
        return False

    def pertsonalizazioa_aldatu(self, atzeko, botoi, adreilu, musika, erabiltzaile):
        self.cur.execute("UPDATE JOKALARIAK SET soinua=(?) WHERE erabiltzailea=(?)", (musika, erabiltzaile,))
        self.con.commit()

    def get_jokalari_musika(self, erabiltzaile):
        emaitza = self.cur.execute("SELECT soinua FROM JOKALARIAK WHERE erabiltzailea=(?)", (erabiltzaile,))
        return emaitza.fetchone()[0]

    def paletak_sortu(self):
        lauki = 'yellow'
        zutabe = 'cyan'
        lforma = 'blue'
        lformaalderantzizko = 'orange'
        zforma = 'green'
        zformaalderantzizko = 'red'
        tforma = 'purple'
        self.cur.execute("INSERT INTO PALETAK VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                         (1, lauki, zutabe, lforma, lformaalderantzizko, zforma, zformaalderantzizko, tforma))
        self.con.commit()
        lauki = 'snow'
        zutabe = 'SkyBlue2'
        lforma = 'LightBlue1'
        lformaalderantzizko = 'cyan'
        zforma = 'blue4'
        zformaalderantzizko = 'sky blue'
        tforma = 'SkyBlue4'
        self.cur.execute("INSERT INTO PALETAK VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                         (2, lauki, zutabe, lforma, lformaalderantzizko, zforma, zformaalderantzizko, tforma))
        self.con.commit()
        self.cur.execute("INSERT INTO PALETAK VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                         (3, lauki, zutabe, lforma, lformaalderantzizko, zforma, zformaalderantzizko, tforma))
        self.con.commit()
        self.cur.execute("INSERT INTO PALETAK VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                         (4, lauki, zutabe, lforma, lformaalderantzizko, zforma, zformaalderantzizko, tforma))
        self.con.commit()

    def konexioa_itxi(self):
        self.con.close()
