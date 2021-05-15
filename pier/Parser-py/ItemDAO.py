#! /usr/bin/env python
# -*- coding: utf-8 -*-
import PostgresDB

class ItemDAO:

	def __init__(self):
		self.pg = PostgresDB.PostgresDB()
		self.pg.connect()
		self.itemDict = dict()
		self.itemTipoDict = dict()

	def retrieveAll(self):
		query = "SELECT * FROM item"
		rows = self.pg.executeQuery(query)
		for row in rows:
			self.itemDict[row[3]] = row[0]
			self.itemTipoDict[row[0]] = row[2]

	def wichItem(self,string):
		for key in self.itemDict:
			if key in string:
				return self.itemDict[key]
		return 0

	def wichTipo(self,itemId):
		if itemId != 0 :
			return self.itemTipoDict[itemId]
		return 0
