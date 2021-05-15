#! /usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2

class PostgresDB:
	conn = None

	# Metodo criado para realizar com a conexao com banco de dados Mysql
	def connect(self):
		self.conn = psycopg2.connect(host='localhost', port=5432, user='pier', password='pier', database='pier')

	#Metodo utilizado para executar  um query e retorar seu resultado
	def executeQuery (self,query):
		cur = self.conn.cursor()
		cur.execute(query)
		return cur

	#Método criado para fechar a conexão com o banco de dados.
	def disconnect(self):
		self.conn.close()

	def commit(self):
		self.conn.commit()

	def rollback(self):
		self.conn.rollback()