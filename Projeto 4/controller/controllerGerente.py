from model.atm import *
import json

gerDirectory = "database\\gerentes.json"

class GerenteController:

    def __init__(self, gerList, gerDirectory):
        self.gerList = gerList
        self.gerDirectory = gerDirectory

    def login(self, cpf, senha):

        for user in self.gerList:
            if user['cpf'] == cpf and user['senha'] == senha:
                print("Login realizado com sucesso")
                return user
        else:
            print("CPF ou senha inválido(s)!")
            return None

