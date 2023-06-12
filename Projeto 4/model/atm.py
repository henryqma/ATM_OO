class Conta:
    
    def __init__(self, id, saldo):
        self.id = id
        self.saldo = saldo

    def to_dict(self):
        return {
            'id': self.id,
            'saldo': self.saldo
        }
    
    def get_id(self):
        return self.id
    
    def get_saldo(self):
        return self.saldo

class User:

    def __init__(self, nome, senha, cpf, conta):
        self.nome = nome
        self.senha = senha
        self.cpf = cpf
        self.conta = conta

    def get_nome(self):
        return self.nome
    
    def get_senha(self):
        return self.senha
    
    def get_cpf(self):
        return self.cpf
    
    def get_conta(self):
        return self.conta