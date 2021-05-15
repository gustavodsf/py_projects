from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

class CotacaoMilho(object):

    @staticmethod
    def get(url="https://canalrural.uol.com.br/cotacao/milho/"):
        html = urlopen(url)
        res = BeautifulSoup(html.read(), "html5lib");
        res = res.findAll("div", {"class": "quote-table"})

        title = res[0].find("div",{"class": "quote-table-head"})
        title = title.getText().split("\n")
        title = list(map(lambda x: x.replace(" ","").strip().lower(), title))
        title = list(filter(lambda x: x not in [''], title))

        list_cotacao = []
        for row in res[0].find("tbody").findAll("tr"):
            row = row.getText().split("\n")
            row = list(map(lambda x: x.replace(" ","").strip().lower(), row))
            row = list(filter(lambda x: x not in [''], row))
            list_cotacao.append({
                "praca":    row[0],
                "maxima":   row[1],
                "minima":   row[2],
                "abertura": row[3],
                "variacao": row[4]
            })
        data = datetime.strptime(title[3], 'atualizadoem%d/%m/%Yàs%H:%M')
        milho_cotacao = {
            "nome": title[0],
            "tipo": title[1],
            "data": data,
            "dia_semana": data.weekday(),
            "cotacoes": list_cotacao
        }
        return milho_cotacao
