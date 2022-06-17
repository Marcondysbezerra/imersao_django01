from django.test import Client

def test_home_status_code(client:Client):
    restposta = client.get('/')
    assert restposta.status_code == 200