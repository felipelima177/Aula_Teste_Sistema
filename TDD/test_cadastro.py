from cliente import Cliente
from cadastro_clientes import CadastroCliente

def test_cadastro_cliente_com_sucesso():
    cliente = Cliente('Will',20,'will@teste.com')
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert resposta == "Cadastro realizado com sucesso"
    
def test_cadastro_cliente_com_nome_menor_que_tres_caracteres():
    cliente = Cliente('Wi', 20, 'will@teste.com')
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert resposta == "Cadastro não realizado, nome incorreto"  
    
def test_cadastro_cliente_com_menos_18_anos():
    cliente = Cliente ('Will', 17, 'will@teste.com')
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert resposta == "Cadastro não realizado, idade inferior a 18 anos" 
    
    
def test_cadastro_cliente_com_email_invalido():
    cliente = Cliente ('Will', 19, 'willteste.com')
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert resposta == "Cadastro não realizado, email invalido"  