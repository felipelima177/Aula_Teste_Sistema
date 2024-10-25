# Exemplos de testes aula 24/10/2024

def soma (a,b):
    return a + b

def subtracao (a,b):
    return a - b

def multiplicacao (a,b):
    return a * b

def divisao (a,b):
    return a / b

def test_se_a_mais_b ():
    assert soma (8,9) == 17
    assert soma (10,5) == 15
    assert soma (8,5) == 13

def test_subtracao ():
    assert subtracao (5,3) == 2
    assert subtracao (3,3) == 0
    assert subtracao (5,4) == 1
    
def test_multiplicacao ():
    assert multiplicacao (2,2) == 4
    assert multiplicacao (5,5) == 25
    assert multiplicacao (4,9) == 36
    
def test_divisao ():
    assert divisao (4,2) == 2
    assert divisao (10,2) == 5
    assert divisao (8,2) == 4