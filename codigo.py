import math

def email_valido(email): # Função de verificação de email 
    return '@' in email and '.' in email

def eh_par(n):   #  Função para verificar se um número é par  
    return n % 2 == 0

def fatorial(n): # Função para calcular o fatorial 
    if n == 0:
        return 1
    return n * fatorial(n - 1)

def quadrado(n): # Função verificar quadrado
    return n ** 2

def eh_positivo(n): # Função de é positivo
    return n > 0

def verificar_maioridade(idade):
    if idade >= 18:
        return 'maior de idade'
    else:
        return 'menor de idade'

def classificar_temperatura(temp):
    if temp < 0:
        return 'frio'
    elif 0 <= temp <= 25:
        return 'moderado'
    else:
        return 'quente'

def avaliar_nota(nota):
    if nota >= 7:
        return 'aprovado'
    elif 5 <= nota < 7:
        return 'recuperacao'
    else:
        return 'reprovado'

def pode_votar(idade):
    if idade >= 18:
        return 'voto obrigatório'
    elif 16 <= idade < 18:
        return 'voto facultativo'
    else:
        return 'não pode votar'

def avaliar_produto(estrelas):
    if estrelas == 5:
        return 'excelente'
    elif estrelas == 4:
        return 'bom'
    elif estrelas == 3:
        return 'regular'
    elif estrelas == 2:
        return 'ruim'
    elif estrelas == 1:
        return 'péssimo'
    else:
        return 'valor inválido'
    
# Função para Soma
def soma(a, b):
    return a + b

# Função para Subtração
def subtrai(a, b):
    return a - b

# Função para Multiplicação
def multiplica(a, b):
    return a * b

# Função para Divisão
def divide(a, b):
    if b == 0:
        return "Erro: divisão por zero não permitida."
    return a / b

# Função para Calcular a Área de um Círculo
def area_circulo(raio):
    if raio < 0:
        return "Erro: o raio não pode ser negativo."
    return math.pi * (raio ** 2)

# Função para Calcular a Área de um Retângulo
def area_retangulo(largura, altura):
    if largura < 0 or altura < 0:
        return "Erro: largura e altura devem ser não-negativos."
    return largura * altura
