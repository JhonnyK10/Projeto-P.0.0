import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('sqlite:///poo.db', echo=True)  
Base = declarative_base()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

class Filme(Base):
    __tablename__ = 'FILME'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nomeFilme = Column('NOME', String(100))
    duracaoFilme = Column('DURACAO_FILME', Integer)
    anoLancamentoFilme = Column('ANO_LANCAMENTO', Integer)
    generoFilme = Column('GENERO', String(100))

    def __init__(self, nomeFilme, duracaoFilme, anoLancamentoFilme, generoFilme):
        self.nomeFilme = nomeFilme
        self.duracaoFilme = duracaoFilme
        self.anoLancamentoFilme = anoLancamentoFilme
        self.generoFilme = generoFilme

nome_filme = input("Digite o nome do filme: ")
duracao_filme = int(input("Digite a duração do filme (em minutos): "))
ano_lancamento_filme = int(input("Digite o ano de lançamento do filme: "))
genero_filme = input("Digite o gênero do filme: ")

novo_filme = Filme(nome_filme, duracao_filme, ano_lancamento_filme, genero_filme)

session.add(novo_filme)
session.commit()

print("Filme adicionado com sucesso!")
