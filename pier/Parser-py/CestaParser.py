import  ReadFile
import re
import CestaDAO


class CestaParser:

	def parse(self,path,counter):
		cestaDAO = CestaDAO.CestaDAO()
		read = ReadFile.ReadFile()
		lines = read.readCsvFile(path)
		line = lines.readline()
		while line:
			line = re.sub(' +',' ',line)
			line = line.split(' ')
			if "[S]" in line:	
				query = "INSERT INTO cesta(qtd_pecas, valor, codigo, loja)VALUES("+line[len(line)-3]+",\'"+line[len(line)-2]+"\',"+line[2]+","+str(counter)+");"
				cestaDAO.pg.executeQuery(query)
			elif  "[DS]" in line:
				query = "INSERT INTO cesta(qtd_pecas, valor, codigo, loja)VALUES("+line[len(line)-4]+",\'"+line[len(line)-3]+"\',"+line[2]+","+str(counter)+");"
				cestaDAO.pg.executeQuery(query)
			line = lines.readline()
		lines.close()
		cestaDAO.pg.commit()
		cestaDAO.pg.disconnect()