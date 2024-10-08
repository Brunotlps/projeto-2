from werkzeug.security import generate_password_hash, check_password_hash
from model import Usuario, session
import re #O módulo re do Python fornece funções para trabalhar com expressões regulares, que são padrões de pesquisa usados para verificar, extrair ou substituir partes de uma string.

def validar_email(email):
    padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao_email, email) is not None 

def validar_senha(senha):
    if len(senha) < 8:
        return False, "A senha deve ter pelo menos 8 caracteres."
    
    if not any(char.isdigit() for char in senha):
        return False, "A senha deve conter pelo menos um número."
    
    if not any(char.isupper() for char in senha):
        return False, "A senha deve conter pelo menos uma letra maiúscula."
    
    if not any(char.islower() for char in senha):
        return False, "A senha deve conter pelo menos uma letra minúscula"
    
    return True, ""

def cadastrar_usuario(nome, email, senha):
    
    if not nome or not email or not senha:
        print("Obrigatório preencher todos os campos solicitados.")
        return # Em resumo, o return sozinho serve para garantir que, caso algum campo esteja vazio, a função seja interrompida e nada mais seja executado.
    
    if not validar_email(email):
        print("Email inválido.")
        return

    if session.query(Usuario).filter_by(email=email).first():
        print("Email já cadastrado.")
        return
        
    senha_valida, msg = validar_senha(senha)
    if not senha_valida:
        print(msg)
        return
        
    
    senha_hash = generate_password_hash(senha)  # Gerando o hash da senha
    novo_usuario = Usuario(nome=nome, email=email, senha=senha_hash)  # Armazenando o hash, não a senha pura
    session.add(novo_usuario)
    session.commit()
    print(f'Usuário {novo_usuario.id} cadastrado com sucesso!')

def login_usuario(email, senha):

    if not email or  not senha:
        print("Email e senha são obrigatórios.")
        return
    
    if not validar_email(email):
        print("Email inválido.")
        return
    
    usuario = session.query(Usuario).filter_by(email=email).first()
    if usuario and check_password_hash(usuario.senha, senha):  # Verificando a senha hash
        print(f'Bem-vindo, {usuario.nome}!')
    else:
        print('Login ou senha incorretos')

# Cadastro do usuário
# cadastrar_usuario('Bruno', 'bruno@example.com', 'bruno123')

# Tentativa de login
# login_usuario('bruno@example.com', 'bruno123')
