from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

class CotacaoSoja(object):

    @staticmethod
    def get(url="https://canalrural.uol.com.br/cotacao/soja/"):
        html = urlopen(url)
        res = BeautifulSoup(html.read(), "html5lib");
        res = res.findAll("div", {"class": "quote-table"})

        grao_cotacao_soja = {}
        premio_cotacao_soja = {}
        farelo_cotacao_soja = {}
        farelo_premio_cotacao_soja = {}
        oleo_bruto_cotacao_soja = {}
        oleo_premio_soja = {}

        for tag in res:
            title = tag.find("div",{"class": "quote-table-head"})
            title = title.getText().split("\n")
            title = list(map(lambda x: x.replace(" ","").strip().lower(), title))
            title = list(filter(lambda x: x not in [''], title))

            list_catacao = []
            for row in tag.find("tbody").findAll("tr"):
                row = row.getText().split("\n")
                row = list(map(lambda x: x.replace(" ","").strip().lower(), row))
                row = list(filter(lambda x: x not in [''], row))
                if len(row) == 6:
                    list_catacao.append({
                        "praca":      row[0],
                        "compra":     row[1],
                        "venda":      row[2],
                        "minima":     row[3],
                        "maxima":     row[4],
                        "abertura":   row[5],
                        "fechamento": row[6]
                    })
                else:
                    list_catacao.append({
                        "praca":      row[0],
                        "minima":     row[1],
                        "maxima":      row[2],
                    })

            if title[0] == "grão":
                grao_cotacao_soja = {
                    "nome": title[0],
                    "tipo": title[1],
                    "data": datetime.strptime(title[3], 'atualizadoem%d/%m/%Yàs%H:%M'),
                    "cotacao": list_catacao
                }

            elif title[0] == "prêmio":
                premio_cotacao_soja = {
                    "nome": title[0],
                    "tipo": title[1],
                    "cotacao": list_catacao
                }

            elif title[0] == "farelo":
                farelo_cotacao_soja = {
                    "nome": title[0],
                    "tipo": title[1],
                    "cotacao": list_catacao
                }

            elif title[0] == "fareloprêmio":
                farelo_premio_cotacao_soja = {
                    "nome":  "farelo prêmio",
                    "tipo": title[1],
                    "cotacao": list_catacao
                }

            elif title[0] == "óleobruto":
                oleo_bruto_cotacao_soja = {
                    "nome":  "óleo bruto",
                    "tipo": title[1],
                    "cotacao": list_catacao
                }

            elif title[0] == "óleoprêmio":
                oleo_premio_cotacao_soja = {
                    "nome":  "óleo prêmio",
                    "tipo": title[1],
                    "cotacao": list_catacao
                }
        return {
                    "grao": grao_cotacao_soja, 
                    "premio": premio_cotacao_soja, 
                    "farelo": farelo_cotacao_soja, 
                    "farelo_premio": farelo_premio_cotacao_soja, 
                    "oleo": oleo_bruto_cotacao_soja,
                    "oleo_premio": oleo_premio_soja,
                    "data": datetime.now(),
                    "data_now": datetime.now().weekday()
                }