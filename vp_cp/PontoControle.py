#! /usr/bin/env python
# -*- coding: utf-8 -*-

class PontoControle:
	
	def __init__(self):
		# Nome da Linha
		self.nomeLinha = ""

		# latitude do ponto de controle
		self.pcCadLatitude = 0

		# longitude do ponto de controle 
		self.pcCadLongitude = 0

		# codigo do ponto de controle
		self.pcCadCodigo = 0

		# linha sequencia do ponto de controle
		self.linPcSequencia =  0 

		self.linCodigo = 0
		
		self.inutilizado = False