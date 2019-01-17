import responses

from crawler.HouseRequest import HouseRequest


def test_get_request():
    house = HouseRequest()
    assert house._venda_or_locacao == 'venda'
    expected = 'https://www.netimoveis.com/venda/&pagina=10&busca=' \
               '{"valorMinimo": null, "valorMaximo": null, "quartos": null, ' \
               '"suites": null, "banhos": null, "vagas": null, ' \
               '"idadeMinima": null, "areaMinima": null, "areaMaxima": null, ' \
               '"bairros": [], "ordenar": null}&quantidadeDeRegistro=50'
    assert house._create_get_request(10) == expected

def test_get_req_num_houses():
    house = HouseRequest(False)
    assert house._venda_or_locacao == 'locacao'
    expected = 'https://www.netimoveis.com/quantidade/Resultado/' \
               'ResultadoQuantidade/?transacao=locacao&estado=minas-gerais&' \
               'cidade=belo-horizonte&tipo=apartamento&' \
               'busca={"valorMinimo": null, "valorMaximo": null, ' \
               '"quartos": null, "suites": null, "banhos": null, ' \
               '"vagas": null, "idadeMinima": null, "areaMinima": null, ' \
               '"areaMaxima": null, "bairros": [], "ordenar": null}'
    assert house._create_get_req_num_houses('minas-gerais',
                                            'belo-horizonte',
                                            'apartamento') == expected

@responses.activate
def test_total_registros():
    house = HouseRequest()
    url_num_houses = house._create_get_req_num_houses('minas-gerais',
                                                      'belo-horizonte',
                                                      'apartamento')
    responses.add(responses.GET, url_num_houses,
                  json={'erro': False, 'mensagem': None,
                        'totalDeRegistros': 2211, 'unico': None,
                        'lista': None}, status=200)
    assert house.number_houses('minas-gerais',
                               'belo-horizonte',
                               'apartamento') == 2211

