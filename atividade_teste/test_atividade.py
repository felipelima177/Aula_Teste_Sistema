import requests
import pytest
from unittest import mock
from unittest.mock import MagicMock

class BancoDeDados:
    def buscar_pedido(self, pedido_id):
        # Simula uma consulta ao banco de dados para obter um pedido
        raise NotImplementedError("Consulta real ao banco de dados")

def calcular_valor_total(pedido_id):
    # Simula uma chamada a uma API externa para obter detalhes dos produtos
    resposta = requests.get(f"http://api.loja.com/pedidos/{pedido_id}")
    dados_produtos = resposta.json()
    
    # Calcula o valor total com base no preço e quantidade de cada produto
    total = sum(item["preco"] * item["quantidade"] for item in dados_produtos)
    return total

def obter_pedido_com_valor_total(pedido_id, banco):
    # Busca o pedido no banco de dados
    pedido = banco.buscar_pedido(pedido_id)
    
    # Calcula o valor total do pedido
    valor_total = calcular_valor_total(pedido_id)
    
    # Adiciona o valor total ao pedido
    pedido["valor_total"] = valor_total
    
    return pedido


# 1. Teste para a função calcular_valor_total()
def test_calcular_valor_total(mocker):
    # Criar um mock para requests.get()
    mock_resposta = mock.Mock()
    mock_resposta.json.return_value = [
        {"preco": 100, "quantidade": 2},
        {"preco": 50, "quantidade": 3}
    ]
    
    mocker.patch("requests.get", return_value=mock_resposta)

    # Testar a função calcular_valor_total
    pedido_id = 1
    total = calcular_valor_total(pedido_id)
    
    # Verificar se o cálculo do total foi correto
    assert total == (100 * 2 + 50 * 3)  # 200 + 150 = 350


# 2. Fixture para simular o banco de dados

@pytest.fixture
def mock_banco():
    banco_mock = MagicMock()
    banco_mock.buscar_pedido.return_value = {"id": 1, "cliente": "João"}
    return banco_mock

# 3. Teste para a função obter_pedido_com_valor_total()
def test_obter_pedido_com_valor_total(mock_banco, mocker):
    # Mockar a função calcular_valor_total
    mocker.patch("requests.get", return_value=mock.Mock(json=mock.Mock(return_value=[
        {"preco": 100, "quantidade": 2},
        {"preco": 50, "quantidade": 3}
    ])))

    pedido_id = 1
    
    # Chamar a função principal
    pedido_com_valor_total = obter_pedido_com_valor_total(pedido_id, mock_banco)

    # Verificar se o pedido contém o valor total correto
    assert pedido_com_valor_total["valor_total"] == 350
    assert pedido_com_valor_total["id"] == 1
    assert pedido_com_valor_total["cliente"] == "João"