	
import FireBirdDB

class PontoControleDAO:

	def __init__(self):
		self.fireBirdDB = FireBirdDB.FireBirdDB()
		self.fireBirdDB.connect();

	def getLinhaPontoControle(self):
		query = "SELECT l.LINNOME,p.PCCADLATITUDE,p.PCCADLONGITUDE,r.LINPCSEQUENCIA,p.PCCADCODIGO,r.LINCODIGO FROM LINHAPC r JOIN LINHA l on l.LINCODIGO = r.LINCODIGO JOIN PCCAD p ON p.PCCADCODIGO = r.PCCADCODIGO ORDER BY l.LINNOME,r.LINPCSEQUENCIA"
		cur = self.fireBirdDB.executeQuery(query)
		rows = cur.fetchall()
		cur.close();
		return rows



