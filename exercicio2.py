#Definição das funções requisitadas

def acordar_cedo(horario):
    if horario > 6: #e acordar cedo após as 6 faça:
        return 'Tente novamente amanhã'
    return 'Você é um guerreiro'

def tempo_exercicio(peso,tempo):
    if tempo > 2: #Se o tempo de exercicio for maior que 2 faça:
        peso -= 1
        return peso
    pass #Passa a função sem return
      
def tem_exercicio(esporte):
    if esporte == 'Descanso': #Se passar 'Descanso' retorna False
        return False
    return True
        