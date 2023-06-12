from model.atm import *
import json

usersDirectory = "database\\users.json"

class UserController:
    def __init__(self, userList, usersDirectory):
        self.userList = userList
        self.usersDirectory = usersDirectory

    def updateJson(self):
        with open(self.usersDirectory, 'w') as updateFile:
            json.dump(self.userList, updateFile, indent=5)

    def get_last_account_id(self):
        if len(self.userList) > 0:
            last_user = self.userList[-1]
            conta = last_user.get('conta')
            if conta:
                return conta.get('id')
        return 1000
    
    def registrar(self, nome, senha, cpf):
        last_account_id = self.get_last_account_id()
        new_id = last_account_id + 1
        newConta = Conta(new_id, 0.0)
        newUser = User(nome, senha, cpf, newConta)
        convertedUser = vars(newUser)
        convertedUser['conta'] = newConta.to_dict()
        self.userList.append(convertedUser)
        self.updateJson()
    
    def login(self, cpf, senha):
        for user in self.userList:
            if user['cpf'] == cpf and user['senha'] == senha:
                print("Login realizado com sucesso")
                return user
        else:
            print("CPF ou senha inválido(s)!")
            return None
   
    def deposito(self, valor, Loggeduser):
        for user in self.userList:
            if user['nome'] == Loggeduser['nome']:
                user['conta']['saldo'] += valor
                self.updateJson()

    def sacar(self, valor, Loggeduser):
        for user in self.userList:
            if user['nome'] == Loggeduser['nome']:
                if valor <= user['conta']['saldo']:
                    user['conta']['saldo'] -= valor
                    self.updateJson()
                    print(f'Você sacou {valor} reais')
                else:
                    print("Saldo insuficiente")
