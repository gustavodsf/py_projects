import PostgresDB

class LojaDAO:

	def __init__(self):
		self.pg = PostgresDB.PostgresDB()
		self.pg.connect()
		self.lojaDict = dict()

	def retrieveAll(self):
		query = "SELECT * FROM loja"
		rows = self.pg.executeQuery(query)
		counter = 0
		for row in rows:
			self.lojaDict[counter] = row[0]
			counter+=1
