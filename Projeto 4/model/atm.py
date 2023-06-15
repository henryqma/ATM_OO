class Conta:
    
    def __init__(self, id, saldo, credito, valorP, valorN):
        
        self.id = id
        self.saldo = saldo
        self.credito = credito
        self.valorP = valorP
        self.valorN = valorN

    def to_dict(self):
        
        return {
                'id': self.id,
                'saldo': self.saldo,
                'credito': self.credito,
                'valorP': self.valorP,
                'valorN': self.valorN
        }

class User:

    def __init__(self, nome, senha, cpf, conta):
        
        self.nome = nome
        self.senha = senha
        self.cpf = cpf
        self.conta = conta

class Gerente:

    def __init__(self, nome, senha, cpf):

        self.nome = nome
        self.senha = senha
        self.cpf = senha