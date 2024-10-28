import pytest

# Definindo uma fixture chamada 'lista_simples'
@pytest.fixture
def lista_simples():
    return [1, 2, 3, 4, 5]

# Usando a fixture 'lista_simples' em um teste
def test_soma(lista_simples):
    assert sum(lista_simples) == 15

# Teste para contar elementos e verificar valores
def test_elementos(lista_simples):
    # Contando a quantidade de elementos
    quantidade_elementos = len(lista_simples)
    
    # Verificando se a quantidade está correta
    assert quantidade_elementos == 5
    
    # Verificando os valores em cada posição
    valores_expectados = [1, 2, 3, 4, 5]
    for i in range(quantidade_elementos):
        assert lista_simples[i] == valores_expectados[i]
        

