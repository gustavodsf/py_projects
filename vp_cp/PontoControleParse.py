#! /usr/bin/env python
# -*- coding: utf-8 -*-

import FireBirdDB
import PontoControleDAO
import PontoControle
import Linha


class PontoControleParse:

	def parse(self):
		pontoControleDAO = PontoControleDAO.PontoControleDAO();
		rows = pontoControleDAO.getLinhaPontoControle()
		linhas = {}
		for row in rows:
			if row[0] not in linhas:
				linhas[row[0]] = Linha.Linha()
			pc = PontoControle.PontoControle();
			pc.nomeLinha = row[0]
			pc.pcCadLatitude = -row[1]
			pc.pcCadLongitude =  -row[2]
			pc.linPcSequencia = row[3]
			pc.pcCadCodigo = row[4]
			pc.linCodigo = row[5]
			linhas[row[0]].pontosControle.append(pc)
		return linhas













