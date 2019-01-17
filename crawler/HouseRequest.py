import functools
import json

import requests


class HouseRequest:
    _headers = {'Content-type': 'application/json',
                'Accept': 'text/plain'}
    _url = "https://www.netimoveis.com/{venda_locacao}/&pagina={page_number}&" \
           "busca={json_search}&quantidadeDeRegistro=50"
    _url_num_houses = "https://www.netimoveis.com/quantidade/Resultado/" \
                      "ResultadoQuantidade/?transacao={venda_locacao}&" \
                      "estado={state}&cidade={city}&tipo={type}&" \
                      "busca={json_search}"
    _busca = {
        'valorMinimo': None,
        'valorMaximo': None,
        'quartos': None,
        'suites': None,
        'banhos': None,
        'vagas': None,
        'idadeMinima': None,
        'areaMinima': None,
        'areaMaxima': None,
        'bairros': [],
        'ordenar': None
    }

    def __init__(self, search_venda=True):
        self._venda_or_locacao = 'venda' if search_venda else 'locacao'
        self._request = self._create_get_request_data()


    def _create_get_request_data(self, page_number=1):
        return self._url.format(
            venda_locacao = self._venda_or_locacao,
            json_search = json.dumps(self._busca),
            page_number = page_number,
        )

    def _create_get_req_num_houses(self, state, city, type=''):
        return self._url_num_houses.format(
            venda_locacao=self._venda_or_locacao,
            json_search=json.dumps(self._busca),
            state = state,
            city = city,
            type = type,
        )

    @functools.lru_cache()
    def number_houses(self, state, city, type=''):
        get_num_houses = self._create_get_req_num_houses(state, city, type)
        req_num_houses = requests.get(get_num_houses)
        values_json = req_num_houses.json()
        if req_num_houses.status_code == 200 and not values_json['erro']:
            return values_json['totalDeRegistros']
        return self.number_houses(state, city, type)


