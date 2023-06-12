from model.atm import *
from controller.controllUser import *
import json

usersDirectory = "database\\users.json"
with open(usersDirectory) as userfile:
        userList = json.load(userfile)

teste = UserController(userList, usersDirectory)
logged = teste.login("3333", "321")
teste.deposito(500, logged)
#teste.deposito(500, logged)
