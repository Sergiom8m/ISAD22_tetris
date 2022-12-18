from controller.db_conn import DbConn


class Ranking(object):

    def get_ranking(self, tamaina, abiadura):
        return DbConn().ranking_lortu(tamaina, abiadura)  # TODO hay que mejorarlo para no pasar solo una clase
