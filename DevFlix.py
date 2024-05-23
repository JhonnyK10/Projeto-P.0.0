from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine('sqlite:///devflix.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Plano(Base):
    __tablename__ = 'planos'

    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=True, nullable=False)
    filmes = relationship('Filme', backref='plano')
    series = relationship('Serie', backref='plano')

    def __repr__(self):
        return f'<Plano(nome={self.nome})>'

class Filme(Base):
    __tablename__ = 'filmes'

    id = Column(Integer, primary_key=True)
    nome_do_filme = Column(String, nullable=False)
    duracao = Column(Integer, nullable=False) 
    genero = Column(String, nullable=False)
    ano_de_lancamento = Column(Integer, nullable=False)
    autor = Column(String, nullable=False)
    plano_id = Column(Integer, ForeignKey('planos.id'))

    def __repr__(self):
        return f'<Filme(nome_do_filme={self.nome_do_filme}, duracao={self.duracao} min, genero={self.genero}, ano_de_lancamento={self.ano_de_lancamento}, autor={self.autor})>'

class Serie(Base):
    __tablename__ = 'series'

    id = Column(Integer, primary_key=True)
    nome_da_serie = Column(String, nullable=False)
    temporadas = Column(Integer, nullable=False)
    duracao_dos_episodios = Column(Integer, nullable=False)  
    genero = Column(String, nullable=False)
    ano_de_lancamento = Column(Integer, nullable=False)
    autor = Column(String, nullable=False)
    plano_id = Column(Integer, ForeignKey('planos.id'))

    def __repr__(self):
        return f'<Serie(nome_da_serie={self.nome_da_serie}, temporadas={self.temporadas}, duracao_dos_episodios={self.duracao_dos_episodios} min, genero={self.genero}, ano_de_lancamento={self.ano_de_lancamento}, autor={self.autor})>'

Base.metadata.create_all(engine)

def adicionar_plano(nome):
    try:
        plano = session.query(Plano).filter_by(nome=nome).first()
        if not plano:
            plano = Plano(nome=nome)
            session.add(plano)
            session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f'Erro ao adicionar plano: {e}')

def adicionar_filme(nome_do_filme, duracao, genero, ano_de_lancamento, autor, plano_nome):
    try:
        plano = session.query(Plano).filter_by(nome=plano_nome).first()
        if not plano:
            print(f'Plano "{plano_nome}" não encontrado.')
            return

        filme = Filme(nome_do_filme=nome_do_filme, duracao=duracao, genero=genero, ano_de_lancamento=ano_de_lancamento, autor=autor, plano=plano)
        session.add(filme)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f'Erro ao adicionar filme: {e}')

def adicionar_serie(nome_da_serie, temporadas, duracao_dos_episodios, genero, ano_de_lancamento, autor, plano_nome):
    try:
        plano = session.query(Plano).filter_by(nome=plano_nome).first()
        if not plano:
            print(f'Plano "{plano_nome}" não encontrado.')
            return

        serie = Serie(nome_da_serie=nome_da_serie, temporadas=temporadas, duracao_dos_episodios=duracao_dos_episodios, genero=genero, ano_de_lancamento=ano_de_lancamento, autor=autor, plano=plano)
        session.add(serie)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f'Erro ao adicionar série: {e}')

def alterar_filme(filme_id, novo_nome_do_filme, nova_duracao, novo_genero, novo_ano_de_lancamento, novo_autor):
    try:
        filme = session.query(Filme).get(filme_id)
        if filme:
            filme.nome_do_filme = novo_nome_do_filme
            filme.duracao = nova_duracao
            filme.genero = novo_genero
            filme.ano_de_lancamento = novo_ano_de_lancamento
            filme.autor = novo_autor
            session.commit()
        else:
            print(f'Filme com ID {filme_id} não encontrado.')
    except SQLAlchemyError as e:
        session.rollback()
        print(f'Erro ao alterar filme: {e}')

def alterar_serie(serie_id, novo_nome_da_serie, novas_temporadas, nova_duracao_dos_episodios, novo_genero, novo_ano_de_lancamento, novo_autor):
    try:
        serie = session.query(Serie).get(serie_id)
        if serie:
            serie.nome_da_serie = novo_nome_da_serie
            serie.temporadas = novas_temporadas
            serie.duracao_dos_episodios = nova_duracao_dos_episodios
            serie.genero = novo_genero
            serie.ano_de_lancamento = novo_ano_de_lancamento
            serie.autor = novo_autor
            session.commit()
        else:
            print(f'Serie com ID {serie_id} não encontrada.')
    except SQLAlchemyError as e:
        session.rollback()
        print(f'Erro ao alterar série: {e}')

