from view.telaLogin import *
from view.telaPrincipal import *
from controller.controllUser import *
from controller.controllOp import *
from controller.controllLogin import *

if __name__ == "__main__":
    
    logged = Entrada().logged
    Operacoes(logged)