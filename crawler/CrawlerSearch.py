from crawler.HouseRequest import HouseRequest


class CrawlerSearch:

    def __init__(self, venda=True, locacao=True):
        self._venda = venda
        self._locacao = locacao
        self._query_venda = HouseRequest(search_venda=True)
        self._query_locacao = HouseRequest(search_venda=False)


