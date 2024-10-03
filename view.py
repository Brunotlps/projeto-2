from controller import *

def menu():
    print("1. Cadastrar Usuário")
    print("2. Fazer Login")
    print("3. Sair")

while True:
    
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        cadastrar_usuario(nome, email, senha)
    
    elif opcao == "2":
        email = input("Email: ")
        senha = input("Senha: ")
        login_usuario(email, senha)
    
    elif opcao == "3":
        break
    
    else:
        print("Opção inválida!")
