from termcolor import colored
from functions import *

breaker = False
while breaker == True:
    print("\n --------------------------------------- \nbem vindo ao menu do InstaBot version BETA \n para sair digite 'X' no login ou senha \n  --------------------------------------- \n por favor digite seu login e senha abaixo:")
    login = input("Login: ")
    senha = input("Senha: ")
    if senha in 'Xx':
        print(colored('Saindo...', 'red'))
        break
    else:
        print(colored('testando credenciais de login...', 'yellow'))
        try:
            user01 = InstaBot(login, senha)
            user01.login()
            print(colored('login realizado com sucesso!', 'green'))
            time.sleep(1.5)
        except:
            print(colored('problema com o login, tente de novo.', 'red'))
            time.sleep(3)
        else:
            while True:
                menuLogado = input(
                    "bem vindo ao menu do InstaBot, agora que está logado, escolha uma opçao:  \n digite [1] para curtir fotos de uma hashTag   \n digite [2] para seguir os seguidores de uma conta especifica \n digite [3] para baixar as fotos de um usuario especifico (você precisa o estar seguindo) \n digite [4] para sair")
                if menuLogado == '4':
                    print(colored('Saindo...', 'red'))
                    time.sleep(0.5)
                    breaker = True

                if menuLogado == '1':
                    hashtag = input('Digite a hashtag que você quer usar: ')
                    numeroDeLikes = int(
                        input('qual numero de likes que voce quer dar? '))
                    user01.curtir_fotos_porHashTag(hashtag, numeroDeLikes)
                if menuLogado == '2':
                    contaEspecifica = input(
                        'Digite o nome da conta que você quer que tenha os seguidores seguidos')
                    numeroSeguidores = int(
                        input('Digite quantas seguidas você quer dar'))
                    user01.seguir_target(contaEspecifica, numeroSeguidores)

              



