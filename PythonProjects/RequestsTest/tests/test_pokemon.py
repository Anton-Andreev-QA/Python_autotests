import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'

TOKEN = '85dcb5a41a940dc8975422f79b71e62e'

HEADERS = {'Content-Type' : 'application/json'}

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id" : 2426})
    assert response.status_code == 200


def test_part_of_response():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id" : 2426})
    assert response.json()['data'][0]['trainer_name'] == 'ВУДИ'