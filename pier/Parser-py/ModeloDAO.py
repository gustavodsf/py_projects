import PostgresDB

class ModeloDAO:

	def __init__(self):
		self.pg = PostgresDB.PostgresDB()
		self.pg.connect()
		self.modeloDict = dict()

	def retrieveAll(self):
		query = "SELECT * FROM modelo"
		rows = self.pg.executeQuery(query)
		for row in rows:
			self.modeloDict[row[2]] = row[0]

	
	def wichModelo(self,string):
		for key in self.modeloDict:
			if key in string:
				return self.modeloDict[key]
		return 0
