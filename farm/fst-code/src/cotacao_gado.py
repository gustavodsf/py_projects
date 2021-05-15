from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime


class CotacaoGado(object):

    @staticmethod
    def get_arroba_gordo(url):
        html = urlopen(url)
        res = BeautifulSoup(html.read(),"html5lib");
        cotacao = res.findAll("tr", {"class": "conteudo"})
        cotacoes = []
        for tag in cotacao:
            text = tag.getText()
            text = text.split('\n')
            text = [ t.strip() for t in text]
            text = list(filter(lambda x: x not in [''], text))
            if len(text) == 6:
                cotacao_dict = {
                    "estado":  						text[0],
                    "livre_funrural_a_vista": 		float(text[1].replace(',','.')),
                    "livre_funrural_30_dias": 		float(text[2].replace(',','.')),
                    "livre_funrural_variacao": 		"sem_variacao"if text[3] == '-' else float(text[3].replace(',','.').replace('%','')),
                    "livre_funrural_senar_a_vista": float(text[4].replace(',','.')),
                    "livre_funrural_senar_30_dias": float(text[5].replace(',','.')),
                    "data": datetime.now()
                }
            elif len(text) == 5:
                cotacao_dict = {
                    "estado":  						text[0],
                    "livre_funrural_a_vista": 		float(text[1].replace(',','.')),
                    "livre_funrural_30_dias": 		float(text[2].replace(',','.')),
                    "livre_funrural_senar_a_vista": float(text[3].replace(',','.')),
                    "livre_funrural_senar_30_dias": float(text[4].replace(',','.')),
                    "data": datetime.now()
                }
            cotacoes.append(cotacao_dict)
        return {"data": datetime.now(), "dia_semana": datetime.now().weekday(), "cotacao": cotacoes}

    @staticmethod
    def get_custo_producao(url="https://www.scotconsultoria.com.br/cotacoes/custo-producao/recria_engorda/"):
        html = urlopen(url)
        res = BeautifulSoup(html.read(),"html5lib")
        custo_producao = res.findAll("tr", {"class": "conteudo"})
        custos_producao = []
        for tag in custo_producao:
            text = tag.getText()
            text = text.split('\n')
            text = [ t.strip() for t in text]
            text = list(filter(lambda x: x not in [''], text))
            custo_dict = {
                "descricao":    text[0],
                "custo/arroba": float(text[1].replace(',','.').replace('R$','')),
                "participacao": float(text[2].replace(',','.').replace('%',''))
                }
            custos_producao.append(custo_dict)
        return {"data": datetime.now(), "dia_semana": datetime.now().weekday(), "custos": custos_producao}

    def get_custo_reposicao(url = "https://www.scotconsultoria.com.br/cotacoes/reposicao/?ref=sm"):
        html = urlopen(url)
        res = BeautifulSoup(html.read(), "html5lib");
        tabelas_reposicao = res.findAll("table")

        nelore_boi_reposicao   = {}
        mestico_boi_reposicao  = {}
        nelore_vaca_reposicao  = {}
        mestico_vaca_reposicao = {}

        for idx in range(len(tabelas_reposicao)):
            table_title = tabelas_reposicao[idx].find("thead").getText()
            table_title = table_title.replace("\n","").replace("\t","")
            title, date = table_title.split("-")
            title = title.strip()
            date = date.strip()
            date = datetime.strptime(date, '%d/%m/%Y')

            name_column = tabelas_reposicao[idx].find("tr", {"class": "top"})
            name_column = name_column.getText().replace("\n","").replace("\t","#").lower()
            name_column = ' '.join(name_column.split())
            name_column = name_column.split("#")
            name_column = list(filter(lambda x: x not in [''], name_column))
            name_column = list(map(lambda x: x.replace(" ","_"), name_column))
            reposicao_by_uf = []
            for row in tabelas_reposicao[idx].findAll("tr", {"class": "conteudo"}):
                preco = row.getText().replace("\n","").replace("\t\t\t",",").replace("\t\t","").split(",")
                reposicao = {
                    "uf": preco[1]
                }
                reposicao[ name_column[0]+'_preco_cab']    = float(preco[2])
                reposicao[ name_column[0]+'_preco_arroba'] = float(preco[3])
                reposicao[ name_column[0]+'_troca']        = float(preco[4])
                reposicao[ name_column[1]+'_preco_cab']    = float(preco[5])
                reposicao[ name_column[1]+'_preco_arroba'] = float(preco[6])
                reposicao[ name_column[1]+'_troca']        = float(preco[7])
                reposicao[ name_column[2]+'_preco_cab']    = float(preco[8])
                reposicao[ name_column[2]+'_preco_arroba'] = float(preco[9])
                reposicao[ name_column[2]+'_troca']        = float(preco[10])
                reposicao_by_uf.append(reposicao)

            if "MACHO NELORE" == title:
                nelore_boi_reposicao["data"] = date
                nelore_boi_reposicao["reposicao"] = reposicao_by_uf

            elif "MACHO MESTIÇO" == title:
                mestico_boi_reposicao["data"] = date
                mestico_boi_reposicao["reposicao"] = reposicao_by_uf

            elif "FÊMEA NELORE" == title:
                nelore_vaca_reposicao["data"] = date
                nelore_vaca_reposicao["reposicao"] = reposicao_by_uf

            elif "FÊMEA MESTIÇA" == title:
                mestico_vaca_reposicao["data"] = date	
                mestico_vaca_reposicao["reposicao"] = reposicao_by_uf
        return 	nelore_boi_reposicao, mestico_boi_reposicao, nelore_vaca_reposicao, mestico_vaca_reposicao

    def get_preco_boi_mundo(url = 'https://www.scotconsultoria.com.br/cotacoes/boi-no-mundo/?ref=smn'):
        html = urlopen(url)
        res = BeautifulSoup(html.read(), "html5lib");
        tabelas_cotacao = res.find("table")

        table_title = tabelas_cotacao.find("thead").getText()
        table_title = table_title.replace("\n","").replace("\t","")
        title, date = table_title.split("-")
        title = title.strip()
        date = date.replace("HÁ 1 ANO","")
        date = date.strip()
        date = datetime.strptime(date, '%d/%m/%Y')

        international_price = []
        for tag in tabelas_cotacao.findAll("tr", {"class": "conteudo"}):
            tag = tag.get_text().replace("\n","#").replace(" ","")
            tag = tag.split("#")
            tag = list(filter(lambda x: x not in [''], tag))
            international_price.append({
                "pais": tag[0],
                "preco_atual_dolar": float(tag[1].replace(",",".")),
                "preco_ano_passado_dolar": float(tag[2].replace(",","."))
            })
        return {"data": datetime.now(), "dia_semana": datetime.now().weekday(), "cotacao": international_price}