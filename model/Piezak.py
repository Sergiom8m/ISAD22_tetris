from controller.Soinuak import Soinuak
from controller.db_conn import DbConn
erabiltzailea=""

class Pieza:
	def __init__(self, forma, kolorea):
		self.forma = forma
		self.kolorea = kolorea


	def get_kolorea(self):
		return self.kolorea
	def get_x(self, i):
		return self.forma[i][0]
	def get_y(self, i):
		return self.forma[i][1]

	def set_x(self, i,b):
		self.forma[i][0] = b
	def set_y(self, i,b):
		self.forma[i][1] = b

	def biratuEzkerrera(self):
		Soinuak.play_rotate(Soinuak)
		for i in range(4):
			aurr_x = self.get_x(i)
			aurr_y = self.get_y(i)

			self.set_x(i, aurr_y)
			self.set_y(i, -aurr_x)

	def biratuEskuinera(self):
		Soinuak.play_rotate(Soinuak)
		for i in range(4):
			aurr_x = self.get_x(i)
			aurr_y = self.get_y(i)

			self.set_x(i, -aurr_y)
			self.set_y(i, aurr_x)

	def min_x(self):
		return min([x[0] for x in self.forma])
	def min_y(self):
		return min([x[1] for x in self.forma])


class Laukia(Pieza):
	def __init__(self, kolorea=None):

		paleta = DbConn.paleta_lortu(DbConn(), erabiltzailea)
		if paleta == 1:
			kolorea = "yellow"
		elif paleta == 2:
			kolorea = "orange"
		elif paleta == 3:
			kolorea = "red"
		else:
			kolorea = "green"

		super(Laukia, self).__init__([[0,0],[0,1],[1,0],[1,1]], kolorea)

class Zutabea(Pieza):
	def __init__(self, kolorea=None):

		paleta = DbConn.paleta_lortu(DbConn(), erabiltzailea)
		if paleta == 1:
			kolorea = "yellow"
		elif paleta == 2:
			kolorea = "orange"
		elif paleta == 3:
			kolorea = "red"
		else:
			kolorea = "green"

		super(Zutabea, self).__init__([[0,-1],[0,0],[0,1],[0,2]], kolorea)

class Lforma(Pieza):
	def __init__(self, kolorea=None):

		paleta = DbConn.paleta_lortu(DbConn(), erabiltzailea)
		if paleta == 1:
			kolorea = "yellow"
		elif paleta == 2:
			kolorea = "orange"
		elif paleta == 3:
			kolorea = "red"
		else:
			kolorea = "green"

		super(Lforma, self).__init__([[-1,-1],[0,-1],[0,0],[0,1]], kolorea)

class LformaAlderantzizko(Pieza):
	def __init__(self, kolorea=None):

		paleta = DbConn.paleta_lortu(DbConn(), erabiltzailea)
		if paleta == 1:
			kolorea = "yellow"
		elif paleta == 2:
			kolorea = "orange"
		elif paleta == 3:
			kolorea = "red"
		else:
			kolorea = "green"

		super(LformaAlderantzizko, self).__init__([[1,-1],[0,-1],[0,0],[0,1]], kolorea)


class Zforma(Pieza):
	def __init__(self, kolorea=None):

		paleta = DbConn.paleta_lortu(DbConn(), erabiltzailea)
		if paleta == 1:
			kolorea = "yellow"
		elif paleta == 2:
			kolorea = "orange"
		elif paleta == 3:
			kolorea = "red"
		else:
			kolorea = "green"


		super(Zforma, self).__init__([[0,-1],[0,0],[-1,0],[-1,1]], kolorea)

class ZformaAlderantzizko(Pieza):
	def __init__(self, kolorea=None):

		paleta = DbConn.paleta_lortu(DbConn(), erabiltzailea)
		if paleta == 1:
			kolorea = "yellow"
		elif paleta == 2:
			kolorea = "orange"
		elif paleta == 3:
			kolorea = "red"
		else:
			kolorea = "green"

		super(ZformaAlderantzizko, self).__init__([[0,-1],[0,0],[1,0],[1,1]], kolorea)

class Tforma(Pieza):
	def __init__(self, kolorea=None):

		paleta = DbConn.paleta_lortu(DbConn(), erabiltzailea)
		if paleta == 1:
			kolorea = "yellow"
		elif paleta == 2:
			kolorea = "orange"
		elif paleta == 3:
			kolorea = "red"
		else:
			kolorea = "green"

		super(Tforma, self).__init__([[-1,0],[0,0],[1,0],[0,1]], kolorea)