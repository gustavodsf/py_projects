#! /usr/bin/env python
# -*- coding: utf-8 -*-


# bibloteca do python que ajuda a  manipular  o banco de dados
import kinterbasdb

class FireBirdDB:
	con = None

	# Metodo criado para realizar com a conexao com banco de dados Mysql
	def connect(self):
		self.con = kinterbasdb.connect(dsn='/home/gustavo/Documentos/LG3_7_TRS.FDB', user='sysdba', password='123456')

	#Metodo utilizado para executar  um query e retorar seu resultado
	def executeQuery (self,query):
		cur = self.con.cursor()
		cur.execute(query)
		return cur

	#Método criado para fechar a conexão com o banco de dados.
	def disconnect(self):
		self.con.close()

	def commit(self):
		self.con.commit()	

	def rollback(self):
		self.con.rollback()