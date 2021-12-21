import pytest
from ressources.client_ressource import ClientRessource


@pytest.fixture
def client():
    return ClientRessource(5,'client1')

def test_construction(client):
    assert 5 == client.id
    assert 'client1' == client.name

def test_get_client(client):
    res = client.get_client()
    assert  res == {'id': 5, 'name': 'client1'}
    assert  res['id'] == 5
    assert  res['name'] == 'client1'

def test_insert_client(client):
    res = client.insert_client()
    assert  res == ({'id': 5, 'name':'client1'}, 201)
    assert  res[0]['id'] == 5
    assert  res[0]['name'] == 'client1'
    
def test_update_client(client):
    res = client.update_client()
    assert  res == ({'id': 5, 'name':'client1'}, 201)
    assert  res[0]['id'] == 5
    assert  res[0]['name'] == 'client1'
