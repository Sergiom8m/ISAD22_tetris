from view.JokatuLehioa import JokatuLehioa
import sqlite3


if __name__ == '__main__':
	con = sqlite3.connect("datubase.db")
	cur = con.cursor()
	#cur.execute("CREATE TABLE JOKALARIAK(erabiltzailea, pasahitza, puntuazioa)")
	cur.execute("INSERT INTO JOKALARIAK VALUES ('admin',12345, 0 )")
	for row in cur.execute("SELECT erabiltzailea, puntuazioa FROM JOKALARIAK"):
		print(row)

	tetris = JokatuLehioa()