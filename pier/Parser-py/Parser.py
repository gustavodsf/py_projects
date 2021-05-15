#! /usr/bin/env python
# -*- coding: utf-8 -*-
import CsvParser
import string
import nltk
import FrequencyDAO
import DateDAO
import CestaParser
import CompraParser

class Parser:

	def __init__(self,arg):
		if arg == 'dict':
			self.mountDict()
		elif arg == 'db':
			self.mountDB()

	def mountDict(self):
		print("..:: Montando o dicionário das palavras ::..")
		freqSave = FrequencyDAO.FrequencyDAO()
		csvParser = CsvParser.CsvParser()
		print("..:: Lendo as palavras do CSV ::..")
		words = csvParser.parserForNltk("..//Data/good_store.csv")
		words = words+" "+csvParser.parserForNltk("..//Data/bad_store.csv")
		print("..:: Removendo os números ::..")
		words = ''.join([i for i in words if not i.isdigit()])
		print("..:: Removendo a pontuação ::..")
		words = ''.join([s for s in words if s not in string.punctuation])
		print("..:: Quebrando o texto em tokens ::..")
		words = nltk.tokenize.wordpunct_tokenize(words)
		print("..:: Calculando a frequência das palavras ::..")
		frequencias = nltk.FreqDist(words)
		print("..:: Salvando as palavras na tabela dicionário ::..")
		freqSave.save(frequencias)

	def mountDB(self):
		counter = 0
		compraParser = CompraParser.CompraParser()

		print("..:: Montando o banco de dados ::..")
		print("..:: Preenchendo a Tabela de Data ::..")
		dateDAO = DateDAO.DateDAO()
		dateDAO.generateTable()
		print("..:: Preenchendo a Tabela de Cesta ::..")
		cestaParser = CestaParser.CestaParser()
		cestaParser.parse("..//Data/good_store.csv",counter)
		compraParser.parseItem("..//Data/good_store.csv",counter)

		counter+=1
		cestaParser.parse("..//Data/bad_store.csv",counter)
		compraParser.parseItem("..//Data/bad_store.csv",counter)
