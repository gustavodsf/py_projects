import CestaDAO
import ColecaoDAO
import CorDAO
import DateDAO
import EstadoDAO
import FaixaEtariaDAO
import GeneroDAO
import LojaDAO
import MaterialDAO
import ModeloDAO
import OperacaoDAO
import TamanhoDAO
import TipoDAO
import ItemDAO
import ReadFile
import re
import CompraDAO

class CompraParser:

	def __init__(self):
		self.cestaDAO = CestaDAO.CestaDAO()
		self.corDAO = CorDAO.CorDAO()
		self.colecaoDAO = ColecaoDAO.ColecaoDAO()
		self.dateDAO = DateDAO.DateDAO()
		self.estadoDAO = EstadoDAO.EstadoDAO()
		self.faixaEtariaDAO = FaixaEtariaDAO.FaixaEtariaDAO()
		self.generoDAO = GeneroDAO.GeneroDAO()
		self.lojaDAO = LojaDAO.LojaDAO()
		self.materialDAO = MaterialDAO.MaterialDAO()
		self.modeloDAO = ModeloDAO.ModeloDAO()
		self.operacaoDAO = OperacaoDAO.OperacaoDAO()
		self.itemDAO = ItemDAO.ItemDAO()
		self.tamanhoDAO = TamanhoDAO.TamanhoDAO()
		self.tipoDAO = TipoDAO.TipoDAO()
		self.compraDAO = CompraDAO.CompraDAO()

		self.colecaoDAO.retrieveAll()
		self.corDAO.retrieveAll()
		
		self.estadoDAO.retrieveAll()
		self.faixaEtariaDAO.retrieveAll()
		self.generoDAO.retrieveAll()
		self.lojaDAO.retrieveAll()
		self.materialDAO.retrieveAll()
		self.modeloDAO.retrieveAll()
		self.operacaoDAO.retrieveAll()
		self.itemDAO.retrieveAll()
		self.tamanhoDAO.retrieveAll()
		self.tipoDAO.retrieveAll()

	def parseItem(self,path,counter):
		self.cestaDAO.retrieveAll(counter)
		self.dateDAO.retrieveAll()
		lojaId = self.lojaDAO.lojaDict[counter]
		read = ReadFile.ReadFile()
		lines = read.readCsvFile(path)
		line = lines.readline()
		while line:	
			if "[S]" in line or "[DS]" in line:
				operacaoId = self.operacaoDAO.wichOperacao(line)
				line = re.sub(' +',' ',line)
				line = line.split(' ')
				cestaId = self.cestaDAO.cestaDict[int(line[2])]
				date = line[0].replace("\"","")
				dateId = self.dateDAO.dateDict[date]
			
			if "Código" in line:
				line = lines.readline()
				while "Destino" not in line:
					colecaoId = self.colecaoDAO.wichColecao(line)
					corId = self.corDAO.wichCor(line)
					estadoId = self.estadoDAO.wichEstado(line)
					faixaEtariaId = self.faixaEtariaDAO.wichFaixaEtaria(line)
					generoId = self.generoDAO.wichGenero(line)
					materialId = self.materialDAO.wichMaterial(line)
					modeloId = self.modeloDAO.wichModelo(line)
					tamanhoId = self.tamanhoDAO.wichTamanho(line)
					itemId = self.itemDAO.wichItem(line)
					tipoId = self.tipoDAO.wichTipo(self.itemDAO.wichTipo(itemId))
					line = re.sub(' +',' ',line)
					line = line.split(' ')
					valor=line[len(line)-3]
					qtd  =line[len(line)-4]

					if itemId != 0:
						self.compraDAO.saveCompra(lojaId,cestaId,dateId,operacaoId,colecaoId,corId,estadoId,faixaEtariaId,generoId,materialId,modeloId,tamanhoId,itemId,tipoId,valor,qtd)
					line = lines.readline()

					

			line = lines.readline()
		lines.close()
		self.compraDAO.pg.commit()