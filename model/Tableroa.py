from controller.Soinuak import Soinuak
from controller.db_conn import DbConn


class Tableroa:
	def __init__(self, tamaina):
		self.tamaina = tamaina
		self.hasieratu_tableroa()

	def kargatu_partida(self, partida):
		datuak = str(partida).split(sep='#')
		self.hasieratu_tableroa()
		self.puntuazioa = int(datuak.pop(0))
		datuak.pop(0)
		datuak.pop(0)
		for i in range(self.tamaina[1]):
			for j in range(self.tamaina[0]):
				unekoa = datuak.pop(0)
				if unekoa.__eq__("None"):
					self.tab[i][j] = None
				else:
					self.tab[i][j] = unekoa

	def puntuazioa_eguneratu_DBan(self, erabiltzaile, abiadura): #TODO ABIADURA ES GLOBAL, SE GUARDA BIEN?
		DbConn.puntuazioa_eguneratu(DbConn(), erabiltzaile.erabiltzaile_id, self.tamaina[0], abiadura, self.puntuazioa)

	def hasieratu_tableroa(self):
		self.tab = [ [ None for y in range(self.tamaina[0])]for x in range(self.tamaina[1])]
		self.pieza = None
		self.puntuazioa = 0

	def probatu_mugimendua(self, pos_berria):

		for i in range(4):
			x = pos_berria[0] + self.pieza.get_x(i)
			y = pos_berria[1] + self.pieza.get_y(i)
			if x < 0 or y < 0:
				return False
			if x >= self.tamaina[1] or y >= self.tamaina[0]:
				return False
			if self.tab[x][y] != None:
				return False
		return True

	def pieza_finkotu(self, pos):
		if not self.probatu_mugimendua(pos):
			raise Exception("Pieza ezin da hor sartu")
		for i in range(4):
			xb = pos[0] + self.pieza.get_x(i)
			yb = pos[1] + self.pieza.get_y(i)
			self.tab[xb][yb] = self.pieza.get_kolorea()
		self.pieza = None


	def pieza_kokatu_behean(self):
		Soinuak.play_fall(Soinuak)
		for i in range(1,self.tamaina[1]):
			posizio_berria = (self.posizioa[0]+i, self.posizioa[1])
			if not self.probatu_mugimendua(posizio_berria):
				self.posizioa = (posizio_berria[0]-1,posizio_berria[1])
				break
		self.puntuazioa += (i-1)*2

	def sartu_pieza(self,pieza):
		x = -pieza.min_x()
		self.posizioa = (x,(self.tamaina[0]//2)-1)
		self.pieza = pieza
		if not self.probatu_mugimendua(self.posizioa):
			raise Exception("Pieza ezin da hor sartu")

	def mugitu_behera(self):
		if not self.pieza:
			raise Exception("Ez dago piezarik")
		posizio_berria = (self.posizioa[0]+1, self.posizioa[1])
		if self.probatu_mugimendua(posizio_berria):
			self.posizioa = posizio_berria
		else:
			raise Exception("Pieza ezin da horra mugitu")

	def mugitu_ezkerrera(self):
		if not self.pieza:
			return
		posizio_berria = (self.posizioa[0], self.posizioa[1]-1)
		if self.probatu_mugimendua(posizio_berria):
			self.posizioa = posizio_berria
		else:
			raise Exception("Pieza ezin da horra mugitu")

	def mugitu_eskumara(self):
		if not self.pieza:
			return
		posizio_berria = (self.posizioa[0], self.posizioa[1]+1)
		if self.probatu_mugimendua(posizio_berria):
			self.posizioa = posizio_berria
		else:
			raise Exception("Pieza ezin da horra mugitu")

	def biratu_pieza(self):
		if not self.pieza:
			return
		self.pieza.biratuEzkerrera()
		if not self.probatu_mugimendua(self.posizioa):
			self.pieza.biratuEskuinera()
			raise Exception("Pieza ezin da orain biratu")

	def lerroa_ezabatu(self, lerro):
		Soinuak.play_crash(Soinuak())
		for l in range(lerro-1,0,-1):
			for j in range(self.tamaina[0]):
				self.tab[l+1][j] = self.tab[l][j]

	def lerroa_beteta_dago(self, i):
		for j in range(self.tamaina[0]):
			if self.tab[i][j] == None:
				return False
		return True

	def betetako_lerroak_ezabatu(self):
		count = 0
		for i in range(self.tamaina[1]):
			if self.lerroa_beteta_dago(i):
				self.lerroa_ezabatu(i)
				count +=1
		if count == 1:
			self.puntuazioa += 100
		elif count == 2:
			self.puntuazioa += 300
		elif count == 3:
			self.puntuazioa += 500
		elif count == 4:
			self.puntuazioa += 800

		
	def imprimatu(self):
		tmp_tab = [[y for y in x] for x in self.tab]
		for i in range(4):
			x = self.posizioa[0] + self.pieza.get_x(i)
			y = self.posizioa[1] + self.pieza.get_y(i)
			tmp_tab[x][y] = self.pieza.get_kolorea()
		for i in range(10):
			print()
		for i in range(self.tamaina[1]):
			print('|',end='')
			for j in range(self.tamaina[0]):
				print('#' if tmp_tab[i][j] else ' ',end='')
			print('|')



if __name__ == '__main__':
	t = Tableroa()
	t.jokatu(Tableroa.imprimatu)


