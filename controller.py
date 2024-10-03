from werkzeug.security import generate_password_hash, check_password_hash
from model import Usuario, session

def cadastrar_usuario(nome, email, senha):
    
    senha_hash = generate_password_hash(senha)  # Gerando o hash da senha
    novo_usuario = Usuario(nome=nome, email=email, senha=senha_hash)  # Armazenando o hash, não a senha pura
    session.add(novo_usuario)
    session.commit()
    print(f'Usuário {novo_usuario.id} cadastrado com sucesso!')

def login_usuario(email, senha):
    
    usuario = session.query(Usuario).filter_by(email=email).first()
    if usuario and check_password_hash(usuario.senha, senha):  # Verificando a senha hash
        print(f'Bem-vindo, {usuario.nome}!')
    else:
        print('Login ou senha incorretos')

# Cadastro do usuário
# cadastrar_usuario('Bruno', 'bruno@example.com', 'bruno123')

# Tentativa de login
# login_usuario('bruno@example.com', 'bruno123')
