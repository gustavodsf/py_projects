import PostgresDB

class CorDAO:

	def __init__(self):
		self.pg = PostgresDB.PostgresDB()
		self.pg.connect()
		self.corDict = dict()

	def retrieveAll(self):
		query = "SELECT * FROM cor"
		rows = self.pg.executeQuery(query)
		for row in rows:
			self.corDict[row[2]] = row[0]

	def wichCor(self,string):
		for key in self.corDict:
			if key in string:
				return self.corDict[key]
		return 0