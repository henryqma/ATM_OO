from controller.controllUser import *
from view.telaPrincipal import *    
from view.telaLogin import *
import json

usersDirectory = "database\\users.json"
with open(usersDirectory) as userfile:
        userList = json.load(userfile)

op = UserController(userList, usersDirectory)

class Operacoes:
        
        def __init__(self, logged):
                self.logged = logged
                Tela()
                x = input()
                if x == '1':
                        print("---------------------------")
                        print(f"Conta:{logged['conta']['id']}")
                        print(f"Nome:{logged['nome']} CPF:{logged['cpf']}")
                        print("---------------------------")
                        print(f"Saldo disponível:{logged['conta']['saldo']}")
                        print("---------------------------")
                        Operacoes(logged)
                elif x == '2':
                        valor_str = input("Insira o valor a ser sacado:")
                        valor = float(valor_str)
                        op.sacar(valor, logged)
                        logged['conta']['saldo'] -= valor
                        Operacoes(logged)
                elif x == '3':
                        valor_str = input("Insira o valor a ser depositado:")
                        valor = float(valor_str)
                        op.deposito(valor, logged)
                        print("Valor depositado com sucesso!")
                        logged['conta']['saldo'] += valor
                        Operacoes(logged)
                elif x == '4':
                        pass
                elif x == '5':    
                        pass
                elif x == '6':
                        exit
                else:
                        print("Opção Inválida!")
                        Operacoes(logged)