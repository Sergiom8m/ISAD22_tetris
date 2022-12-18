from controller.db_conn import DbConn

class MailenZerrenda(object):


    def get_maila_beharrezko_puntuazioa(self, tamaina, abiadura):
        return DbConn().beharrezko_puntuazioa_lortu(tamaina, abiadura)
