from enum import Enum


class Transacao(Enum):
    Locacao = 'locacao'
    Venda = 'venda'
    Venda_locacao = 'venda_locacao'


class UrlRequest(Enum):
    url_quantidade = "https://www.netimoveis.com/quantidade/Resultado/" \
                      "ResultadoQuantidade/?transacao={venda_locacao}&" \
                      "estado={state}&cidade={city}&tipo={type}&" \
                      "busca={json_search}"

    url_data = "https://www.netimoveis.com/{venda_locacao}/{state}/{city}/" \
               "{type_property}&pagina={page_number}&" \
               "busca={json_search}&quantidadeDeRegistro=50"

    url_header = {'Content-type': 'application/json', 'Accept': 'text/plain'}


class BuscaJson(Enum):
    valor_minimo = 'valorMinimo'
    valor_maximo = 'valorMaximo'
    quartos = 'quartos'
    suites = 'suites'
    banheiro = 'banhos'
    vagas_garagem = 'vagas'
    idade_min_imovel = 'idadeMinima'
    area_minima = 'areaMinima'
    area_maxima = 'areaMaxima'
    bairros = 'bairros'
    ordenar = 'ordenar'


