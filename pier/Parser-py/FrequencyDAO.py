#! /usr/bin/env python
# -*- coding: utf-8 -*-
import PostgresDB

class FrequencyDAO:

	def __init__(self):
		self.pg = PostgresDB.PostgresDB()
		self.pg.connect()


	def save(self,frequencias):
		for key in frequencias:
			query = "INSERT INTO dicionario(palavra, frequencia) VALUES (\'"+ key+"\',"+str(frequencias[key])+")"
			self.pg.executeQuery(query)
		self.pg.commit()
		self.pg.disconnect()