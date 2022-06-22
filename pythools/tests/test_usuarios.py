import pytest

from pythools.spam.db import Conexao
from pythools.spam.modelos import Usuario


def test_salvar_usuario(conexao,sessao):
    usuario = Usuario(nome='Renzo')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)

@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()


@pytest.fixture
def conexao():
    #setup
    conexao_obj =  Conexao()
    yield conexao_obj
    # Tear Down
    conexao_obj.fechar()


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Renzo'), Usuario(nome='Luciano')]

    for usuario in usuarios:
        sessao.salvar(usuario)

    assert usuarios == sessao.listar()

