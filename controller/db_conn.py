import sqlite3


class DbConn(object):

    def __init__(self):
        super(DbConn, self).__init__()
        self.con = sqlite3.connect("datubase.db")  # konexioa ezarri
        self.cur = self.con.cursor()

        #https://www.sqlitetutorial.net/sqlite-foreign-key/
        # Taulak sortu:
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS JOKALARIAK(erabiltzailea, galdera, erantzuna, pasahitza, puntuazioa, partida, soinua, atzeko, botoiKol, paleta)")
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS MAILAK(tamaina, abiadura)")
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS JOKALARIAREN_PR_MAILAKO(erabiltzailea, tamaina_maila, abiadura_maila, puntuazio_record, "
            "FOREIGN KEY(erabiltzailea) REFERENCES JOKALARIAK(erabiltzailea),"
            "FOREIGN KEY(tamaina_maila) REFERENCES MAILAK(tamaina), "
            "FOREIGN KEY(abiadura_maila) REFERENCES MAILAK(abiadura))")
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS SARIAK( tamaina_maila, abiadura_maila, izena, beharrezko_puntuazioa, "
            "FOREIGN KEY(tamaina_maila) REFERENCES MAILAK(tamaina), "
            "FOREIGN KEY(abiadura_maila) REFERENCES MAILAK(abiadura))")
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS JOKALARIAREN_SARIAK(erabiltzailea, izena, tamaina_maila, abiadura_maila, "
            "FOREIGN KEY(erabiltzailea) REFERENCES JOKALARIAK(erabiltzailea),"
            "FOREIGN KEY(izena) REFERENCES SARIAK(izena),"
            "FOREIGN KEY(tamaina_maila) REFERENCES SARIAK(tamaina_maila), "
            "FOREIGN KEY(abiadura_maila) REFERENCES SARIAK(abiadura_maila))")

        # "admin" erabiltzailea sortu eta taulan sartu:
        erabiltzaile_izena = "admin"
        query = self.cur.execute("SELECT * FROM JOKALARIAK WHERE erabiltzailea=(?)", (erabiltzaile_izena,))
        if query.fetchone() is None:
            galdera = "XXX"
            erantzuna = "XXX"
            pasahitza = "123"
            puntuazioa = "0"
            partida = "#"
            musika = "original"
            atzeko = "#7ec0ee"
            botoiKol = "#ffffff"
            paleta = 1
            self.cur.execute("INSERT INTO JOKALARIAK VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
            erabiltzaile_izena, galdera, erantzuna, pasahitza, puntuazioa, partida, musika, atzeko, botoiKol, paleta))
            self.con.commit()
        #Sariak eta mailak taulak bete:
        self.mailak_taula_bete()
        self.sariak_taula_bete()

    ############################ ERABILTZAILEAREN INFORMAZIOA ############################
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

    ############################ ERREGISTROA ############################
    def erabiltzaile_berria_erregistratu(self, id_erabiltzaile, galdera, erantzuna, pasahitza, puntuazioa, partida,
                                         musika, atzeko, botoiKol, paleta):
        self.cur.execute("INSERT INTO JOKALARIAK VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                         (id_erabiltzaile, galdera, erantzuna, pasahitza, puntuazioa, partida, musika, atzeko, botoiKol, paleta))
        self.con.commit()  # Datu basean insert-aren commit-a egiten da

    ############################ PARTIDA GORDE/KARGATU ############################
    def partida_gorde(self, id_erabiltzaile, partida, puntuazioa):
        self.cur.execute("UPDATE JOKALARIAK SET partida=(?), puntuazioa=(?) WHERE erabiltzailea=(?)",
                         (partida, puntuazioa, id_erabiltzaile))
        self.con.commit()

    def partida_kargatuta(self, id_erabiltzaile):
        res = self.cur.execute("SELECT partida FROM JOKALARIAK WHERE erabiltzailea=(?)", (id_erabiltzaile,))
        return res.fetchone()[0]

    def puntuazioa_lortu(self, id_erabiltzaile):
        res = self.cur.execute("SELECT puntuazioa FROM JOKALARIAK WHERE erabiltzailea=(?)", (id_erabiltzaile,))
        return res.fetchone()[0]

    ############################ ERABILTZAILEAK EZABATZEKO ############################
    def erabiltzaile_guztiak_lortu(self):
        return self.cur.execute("SELECT erabiltzailea FROM jokalariak").fetchall()

    def erabiltzaile_ezabatu(self, id_erabiltzaile):
        self.cur.execute("DELETE FROM jokalariak WHERE erabiltzailea=(?)", (id_erabiltzaile,))
        self.con.commit()

    ############################ PASAHITZA ALDATZEKO ############################
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

    ############################ RANKING-AK KUDEATZEKO ##############################
    def puntuazioa_eguneratu(self, id_erabiltzaile, tamaina, abiadura, puntuazioa):
        #OROKORREAN
        puntu = self.cur.execute("SELECT puntuazio_record FROM JOKALARIAREN_PR_MAILAKO WHERE erabiltzailea=(?) AND "
                               "tamaina_maila=(?) AND abiadura_maila=(?)", (id_erabiltzaile, 0, 0,)).fetchone()
        if puntu is None:
            self.cur.execute("INSERT INTO JOKALARIAREN_PR_MAILAKO VALUES (?, ?, ?, ?)", (id_erabiltzaile, 0, 0, puntuazioa))
            self.con.commit()
            self.saria_eguneratu(id_erabiltzaile, 0, 0, puntuazioa)
        else:
            puntu=puntu[0]+puntuazioa
            self.cur.execute("UPDATE JOKALARIAREN_PR_MAILAKO SET puntuazio_record=(?) WHERE erabiltzailea=(?) AND "
                               "tamaina_maila=(?) AND abiadura_maila=(?)", (puntu, id_erabiltzaile, 0, 0,))
            self.con.commit()
            self.saria_eguneratu(id_erabiltzaile, 0, 0, puntu)
        #MAILETAN
        puntu2 = self.cur.execute("SELECT puntuazio_record FROM JOKALARIAREN_PR_MAILAKO WHERE erabiltzailea=(?) AND "
                                 "tamaina_maila=(?) AND abiadura_maila=(?)", (id_erabiltzaile, tamaina, abiadura,)).fetchone()
        if puntu2 is None:
            self.cur.execute("INSERT INTO JOKALARIAREN_PR_MAILAKO VALUES (?, ?, ?, ?)",
                             (id_erabiltzaile, tamaina, abiadura, puntuazioa))
            self.con.commit()
            self.saria_eguneratu(id_erabiltzaile, tamaina, abiadura, puntuazioa)
        else:
            if puntu2[0]<puntuazioa:
                self.cur.execute("UPDATE JOKALARIAREN_PR_MAILAKO SET puntuazio_record=(?) WHERE erabiltzailea=(?) AND "
                             "tamaina_maila=(?) AND abiadura_maila=(?)", (puntuazioa, id_erabiltzaile, tamaina, abiadura,))
                self.con.commit()
                self.saria_eguneratu(id_erabiltzaile, tamaina, abiadura, puntuazioa)
    ############################ RANKING-AK LORTZEKO ##############################
    def nire_posizioa_rankingean(self, erabiltzaile, tamaina, abiadura):
        ranking = self.ranking_lortu(tamaina, abiadura)
        lerroKop = len(ranking)
        for i in range(lerroKop):
            if ranking[i][0].__eq__(erabiltzaile):
                return [i+1,ranking[i][1]]
        return None
    def ranking_lortu(self, tamaina, abiadura):
        return self.cur.execute("SELECT erabiltzailea, puntuazio_record, RANK() OVER( "
                                "ORDER BY puntuazio_record DESC) posizio "
                                "FROM JOKALARIAREN_PR_MAILAKO "
                                "WHERE tamaina_maila=(?) AND abiadura_maila=(?)", (tamaina, abiadura,)).fetchall()


    ########################### SARIAK LORTU ############################
    def saria_eguneratu(self, erabiltzaile, tamaina, abiadura, puntuazioa):
        maila_sariak = self.cur.execute("SELECT izena, beharrezko_puntuazioa FROM SARIAK WHERE tamaina_maila=(?) "
                                        "AND abiadura_maila=(?)",(tamaina, abiadura,)).fetchall()
        lerroKop=len(maila_sariak)
        for i in range(lerroKop):
            if maila_sariak[i][1]<puntuazioa:
                re = self.cur.execute("SELECT * FROM JOKALARIAREN_SARIAK WHERE erabiltzailea=(?) AND "
                                 "izena=(?) AND tamaina_maila=(?) AND abiadura_maila=(?)", (erabiltzaile,maila_sariak[i][0], tamaina,abiadura,)).fetchone()
                if re is None:
                    self.cur.execute("INSERT INTO JOKALARIAREN_SARIAK VALUES (?, ?, ?, ?)",
                                     (erabiltzaile, maila_sariak[i][0],tamaina, abiadura))
                    self.con.commit()
    def sariak_lortu(self):
        return self.cur.execute("SELECT * FROM SARIAK").fetchall()
    def saria_du(self, erabiltzaile, izena, tamaina, abiadura):
        res = self.cur.execute("SELECT * FROM JOKALARIAREN_SARIAK WHERE erabiltzailea=(?) AND izena=(?)"
                               "AND tamaina_maila=(?) AND abiadura_maila=(?)", (erabiltzaile, izena, tamaina, abiadura,))
        if (res.fetchone() is not None):
            return True
        return False
    def puntuazio_record_lortu(self, erabiltzaile, tamaina, abiadura):
        res = self.cur.execute("SELECT puntuazio_record FROM JOKALARIAREN_PR_MAILAKO WHERE erabiltzailea=(?)"
                               "AND tamaina_maila=(?) AND abiadura_maila=(?)", (erabiltzaile, tamaina, abiadura,))
        emaitza = res.fetchone()
        if emaitza is None:
            return "XXXXX"
        return emaitza[0] #TODO IGUAL DA ERROR

    ############################ PERTSONALIZATU ############################
    def pertsonalizazioa_aldatu(self, atzeko, adreilu, botoi, musika, erabiltzaile):
        # EZ BADA EZER ALDATU NAHI PARAMETROREN BATEAN EZ DIRA UPDATE-AK EGIN BEHAR -> if X is not None
        if musika is not None:
            self.cur.execute("UPDATE JOKALARIAK SET soinua=(?) WHERE erabiltzailea=(?)", (musika, erabiltzaile,))

        if atzeko is not None:
            self.cur.execute("UPDATE JOKALARIAK SET atzeko=(?) WHERE erabiltzailea=(?)", (atzeko, erabiltzaile,))

        if botoi is not None:
            self.cur.execute("UPDATE JOKALARIAK SET botoiKol=(?) WHERE erabiltzailea=(?)", (botoi, erabiltzaile,))

        if adreilu is not None:
            self.cur.execute("UPDATE JOKALARIAK SET paleta=(?) WHERE erabiltzailea=(?)", (adreilu, erabiltzaile,))

        self.con.commit()

    def get_jokalari_musika(self, erabiltzaile):
        if erabiltzaile is not None:
            emaitza = self.cur.execute("SELECT soinua FROM JOKALARIAK WHERE erabiltzailea=(?)", (erabiltzaile,))
            return emaitza.fetchone()[0]
        return "ez"

    def get_jokalari_fondoa(self, erabiltzaile):
        if erabiltzaile is not None:
            fondo = self.cur.execute("SELECT atzeko FROM JOKALARIAK WHERE erabiltzailea=(?)", (erabiltzaile,))
            #botKol = self.cur.execute("SELECT botoiKol FROM JOKALARIAK WHERE erabiltzailea=(?)", (erabiltzaile,))
            return fondo.fetchone()[0]
        return "#7ec0ee"

    def get_jokalari_botoi_kolor(self, erabiltzaile):
        if erabiltzaile is not None:
            botoi_kolor = self.cur.execute("SELECT botoiKol FROM JOKALARIAK WHERE erabiltzailea=(?)", (erabiltzaile,))
            return botoi_kolor.fetchone()[0]
        return "#ffffff"

    def paleta_lortu(self, erabiltzaile):
        if erabiltzaile is not None:
            emaitza = self.cur.execute("SELECT paleta FROM JOKALARIAK WHERE erabiltzailea=(?)", (erabiltzaile,))
            return emaitza.fetchone()[0]
        return 1

    ############################# TAULAK BETE ############################
    def mailak_taula_bete(self):
        query = self.cur.execute("SELECT * FROM MAILAK")
        if query.fetchone() is None:
            #Maila orokorra 0 bidez adieraziko dugu:
            self.cur.execute("INSERT INTO MAILAK VALUES (?, ?)", (0, 0))
            self.con.commit()
            #Beste maila guztiak
            tamaina= [10,20,30,40]
            abiadura=[800,400,200,100]
            for i in range(len(tamaina)):
                for j in range(len(abiadura)):
                    self.cur.execute("INSERT INTO MAILAK VALUES (?, ?)", (
                        tamaina[i], abiadura[j]))
                    self.con.commit()

    def sariak_taula_bete(self):
        query = self.cur.execute("SELECT * FROM SARIAK")
        if query.fetchone() is None:
            sariak = ["Basic", "Pro", "Super Pro"]
            puntuazio_min=[1000, 10000, 100000]
            # Maila orokorra 0 bidez adieraziko dugu:
            for i in range(len(sariak)):
                self.cur.execute("INSERT INTO SARIAK VALUES (?, ?, ?, ?)",
                                 (0, 0, sariak[i], puntuazio_min[i]))
                self.con.commit()
            # Beste maila guztiak
            tamaina = [10, 20, 30, 40]
            abiadura = [800, 400, 200, 100]
            for i in range(len(tamaina)):
                for j in range(len(abiadura)):
                    for x in range(len(sariak)):
                        self.cur.execute("INSERT INTO SARIAK VALUES (?, ?, ?, ?)", (
                            tamaina[i], abiadura[j], sariak[x], puntuazio_min[x]))
                        print(str(tamaina[i]) +', ' + str(abiadura[j]) +', ' + sariak[x] +', ' + str(puntuazio_min[x]))
                        self.con.commit()

    ############################ ITXI ############################
    def konexioa_itxi(self):
        self.con.close()
