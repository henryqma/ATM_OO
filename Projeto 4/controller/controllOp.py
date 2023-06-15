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
                
                if x == '1': #Exibe o extrato
                        
                        logged = op.atualizar(logged)
                        print("\n---------------------------")
                        print(f"Conta:{logged['conta']['id']}")
                        print(f"Nome:{logged['nome']} CPF:{logged['cpf']}")
                        print("---------------------------")
                        print(f"Saldo disponível:{logged['conta']['saldo']}")
                        print(f"Crédito devido:{logged['conta']['credito']}")
                        print("---------------------------\n")
                        Operacoes(logged)
                
                elif x == '2': #Sacar
                       
                        valor_str = input("Insira o valor a ser sacado:")
                        valor = float(valor_str)
                        op.sacar(valor, logged)
                        Operacoes(logged)
                
                elif x == '3': #Depositar
                        
                        valor_str = input("Insira o valor a ser depositado:")
                        valor = float(valor_str)
                        op.deposito(valor, logged)
                        print("Valor depositado com sucesso!")
                        Operacoes(logged)
                
                elif x == '4': #Programa um pagamento, se realizando quando tiver o saldo necessário
                        
                        valorP_str = input("Insira o valor do pagamento:")
                        valorP = float(valorP_str)
                        valorN_str = input("Insira o valor preciso para que o pagamento aconteça:")
                        valorN = float(valorN_str)
                        op.programado(logged, valorP, valorN)
                        print(f"Um pagamento de {valorP} reais será realizado quando {valorN} reais estiverem disponíveis")
                        Operacoes(logged)
                
                elif x == '5': #Crédito
                        
                        valor_str = input("Insira o valor do empréstimo:")
                        valor = float(valor_str)
                        op.credito(valor, logged)
                        Operacoes(logged)
                
                elif x == '6': #Encerrar o programa
                        
                        exit
                
                else:
                        
                        print("Opção Inválida!")
                        Operacoes(logged)