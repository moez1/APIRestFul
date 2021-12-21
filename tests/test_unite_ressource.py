import pytest
from ressources.unite_ressource import UniteRessource


@pytest.fixture
def unite():
    return UniteRessource(5,'unite1',9)

def test_construction(unite):
    assert 5 == unite.id
    assert 'unite1' == unite.name
    assert 9 == unite.id_mall

def test_get_unite(unite):
    res = unite.get_unite()
    assert  res == ({'id': 5, 'name': 'unite1','id_mall': 9},200)
    assert  res[0]['id'] == 5
    assert  res[0]['name'] == 'unite1'
    assert  res[0]['id_mall'] == 9

def test_insert_unite(unite):
    res = unite.insert_unite()
    assert  res == ({'id': 5, 'name':'unite1','id_mall': 9}, 201)
    assert  res[0]['id'] == 5
    assert  res[0]['name'] == 'unite1'
    assert  res[0]['id_mall'] == 9
    
def test_update_unite(unite):
    res = unite.update_unite()
    assert  res == ({'id': 5, 'name':'unite1','id_mall': 9}, 201)
    assert  res[0]['id'] == 5
    assert  res[0]['name'] == 'unite1'
    assert  res[0]['id_mall'] == 9

