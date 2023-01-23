import requests
from random import randint
from django.conf import settings
from django.contrib.gis.geoip2 import GeoIP2
from django.contrib.gis.geoip2 import geoip2

YELP_SEARCH_ENDPOINT = 'https://api.yelp.com/v3/businesses/search'

def yelp_search(keyword=None, location=None):
    """
    Essa função passa os dados para a api do yelp setando o key.
    Passamos dois parâmetros que são o termo e a localização
    Criamos dois parâmetros padronizados caso haja algum erro no envio dos dados.
    """
    headers = {"Authorization": "Bearer "+ settings.YELP_API_KEY}

    if keyword and location:
        params = {'term': keyword, 'location': location}
    else:
        params = {'term': 'Pizzaria', 'location': 'São Paulo'}
    
    r = requests.get(YELP_SEARCH_ENDPOINT, headers=headers, params=params)

    return r.json()


def get_random_ip():
    """
    Função que cria de forma randômica os IPs.
    """
    return '.'.join([str(randint(0, 255)) for x in range(4)])


def get_client_data():
    """
    Retornar os dados de uma cidade através do ip.
    """
    g = GeoIP2() # instancio um objeto
    ip = get_random_ip() # chamo a função que cria ip de forma randômica
    try:
        return g.city(ip)
    except geoip2.errors.AddressNotFoundError: # Caso não encontre o IP o sistema retorna esse error
        return None