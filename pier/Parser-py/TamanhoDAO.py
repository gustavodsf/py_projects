import PostgresDB

class TamanhoDAO:

	def __init__(self):
		self.pg = PostgresDB.PostgresDB()
		self.pg.connect()
		self.tamanhoDict = dict()

	def retrieveAll(self):
		query = "SELECT * FROM tamanho"
		rows = self.pg.executeQuery(query)
		for row in rows:
			self.tamanhoDict[row[2]] = row[0]

	def wichTamanho(self,string):
		for key in self.tamanhoDict:
			if key in string:
				return self.tamanhoDict[key]
		return 0

