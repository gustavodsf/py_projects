#! /usr/bin/env python
# -*- coding: utf-8 -*-
import PostgresDB

class ColecaoDAO:

	def __init__(self):
		self.pg = PostgresDB.PostgresDB()
		self.pg.connect()
		self.colecaoDict = dict()

	def retrieveAll(self):
		query = "SELECT * FROM colecao"
		rows = self.pg.executeQuery(query)
		for row in rows:
			self.colecaoDict[row[2]] = row[0]
  
	def wichColecao(self,string):
		for key in self.colecaoDict:
			if key in string:
				return self.colecaoDict[key]
		return 0