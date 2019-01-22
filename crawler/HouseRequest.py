import functools
import json

import requests


class HouseRequest:

    def __init__(self):
        self._request = self._create_get_request_data()
        self._type_property = []


    def _create_get_request_data(self, page_number=1):
        return self._url.format(
            json_search = json.dumps(self._busca),
            page_number = page_number,
        )

    def __url_data(self, page_number=1, venda_locacao=None):
        pass
    def __url_num_houses(self, state, city, type='', venda_locacao=None):
        if not venda_locacao:
            venda_locacao = self._venda

        return self._url_num_houses.format(
            venda_locacao=venda_locacao,
            json_search=json.dumps(self._busca),
            state=state,
            city=city,
            type=type,
        )

    @functools.lru_cache()
    def _num_houses(self, state, city, type, transaction):
        get_num_houses = self.__url_num_houses(state, city, type, transaction)
        req_num_houses = requests.get(get_num_houses)
        values_json = req_num_houses.json()
        if req_num_houses.status_code == 200 and not values_json['erro']:
            return values_json['totalDeRegistros']
        return self._num_houses(state, city, type, transaction)

    def num_houses_venda(self, state, city, type=''):
        return self._num_houses(state, city, type, self._venda)

    def num_houses_locacao(self, state, city, type=''):
        return self._num_houses(state, city, type, self._locacao)
