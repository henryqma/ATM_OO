from controller.controllUser import *  
from view.telaLogin import *
import json

usersDirectory = "database\\users.json"
with open(usersDirectory) as userfile:
        userList = json.load(userfile)

lg = UserController(userList, usersDirectory)

def log():
       
    TelaLogin()
    x = input()
        
    if x == '1': # Login
                
        cpf = input("Insira o seu CPF: ")
        senha = input("Insira a sua senha: ")
        return lg.login(cpf, senha)
            
    elif x == '2': # Registro
                
        nome = input("Insira seu nome: \n")
        cpf = input("Insira seu CPF: \n")
        senha = input("Insira sua senha: \n")
        lg.registrar(nome, senha, cpf)
        print("Usuário cadastrado com sucesso!")
        return log()

    else:
                
        print("Opção Inválida")
        return log()

class Entrada():
       
       logged = log()