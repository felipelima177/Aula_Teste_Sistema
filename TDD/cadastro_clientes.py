IDADE_MINIMA = 18
CARACTER_OBRIGATORIO = '@'
TAMANHO_MINIMO = 3

class CadastroCliente():
    def __init__(self):
        self.cadastro = []
        
    def cadastrar_cliente (self, cliente):
        if cliente.idade < IDADE_MINIMA:
            return "Cadastro não realizado, idade inferior a 18 anos"
        if not '@' in cliente.email:
            return "Cadastro não realizado, email invalido"
        if len(cliente.nome) < 3:
            return "Cadastro não realizado, nome incorreto"
        self.cadastro.append(cliente)
        if len(self.cadastro) > 0:
            return "Cadastro realizado com sucesso"
        
    