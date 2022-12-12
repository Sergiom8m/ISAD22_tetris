from view.HasierakoMenua import HasierakoMenua
from controller.db_conn import DbConn

if __name__ == '__main__':
	DbConn().__init__()
	tetris = HasierakoMenua()
