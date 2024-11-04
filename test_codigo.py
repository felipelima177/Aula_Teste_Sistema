
from codigo import *

def test_email_valido():
    assert email_valido("teste@exemplo.com") == True
    assert email_valido("teste@exemplo") == False
    assert email_valido("teste.com") == False

def test_eh_par():
    assert eh_par(2) == True
    assert eh_par(3) == False

def test_fatorial():
    assert fatorial(0) == 1
    assert fatorial(5) == 120
    assert fatorial(1) == 1

def test_quadrado():
    assert quadrado(2) == 4
    assert quadrado(-3) == 9

def test_eh_positivo():
    assert eh_positivo(1) == True
    assert eh_positivo(-1) == False
    assert eh_positivo(0) == False

def test_verificar_maioridade():
    assert verificar_maioridade(18) == 'maior de idade'
    assert verificar_maioridade(17) == 'menor de idade'

def test_classificar_temperatura():
    assert classificar_temperatura(-5) == 'frio'
    assert classificar_temperatura(20) == 'moderado'
    assert classificar_temperatura(30) == 'quente'

def test_avaliar_nota():
    assert avaliar_nota(8) == 'aprovado'
    assert avaliar_nota(6) == 'recuperacao'
    assert avaliar_nota(4) == 'reprovado'

def test_pode_votar():
    assert pode_votar(18) == 'voto obrigatório'
    assert pode_votar(17) == 'voto facultativo'
    assert pode_votar(15) == 'não pode votar'

def test_avaliar_produto():
    assert avaliar_produto(5) == 'excelente'
    assert avaliar_produto(3) == 'regular'
    assert avaliar_produto(0) == 'valor inválido'
    assert avaliar_produto(1) == 'péssimo'
    assert avaliar_produto(2) == 'ruim'
    assert avaliar_produto(4) == 'bom'
    
    
def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(-1, -1) == -2

def test_subtrai():
    assert subtrai(5, 3) == 2
    assert subtrai(3, 5) == -2
    assert subtrai(-1, -1) == 0

def test_multiplica():
    assert multiplica(2, 3) == 6
    assert multiplica(-1, 1) == -1
    assert multiplica(0, 10) == 0

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 0) == "Erro: divisão por zero não permitida."
    assert divide(-6, 2) == -3

def test_area_circulo():
    assert area_circulo(3) == math.pi * 9
    assert area_circulo(-1) == "Erro: o raio não pode ser negativo."

def test_area_retangulo():
    assert area_retangulo(3, 4) == 12
    assert area_retangulo(-1, 4) == "Erro: largura e altura devem ser não-negativos."
    assert area_retangulo(3, -2) == "Erro: largura e altura devem ser não-negativos."


