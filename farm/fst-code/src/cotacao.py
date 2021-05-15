import logging
from src.cotacao_dolar import CotacaoDolar
from src.cotacao_gado  import CotacaoGado
from src.cotacao_milho import CotacaoMilho
from src.cotacao_soja  import CotacaoSoja
from src.save_database import SaveDatabase

class Cotacao(object):

	def __init__(self):
		save_db = SaveDatabase()
		# dolar
		#cotacao_dolar = CotacaoDolar.get()
		#save_db.save_cotacao_dolar(cotacao_dolar)
		#logging.info('Cotação do dólar capturada com sucesso')
		# Milho
		#cotacao_milho = CotacaoMilho.get()
		#save_db.save_cotacao_milho(cotacao_milho)
		#logging.info('Cotação do milho capturada com sucesso')
		#cotacao_soja = CotacaoSoja.get()
		#save_db.save_cotacao_soja(cotacao_soja)
		#logging.info('Cotação do soja capturada com sucesso')
		#nelore_boi_reposicao, mestico_boi_reposicao, nelore_vaca_reposicao, mestico_vaca_reposicao = CotacaoGado.get_custo_reposicao()
		#save_db.save_nelore_boi_reposicao(nelore_boi_reposicao)
		#save_db.save_mestico_boi_reposicao(mestico_boi_reposicao)
		#save_db.save_nelore_vaca_reposicao(nelore_vaca_reposicao)
		#save_db.save_mestico_vaca_reposicao(mestico_vaca_reposicao)
		#logging.info('Preço de reposição capturada com sucesso')
		#international_price = CotacaoGado.get_preco_boi_mundo()
		#save_db.save_international_price(international_price)
		#logging.info('Preço internacional capturada com sucesso')
		
		# custos de producao
		#custos_producao = CotacaoGado.get_custo_producao()
		#save_db.save_custos_producao(custos_producao)
		#logging.info('Custos de produção capturada com sucesso')
		
		boi_gordo = CotacaoGado.get_arroba_gordo("https://www.scotconsultoria.com.br/cotacoes/boi-gordo/?ref=smn")
		save_db.save_boi_gordo(boi_gordo)
		logging.info('Cotação do boi gordo capturada com sucesso')

		vaca_gordo = CotacaoGado.get_arroba_gordo("https://www.scotconsultoria.com.br/cotacoes/vaca-gorda/?ref=smn")
		save_db.save_vaca_gordo(vaca_gordo)
		logging.info('Cotação do vaca gorda capturada com sucesso')

		import pdb; pdb.set_trace()