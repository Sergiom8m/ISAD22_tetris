from controller.db_conn import DbConn

class SarienZerrenda(object):
    __instance = None

    def __new__(cls):
        if SarienZerrenda.__instance is None:
            SarienZerrenda.__instance = object.__new__(cls)
        return SarienZerrenda.__instance

    def get_sari_guztiak(self):
        DbConn().sariak_lortu()
