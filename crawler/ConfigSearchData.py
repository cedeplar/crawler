class ConfigSearchData:

    def __init__(self, options, list_imovel, state, city, venda_locacao):
        self._options = options
        self._list_imovel = list_imovel
        self._state = state
        self._city = city
        self._venda_locacao = venda_locacao

    def __setattr__(self, key, value):
        if key in self._options:
            self._options[key] = value
        else:
            setattr(self, key, value)

    def __getattr__(self, item):
        if item in self._options:
            return self._options[item]
        return getattr(self, item)
