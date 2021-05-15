import PostgresDB

class TipoDAO:

	def __init__(self):
		self.pg = PostgresDB.PostgresDB()
		self.pg.connect()
		self.tipoDict = dict()

	def retrieveAll(self):
		query = "SELECT * FROM tipo"
		rows = self.pg.executeQuery(query)
		for row in rows:
			self.tipoDict[row[2]] = row[0]

	def wichTipo(self,pattern):
		if pattern != 0:
			return self.tipoDict[pattern]
		return 0

