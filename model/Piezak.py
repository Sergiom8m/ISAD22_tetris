from controller.Soinuak import Soinuak
erabiltzailea= None

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
		paleta = erabiltzailea.paleta if not None else 1
		if paleta == 1:
			kolorea = "yellow"
		elif paleta == 2:
			kolorea = "sky blue"
		elif paleta == 3:
			kolorea = "snow"
		else:
			kolorea = "green"

		super(Laukia, self).__init__([[0,0],[0,1],[1,0],[1,1]], kolorea)

class Zutabea(Pieza):
	def __init__(self, kolorea=None):

		paleta = erabiltzailea.paleta if not None else 1
		if paleta == 1:
			kolorea = "cyan"
		elif paleta == 2:
			kolorea = "pink"
		elif paleta == 3:
			kolorea = "SkyBlue2"
		else:
			kolorea = "SeaGreen1"

		super(Zutabea, self).__init__([[0,-1],[0,0],[0,1],[0,2]], kolorea)

class Lforma(Pieza):
	def __init__(self, kolorea=None):

		paleta = erabiltzailea.paleta if not None else 1
		if paleta == 1:
			kolorea = "blue"
		elif paleta == 2:
			kolorea = "MediumOrchid1"
		elif paleta == 3:
			kolorea = "LightBlue1"
		else:
			kolorea = "SpringGreen4"

		super(Lforma, self).__init__([[-1,-1],[0,-1],[0,0],[0,1]], kolorea)

class LformaAlderantzizko(Pieza):
	def __init__(self, kolorea=None):

		paleta = erabiltzailea.paleta if not None else 1
		if paleta == 1:
			kolorea = "orange"
		elif paleta == 2:
			kolorea = "khaki"
		elif paleta == 3:
			kolorea = "cyan"
		else:
			kolorea = "OliveDrab2"

		super(LformaAlderantzizko, self).__init__([[1,-1],[0,-1],[0,0],[0,1]], kolorea)


class Zforma(Pieza):
	def __init__(self, kolorea=None):

		paleta = erabiltzailea.paleta if not None else 1
		if paleta == 1:
			kolorea = "green"
		elif paleta == 2:
			kolorea = "pale green"
		elif paleta == 3:
			kolorea = "SkyBlue4"
		else:
			kolorea = "dark green"


		super(Zforma, self).__init__([[0,-1],[0,0],[-1,0],[-1,1]], kolorea)

class ZformaAlderantzizko(Pieza):
	def __init__(self, kolorea=None):

		paleta = erabiltzailea.paleta
		if paleta == 1:
			kolorea = "red"
		elif paleta == 2:
			kolorea = "VioletRed1"
		elif paleta == 3:
			kolorea = "sky blue"
		else:
			kolorea = "SpringGreen4"

		super(ZformaAlderantzizko, self).__init__([[0,-1],[0,0],[1,0],[1,1]], kolorea)

class Tforma(Pieza):
	def __init__(self, kolorea=None):

		paleta = erabiltzailea.paleta if not None else 1
		if paleta == 1:
			kolorea = "purple"
		elif paleta == 2:
			kolorea = "peach puff"
		elif paleta == 3:
			kolorea = "navy"
		else:
			kolorea = "forest green"

		super(Tforma, self).__init__([[-1,0],[0,0],[1,0],[0,1]], kolorea)