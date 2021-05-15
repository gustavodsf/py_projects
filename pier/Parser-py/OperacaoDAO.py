import PostgresDB

class OperacaoDAO:

	def __init__(self):
		self.pg = PostgresDB.PostgresDB()
		self.pg.connect()
		self.operacaoDict = dict()

	def retrieveAll(self):
		query = "SELECT * FROM operacao"
		rows = self.pg.executeQuery(query)
		for row in rows:
			self.operacaoDict[row[2]] = row[0]

	def wichOperacao(self,string):
		for key in self.operacaoDict:
			if key in string:
				return self.operacaoDict[key]
		return 0