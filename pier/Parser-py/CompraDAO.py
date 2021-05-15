import PostgresDB

class CompraDAO:

	def __init__(self):
		self.pg = PostgresDB.PostgresDB()
		self.pg.connect()


	def saveCompra(self,lojaId,cestaId,dateId,operacaoId,colecaoId,corId,estadoId,faixaEtariaId,generoId,materialId,modeloId,tamanhoId,itemId,tipoId,valor,qtd):
			query = "INSERT INTO compra(cesta_id, colecao_id, cor_id, data_id, genero_id, loja_id,material_id, modelo_id, item_id, tamanho_id, tipo_id, operacao_id,faixa_etaria_id, estado_id, valor, qtd) VALUES ("

			if cestaId != 0:
				query = query + str(cestaId)
			else:
				query = query + "NULL"
			query = query + ","
			if colecaoId != 0:
				query = query + str(colecaoId)
			else:
				query = query + "NULL"
			query = query + ","
			if corId != 0:
				query = query + str(corId)
			else:
				query = query + "NULL"
			query = query + ","
			if dateId != 0:
				query = query + str(dateId)
			else:
				query = query + "NULL"
			query = query + ","
			if generoId != 0:
				query = query + str(generoId)
			else:
				query = query + "NULL"
			query = query + ","
			if lojaId != 0:
				query = query + str(lojaId)
			else:
				query = query + "NULL"
			query = query + ","
			if materialId != 0:
				query = query + str(materialId)
			else:
				query = query + "NULL"
			query = query + ","
			if modeloId != 0:
				query = query + str(modeloId)
			else:
				query = query + "NULL"
			query = query + ","
			if itemId != 0:
				query = query + str(itemId)
			else:
				query = query + "NULL"
			query = query + ","
			if tamanhoId != 0 :
				query = query + str(tamanhoId)
			else:
				query = query + "NULL"
			query = query + ","
			if tipoId != 0:
				query = query + str(tipoId)
			else:
				query = query + "NULL"
			query = query + ","
			if operacaoId != 0:
				query = query + str(operacaoId)
			else:
				query = query + "NULL"
			query = query + ","
			if faixaEtariaId != 0:
				query = query + str(faixaEtariaId)
			else:
				query = query + "NULL"
			query = query + ","
			if estadoId != 0:
				query = query + str(estadoId)
			else:
				query = query + "NULL"
			query = query + ","
			query = query + "\'"+valor+"\',"
			query = query + str(qtd)+");"
			self.pg.executeQuery(query)

