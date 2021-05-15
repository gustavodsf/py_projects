import PostgresDB

class CestaDAO:

	def __init__(self):
		self.pg = PostgresDB.PostgresDB()
		self.pg.connect()
		self.cestaDict = dict()

	def retrieveAll(self,counter):
		query = "SELECT * FROM cesta WHERE loja="+str(counter)
		rows = self.pg.executeQuery(query)
		for row in rows:
			self.cestaDict[row[3]] = row[0]
