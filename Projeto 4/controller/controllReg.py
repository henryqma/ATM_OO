from controller.controllerGerente import *
from controller.controllUser import *
from view.telaGerente import *
import json


gerDirectory = "database\\gerentes.json"
with open(gerDirectory) as userfile:
    gerList = json.load(userfile)

usersDirectory = "database\\users.json"
with open(usersDirectory) as userfile:
        userList = json.load(userfile)

rg = UserController(userList, usersDirectory)

gr = GerenteController(gerList, usersDirectory)

class LoginGerente:

    loggedG = None
    while loggedG is None:
        TelaGerente()
        cpf = input("Insira o seu CPF: ")
        senha = input("Insira a sua senha: ")
        loggedG = gr.login(cpf, senha)

class Registro:

    nome = input("Insira o nome do cliente: \n")
    cpf = input("Insira o CPF do cliente: \n")
    senha = input("Insira a senha do cliente: \n")
    rg.registrar(nome, senha, cpf)
    print("Usuário cadastrado com sucesso!")