import PostgresDB

class EstadoDAO:

	def __init__(self):
		self.pg = PostgresDB.PostgresDB()
		self.pg.connect()
		self.estadoDict = dict()

	def retrieveAll(self):
		query = "SELECT * FROM estado"
		rows = self.pg.executeQuery(query)
		for row in rows:
			self.estadoDict[row[2]] = row[0]

	def wichEstado(self,string):
		for key in self.estadoDict:
			if key in string:
				return self.estadoDict[key]
		return self.estadoDict["NORMAL"]