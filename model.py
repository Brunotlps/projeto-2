# 1. Criei um banco de dados no phpmyadmin
# 2. Criei a tabela usuarios 
# 3. Fazendo algumas importações necessárias

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 4. Criando as constantes para estalecer uma conexão com banco de dados
USER = "root"
PASSWORD = "bruno123"
HOST = "localhost"
DB = "projeto-2"
PORT = 3306

# 5. Criando a string de conexão com banco de dados
CONNECTION = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

Base = declarative_base()
# Base é uma classe base criada pela função declarative_base() do SQLAlchemy. Ela serve como uma superclasse para todas as classes de modelo que você define em seu projeto. 
# As classes de modelo, por sua vez, representam as tabelas no banco de dados.

# 6. Criando uma classe Usuario que se conecta ao banco de dados e interage com a tabela Usuarios
# Uma instância desta classe representa uma linha na tabela usuarios

class Usuario(Base):
    __tablename__ = "usuarios" 

    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    email = Column(String(100), unique=True)
    senha = Column(String(255))

engine = create_engine(CONNECTION, echo=True) # engine representa o 'motor ' que conecta o SQLAlchemy ao banco de dados.
# A função create_engine do SQLAlchemy é responsável por configurar a conexão com o banco de dados. Ela aceita a string de conexão e outros parâmetros que influenciam o 
# comportamento dessa conexão.

# Base.metadata.create_all(engine)
# verifica se as tabelas definidas pelos seus modelos (como Usuario) já existem no banco de dados. Se não existirem, ele cria essas tabelas automaticamente. Esse processo é 
# essencial para sincronizar o estado do banco com o esquema definido nos modelos Python.

Session = sessionmaker(bind=engine)
session = Session()
#são responsáveis por criar e instanciar uma sessão de interação com o banco de dados