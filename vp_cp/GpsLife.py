#! /usr/bin/env python
# -*- coding: utf-8 -*-
import PontoControleParse
import LinhaPCUnico
import Linha
from geopy import distance
from geopy import Point
import csv

class GpsLife:

	def __init__(self):
		pontoControleParse = PontoControleParse.PontoControleParse();
		linhas = pontoControleParse.parse();
		self.calcDistanciaPontoInicialFinal(linhas)
		pontosControleUnico = self.pontoControleUnicos(linhas)
		novasLinhas = self.novosLinhasPontoControle(linhas,pontosControleUnico)
		deteleSQLSemDuplo = self.montaDelete(novasLinhas,linhas)
		self.retirandoPontoPorDistancia(novasLinhas)
		deteleSQLPorDistancia = self.montaDeleteInutilizado(novasLinhas)
		self.escreveSemPontoDuplo(novasLinhas)
		self.escreveSemPontoPorDistancia(novasLinhas)
		self.escreveDeleteSql(deteleSQLSemDuplo,"delete_script_sem_duplo.sql")
		self.escreveDeleteSql(deteleSQLPorDistancia,"delete_script_por_distancia.sql")

	def calcDistanciaPontoInicialFinal(self,linhas):
		for key in linhas:
			p1  = Point(str(linhas[key].pontosControle[0].pcCadLatitude)+" "+str(linhas[key].pontosControle[0].pcCadLongitude))
			p2  = Point(str(linhas[key].pontosControle[len(linhas[key].pontosControle) -1 ].pcCadLatitude)+" "+str(linhas[key].pontosControle[len(linhas[key].pontosControle) -1 ].pcCadLongitude))
			linhas[key].distancia = distance.distance(p1,p2).kilometers

	def pontoControleUnicos(self,linhas):
		pontosControleUnico = {}
		for key in linhas:
			for pc in linhas[key].pontosControle:
				if pc.pcCadCodigo not in pontosControleUnico:
					lpcUnico = LinhaPCUnico.LinhaPCUnico()
					lpcUnico.pc = pc
					lpcUnico.distancia =  linhas[key].distancia
					pontosControleUnico[pc.pcCadCodigo] = lpcUnico
				elif pontosControleUnico[pc.pcCadCodigo].distancia > linhas[key].distancia:
					lpcUnico = LinhaPCUnico.LinhaPCUnico()
					lpcUnico.pc = pc
					lpcUnico.distancia =  linhas[key].distancia
					pontosControleUnico[pc.pcCadCodigo] = lpcUnico
		return pontosControleUnico

	def retirandoPontoPorDistancia(self,novasLinhas):
		for key in novasLinhas:
			for i in range(1, len(novasLinhas[key].pontosControle) - 1):
				for key1 in novasLinhas:
					if key != key1:
						for j in range(1,len(novasLinhas[key1].pontosControle) - 1):
							pc = novasLinhas[key].pontosControle[i]
							pc1 = novasLinhas[key1].pontosControle[j]
							p1  = Point( str(pc.pcCadLatitude)+" "+str(pc.pcCadLongitude))
							p2  = Point(str(pc1.pcCadLatitude)+" "+str(pc1.pcCadLongitude))
							if distance.distance(p1,p2).kilometers < 5:
								if novasLinhas[key].distancia < novasLinhas[key1].distancia and not pc.inutilizado and  not pc1.inutilizado:
									pc1.inutilizado = True
								elif novasLinhas[key].distancia > novasLinhas[key1].distancia and not pc.inutilizado and  not pc1.inutilizado:
									pc.inutilizado = True

	def novosLinhasPontoControle(self,linhas,pontosControleUnico):
		novasLinhas = {}
		for key in linhas:
			l = Linha.Linha()
			l.pontosControle.append(linhas[key].pontosControle[0])
			for key2 in pontosControleUnico:
				if key == pontosControleUnico[key2].pc.nomeLinha:
					l.pontosControle.append(pontosControleUnico[key2].pc)
			l.pontosControle.append(linhas[key].pontosControle[len(linhas[key].pontosControle) -1 ])
			l.distancia = linhas[key].distancia
			novasLinhas[key] = l
		return novasLinhas

	def montaDelete(self,novasLinhas,linhas):
		deteleSQL = '';
		for key in linhas:
			for i in range(1, len(linhas[key].pontosControle) - 1):
				pc = linhas[key].pontosControle[i]
				achou = False
				for j in range(1, len(novasLinhas[key].pontosControle) - 1):
					pc1 = novasLinhas[key].pontosControle[j]
					if pc.pcCadCodigo ==  pc1.pcCadCodigo:
						achou = True
				if not achou :
					deteleSQL = deteleSQL + 'DELETE FROM LINHAPC a WHERE a.LINCODIGO = '+str(pc.linCodigo)+' AND  a.PCCADCODIGO = '+str(pc.pcCadCodigo)+';\n '
		return deteleSQL

	def montaDeleteInutilizado(self,novasLinhas):
		deteleSQL = '';
		for key in novasLinhas:
			for pc in novasLinhas[key].pontosControle:
				if pc.inutilizado:
					deteleSQL = deteleSQL + 'DELETE FROM LINHAPC a WHERE a.LINCODIGO = '+str(pc.linCodigo)+' AND  a.PCCADCODIGO = '+str(pc.pcCadCodigo)+';\n '
	 	return deteleSQL


	def escreveSemPontoDuplo(self,novasLinhas):
		target = open("sem_pontos_duplos.csv", 'w')
		target.write("linha")
		target.write(",")
		target.write("latitude'")
		target.write(",")
		target.write("longitude")
		target.write(",")
		target.write("pc_id")
		target.write(",")
		target.write("pc_sequencia")
		target.write("\n")
		
		for key in novasLinhas:
			for pc in novasLinhas[key].pontosControle:
				target.write(key.encode('ascii', 'ignore'))
				target.write(",")
				target.write(str(pc.pcCadLatitude))
				target.write(",")
				target.write(str(pc.pcCadLongitude))
				target.write(",")
				target.write(str(pc.pcCadCodigo))
				target.write(",")
				target.write(str(pc.linPcSequencia))
				target.write("\n")
		target.close()

	def escreveSemPontoPorDistancia(self,novasLinhas):
		target = open("sem_pontos_por_distancia.csv", 'w')
		for key in novasLinhas:
			for pc in novasLinhas[key].pontosControle:
				if not pc.inutilizado:	
					target.write(key.encode('ascii', 'ignore'))
					target.write(",")
					target.write(str(pc.pcCadLatitude))
					target.write(",")
					target.write(str(pc.pcCadLongitude))
					target.write(",")
					target.write(str(pc.pcCadCodigo))
					target.write(",")
					target.write(str(pc.linPcSequencia))
					target.write("\n")
		target.close()

	def escreveDeleteSql(self,deteleSQL,nomeFile):
		target = open(nomeFile, 'w')
		target.write(deteleSQL)
		target.close()

	