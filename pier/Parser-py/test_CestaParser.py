#! /usr/bin/env python
# -*- coding: utf-8 -*-
import CestaParser
import PostgresDB

def test_lojaBoa5Cestas():
	counter = 0
	pg = PostgresDB.PostgresDB()
	pg.connect()
	pg.executeQuery("TRUNCATE cesta CASCADE")
	pg.commit()
	pg.disconnect()
	cestaParser = CestaParser.CestaParser()
	cestaParser.parse("..//Data/test_good.csv",counter)
	pg.connect()
	cur = 	pg.executeQuery("SELECT count(*) FROM cesta")
	aux = cur.fetchone()
	pg.commit()
	pg.disconnect()
	print(aux)
	assert 5 == int(aux[0])

def test_lojaRuim5Cestas():
	counter = 0
	pg = PostgresDB.PostgresDB()
	pg.connect()
	pg.executeQuery("TRUNCATE cesta CASCADE")
	pg.commit()
	pg.disconnect()
	cestaParser = CestaParser.CestaParser()
	cestaParser.parse("..//Data/test_bad.csv",counter)
	pg.connect()
	cur = 	pg.executeQuery("SELECT count(*) FROM cesta")
	aux = cur.fetchone()
	pg.commit()
	pg.disconnect()
	print(aux)
	assert 4 == int(aux[0])