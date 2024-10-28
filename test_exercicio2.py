from exercicio2 import *

def test_acordar_cedo():
    # Teste se o tipo retornado é str
    assert isinstance(acordar_cedo(5), str)
    
    # Teste para falha de acordar_cedo
    assert acordar_cedo(7) == 'Tente novamente amanhã'
    
    # Teste para conclusão de acordar_cedo
    assert acordar_cedo(6) == 'Você é um guerreiro'

def test_tempo_exercicio():
    # Teste para conclusão de tempo_exercicio
    assert tempo_exercicio(70, 3) == 69
    
    # Teste para falha de tempo_exercicio
    assert tempo_exercicio(70, 1) is None  # Deve ser None devido ao pass

def test_tem_exercicio():
    # Teste para verificar se passar 'Descanso' retorna False
    assert not tem_exercicio('Descanso')
    
    # Teste para verificar se passar um esporte retorna True
    assert tem_exercicio('Futebol')
