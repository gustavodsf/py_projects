import PostgresDB

class GeneroDAO:

	def __init__(self):
		self.pg = PostgresDB.PostgresDB()
		self.pg.connect()
		self.generoDict = dict()

	def retrieveAll(self):
		query = "SELECT * FROM genero"
		rows = self.pg.executeQuery(query)
		for row in rows:
			self.generoDict[row[2]] = row[0]

	def wichGenero(self,string):
		for key in self.generoDict:
			if key in string:
				return self.generoDict[key]
		return 0