def deletar_filme(filme_id):
    try:
        filme = session.query(Filme).get(filme_id)
        if filme:
            session.delete(filme)
            session.commit()
        else:
            print(f'Filme com ID {filme_id} não encontrado.')
    except SQLAlchemyError as e:
        session.rollback()
        print(f'Erro ao deletar filme: {e}')

def deletar_serie(serie_id):
    try:
        serie = session.query(Serie).get(serie_id)
        if serie:
            session.delete(serie)
            session.commit()
        else:
            print(f'Serie com ID {serie_id} não encontrada.')
    except SQLAlchemyError as e:
        session.rollback()
        print(f'Erro ao deletar série: {e}')

def consultar_filmes():
    try:
        filmes = session.query(Filme).all()
        for filme in filmes:
            print(filme)
    except SQLAlchemyError as e:
        print(f'Erro ao consultar filmes: {e}')

def consultar_series():
    try:
        series = session.query(Serie).all()
        for serie in series:
            print(serie)
    except SQLAlchemyError as e:
        print(f'Erro ao consultar séries: {e}')

def recomendacoes():
    print("Filme: ", "Deu a louca na chapeuzinho ", "Duração do Filme: ", 160, "Genero:", " animação",  "Ano de lançamento: ", 2006, " Cory Edwards")
    print("Série: ", "Peaky Blinders ", "Temporada: ", 6, "Duração Episodio: ", 57,  " Genero:", " Historical drama: ",  2013, " Steven Knight")  

def cancelar_plano():
    print("Plano cancelado. Encerrando o programa.")
    exit()

