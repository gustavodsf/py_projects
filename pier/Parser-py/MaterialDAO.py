import PostgresDB

class MaterialDAO:

	def __init__(self):
		self.pg = PostgresDB.PostgresDB()
		self.pg.connect()
		self.materialDict = dict()

	def retrieveAll(self):
		query = "SELECT * FROM material"
		rows = self.pg.executeQuery(query)
		for row in rows:
			self.materialDict[row[2]] = row[0]

	def wichMaterial(self,string):
		for key in self.materialDict:
			if key in string:
				return self.materialDict[key]
		return 0

