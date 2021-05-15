#! /usr/bin/env python
# -*- coding: utf-8 -*-
import CestaParser
import PostgresDB
import CompraParser

def test_lojaBoa10Compras():
	counter = 0
	pg = PostgresDB.PostgresDB()
	pg.connect()
	pg.executeQuery("TRUNCATE cesta CASCADE")
	pg.executeQuery("TRUNCATE compra")
	pg.commit()
	pg.disconnect()
	cestaParser = CestaParser.CestaParser()
	cestaParser.parse("..//Data/test_good.csv",counter)
	compraParser = CompraParser.CompraParser()
	compraParser.parseItem("..//Data/test_good.csv",counter)
	pg.connect()
	cur = 	pg.executeQuery("SELECT count(*) FROM compra")
	aux = cur.fetchone()
	pg.commit()
	pg.disconnect()
	print(aux)
	assert 10 == int(aux[0])

def test_lojaRuim10Compras():
	counter = 0
	pg = PostgresDB.PostgresDB()
	pg.connect()
	pg.executeQuery("TRUNCATE cesta CASCADE")
	pg.executeQuery("TRUNCATE compra")
	pg.commit()
	pg.disconnect()
	cestaParser = CestaParser.CestaParser()
	cestaParser.parse("..//Data/test_bad.csv",counter)
	compraParser = CompraParser.CompraParser()
	compraParser.parseItem("..//Data/test_bad.csv",counter)
	pg.connect()
	cur = 	pg.executeQuery("SELECT count(*) FROM compra")
	aux = cur.fetchone()
	pg.commit()
	pg.disconnect()
	print(aux)
	assert 7 == int(aux[0])
