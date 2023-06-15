from controller.controllUser import *  
from view.telaLogin import *
import json

usersDirectory = "database\\users.json"
with open(usersDirectory) as userfile:
        userList = json.load(userfile)

lg = UserController(userList, usersDirectory)
class Entrada():

    logged = None
    while logged is None:
        TelaLogin()
        cpf = input("Insira o seu CPF: ")
        senha = input("Insira a sua senha: ")
        logged = lg.login(cpf, senha)