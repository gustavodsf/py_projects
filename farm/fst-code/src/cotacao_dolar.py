from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

class CotacaoDolar(object):

    @staticmethod
    def get(url="https://www.dolarhoje.net.br/"):
        html = urlopen(url)
        res = BeautifulSoup(html.read(), "html5lib")
        res = res.find("div", {"id": "divSpdInText"})
        res = res.find("tbody")
        cotacao_dolar = []
        for tag in res.findAll("tr"):
            tag = tag.getText()
            tag = tag.replace("\n", "")
            tag = tag.split("\t\t\t")
            tag = list(map(lambda x: x.replace("R$" , "").strip().lower(), tag))
            tag = list(filter(lambda x: x not in [''], tag))
            cotacao_dolar.append({
                "nome": tag[0],
                "valor": tag[1].replace("," , "."),
                "data": datetime.now(),
                'dia_semana': datetime.now().weekday(),
            })
        return cotacao_dolar
