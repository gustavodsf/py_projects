#! /usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

class DateParser:

	def __init__(self):
		self.days =[ 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado','Domingo' ]
		self.months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho','Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro' ]
		self.sessons = ['Verão','Outono','Inverno','Primavera']
		self.holidayStatus = ['Feriado','Pré-Feriado','Pós-Feriado','Normal']
		self.businessDays = dict()
		self.mountBusinessDays()
		self.dateConverted = None

	def convert(self,dateStr):
		self.dateConverted = datetime.datetime.strptime(dateStr, '%d/%m/%Y')

	def dayOfWeek(self):
		return self.days[self.dateConverted.weekday()]

	def monthName(self):
		return self.months[(self.dateConverted.month-1)]
	
	#Outono: de 21 de março a 21 de junho
	#Inverno: de 21 de junho a 23 de setembro
	#Primavera: de 23 de setembro a 21 de dezembro
	#Verão: de 21 de dezembro a 21 de março
	def season(self):
		#Verão(Janeiro|Fevereiro)
		if self.dateConverted.month in [1,2]:
			return self.sessons[0]
		#Outono(Abril|Maio)
		elif self.dateConverted.month in [4,5]:
			return self.sessons[1]
		#Inverno(Julho|Agosto)	
		elif self.dateConverted.month in [7,8]:
			return self.sessons[2]
		#Primavera(Outrubro|Novembro)	
		elif self.dateConverted.month in [10,11]:
			return self.sessons[3]	
		#Troca de estações(Verão|Outono)
		elif self.dateConverted.month == 3:
			if self.dateConverted.day < 22:
				return self.sessons[0]
			else:
				return self.sessons[1]
		#Troca de estações(Outono|Inverno)
		elif self.dateConverted.month == 6:
			if self.dateConverted.day < 22:
				return self.sessons[1]
			else:
				return self.sessons[2]

		#Troca de estações(Inverno|Primavera)
		elif self.dateConverted.month == 9:
			if self.dateConverted.day < 24:
				return self.sessons[2]
			else:
				return self.sessons[3]

		#Troca de estações(Primavera|Verão)
		elif self.dateConverted.month == 12:
			if self.dateConverted.day < 22:
				return self.sessons[3]
			else:
				return self.sessons[0]

	'''
		Feriado 2014
		Março: 4: Carnaval (3,4)
		Abril: 20: Páscoa 21: Tiradentes 23: Dia de São Jorge(4,20),(4,21),(4,23)
		Maio: 1: Dia do Trabalho 11: Dia das mães (5,1),(5,11)
		Junho: 12: Dia dos Namorados (6,12)
		Agosto: 10: Dia dos Pais 15: Nsa. Sra. da Conceição (7,10),(7,15)
		Setembro: 7: Independência do Brasil (9,7)
		Outubro: 12: Nsa. Sra. Aparecida  20: Dia do Comércio  (10,12),(10,20)
	  Novembro: 2: Finados 13: Aniversário de Cabo Frio 15: Proclamação da República 20: Dia da Consciência Negra / Zumbi dos Palmares (11,2),(11,13),(11,15),(11,20)
	  Dezembro: 25: Natal
	'''
	def dateStatus(self):
		d = (self.dateConverted.month,self.dateConverted.day)
		if self.holiday(d):
			return self.holidayStatus[0]
		elif (2,27) < d < (3,4) or (4,14) < d < (4,23) or (4,27) < d < (5,1) or (5,5) < d < (5,11) or (6,6) < d < (6,12) or (8,4) < d < (8,10)  or (8,9) < d < (7,15) or (9,1) < d <  (9,7) or (10,6) < d < (10,12)  or (10,14)  < d < (10,20) or (10,27) < d < (11,2) or (11,7) < d < (11,13) or (11,9) < d < (11,15) or (11,14) < d < (11,20) or  (12,14) < d < (12,25):
			return self.holidayStatus[1]
		elif (3,4) < d < (3,10) or (4,23) < d < (4,29) or (5,1) < d < (5,7) or (5,11) < d < (5,17) or (6,12) < d < (6,18) or (8,10) < d < (8,15) or (8,15) < d < (8,21) or (9,7) < d <  (9,13) or (10,12) < d < (10,17) or (10,20)  < d < (10,26) or (11,2) < d < (11,8) or (11,13) < d < (11,19)  or (11,15) < d < (11,21) or (11,20) < d < (11,26) or (12,25) < d < (12,31):
			return self.holidayStatus[2]
		return self.holidayStatus[3]

	def holiday(self,d):
		if d in [(3,4),(4,18),(4,20),(4,21),(4,23),(5,1),(5,11),(6,12),(8,10),(8,15),(9,7),(10,12),(10,20),(11,2),(11,13),(11,15),(11,20),(12,25)]:
			return True
		return False
	
	def monthBusinessDay(self):
		  strDate = self.dateConverted.strftime('%d/%m/%Y')
		  return self.businessDays[strDate]

	def mountBusinessDays(self):
		date  = datetime.datetime(2014,1,1,0,0,0)
		month = 1
		counter = 1
		for i in range(365): 
			if (date.month,date.day) in [(1,1),(3,4),(4,18),(4,21),(4,23),(5,1),(7,15),(9,7),(10,12),(10,20),(11,2),(11,13),(11,15),(11,20),(12,25)]:
				self.businessDays[date.strftime('%d/%m/%Y')] = 0
			else:
				if date.weekday() not in (5,6):
					self.businessDays[date.strftime('%d/%m/%Y')] = counter
					counter+=1
				else:
					self.businessDays[date.strftime('%d/%m/%Y')] = -1
			date += datetime.timedelta(days=1)
			if month != date.month:
				month = date.month
				counter = 1