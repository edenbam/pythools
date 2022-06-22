import pytest

from pythools.spam.db import Conexao


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()


@pytest.fixture(scope='module')
def conexao():
    #setup
    conexao_obj =  Conexao()
    yield conexao_obj
    # Tear Down
    conexao_obj.fechar()
