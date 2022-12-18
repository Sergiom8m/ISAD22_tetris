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
            "CREATE TABLE IF NOT EXISTS MAILAK(tamaina, abiadura, beharrezko_puntuazioa)")
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS JOKALARIAREN_PR_MAILAKO(erabiltzailea, tamaina_maila, abiadura_maila, puntuazio_record, lortutako_kopurua, "
            "FOREIGN KEY(erabiltzailea) REFERENCES JOKALARIAK(erabiltzailea),"
            "FOREIGN KEY(tamaina_maila) REFERENCES MAILAK(tamaina), "
            "FOREIGN KEY(abiadura_maila) REFERENCES MAILAK(abiadura))")
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS SARIAK( tamaina_maila, abiadura_maila, izena, beharrezko_kopurua, "
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
        res = self.cur.execute("SELECT * FROM JOKALARIAK WHERE erabiltzailea=(?)", (id_erabiltzaile,))
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

    ############################ ERABILTZAILEAK EZABATZEKO ############################
    def erabiltzaile_guztiak_lortu(self):
        return self.cur.execute("SELECT erabiltzailea FROM jokalariak").fetchall()

    def erabiltzaile_ezabatu(self, id_erabiltzaile):
        self.cur.execute("DELETE FROM jokalariak WHERE erabiltzailea=(?)", (id_erabiltzaile,))
        self.con.commit()

    ############################ RANKING-AK KUDEATZEKO ##############################
    def puntuazioa_eguneratu(self, id_erabiltzaile, tamaina, abiadura, puntuazioa):
        if tamaina != 0:
            beharrezko_puntuazioa = self.beharrezko_puntuazioa_lortu(tamaina, abiadura)[0]
            baduPuntuazioa = False
            if beharrezko_puntuazioa <= puntuazioa:
                baduPuntuazioa = True
        #OROKORREAN
        puntu = self.cur.execute("SELECT puntuazio_record FROM JOKALARIAREN_PR_MAILAKO WHERE erabiltzailea=(?) AND "
                               "tamaina_maila=(?) AND abiadura_maila=(?)", (id_erabiltzaile, 0, 0,)).fetchone()
        if puntu is None:
            self.cur.execute("INSERT INTO JOKALARIAREN_PR_MAILAKO VALUES (?, ?, ?, ?, ?)", (id_erabiltzaile, 0, 0, puntuazioa, 0))
            self.con.commit()
        else:
            puntu=puntu[0]+puntuazioa
            self.cur.execute("UPDATE JOKALARIAREN_PR_MAILAKO SET puntuazio_record=(?) WHERE erabiltzailea=(?) AND "
                               "tamaina_maila=(?) AND abiadura_maila=(?)", (puntu, id_erabiltzaile, 0, 0,))
            self.con.commit()
        #MAILETAN
        puntu2 = self.cur.execute("SELECT puntuazio_record, lortutako_kopurua FROM JOKALARIAREN_PR_MAILAKO WHERE erabiltzailea=(?) AND "
                               "tamaina_maila=(?) AND abiadura_maila=(?)", (id_erabiltzaile, tamaina, abiadura,)).fetchone()
        if puntu2 is None:
            if baduPuntuazioa:
                self.cur.execute("INSERT INTO JOKALARIAREN_PR_MAILAKO VALUES (?, ?, ?, ?, ?)",
                             (id_erabiltzaile, tamaina, abiadura, puntuazioa, 1))
            else:
                self.cur.execute("INSERT INTO JOKALARIAREN_PR_MAILAKO VALUES (?, ?, ?, ?, ?)",
                                 (id_erabiltzaile, tamaina, abiadura, puntuazioa, 0))
            self.con.commit()
        else:
            if puntu2[0]<puntuazioa:
                self.cur.execute("UPDATE JOKALARIAREN_PR_MAILAKO SET puntuazio_record=(?) WHERE erabiltzailea=(?) AND "
                             "tamaina_maila=(?) AND abiadura_maila=(?)", (puntuazioa, id_erabiltzaile, tamaina, abiadura,))
                self.con.commit()
            if baduPuntuazioa:
                k= puntu2[1]+1
                self.cur.execute("UPDATE JOKALARIAREN_PR_MAILAKO SET lortutako_kopurua=(?) WHERE erabiltzailea=(?) AND "
                                 "tamaina_maila=(?) AND abiadura_maila=(?)",
                                 (k, id_erabiltzaile, tamaina, abiadura,))
                self.con.commit()
                self.saria_eguneratu(id_erabiltzaile, tamaina, abiadura, k)

    ############################ RANKING-AK LORTZEKO ##############################

    def ranking_lortu(self, tamaina, abiadura):
        return self.cur.execute("SELECT erabiltzailea, puntuazio_record, RANK() OVER( "
                                "ORDER BY puntuazio_record DESC) posizio "
                                "FROM JOKALARIAREN_PR_MAILAKO "
                                "WHERE tamaina_maila=(?) AND abiadura_maila=(?)", (tamaina, abiadura,)).fetchall()


    ########################### SARIAK LORTU ############################
    def saria_eguneratu(self, erabiltzaile, tamaina, abiadura, kopurua):
        #self.cur.execute()
        maila_sariak = self.cur.execute("SELECT izena, beharrezko_kopurua FROM SARIAK WHERE tamaina_maila=(?) "
                                        "AND abiadura_maila=(?)",(tamaina, abiadura,)).fetchall()
        lerroKop=len(maila_sariak)
        for i in range(lerroKop):
            if maila_sariak[i][1]<=kopurua:
                re = self.cur.execute("SELECT * FROM JOKALARIAREN_SARIAK WHERE erabiltzailea=(?) AND "
                                 "izena=(?) AND tamaina_maila=(?) AND abiadura_maila=(?)", (erabiltzaile,maila_sariak[i][0], tamaina,abiadura,)).fetchone()
                if re is None:
                    self.cur.execute("INSERT INTO JOKALARIAREN_SARIAK VALUES (?, ?, ?, ?)",
                                     (erabiltzaile, maila_sariak[i][0],tamaina, abiadura))
                    self.con.commit()

    def sariak_lortu(self):
        return self.cur.execute("SELECT * FROM SARIAK").fetchall()

    def beharrezko_puntuazioa_lortu(self, tamaina, abiadura):
        return self.cur.execute("SELECT beharrezko_puntuazioa FROM MAILAK WHERE tamaina=(?) AND abiadura=(?)", (tamaina, abiadura, )).fetchone()

    def saria_du(self, erabiltzaile, izena, tamaina, abiadura):
        res = self.cur.execute("SELECT * FROM JOKALARIAREN_SARIAK WHERE erabiltzailea=(?) AND izena=(?)"
                               "AND tamaina_maila=(?) AND abiadura_maila=(?)", (erabiltzaile, izena, tamaina, abiadura,))
        return res.fetchone()

    def puntuazio_record_lortu(self, erabiltzaile, tamaina, abiadura):
        res = self.cur.execute("SELECT puntuazio_record FROM JOKALARIAREN_PR_MAILAKO WHERE erabiltzailea=(?)"
                               "AND tamaina_maila=(?) AND abiadura_maila=(?)", (erabiltzaile, tamaina, abiadura,))
        emaitza = res.fetchone()
        if emaitza is None:
            return "XXXXX"
        return emaitza[0] #TODO IGUAL DA ERROR

    ############################ PERTSONALIZATU ############################
    def get_jokalari_musika(self, erabiltzaile):
        if erabiltzaile is not None:
            emaitza = self.cur.execute("SELECT soinua FROM JOKALARIAK WHERE erabiltzailea=(?)", (erabiltzaile,))
            return emaitza.fetchone()[0]
        return "ez"

    ############################# TAULAK BETE ############################
    def mailak_taula_bete(self):
        query = self.cur.execute("SELECT * FROM MAILAK")
        if query.fetchone() is None:
            #Beste maila guztiak
            tamaina= [10,20,30,40]
            abiadura=[800,400,200,100]
            beharrezkoPuntuazio=[100, 50, 30, 10]
            for i in range(len(tamaina)):
                for j in range(len(abiadura)):
                    self.cur.execute("INSERT INTO MAILAK VALUES (?, ?, ?)", (
                        tamaina[i], abiadura[j], beharrezkoPuntuazio[j]))
                    self.con.commit()

    def sariak_taula_bete(self):
        query = self.cur.execute("SELECT * FROM SARIAK")
        if query.fetchone() is None:
            sariak = ["Basic", "Pro", "Super Pro"]
            puntuazio_min=[2, 4, 6]
            tamaina = [10, 20, 30, 40]
            abiadura = [800, 400, 200, 100]

            for i in range(len(tamaina)):
                for j in range(len(abiadura)):
                    for x in range(len(sariak)):
                        self.cur.execute("INSERT INTO SARIAK VALUES (?, ?, ?, ?)", (
                            tamaina[i], abiadura[j], sariak[x], puntuazio_min[x]))
                        self.con.commit()

    ############################## ERABILTZAILE EGUNERATZEKO #########################
    def erabiltzailea_eguneratu(self, erabiltzailea):
        self.cur.execute("UPDATE JOKALARIAK "
                         "SET galdera=(?), erantzuna=(?), pasahitza=(?), "
                         "puntuazioa=(?), partida=(?),soinua=(?), "
                         "atzeko=(?), botoiKol=(?), paleta=(?)"
                         "WHERE erabiltzailea=(?)",
                         (
                             erabiltzailea.galdera, erabiltzailea.erantzuna, erabiltzailea.pasahitza,
                             erabiltzailea.puntuazioa, erabiltzailea.partida, erabiltzailea.soinua,
                             erabiltzailea.atzeko_kolore, erabiltzailea.botoi_kolore, erabiltzailea.paleta,
                             erabiltzailea.erabiltzaile_id
                         ))
        self.con.commit()

    ############################ ITXI ############################
    def konexioa_itxi(self):
        self.con.close()