def main():
    adicionar_plano('Gold')
    adicionar_plano('Platinum')
    adicionar_plano('Diamond')

    while True:
        print('\nEscolha o plano que deseja obter:')
        print('1. Plano Gold (Neste plano você só tem direito a filmes)')
        print('2. Plano Platinum (Neste plano você só tem direito a séries)')
        print('3. Plano Diamond (Neste plano você tem direito a filmes e séries)')
        print('4. Recomendações DevFlix (Nossa recomendação de filmes e séries)')
        print('5. Cancelar Plano e Sair')

        opcao = input('Opção: ')
        if opcao == '1':
            while True:
                print('\nOpções do Plano Gold:')
                print('1. Adicionar Filme')
                print('2. Alterar Filme')
                print('3. Deletar Filme')
                print('4. Consultar Filmes')
                print('5. Voltar')

                escolha = input('Opção: ')
                if escolha == '1':
                    nome_do_filme = input('Nome do Filme: ')
                    duracao = int(input('Duração do Filme (em minutos): '))
                    genero = input('Gênero do Filme: ')
                    ano_de_lancamento = int(input('Ano de Lançamento do Filme: '))
                    autor = input('Nome do Autor: ')
                    adicionar_filme(nome_do_filme, duracao, genero, ano_de_lancamento, autor, 'Gold')
                elif escolha == '2':
                    filme_id = int(input('ID do Filme: '))
                    novo_nome_do_filme = input('Novo Nome do Filme: ')
                    nova_duracao = int(input('Nova Duração do Filme (em minutos): '))
                    novo_genero = input('Novo Gênero do Filme: ')
                    novo_ano_de_lancamento = int(input('Novo Ano de Lançamento do Filme: '))
                    novo_autor = input('Novo Nome do Autor: ')
                    alterar_filme(filme_id, novo_nome_do_filme, nova_duracao, novo_genero, novo_ano_de_lancamento, novo_autor)
                elif escolha == '3':
                    filme_id = int(input('ID do Filme: '))
                    deletar_filme(filme_id)
                elif escolha == '4':
                    consultar_filmes()
                elif escolha == '5':
                    break
                else:
                    print('Opção inválida. Tente novamente.')

        elif opcao == '2':
            while True:
                print('\nOpções do Plano Platinum:')
                print('1. Adicionar Série')
                print('2. Alterar Série')
                print('3. Deletar Série')
                print('4. Consultar Séries')
                print('5. Voltar')

                escolha = input('Opção: ')
                if escolha == '1':
                    nome_da_serie = input('Nome da Série: ')
                    temporadas = int(input('Número de Temporadas: '))
                    duracao_dos_episodios = int(input('Duração dos Episódios (em minutos): '))
                    genero = input('Gênero da Série: ')
                    ano_de_lancamento = int(input('Ano de Lançamento da Série: '))
                    autor = input('Nome do Autor: ')
                    adicionar_serie(nome_da_serie, temporadas, duracao_dos_episodios, genero, ano_de_lancamento, autor, 'Platinum')
                elif escolha == '2':
                    serie_id = int(input('ID da Série: '))
                    novo_nome_da_serie = input('Novo Nome da Série: ')
                    novas_temporadas = int(input('Novo Número de Temporadas: '))
                    nova_duracao_dos_episodios = int(input('Nova Duração dos Episódios (em minutos): '))
                    novo_genero = input('Novo Gênero da Série: ')
                    novo_ano_de_lancamento = int(input('Novo Ano de Lançamento da Série: '))
                    novo_autor = input('Novo Nome do Autor: ')
                    alterar_serie(serie_id, novo_nome_da_serie, novas_temporadas, nova_duracao_dos_episodios, novo_genero, novo_ano_de_lancamento, novo_autor)
                elif escolha == '3':
                    serie_id = int(input('ID da Série: '))
                    deletar_serie(serie_id)
                elif escolha == '4':
                    consultar_series()
                elif escolha == '5':
                    break
                else:
                    print('Opção inválida. Tente novamente.')

        elif opcao == '3':
            while True:
                print('\nOpções do Plano Diamond:')
                print('1. Adicionar Filme')
                print('2. Adicionar Série')
                print('3. Alterar Filme')
                print('4. Alterar Série')
                print('5. Deletar Filme')
                print('6. Deletar Série')
                print('7. Consultar Filmes')
                print('8. Consultar Séries')
                print('9. Voltar')

                escolha = input('Opção: ')
                if escolha == '1':
                    nome_do_filme = input('Nome do Filme: ')
                    duracao = int(input('Duração do Filme (em minutos): '))
                    genero = input('Gênero do Filme: ')
                    ano_de_lancamento = int(input('Ano de Lançamento do Filme: '))
                    autor = input('Nome do Autor: ')
                    adicionar_filme(nome_do_filme, duracao, genero, ano_de_lancamento, autor, 'Diamond')
                elif escolha == '2':
                    nome_da_serie = input('Nome da Série: ')
                    temporadas = int(input('Número de Temporadas: '))
                    duracao_dos_episodios = int(input('Duração dos Episódios (em minutos): '))
                    genero = input('Gênero da Série: ')
                    ano_de_lancamento = int(input('Ano de Lançamento da Série: '))
                    autor = input('Nome do Autor: ')
                    adicionar_serie(nome_da_serie, temporadas, duracao_dos_episodios, genero, ano_de_lancamento, autor, 'Diamond')
                elif escolha == '3':
                    filme_id = int(input('ID do Filme: '))
                    novo_nome_do_filme = input('Novo Nome do Filme: ')
                    nova_duracao = int(input('Nova Duração do Filme (em minutos): '))
                    novo_genero = input('Novo Gênero do Filme: ')
                    novo_ano_de_lancamento = int(input('Novo Ano de Lançamento do Filme: '))
                    novo_autor = input('Novo Nome do Autor: ')
                    alterar_filme(filme_id, novo_nome_do_filme, nova_duracao, novo_genero, novo_ano_de_lancamento, novo_autor)
                elif escolha == '4':
                    serie_id = int(input('ID da Série: '))
                    novo_nome_da_serie = input('Novo Nome da Série: ')
                    novas_temporadas = int(input('Novo Número de Temporadas: '))
                    nova_duracao_dos_episodios = int(input('Nova Duração dos Episódios (em minutos): '))
                    novo_genero = input('Novo Gênero da Série: ')
                    novo_ano_de_lancamento = int(input('Novo Ano de Lançamento da Série: '))
                    novo_autor = input('Novo Nome do Autor: ')
                    alterar_serie(serie_id, novo_nome_da_serie, novas_temporadas, nova_duracao_dos_episodios, novo_genero, novo_ano_de_lancamento, novo_autor)
                elif escolha == '5':
                    filme_id = int(input('ID do Filme: '))
                    deletar_filme(filme_id)
                elif escolha == '6':
                    serie_id = int(input('ID da Série: '))
                    deletar_serie(serie_id)
                elif escolha == '7':
                    consultar_filmes()
                elif escolha == '8':
                    consultar_series()
                elif escolha == '9':
                    break
                else:
                    print('Opção inválida. Tente novamente.')

        elif opcao == '4':
             while True:
                 recomendacoes()
                 print('1. Voltar')
                 escolha = input('Opção: ')
                 if escolha == '1':  
                    break
        elif opcao == '5':
            cancelar_plano()
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()
