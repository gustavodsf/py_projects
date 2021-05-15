#! /usr/bin/env python
# -*- coding: utf-8 -*-
import DateParser

'''
 	  TESTE DIAS DA SEMANA
'''
def test_day_of_week_domingo():
	date = DateParser.DateParser()
	date.convert("22/02/2015")
	assert date.dayOfWeek() == "Domingo"

def test_day_of_week_terca():
	date = DateParser.DateParser()
	date.convert("25/11/2014")
	assert date.dayOfWeek() == "Terça"

def test_day_of_week_quinta():
	date = DateParser.DateParser()
	date.convert("18/02/2016")
	assert date.dayOfWeek() == "Quinta"

def test_day_of_week_sexta():
	date = DateParser.DateParser()
	date.convert("09/01/2015")
	assert date.dayOfWeek() == "Sexta"

'''
 	  TESTE MESES DO ANO
'''
def test_month_name_fevereiro():
	date = DateParser.DateParser()
	date.convert("22/02/2015")
	assert date.monthName() == "Fevereiro"

def test_month_name_outubro():
	date = DateParser.DateParser()
	date.convert("28/10/1987")
	assert date.monthName() == "Outubro"

def test_month_name_maio():
	date = DateParser.DateParser()
	date.convert("26/05/1985")
	assert date.monthName() == "Maio"

'''
 	  TESTE ESTAÇÕES DO ANO
'''
def test_seasson_easy_verao():
	date = DateParser.DateParser()
	date.convert("26/01/2015")
	assert date.season() == "Verão"

def test_seasson_easy_outono():
	date = DateParser.DateParser()
	date.convert("26/04/2015")
	assert date.season() == "Outono"

def test_seasson_easy_inverno():
	date = DateParser.DateParser()
	date.convert("26/08/2015")
	assert date.season() == "Inverno"

def test_seasson_easy_primavera():
	date = DateParser.DateParser()
	date.convert("26/11/2015")
	assert date.season() == "Primavera"

def test_seasson_transition_verao_outono():
	date = DateParser.DateParser()
	date.convert("21/03/2015")
	assert date.season() == "Verão"
	date.convert("22/03/2015")
	assert date.season() == "Outono"

def test_seasson_transition_outono_inverno():
	date = DateParser.DateParser()
	date.convert("21/06/2015")
	assert date.season() == "Outono"
	date.convert("22/06/2015")
	assert date.season() == "Inverno"

def test_seasson_transition_inverno_primavera():
	date = DateParser.DateParser()
	date.convert("23/09/2015")
	assert date.season() == "Inverno"
	date.convert("24/09/2015")
	assert date.season() == "Primavera"

def test_seasson_transition_primavera_verao():
	date = DateParser.DateParser()
	date.convert("21/12/2015")
	assert date.season() == "Primavera"
	date.convert("22/12/2015")
	assert date.season() == "Verão"

'''
 	  TESTE STATUS DO DIA (FERIADO,PRE_FERIADO,POS_FERIADO,NORMAL)
'''
def test_holiday_natal():
	date = DateParser.DateParser()
	date.convert("25/12/2015")
	assert date.dateStatus() == "Feriado"

def test_holiday_pre_feriado_natal():
	date = DateParser.DateParser()
	date.convert("16/12/2015")
	assert date.dateStatus() == "Pré-Feriado"


def test_holiday_pos_feriado_natal():
	date = DateParser.DateParser()
	date.convert("28/12/2015")
	assert date.dateStatus() == "Pós-Feriado"

def test_holiday_preferiado():
	date = DateParser.DateParser()
	date.convert("02/03/2015")
	assert date.dateStatus() == "Pré-Feriado"

def test_holiday_posferiado():
	date = DateParser.DateParser()
	date.convert("08/03/2015")
	assert date.dateStatus() == "Pós-Feriado"

def test_holiday_normal():
	date = DateParser.DateParser()
	date.convert("11/03/2015")
	assert date.dateStatus() == "Normal"

'''
 	  DIA ÚTIL NO MÊS
'''
def test_month_business_day_marco():
	date = DateParser.DateParser()
	date.convert("11/03/2014")
	assert date.monthBusinessDay() == 6

def test_month_business_day_abril():
	date = DateParser.DateParser()
	date.convert("22/04/2014")
	assert date.monthBusinessDay() == 14

def test_month_business_day_sabado():
	date = DateParser.DateParser()
	date.convert("29/11/2014")
	assert date.monthBusinessDay() == -1

def test_month_business_day_feriado():
	date = DateParser.DateParser()
	date.convert("25/12/2014")
	assert date.monthBusinessDay() == 0