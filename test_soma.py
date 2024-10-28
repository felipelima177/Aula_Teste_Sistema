import pytest

@pytest.fixture
def lista_num():
    return[1, 2, 3, 4, 5]

def test_soma_dobro(lista_num):
    assert soma_dobro(lista_num) == 30  # (1+2+3+4+5)*2 = 30

def test_soma_dobro_vazia():
    assert soma_dobro([]) == 0  # Soma de uma lista vazia deve ser 0

def test_soma_dobro_negativos():
    assert soma_dobro([-1, -2, -3]) == -12  # (-1 + -2 + -3) * 2 = -12

def soma_dobro(lista_num):
    return sum(x * 2 for x in lista_num)
    
    
