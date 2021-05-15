#! /usr/bin/env python
# -*- coding: utf-8 -*-
import PostgresDB
import DateParser
import datetime

class DateDAO:

	def __init__(self):
		self.pg = PostgresDB.PostgresDB()
		self.pg.connect()
		self.dateDict = dict()

	def generateTable(self):
		dateParser = DateParser.DateParser()
		date  = datetime.datetime(2014,1,1,0,0,0)
		for i in range(365):
			dateParser.convert(date.strftime('%d/%m/%Y'))
			query = "INSERT INTO data(data, estacao, status, dia_util, dia_da_semana, mes) VALUES (\'"+date.strftime('%Y-%m-%d')+"\',\'"+dateParser.season()+"\',\'"+dateParser.dateStatus()+"\',"+str(dateParser.monthBusinessDay())+",\'"+dateParser.dayOfWeek()+"\',\'"+dateParser.monthName()+"\');"
			self.pg.executeQuery(query)
			date += datetime.timedelta(days=1)
		self.pg.commit()
		self.pg.disconnect()

	def retrieveAll(self):
		query = "SELECT * FROM data"
		rows = self.pg.executeQuery(query)
		for row in rows:
			self.dateDict[row[1].strftime('%d/%m/%y')] = row[0]		
