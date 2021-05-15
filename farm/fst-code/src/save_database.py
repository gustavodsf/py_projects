from pymongo import MongoClient

class SaveDatabase(object):

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.banco = client['fst']

    def save_cotacao_dolar(self, cotacao):
        cotacao_dolar = self.banco['cotacao_dolar']
        return cotacao_dolar.insert_many(cotacao)

    def save_cotacao_milho(self, cotacao):
        cotacao_milho = self.banco['cotacao_milho'] 
        return cotacao_milho.insert_one(cotacao)
    
    def save_cotacao_soja(self, cotacao):
        cotacao_soja = self.banco['cotacao_soja']
        return cotacao_soja.insert_one(cotacao)

    def save_nelore_boi_reposicao(self, cotacao):
        nelore_boi_reposicao = self.banco['nelore_boi_reposicao']
        return nelore_boi_reposicao.insert_one(cotacao)

    def save_mestico_boi_reposicao(self, cotacao):
        mestico_boi_reposicao = self.banco['mestico_boi_reposicao']
        return mestico_boi_reposicao.insert_one(cotacao)

    def save_nelore_vaca_reposicao(self, cotacao):        
        nelore_vaca_reposicao = self.banco['nelore_vaca_reposicao']
        return nelore_vaca_reposicao.insert_one(cotacao)

    def save_mestico_vaca_reposicao(self, cotacao):
        mestico_vaca_reposicao = self.banco['mestico_vaca_reposicao']
        return mestico_vaca_reposicao.insert_one(cotacao)

    def save_international_price(self, cotacao):
        international_price = self.banco['international_price']
        return international_price.insert_one(cotacao)

    def save_custos_producao(self, cotacao):
        custos_producao = self.banco['custos_producao']
        return custos_producao.insert_one(cotacao)
    
    def save_boi_gordo(self, cotacao):
        boi_gordo = self.banco['boi_gordo']
        return boi_gordo.insert_one(cotacao)

    def save_vaca_gordo(self, cotacao):
        vaca_gordo = self.banco['vaca_gordo']
        return vaca_gordo.insert_one(cotacao)