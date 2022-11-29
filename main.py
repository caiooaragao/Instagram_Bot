from functions import *

while True:
    print("bem vindo ao menu do InstaBot version BETA \n para sair digite 'SAIR' no login ou senha \n por favor digite seu login e senha abaixo:")
    login = input("Login: ")
    senha = input("Senha: ")
    if login or senha == 'sair' or 'SAIR':
        break
