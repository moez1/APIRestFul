import pytest
from ressources.mall_ressource import MallRessource


@pytest.fixture
def mall():
    return MallRessource(5,'mall1',9)

def test_construction(mall):
    assert 5 == mall.id
    assert 'mall1' == mall.name
    assert 9 == mall.id_client

def test_get_mall(mall):
    res = mall.get_mall()
    assert  res == {'id': 5, 'name': 'mall1','id_client': 9}
    assert  res['id'] == 5
    assert  res['name'] == 'mall1'
    assert  res['id_client'] == 9

def test_insert_mall(mall):
    res = mall.insert_mall()
    assert  res == ({'id': 5, 'name':'mall1','id_client': 9}, 201)
    assert  res[0]['id'] == 5
    assert  res[0]['name'] == 'mall1'
    assert  res[0]['id_client'] == 9
    
def test_update_mall(mall):
    res = mall.update_mall()
    assert  res == ({'id': 5, 'name':'mall1','id_client': 9}, 201)
    assert  res[0]['id'] == 5
    assert  res[0]['name'] == 'mall1'
    assert  res[0]['id_client'] == 9

