import PostgresDB

class FaixaEtariaDAO:

	def __init__(self):
		self.pg = PostgresDB.PostgresDB()
		self.pg.connect()
		self.faixaEtariaDict = dict()

	def retrieveAll(self):
		query = "SELECT * FROM faixa_etaria"
		rows = self.pg.executeQuery(query)
		for row in rows:
			self.faixaEtariaDict[row[2]] = row[0]

	def wichFaixaEtaria(self,string):
		for key in self.faixaEtariaDict:
			if key in string:
				return self.faixaEtariaDict[key]
		return 0
